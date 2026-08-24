#!/usr/bin/env python3
"""fix_dead_links.py — 死にリンク自動修復神器

link_linter.lint() の結果から、basenameで一意に解決できる死にリンクを自動修正。
曖昧・欠損分はログに残し手動/Opus判断へ。
"""

import re
import sys
from pathlib import Path
from link_linter import lint, ZETTELKASTEN_ROOT

def fix():
    report = lint()
    dead_links = report["dead_links"]
    if not dead_links:
        print("✅ 死にリンクなし")
        return 0

    LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
    fixed = 0
    ambiguous = 0
    not_found = 0
    remaining = []

    for d in dead_links:
        from_file = d["from"]
        link_text = d["link"]
        # エイリアス/アンカー除去
        base = link_text.split("|")[0].split("#")[0].strip()
        base_name = Path(base).name
        if not base_name.endswith(".md"):
            base_name += ".md"

        # 全ノートから basename で検索
        cands = list(ZETTELKASTEN_ROOT.rglob(base_name))
        # 自身を除外
        cands = [c for c in cands if c != ZETTELKASTEN_ROOT / from_file]

        if len(cands) == 0:
            not_found += 1
            remaining.append(d)
            continue
        elif len(cands) == 1:
            # 正しい相対パスを生成
            try:
                new_rel = str(cands[0].relative_to(ZETTELKASTEN_ROOT))
            except ValueError:
                new_rel = str(cands[0].relative_to(ZETTELKASTEN_ROOT))
            new_link = f"[[{new_rel}]]"

            # 元ファイル内のリンクを置換
            file_path = ZETTELKASTEN_ROOT / from_file
            content = file_path.read_text(encoding="utf-8")
            old_pattern = f"[[{link_text}]]"
            if old_pattern in content:
                content = content.replace(old_pattern, new_link)
                file_path.write_text(content, encoding="utf-8")
                fixed += 1
                print(f"✅ [{from_file}] {link_text} → {new_rel}")
            else:
                # パイプ記法など一部マッチしないケース
                remaining.append(d)
        else:
            ambiguous += 1
            remaining.append(d)
            print(f"⚠️  [{from_file}] {link_text} → {len(cands)}件候補: {[str(c.relative_to(ZETTELKASTEN_ROOT)) for c in cands[:3]]}")

    print(f"\n📊 結果: fixed={fixed}, not_found={not_found}, ambiguous={ambiguous}, remaining={len(remaining)}")
    if remaining:
        print("\n--- 要手動/Opus判断 ---")
        for d in remaining:
            print(f"  [{d['from']}] -> [[{d['link']}]]")
    return len(remaining)


if __name__ == "__main__":
    sys.exit(fix())
