---
type: rule
title: 禁忌③ — ViewModelの神クラス化を禁ず
tags: [feature-first, viewmodel, architecture, rule, 三大禁忌]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 禁忌③：ViewModelの神クラス化を禁ず

**親ノート**: [[10_三大禁忌.md]]

## なぜ禁忌か

- 単一のViewModelに全状態が集中すると、試練が書けない
- 変更のたびに無関係な機能まで壊れる（回帰バグ）
- 眷属神への「この画面だけ」委任が不可能になる

## 分割の基準

| 粒度 | 例 | 状態の種類 |
|------|-----|-----------|
| 画面単位 | `GuildViewModel` | タスク一覧・フィルタ状態のみ |
| 機能単位 | `PlayerViewModel` | プレイヤーLv・XP・装備のみ |
| ドメイン単位 | `ShopViewModel` | 商品一覧・購入状態のみ |

## アンチパターン

```dart
// ❌ 神クラス：全画面の全状態を1つに
class GameViewModel {
  List<Task> tasks;
  Player player;
  ShopState shop;
  Settings settings;
  ThemeData theme;
  // ... さらに数十のフィールド
}
```

## Related
- [[10_三大禁忌.md]] — 三大禁忌ハブ
- [[08_絶対掟_FeatureFirst構造.md]] — Feature-First構造の掟
- [[17_禁忌_Widget200行超.md]] — 禁忌①
- [[18_禁忌_Feature跨ぎimport.md]] — 禁忌②
