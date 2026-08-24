---
type: guide
title: 15_API残金管理
tags: [/, moc, 全体像, 本体制, 自律運営, 戦略監視神, cron体系, api残金管理]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 15_API残金管理

**カテゴリ**: 04_自律運営
**ソース**: jiritsu-gugenka-no-okite.md §四、記憶域（新規創生）
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## API残金管理 — 金山毘古神（カナヤマ）の監視

毎週月曜9:00、OpenRouter/DeepSeek等のAPI残高を確認し、枯渇を未然に防ぐ。

---

## 監視対象

| API | 用途 | 確認方法 |
|-----|------|---------|
| OpenRouter | 全Cron JobのLLM駆動（nemotron無料枠） | OpenRouter Dashboard残高確認 |
| DeepSeek | 大国主命・一部Cron | DeepSeek API Platform残高確認 |

---

## 警報閾値

| レベル | 条件 | アクション |
|--------|------|----------|
| 🟢 健全 | $5.00以上 | 報告のみ |
| 🟡 注意 | $2.00〜$4.99 | #自律-定時 に注意喚起 |
| 🔴 危険 | $2.00未満 | #自律-警戒 に警報＋創造主様に召喚 |

---

## コスト目標

- 全日: **$1.50以下**（皐月二十五日 戦略監視神コスト最適化後）
- 全Cronは無料モデル（nemotron/openrouter）を優先
- 戦略監視神のみ `dispatch_in_gateway=false`（手動制御）

---

## Related
- [[02_Cron体系_12本体制.md]] — Cron 12本のモデル割当
- [[12_戦略監視神_全体像.md]] — 最大のAPI利用者
- [[04_MOC_自律運営.md]] — カテゴリハブ
