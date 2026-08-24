---
type: reference
title: 13_コード適応_FeatureFirst詳細
tags: [/, moc, 絶対掟, 表の神器, 設計原則, 三大禁忌, コード適応, 神器と基盤]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 13_コード適応_FeatureFirst詳細

**カテゴリ**: 02_神器と基盤
**ソース**: code-adaptation-shinsho.md §三①, §五
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## Feature-First構造

全Flutter現世が従うべきディレクトリ構造の完全な定義。

---

## 標準構造

```
utsushiyo/<現世名>/
├── lib/
│   ├── core/                        # 共有基盤（全現世共通の3ファイル）
│   │   ├── accessibility/semantic_helper.dart
│   │   ├── testing/widget_keys.dart
│   │   └── error/error_boundary.dart
│   └── features/<機能名>/
│       ├── data/          → Repository具象実装（Supabase/Hive）
│       ├── domain/        → UseCase, Entity（純粋Dart）
│       └── presentation/  → Screen, ViewModel, Widgets
├── test/{widget/, integration/}
└── analysis_options.yaml  （const lint有効化済み）
```

---

## 恩恵

- 変更の局所化：1機能のUI変更がそのfeature内で完結
- 試練の独立：機能ごとのテストが他機能変更で壊れない
- マージ衝突減少（Startup House 2026実測：リファクタ時間25%減）

---

## 新規現世テンプレート

必ず `core/` に上記3ファイルを配置し、最初の画面からSemanticHelperを適用すること。
詳細な検証方法は [[../01_大願と掟/08_絶対掟_FeatureFirst構造.md]] 参照。

---

## Three Major Taboos

① Widget1ファイル200行超禁止 ② Feature跨ぎimport統一（`package:` 基準）③ ViewModelの神クラス化禁止

---

## Related
- [[../01_大願と掟/08_絶対掟_FeatureFirst構造.md]] — Feature-Firstの掟
- [[../01_大願と掟/10_三大禁忌.md]] — 三大禁忌
- [[12_コード適応_8設計原則.md]] — 全8原則
- [[02_表の神器_Flutter.md]] — Flutterパッケージ構成
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
