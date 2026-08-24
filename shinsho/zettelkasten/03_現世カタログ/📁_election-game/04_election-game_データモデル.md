---
type: reference
title: 04_election-game_データモデル
tags: [/, moc, 個別道標, 市民目線, 社会ムード, 現世カタログ, データモデル, election-game]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 04_election-game_データモデル

**カテゴリ**: 03_現世カタログ
**ソース**: election-game-citizen-shinso.md §第二章
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## election-game：データモデル概要

5つの主要モデル。実装詳細は `utsushiyo/election-game/lib/models/` に委ねる。

---

## モデル一覧

| モデル | 役割 | 主要フィールド |
|--------|------|--------------|
| **Citizen** | プレイヤー市民 | name, job, concerns（最大3）, lifeParams（6値） |
| **Candidate** | 候補者 | name, faction, policies（3〜5）, policyEffects, personality |
| **Policy** | 公約 | title, description, category, effects（生活パラメータ変化） |
| **PoliticalGroup** | 政治団体 | name, ideology, economicAxis（-1〜+1）, welfareAxis（-1〜+1） |
| **SocietyState** | 社会状態 | happiness, mood（0〜1）, currentLeaderId, electionCount |

---

## 政治団体（5団体）

| 団体 | 経済軸 | 福祉軸 |
|------|--------|--------|
| 発展の会 | +0.8（自由市場） | -0.2 |
| 共生の会 | -0.3 | +0.9（社会保障重視） |
| 守りの会 | -0.5 | 0.0 |
| 緑の会 | -0.6 | +0.4 |
| 改革の会 | +0.2 | +0.3 |

---

## Related
- [[01_election-game_神想_市民目線.md]] — コア概念
- [[02_election-game_社会ムード.md]] — SocietyStateの活用
- [[06_election-game_個別道標.md]] — 現状の試験数・版数
- [[../03_MOC_現世カタログ.md]] — カテゴリハブへ戻る
