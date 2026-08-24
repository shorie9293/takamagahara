---
type: reference
title: 03_rpg-task_ストリーク
tags: [/, moc, ストリーク, 現世カタログ, rpg-task, キャラカスタマイズ]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 03_rpg-task_ストリーク

**カテゴリ**: 03_現世カタログ
**ソース**: rpg-shinso.md §連なり
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## ストリーク（連なり）システム

日々ログイン→タスク完了の継続をRPGの「冒険の歩み」として可視化。

---

## ロジック（GameViewModel内）

`loadData()` → `_checkAndUpdateStreak()`:
- `lastLoginDate == null` → streakDays=1
- `lastLoginDate == 昨日` → streakDays++
- `lastLoginDate == 今日` → 変更なし（一日複数回訪れても増加しない）
- `lastLoginDate < 昨日` → streakDays=1（絶たれ）
- いずれも `longestStreak = max(longestStreak, streakDays)`

---

## 報い表

| 日数 | 報い |
|------|------|
| 2日 | +100金貨 |
| 3日 | +200金貨 |
| 5日 | +500金貨 +5宝珠 |
| 7日 | +1000金貨 +20宝珠 |
| 14日 | +2000金貨 +50宝珠 |
| 30日 | +5000金貨 +150宝珠 |
| 他 | +50金貨（毎日） |

ストリーク報酬（`pendingStreakReward`）は既存のログインボーナス（`pendingLoginBonusAmount`）と積み重ねて表示。

---

## Related
- [[01_rpg-task_神想.md]] — 神想の芯
- [[06_rpg-task_v2_キャラカスタマイズ.md]] — ストリークと連動する装備解放
- [[../03_MOC_現世カタログ.md]] — カテゴリハブへ戻る
