---
type: guide
title: 01_e2e-pipeline_個別道標
tags: [/, moc, 個別道標, e試練手順, adb自動化, 現世カタログ, e-pipeline, visionai判定]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 01_e2e-pipeline_個別道標

**カテゴリ**: 03_現世カタログ
**ソース**: utsushiyo/e2e-pipeline/docs/roadmap.md
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## 天浮橋計画（e2e-pipeline）ロードマップ

E2E自動テストパイプライン。ADB＋Flutter integration_testで端末実機（P30）の自動試験を実行。

所在: `utsushiyo/e2e-pipeline/`

---

## 現状（皐月二十六日）

| 項目 | 値 |
|------|-----|
| 創生 | 皐月一日〜二日 |
| コード規模 | Python 約1,300行 + Dart 約700行 |
| 試験数 | Flutter integration_test T2 ✅（506全試験通過） |
| **状態** | 🟢 Flutter integration_test移行中 |

---

## 進捗

| フェーズ | 状態 |
|----------|------|
| I1〜I8（integration_test移行基盤） | ✅ 完了 |
| T2（rpg_task_create_test.dart単独通過） | ✅ |
| I9〜I11（残integration_test） | 🔴 未着手 |
| T3〜T5（ADB方式から抽出） | 🔴 未着手 |

---

## Related
- [[../../06_品質と試練/06_E2E試練手順_ADB自動化.md]] — ADBパイプライン詳細
- [[../../06_品質と試練/07_E2E試練手順_VisionAI判定.md]] — Vision API判定
- [[../03_MOC_現世カタログ.md]] — カテゴリハブへ戻る
