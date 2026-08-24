#!/usr/bin/env python3
"""
query_zettelkasten.py — 神書検索神器 (Zettelkasten Query Tool)

ripgrep をエンジンとする Zettelkasten 検索ツール。
MOCファーストロジック: 検索結果にMOCファイルが含まれる場合、
自動的にそのMOC内の Related リンクを展開し、関連ノードも返す。

Usage:
    python3 query_zettelkasten.py "search terms" [--max-depth 1] [--max-results 10]
    python3 query_zettelkasten.py --moc "01_MOC_大願と掟"   # 特定MOCを起点に展開
    python3 query_zettelkasten.py --list-mocs                # MOC一覧を表示
"""

import subprocess
import re
import sys
import json
import os
from pathlib import Path
from typing import Optional


# ── 設定 ──────────────────────────────────────────────
ZETTELKASTEN_ROOT = Path.home() / "Takamagahara" / "shinsho" / "zettelkasten"
MAX_DEPTH = 1          # MOC展開の最大深さ（再帰防止）
MAX_RESULTS = 10       # デフォルト検索結果数上限
MAX_FILE_LINES = 70    # ファイル表示の最大行数（掟に従う）


# ── ripgrep 検索 ────────────────────────────────────────
def _load_synonyms() -> dict[str, list[str]]:
    """同義語辞書を読み込み。存在しなければ空辞書を返す。"""
    import json
    syn_path = ZETTELKASTEN_ROOT / "synonyms.json"
    if syn_path.exists():
        data = json.loads(syn_path.read_text(encoding="utf-8"))
        # 「凡俗→神聖」マップを flatten: 凡俗語 => 同義語リスト
        flat = {}
        for mapping in data.values():
            if isinstance(mapping, dict):
                for k, v in mapping.items():
                    flat[k] = v if isinstance(v, list) else [v]
        return flat
    return {}

SYNONYMS = _load_synonyms()


def _expand_query(query: str) -> str:
    """クエリ内の凡俗語を同義語に展開。神聖語検索のrecallを向上。"""
    terms = query.split()
    expanded = []
    for t in terms:
        expanded.append(t)
        if t in SYNONYMS:
            for syn in SYNONYMS[t]:
                expanded.append(syn)
    return " ".join(expanded)


