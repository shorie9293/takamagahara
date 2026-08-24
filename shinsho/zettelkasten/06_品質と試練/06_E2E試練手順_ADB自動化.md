---
type: guide
title: 06_E2E試練手順_ADB自動化
tags: [/, moc, 思想と方法, e試練手順, 品質と試練, シナリオ一覧, adb自動化, visionai判定]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 06_E2E試練手順_ADB自動化

**カテゴリ**: 06_品質と試練
**ソース**: [★新規] e2e-test-procedure.md §四〜五 / e2e-pipeline実装
**最終更新**: 令和八年皐月二十六日（2026年5月26日）
---

## ADBを使った完全自動E2E試練

P30実機上でrpg-task全6シナリオを自動実行、Vision APIで合否判定。
---

## パイプライン構成（`utsushiyo/e2e-pipeline/`）

| モジュール | 責務 |
|-----------|------|
| `e2e_pipeline.py` | シナリオ順次実行と統括 |
| `adb_utils.py` | タップ・スワイプ・テキスト入力・画面キャプチャ |
| `vision_utils.py` | スクリーンショット合否判定 |
| `report_utils.py` | JSONレポート生成 |
---

## ADB操作

| 操作 | コマンド | 制約 |
|------|---------|------|
| 起動 | `am start -n com.shorie.lifequest/.MainActivity` | — |
| タップ | `input tap X Y` | 座標はVision API動的検出 |
| スワイプ | `input swipe X1 Y1 X2 Y2` | 削除操作 |
| テキスト | `input text "ascii"` | 日本語不可 |
| 戻る | `input keyevent 4` | — |
| 撮影 | `exec-out screencap -p > file.png` | 1080×2340 |

---

## 制約と対策

| 制約 | 対策 |
|------|------|
| 日本語不可 | ASCIIテストデータ |
| IME変換 | `input keyevent` 逐次 |
| 座標ハードコード不可 | Vision API動的検出 |

---

## 実行フロー

```
adb connect → 起動 → for S01..S06: 前提→実行→撮影→Vision判定→記録
→ JSONレポート出力 → 奏上
```

## CI統合

GitHub Actions定期（1日1回）、`hermes cronjob` 深夜発動。
---

## Related
- [[04_E2E試練手順_思想と方法.md]] — 設計思想
- [[05_E2E試練手順_シナリオ一覧.md]] — 全6シナリオ
- [[07_E2E試練手順_VisionAI判定.md]] — Vision API判定
- [[06_MOC_品質と試練.md]] — カテゴリハブ
