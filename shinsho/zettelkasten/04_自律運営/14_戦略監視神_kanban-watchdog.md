---
type: strategy
title: 14_戦略監視神_kanban-watchdog
tags: [/, moc, 全体像, 自律運営, 発動の流れ, 戦略監視神, kanban-watchdog]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 14_戦略監視神_kanban-watchdog

**カテゴリ**: 04_自律運営
**ソース**: senryaku-kanshi-shinsho.md §発動の流れ（新規創生）
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## kanban-ready-watchdog.py — 戦略監視スクリプト

所在: `~/.hermes/scripts/kanban-ready-watchdog.py`

---

## 機能

1. `hermes kanban list --json` で全タスク取得
2. readyタスクをカウント
3. 全現世 `utsushiyo/*/docs/roadmap.md` と全神書を調査
4. ready ≥ 閾値 → `STATUS:OK`（エージェントは「静観」とだけ応答）
5. ready < 閾値 → 全現世調査レポートを注入

---

## 注入される文脈データ

- 各現世の試験数・版数
- 全道標の進捗状態（完了/未着手）
- ブロック中現世の一覧
- 創造主様の最新優先順位（jiritsu-gugenka-no-okite.md §三）

---

## Cron設定

- CronジョブID: `da28dec5577b`
- `no_agent=false`（LLM駆動）
- `dispatch_in_gateway=false`（手動制御）
- `max_parallel_jobs=2`

---

## Related
- [[12_戦略監視神_全体像.md]] — システム全体像
- [[13_戦略監視神_発動の流れ.md]] — 発動フロー
- [[04_MOC_自律運営.md]] — カテゴリハブ
