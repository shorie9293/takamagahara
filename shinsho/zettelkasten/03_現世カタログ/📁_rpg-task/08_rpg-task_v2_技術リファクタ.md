---
type: guide
title: 08_rpg-task_v2_技術リファクタ
tags: [/, moc, 品質の門, 設計原則, コード適応, 依存性注入, 現世カタログ, 技術リファクタ]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 08_rpg-task_v2_技術リファクタ

**カテゴリ**: 03_現世カタログ
**ソース**: rpg-task-v2-roadmap.md §五
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## v2.0 技術リファクタリング計画

中核3項目完了後の、コード品質と保守性を高める5項目。

---

## リファクタ項目

| 項目 | 目的 | 工数 |
|------|------|------|
| **GameViewModel分割** | 単一責任化。TaskVM/PlayerVM/ShopVM/SettingsVM/ThemeVMに5分割 | 4〜6h |
| **DI導入（get_it+injectable）** | テスト時Mock差替容易化 | 2〜3h |
| **Hive→Isar移行評価** | 型安全クエリ・Isolate対応・複合インデックス | 評価1h＋段階的移行 |
| **Feature Flagシステム** | 未完成機能の安全混在・A/Bテスト基盤（v1.4から前倒し） | 2〜3h |
| **イベントバス導入** | ViewModel間の疎結合化 | 1〜2h |

---

## 状態

🟢 完了（分割・DI）＋評価完了（Isar移行は非推奨）。

- **GameViewModel分割**: ✅ 完了。`game_view_model.dart` 1899行→342行のファサードへ。TaskVM/PlayerVM/ShopVM/SettingsVM/ThemeVM（＋TownVM/BattleVM）に委譲（`e85afb9`）。
- **DI導入**: ✅ 完了。`lib/core/di/injection.dart` ＋ `injection.config.dart`。get_it+injectable。二重構造解消済み（`6f5689f`）。
- **Hive→Isar移行**: ❌ 移行は**非推奨**と評価。Isarは2026年時点でメンテ停止（v4安定版未達、コミュニティフォークのみ）。代替として Hive→Hive CE（`hive_ce`）へのドロップイン移行を推奨。評価報告: `utsushiyo/rpg-task/docs/hive_to_isar_evaluation.md`。
- **Feature Flagシステム**: 🔴 未着手（別タスク）。
- **イベントバス導入**: 🔴 未着手（別タスク）。

実装詳細: `utsushiyo/rpg-task/lib/core/di/` 参照。

---

## Related
- [[09_rpg-task_v2_品質の門.md]] — 開顕前チェックリスト
- [[../../02_神器と基盤/16_コード適応_依存性注入.md]] — DIパターン
- [[../../02_神器と基盤/12_コード適応_8設計原則.md]] — 8原則
- [[../03_MOC_現世カタログ.md]] — カテゴリハブへ戻る
