---
type: reference
title: 02_rpg-task_神器と骨組み
tags: [/, moc, 表の神器, コード適応, 現世カタログ, 神器と骨組み, flutter, rpg-task]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 02_rpg-task_神器と骨組み

**カテゴリ**: 03_現世カタログ
**ソース**: rpg-shinso.md §用いる神器/器の骨組み
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## rpg-taskの技術構成

---

## 神器

| 神器 | 用途 |
|------|------|
| Flutter（Dart SDK ^3.5.4） | UIフレームワーク |
| Provider（^6.1.5） | 状態管理 |
| Hive | ローカル永続化 |
| Google Fonts | フォント |

---

## アーキテクチャ

MVVMパターン:
```
screens/ → viewmodels/ → repositories/ → models/
```

| 層 | 主要ファイル | 役割 |
|----|-----------|------|
| View | `lib/screens/`（Guild/Battle/Temple/Town） | UI表示 |
| ViewModel | `lib/viewmodels/GameViewModel` | 全状態の中心 |
| Repository | `lib/repositories/` | Hiveアクセス |
| Model | `lib/models/` | データ型定義 |

---

## 状態管理の要点

- `GameViewModel` が全状態を `ChangeNotifier` で管理
- 各Screenは `context.watch<GameViewModel>()` で自動更新
- `setState()` はEphemeral状態（タブ選択等）のみ

v2.0では技術リファクタリング（ViewModel分割・DI導入）を計画（[[08_rpg-task_v2_技術リファクタ.md]]）。

---

## Related
- [[01_rpg-task_神想.md]] — 神想の芯
- [[../../02_神器と基盤/02_表の神器_Flutter.md]] — Flutterの全パッケージ
- [[../../02_神器と基盤/14_コード適応_Semantics体系.md]] — Semantics基盤（既適用）
- [[../03_MOC_現世カタログ.md]] — カテゴリハブへ戻る
