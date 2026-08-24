#!/usr/bin/env python3
"""graph_metrics.py — 神書グラフ健全性メトリクス計測神器

Zettelkastenのグラフ構造メトリクスを算出:
  - ノード数/エッジ数/平均次数
  - MOC被覆率（全ノートがTakamagahara_MOCから到達可能か）
  - 孤立率
  - 最大連結成分サイズ

Usage:
    python3 graph_metrics.py
    python3 graph_metrics.py --json
"""

import re
import sys
import json
from pathlib import Path
from collections import defaultdict, deque

ZETTELKASTEN_ROOT = Path.home() / "Takamagahara" / "shinsho" / "zettelkasten"
LINK_RE = re.compile(r"\[\[([^\]]+)\]\]")


def build_graph() -> dict[str, set[str]]:
    """全ノートの双方向リンクグラフを構築。"""
    graph = defaultdict(set)
    all_files = {}

    for f in sorted(ZETTELKASTEN_ROOT.rglob("*.md")):
        rel = str(f.relative_to(ZETTELKASTEN_ROOT))
        all_files[rel] = f

    # resolve_link (link_linter.py と同ロジック)
    def resolve(link: str, from_rel: str) -> str | None:
        link = link.split("|")[0].split("#")[0].strip()
        from_dir = (ZETTELKASTEN_ROOT / from_rel).parent
        try:
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
            if resolved.exists():
                return str(resolved.relative_to(ZETTELKASTEN_ROOT))
        except (ValueError, OSError):
            pass
        return None

    for rel, f_path in all_files.items():
        content = f_path.read_text(encoding="utf-8")
        for link in LINK_RE.findall(content):
            target = resolve(link, rel)
            if target and target != rel and target in all_files:
                graph[rel].add(target)
                graph[target].add(rel)  # 双方向

    return dict(graph)


def compute_metrics() -> dict:
    graph = build_graph()
    all_nodes = set()
    for f in ZETTELKASTEN_ROOT.rglob("*.md"):
        all_nodes.add(str(f.relative_to(ZETTELKASTEN_ROOT)))

    # 次数
    degrees = {n: len(graph.get(n, set())) for n in all_nodes}
    avg_degree = sum(degrees.values()) / len(all_nodes) if all_nodes else 0
    max_degree = max(degrees.values()) if all_nodes else 0
    orphans = [n for n, d in degrees.items() if d == 0]

    # MOC到達可能性（BFS）
    root_moc = "Takamagahara_MOC.md"
    reachable = set()
    if root_moc in all_nodes:
        q = deque([root_moc])
        while q:
            node = q.popleft()
            if node in reachable:
                continue
            reachable.add(node)
            for neighbor in graph.get(node, set()):
                if neighbor not in reachable:
                    q.append(neighbor)

    # 連結成分
    visited = set()
    components = []
    for node in all_nodes:
        if node not in visited:
            comp = set()
            q = deque([node])
            while q:
                n = q.popleft()
                if n in visited:
                    continue
                visited.add(n)
                comp.add(n)
                for neighbor in graph.get(n, set()):
                    if neighbor not in visited:
                        q.append(neighbor)
            components.append(comp)

    moc_coverage = len(reachable) / len(all_nodes) * 100 if all_nodes else 0

    return {
        "total_nodes": len(all_nodes),
        "total_edges": sum(len(v) for v in graph.values()) // 2,
        "avg_degree": round(avg_degree, 2),
        "max_degree": max_degree,
        "orphan_rate": round(len(orphans) / len(all_nodes) * 100, 1),
        "orphan_count": len(orphans),
        "moc_reachable_nodes": len(reachable),
        "moc_coverage_pct": round(moc_coverage, 1),
        "connected_components": len(components),
        "largest_component_size": max(len(c) for c in components) if components else 0,
        "largest_component_pct": round(max(len(c) for c in components) / len(all_nodes) * 100, 1) if components else 0,
        "orphan_nodes": orphans[:20],  # 先頭20件のみ
    }


def main():
    as_json = "--json" in sys.argv
    report = compute_metrics()
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("⛩️ Zettelkasten Graph Metrics")
        print(f"  Total nodes:        {report['total_nodes']}")
        print(f"  Total edges:        {report['total_edges']}")
        print(f"  Avg degree:         {report['avg_degree']}")
        print(f"  Max degree:         {report['max_degree']}")
        print(f"  MOC coverage:       {report['moc_coverage_pct']}%")
        print(f"  Orphan rate:        {report['orphan_rate']}% ({report['orphan_count']} nodes)")
        print(f"  Connected comps:    {report['connected_components']}")
        print(f"  Largest component:  {report['largest_component_size']} ({report['largest_component_pct']}%)")
    sys.exit(0)


if __name__ == "__main__":
    main()
