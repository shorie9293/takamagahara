#!/usr/bin/env python3
"""schema_linter.py — 神書 frontmatter スキーマ検証神器

全 .md ファイルのYAML frontmatterを検証し、以下をチェック:
  - type/title/tags/status/timestamp 必須
  - type の語彙制限
  - 70行上限（掟）
  - Related: 節の存在
  - ファイル名に [[...]] のパイプエスケープ崩れがないか

Usage:
    python3 schema_linter.py
    python3 schema_linter.py --json
"""

import re
import sys
import json
import yaml
from pathlib import Path
from collections import Counter

ZETTELKASTEN_ROOT = Path.home() / "Takamagahara" / "shinsho" / "zettelkasten"
VALID_TYPES = {"rule", "guide", "hub", "analysis", "spec", "moc", "reference",
               "audit", "catalog", "history", "strategy", "index", "glossary"}


def lint_schema() -> dict:
    violations = []
    type_counts = Counter()
    missing_related = []
    over_length = []

    for f in sorted(ZETTELKASTEN_ROOT.rglob("*.md")):
        rel = str(f.relative_to(ZETTELKASTEN_ROOT))
        content = f.read_text(encoding="utf-8")

        # YAML frontmatter 抽出
        fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        fm = {}
        if fm_match:
            try:
                fm = yaml.safe_load(fm_match.group(1)) or {}
            except yaml.YAMLError:
                violations.append({"file": rel, "issue": "YAML frontmatter parse error"})
                continue
        else:
            violations.append({"file": rel, "issue": "No YAML frontmatter"})
            continue

        # 必須フィールド
        for key in ["type", "title", "tags", "status", "timestamp"]:
            if key not in fm or fm[key] is None:
                violations.append({"file": rel, "issue": f"Missing required field: {key}"})
            elif key == "type" and fm[key] not in VALID_TYPES:
                violations.append({"file": rel, "issue": f"Invalid type '{fm[key]}'. Valid: {sorted(VALID_TYPES)}"})

        # タイプカウント
        if fm.get("type"):
            type_counts[fm["type"]] += 1

        # 70行上限
        line_count = len(content.split("\n"))
        if line_count > 70:
            over_length.append({"file": rel, "lines": line_count})

        # Related: 節の存在
        if "Related" not in content and "related" not in content.lower():
            missing_related.append(rel)

        # エスケープ崩れ [[...\|
        if re.search(r"\[\[[^]]*\\\\\|", content):
            violations.append({"file": rel, "issue": "Broken pipe escape in link: [[...\\\\|...]]"})

    return {
        "total_notes": sum(1 for _ in ZETTELKASTEN_ROOT.rglob("*.md")),
        "violations": violations,
        "violation_count": len(violations),
        "type_distribution": dict(type_counts),
        "over_70_lines": over_length,
        "over_70_count": len(over_length),
        "missing_related": missing_related,
        "missing_related_count": len(missing_related),
        "valid_types": sorted(VALID_TYPES),
    }


def main():
    as_json = "--json" in sys.argv
    report = lint_schema()
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("⛩️ Zettelkasten Schema Lint Report")
        print(f"  Total notes:        {report['total_notes']}")
        print(f"  Violations:         {report['violation_count']}")
        print(f"  Over 70 lines:      {report['over_70_count']}")
        print(f"  Missing Related:    {report['missing_related_count']}")
        if report["violations"]:
            print("\n--- Violations ---")
            for v in report["violations"][:20]:
                print(f"  [{v['file']}] {v['issue']}")
        if report["over_70_lines"]:
            print("\n--- Over 70 lines ---")
            for o in report["over_70_lines"]:
                print(f"  [{o['file']}] {o['lines']} lines")
    sys.exit(1 if report["violation_count"] > 0 else 0)


if __name__ == "__main__":
    main()
