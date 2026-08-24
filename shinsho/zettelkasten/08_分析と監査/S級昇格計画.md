---
type: audit
title: Zettelkasten S級昇格計画 — B→Sへの三段階神域
tags: [監査, 計画, S級]
status: active
timestamp: 2026-07-07T00:00:00Z
---
# Zettelkasten S級昇格計画

> B判定→S判定（A超え・最高位）への三段階実行計画。FLASH=DeepSeek V4 Flash:free 実行可 / OPUS=天照推論要。

## 現状診断（2026-07-07 実測）
- ノート171件 / Dead links 19（**17件は相対パス基準誤り**、2件真の欠損）/ Orphan 13 / No-outbound 4 / Frontmatter 100%
- 死リンク内訳: 単純パス誤り12件・存在しない参照5件・プレースホルダ1件・エイリアス1件

## Phase 1 — Consistency 完全化（Dead/Orphan 0 恒久保証）
- **1-1 [FLASH]**: `fix_dead_links.py`（決定的アルゴリズムで機械修復、曖昧分のみ1-2へ）→ 19→5以下
- **1-2 [OPUS]**: 欠損参照5件を意味理解で張替え → dead=0
- **1-3 [FLASH]**: Orphan 13件をMOCへ接続（双方向リンク）→ orphan=0
- **1-4 [FLASH]**: pre-commit/CIゲート化（`link_linter.py` でコミット拒否 + 日次cron通知）

## Phase 2 — Sustainability 自動化（1000ノート耐性）
- **2-1 [FLASH]**: `schema_linter.py`（frontmatter必須5項目・70行上限・Related存在を検証）
- **2-2 [FLASH]**: スキーマ違反の一括是正（欠落補完・70行超は分割候補として警告）
- **2-3 [FLASH]**: `graph_metrics.py`（MOC到達率100%を自動計測・日次cron）
- **2-4 [OPUS]**: 1000ノート青写真の設計判断 → `スケール設計指針.md`（1回のみ）

## Phase 3 — Retrieval Quality & Hybrid RAG
- **3-1 [FLASH]**: `synonyms.json`（凡俗↔神聖語彙辞書）+ query_zettelkasten.py にBM25+同義語展開 → 凡俗語クエリのrecall改善
- **3-2 [OPUS]**: 検索評価セット20問＋正解ノート（[[検索評価セット_Phase3-2.md]]）＋埋め込み設計（ローカル・無料）
- **3-3 [FLASH]**: `build_embeddings.py` + `--hybrid`（α*BM25+(1-α)*cosine）。ヒットにBM25/意味/原文を併記し監査可能性維持
- **3-4 [FLASH]**: `CLAUDE.md`→`AGENTS.md` のシンボリックリンク化（二重管理排除）

## コスト集計
| Phase | FLASH | OPUS | Opus想定 |
|-------|-------|------|---------|
| 1 | 1-1,1-3,1-4 | 1-2 | ~5分 |
| 2 | 2-1,2-2,2-3 | 2-4 | ~10分 |
| 3 | 3-1,3-3,3-4 | 3-2 | ~15分 |
| **計** | **9本** | **3本** | **~30分** |

## S級達成条件（全てFLASHで測定可）
1. `link_linter.py`: dead=0, orphan=0, no_outbound=0
2. `schema_linter.py`: 違反=0
3. `graph_metrics.py`: MOC到達率=100%
4. pre-commit hook が壊れリンク拒否（実証済）
5. 検索評価セット recall@5 ≥ 90%（ハイブリッド）
6. `readlink CLAUDE.md` = AGENTS.md

## Related
- [[../04_自律運営/04_MOC_自律運営.md]]
- [[../08_分析と監査/08_MOC_分析と監査.md]]
- [[検索評価セット_Phase3-2.md]] — 評価基盤
