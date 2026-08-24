---
type: reference
title: 検索評価セット_Phase3-2
tags: [分析と監査, 検索評価, benchmark, S級昇格, hybrid-search]
status: active
timestamp: 2026-07-07T00:00:00Z
phase: 3-2
corpus_size: 174
purpose: Phase3-3 ハイブリッド検索のS級品質ベンチマーク
tool_under_test: query_zettelkasten.py (ripgrep + synonyms.json + AND + MOCファースト)
---
# 検索評価セット (Search Evaluation Set) — Phase 3-2

**対象神器**: `query_zettelkasten.py` | **コーパス**: 174ノート / MOC被覆率100%
**採点方法・既知欠陥・合格ライン**: [[検索評価セット_採点と欠陥.md]]

## 評価クエリ 20問

### カテゴリA: 同義語ブリッジ（凡俗語→神聖語）— 7問

| # | クエリ(凡俗語) | 期待ノート | 合格基準 | baseline |
|---|---|---|---|---|
| A1 | `テスト 戦略` | `06_品質と試練/02_試験戦略_汎用.md` | 期待ノートがRecall@5に入る | FAIL(0件) |
| A2 | `バグ 検知` | `04_自律運営/06_Cron体系_具現化監察_直毘神.md` | 期待ノートがRecall@5に入る | FAIL(0件) |
| A3 | `デプロイ 手順` | `02_神器と基盤/06_現世降臨_CI_CD.md` | Hit@1で期待ノート | FAIL(0件) |
| A4 | `セキュリティ` | `02_神器と基盤/18_Supabase連携_安全保障_RLS.md` | Recall@5（語彙集のみは不可） | FAIL(0件) |
| A5 | `バージョン 命名` | `01_大願と掟/22_バージョン命名規則.md` | Hit@1で期待ノート | FAIL(0件) |
| A6 | `データベース 安全` | `02_神器と基盤/04_裏の神器_神庫_Supabase.md` | Recall@5 | FAIL(0件) |
| A7 | `会議 のやり方` | `01_大願と掟/05_絶対掟_四神相談.md` | Recall@5（語彙集のみは不可） | FAIL(語彙集のみ) |

### カテゴリB: 多概念AND — 4問

| # | クエリ | 期待ノート | 合格基準 | baseline |
|---|---|---|---|---|
| B1 | `Supabase RLS` | `02_神器と基盤/18_Supabase連携_安全保障_RLS.md`, `02_神器と基盤/17_Supabase連携_全体図.md` | 両方Recall@5 | PARTIAL |
| B2 | `依存性注入 Flutter` | `02_神器と基盤/16_コード適応_依存性注入.md` | Hit@1 | PASS |
| B3 | `E2E ADB` | `06_品質と試練/06_E2E試練手順_ADB自動化.md` | Recall@5 | PASS |
| B4 | `API 予算` | `05_戦略と外交/15_収益モデルとAPI予算.md` | Recall@5 | FAIL(0件) |

### カテゴリC: 単一概念の精度 — 4問

| # | クエリ | 期待ノート | 合格基準 | baseline |
|---|---|---|---|---|
| C1 | `Widget 200行` | `01_大願と掟/17_禁忌_Widget200行超.md` | Hit@1 | FAIL(8位) |
| C2 | `TDD 循環` | `01_大願と掟/06_絶対掟_TDD.md`, `06_品質と試練/01_TDD循環.md` | 少なくとも1つHit@1、両方Recall@5 | PARTIAL |
| C3 | `ストリーク` | `03_現世カタログ/📁_rpg-task/03_rpg-task_ストリーク.md` | Recall@5 | PASS |
| C4 | `トークン 最適化` | `04_自律運営/18_トークン消費最適化.md` | Hit@1 | FAIL(2位) |

### カテゴリD: MOCトラバーサル — 3問

| # | クエリ | 期待挙動 | 合格基準 | baseline |
|---|---|---|---|---|
| D1 | `品質 試練` | 06_MOC がヒット→Related展開 | `moc_expansions` に **06_MOC_品質と試練** が出現しE2E/TDD系が loaded_notes に含まれる | FAIL |
| D2 | `自律 Cron` | 04_MOC 経由でCron体系へ | Cron体系ノート ≥3件 | PASS |
| D3 | `現世 カタログ` | 03_MOC 展開 | `moc_expansions` に 03_MOC、rpg-task等へ到達 | PARTIAL |

### カテゴリE: エッジケース — 2問

| # | クエリ | 期待挙動 | 合格基準 | baseline |
|---|---|---|---|---|
| E1 | `禍津` | 神聖語単独・高頻度語 | 語彙集*以外*の実コンテンツが上位3件に≥2件 | PARTIAL |
| E2 | `恐竜の飼育方法` | コーパス外（ネガティブ） | 0件を正しく返す。誤ヒット無し | PASS(0件) |

## Related
- [[検索評価セット_採点と欠陥.md]] — 採点方法・既知欠陥・申し送り
- [[S級昇格計画.md]] — S級品質の全体計画
- [[08_MOC_分析と監査.md]] — カテゴリハブ
- [[../01_大願と掟/09_神聖語彙集.md]] — 同義語の源泉
