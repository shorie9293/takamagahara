---
type: spec
title: tsundoku-quest Adventurer System (冒険者ステータス)
tags: [tsundoku-quest, adventurer, stats, ステータス, cross-service]
status: stub
timestamp: 2026-07-07T00:00:00Z
---

# tsundoku-quest Adventurer System (冒険者ステータス)

**status**: stub — 詳細神想は未策定。クロスサービス報酬設計から参照される受け皿ノート。

## Summary

tsundoku-quest における読者を「冒険者」として表現するステータス体系。
読書進捗（完読・連続日数・XP・ページ数）が冒険者ステータスとして蓄積され、
クロスサービス報酬イベントとして rpg-task へ送出される。

## 送出イベント（クロスサービス報酬より）

7 event types: `book_completed`, `reading_streak`, `level_up`, `xp_milestone`,
`trophy_written`, `daily_mission_complete`, `pages_milestone`。

Transport: JSONL (`/data/local/tmp/takamagahara_shared/tsundoku_reward_events.jsonl`)
Identity: Supabase `auth.users(id)`。

## Related
- [[../03_現世カタログ/08_クロスサービス報酬設計.md]] — ステータスを消費するクロスサービス報酬ロジック
- [[../03_現世カタログ/📁_tsundoku-quest/01_tsundoku-quest_神想.md]] — tsundoku-quest 神想