def rg_search(query: str, max_results: int = MAX_RESULTS) -> list[dict]:
    """ripgrep で Zettelkasten 内を全文検索。

    検索セマンティクス:
      - 同義語は OR（例: 「バグ」→「バグ」「禍津」のいずれかを含む行）
      - 異なる用語間は AND（例: 「Supabase RLS」→ 両方を含む行）
      - つまり「(用語1の同義語OR) AND (用語2の同義語OR) AND ...」
    """
    try:
        terms = query.split()
        if not terms:
            return []

        # 各用語を同義語展開したグループに
        term_groups = []
        for t in terms:
            group = [t]
            if t in SYNONYMS:
                group.extend(SYNONYMS[t])
            term_groups.append(group)

        # 最初の用語グループで検索（OR: -e フラグ）
        cmd = ["rg", "--no-heading", "--line-number", "--glob", "*.md"]
        for syn in term_groups[0]:
            cmd += ["-e", syn]
        cmd += ["--", "."]

        result = subprocess.run(
            cmd,
            cwd=str(ZETTELKASTEN_ROOT),
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 1:
            return []  # マッチなし
        if result.returncode > 1:
            print(f"[WARN] rg error: {result.stderr}", file=sys.stderr)
            return []

        # 残りの用語グループ（AND: 各グループのいずれかの同義語を含む必要あり）
        remaining_groups = term_groups[1:]
        matches = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.split(":", 2)
            if len(parts) >= 3:
                content = parts[2].strip()
                # AND検索: 残りの各用語グループのいずれかの同義語が含まれるか
                if remaining_groups and not all(
                    any(syn in content for syn in grp)
                    for grp in remaining_groups
                ):
                    continue
                matches.append({
                    "file": parts[0],
                    "line": int(parts[1]),
                    "content": content,
                })
                if len(matches) >= max_results:
                    break  # グローバル上限で post-filter
        return matches
    except FileNotFoundError:
        print("[ERROR] ripgrep (rg) not found. Install with: sudo apt install ripgrep", file=sys.stderr)
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print("[WARN] rg search timed out", file=sys.stderr)
        return []


# ── ファイル検索（ファイル名 / タイトル） ──────────────────
def find_files_by_name(pattern: str) -> list[Path]:
    """ファイル名または frontmatter のタイトルにマッチする .md ファイルを返す。"""
    matches = []
    for md_file in ZETTELKASTEN_ROOT.rglob("*.md"):
        if re.search(pattern, md_file.name, re.IGNORECASE):
            matches.append(md_file)
    return matches


# ── MOCかどうかの判定 ───────────────────────────────────
def is_moc(path: str) -> bool:
    """ファイル名またはパスに 'MOC' が含まれるか。"""
    return "MOC" in Path(path).name.upper()


# ── MOCパース: Related リンク抽出 ────────────────────────
def parse_moc_links(file_path: str) -> list[str]:
    """MOCファイルから [[...]] 形式の Related リンクを抽出。"""
    full_path = ZETTELKASTEN_ROOT / file_path
    if not full_path.exists():
        return []

    content = full_path.read_text(encoding="utf-8")
    # [[path/to/file]] または [[file]] のパターン
    links = re.findall(r"\[\[([^\]]+)\]\]", content)
    return links


# ── リンクを実際のファイルパスに解決 ─────────────────────
def resolve_link(link: str, from_file: str) -> Optional[Path]:
    """[[...]] 記法のリンクを実際のファイルパスに解決する。"""
    from_dir = (ZETTELKASTEN_ROOT / from_file).parent

    # ../ で始まる相対パス
    if link.startswith("../"):
        resolved = (from_dir / link).resolve()
    # カテゴリディレクトリからの相対
    elif "/" in link:
        resolved = ZETTELKASTEN_ROOT / link
    # 同一ディレクトリ内
    else:
        resolved = from_dir / link

    # .md 拡張子がなければ補完
    if not resolved.suffix:
        resolved = resolved.with_suffix(".md")

    return resolved if resolved.exists() else None


# ── ファイル読み込み（掟に従い上限70行） ─────────────────
def read_note(file_path: str) -> dict:
    """ノートファイルを読み込み、メタデータ付きで返す。"""
    full_path = ZETTELKASTEN_ROOT / file_path
    if not full_path.exists():
        return {"file": file_path, "error": "File not found"}

    lines = full_path.read_text(encoding="utf-8").split("\n")
    content = "\n".join(lines[:MAX_FILE_LINES])
    truncated = len(lines) > MAX_FILE_LINES

    return {
        "file": file_path,
        "is_moc": is_moc(file_path),
        "lines": len(lines),
        "content": content,
        "truncated": truncated,
    }


# ── MOCファースト展開（コアロジック） ─────────────────────
def moc_first_expand(
    matches: list[dict],
    max_depth: int = MAX_DEPTH,
    visited: set = None,
    depth: int = 0,
) -> dict:
    """
    検索結果を解析し、MOCファイルがあればその Related リンクを展開する。
    再帰深度を制限して循環参照を防止。
    """
    if visited is None:
        visited = set()

    result = {
        "query_matches": [],
        "moc_expansions": [],
        "related_notes": [],
        "notes_loaded": [],
    }

    for m in matches:
        result["query_matches"].append(m)
        file_path = m["file"]

        # MOCファイルかつ未訪問なら展開
        if is_moc(file_path) and depth < max_depth:
            moc_key = file_path
            if moc_key not in visited:
                visited.add(moc_key)
                expanded = _expand_single_moc(file_path, visited, depth + 1, max_depth)
                result["moc_expansions"].append(expanded)

    return result


def _expand_single_moc(
    moc_path: str,
    visited: set,
    depth: int,
    max_depth: int,
) -> dict:
    """単一MOCの Related リンクを再帰的に展開。"""
    expansion = {
        "moc_file": moc_path,
        "depth": depth,
        "links": [],
        "loaded_notes": [],
    }

    links = parse_moc_links(moc_path)
    for link in links:
        resolved = resolve_link(link, moc_path)
        if resolved is None:
            continue
        rel_path = str(resolved.relative_to(ZETTELKASTEN_ROOT))

        link_info = {"link": link, "resolved": rel_path}
        expansion["links"].append(link_info)

        # リンク先のノートを読み込み
        note = read_note(rel_path)
        expansion["loaded_notes"].append(note)

    return expansion


# ── 出力整形: LLMプロンプトに最適なMarkdown形式 ──────────
def format_output(data: dict, query: str) -> str:
    """検索結果をLLMが扱いやすいMarkdown形式に整形。"""
    lines = []
    lines.append(f"## Zettelkasten Query Result: `{query}`")
    lines.append(f"*Base: {ZETTELKASTEN_ROOT}*")
    lines.append("")

    # ── 直接マッチ ──
    if data.get("query_matches"):
        lines.append(f"### Direct Matches ({len(data['query_matches'])} hits)")
        lines.append("| File | Line | Content |")
        lines.append("|------|------|---------|")
        for m in data["query_matches"][:MAX_RESULTS]:
            content = m["content"][:100]
            lines.append(f"| `{m['file']}` | {m['line']} | {content} |")
        lines.append("")

    # ── MOC展開 ──
    if data.get("moc_expansions"):
        lines.append(f"### MOC Expansions ({len(data['moc_expansions'])} MOCs expanded)")
        for exp in data["moc_expansions"]:
            lines.append(f"\n#### 📁 MOC: `{exp['moc_file']}` (depth={exp['depth']})")
            lines.append(f"*{len(exp['links'])} related links found*")
            lines.append("")

            for note in exp.get("loaded_notes", []):
                is_moc_tag = " ⚡[MOC]" if note.get("is_moc") else ""
                lines.append(f"##### `{note['file']}`{is_moc_tag}")
                lines.append(f"```markdown")
                lines.append(note["content"][:2000])  # 安全のため上限
                if note.get("truncated"):
                    lines.append(f"... (truncated, {note['lines']} total lines)")
                lines.append("```")
                lines.append("")

    if not data.get("query_matches") and not data.get("moc_expansions"):
        lines.append("> ⛩️ *No results found in the sacred texts.*")

    return "\n".join(lines)


# ── MOC一覧 ───────────────────────────────────────────
def list_all_mocs() -> str:
    """全MOCファイルを一覧表示。"""
    moc_files = sorted(ZETTELKASTEN_ROOT.rglob("*MOC*.md"))
    lines = ["## All MOC Files (Maps of Content)\n"]
    for mf in moc_files:
        rel = mf.relative_to(ZETTELKASTEN_ROOT)
        # frontmatterからtitleを抽出
        content = mf.read_text(encoding="utf-8")
        title_match = re.search(r"title:\s*(.+)", content)
        title = title_match.group(1).strip() if title_match else mf.stem
        lines.append(f"- **{title}** → `{rel}`")
    return "\n".join(lines)


# ── MOC起点展開 ────────────────────────────────────────
def expand_from_moc(moc_name: str, max_depth: int = 1) -> str:
    """指定されたMOC名から全リンクを展開。_MOC_ を含むファイルを優先。"""
    # 数字プレフィックス + _MOC_ パターン（例: "04" → "04_MOC_自律運営.md"）
    moc_files = list(ZETTELKASTEN_ROOT.rglob(f"{moc_name}_MOC_*.md"))
    if not moc_files:
        # _MOC_ + 数字 パターン（例: "自律運営" → "04_MOC_自律運営.md"）
        moc_files = list(ZETTELKASTEN_ROOT.rglob(f"*_MOC_*{moc_name}*.md"))
    if not moc_files:
        # 通常のMOCファイル（例: Takamagahara_MOC.md）
        moc_files = list(ZETTELKASTEN_ROOT.rglob(f"*MOC*{moc_name}*.md"))
    if not moc_files:
        # 最後の手段: 単純な名前一致
        moc_files = list(ZETTELKASTEN_ROOT.rglob(f"*{moc_name}*.md"))
    if not moc_files:
        return f"> ⛩️ MOC not found: `{moc_name}`"

    moc_rel = str(moc_files[0].relative_to(ZETTELKASTEN_ROOT))
    moc_data = read_note(moc_rel)
    expansion = _expand_single_moc(moc_rel, set(), 0, max_depth)

    data = {
        "query_matches": [{"file": moc_rel, "line": 1, "content": f"MOC: {moc_name}"}],
        "moc_expansions": [expansion],
        "related_notes": [],
        "notes_loaded": [],
    }
    return format_output(data, f"MOC:{moc_name}")


# ── CLIエントリポイント ─────────────────────────────────
def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Zettelkasten Query Tool — 神書検索神器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  query_zettelkasten.py "CI-CD"
  query_zettelkasten.py "TDD" --max-results 5
  query_zettelkasten.py --moc "大願と掟"
  query_zettelkasten.py --list-mocs
        """
    )
    parser.add_argument("query", nargs="?", help="Search query string")
    parser.add_argument("--max-depth", type=int, default=MAX_DEPTH,
                        help=f"MOC expansion max depth (default: {MAX_DEPTH})")
    parser.add_argument("--max-results", type=int, default=MAX_RESULTS,
                        help=f"Max direct search results (default: {MAX_RESULTS})")
    parser.add_argument("--moc", type=str, help="Expand from a specific MOC by name")
    parser.add_argument("--list-mocs", action="store_true", help="List all MOC files")
    parser.add_argument("--json", action="store_true", help="Output raw JSON (for programmatic use)")

    args = parser.parse_args()

    # MOC一覧
    if args.list_mocs:
        print(list_all_mocs())
        return

    # MOC起点展開
    if args.moc:
        print(expand_from_moc(args.moc, args.max_depth))
        return

    # 検索クエリ必須
    if not args.query:
        parser.print_help()
        sys.exit(1)

    # 全文検索
    expanded_query = _expand_query(args.query)
    matches = rg_search(expanded_query, args.max_results)

    if args.json:
        data = moc_first_expand(matches, args.max_depth)
        print(json.dumps(data, ensure_ascii=False, indent=2, default=str))
    else:
        data = moc_first_expand(matches, args.max_depth)
        print(format_output(data, args.query))


if __name__ == "__main__":
    main()
