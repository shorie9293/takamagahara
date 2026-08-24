#!/usr/bin/env python3
"""
link_linter.py — 神書リンク健全性検査神器 (Zettelkasten Link Integrity Linter)

全 .md ファイルの [[...]] リンクを走査し、以下を報告する:
  - dead_links: 実ファイルに解決できないリンク
  - orphan_notes: どこからも被リンクされていないノート（MOC除く）
  - no_outbound_notes: 発リンクを持たないノート

Usage:
    python3 link_linter.py            # 人間可読サマリ
    python3 link_linter.py --json     # cron 消費用 JSON

Exit code: 0 = 全リンク健全 / 1 = dead link あり（cron アラート用）
"""

import re
import sys
import json
from pathlib import Path
from typing import Optional

ZETTELKASTEN_ROOT = Path.home() / "Takamagahara" / "shinsho" / "zettelkasten"
LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def resolve_link(link: str, from_file: str) -> Optional[Path]:
    """[[...]] 記法を実ファイルに解決（query_zettelkasten.py と同一ロジック）。"""
    link = link.split("|")[0].split("#")[0].strip()  # エイリアス/アンカー除去
    from_dir = (ZETTELKASTEN_ROOT / from_file).parent
    if link.startswith("./"):
        resolved = (from_dir / link[2:]).resolve()
    elif link.startswith("../"):
        resolved = (from_dir / link).resolve()
    elif "/" in link:
        resolved = ZETTELKASTEN_ROOT / link
    else:
        resolved = from_dir / link
    if not resolved.suffix:
        resolved = resolved.with_suffix(".md")
    return resolved if resolved.exists() else None


def lint() -> dict:
    md_files = sorted(ZETTELKASTEN_ROOT.rglob("*.md"))
    all_rel = {str(f.relative_to(ZETTELKASTEN_ROOT)) for f in md_files}

    dead_links = []
    inbound = {rel: 0 for rel in all_rel}
    no_outbound = []

    for f in md_files:
        rel = str(f.relative_to(ZETTELKASTEN_ROOT))
        content = f.read_text(encoding="utf-8")
        links = LINK_RE.findall(content)
        if not links:
            no_outbound.append(rel)
            continue
        for link in links:
            resolved = resolve_link(link, rel)
            if resolved is None:
                dead_links.append({"from": rel, "link": link})
            else:
                tgt = str(resolved.relative_to(ZETTELKASTEN_ROOT))
                if tgt in inbound:
                    inbound[tgt] += 1

    orphans = [rel for rel, n in inbound.items()
               if n == 0 and "MOC" not in Path(rel).name.upper()]

    return {
        "total_notes": len(md_files),
        "dead_link_count": len(dead_links),
        "dead_links": dead_links,
        "orphan_count": len(orphans),
        "orphan_notes": sorted(orphans),
        "no_outbound_count": len(no_outbound),
        "no_outbound_notes": sorted(no_outbound),
    }


def main():
    as_json = "--json" in sys.argv
    report = lint()
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"⛩️ Zettelkasten Link Integrity Report")
        print(f"  Total notes:      {report['total_notes']}")
        print(f"  Dead links:       {report['dead_link_count']}")
        print(f"  Orphan notes:     {report['orphan_count']}")
        print(f"  No-outbound notes:{report['no_outbound_count']}")
        if report["dead_links"]:
            print("\n  --- Dead links ---")
            for d in report["dead_links"]:
                print(f"    [{d['from']}] -> [[{d['link']}]]")
    sys.exit(1 if report["dead_link_count"] > 0 else 0)


if __name__ == "__main__":
    main()
