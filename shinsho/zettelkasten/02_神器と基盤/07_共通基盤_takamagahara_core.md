---
type: reference
title: 07_共通基盤_takamagahara_core
tags: [/, moc, 表の神器, 共通基盤, core, 神器と基盤, 現世カタログ, flutter]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 07_共通基盤_takamagahara_core

**カテゴリ**: 02_神器と基盤
**ソース**: jingi.md §共通基盤
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## takamagahara_core：純粋Dartユーティリティ

全Flutter現世に共有される、**Flutter非依存**の純粋Dartパッケージ。
型定義・定数・汎用関数を提供する。

---

## 提供するもの

| カテゴリ | 内容 | 例 |
|---------|------|-----|
| 型定義 | 全現世共通のデータ型 | `UserId`, `Timestamp`, `Result<T>` |
| 定数 | 全現世共通の定数値 | バージョン情報、API Endpoint |
| 汎用関数 | 日付処理・文字列操作・バリデーション | `formatDate()`, `validateEmail()` |
| エラー型 | 共通エラーハンドリング | `AppException`, `NetworkException` |

---

## 使い方

```yaml
# 各現世の pubspec.yaml にて
dependencies:
  takamagahara_core:
    path: ../../packages/takamagahara_core
```

---

## 設計原則

- **Flutter非依存** — `dart:ui` や `package:flutter` に依存しない
- **純粋関数優先** — 副作用を避け、テスト容易性を確保
- **単一責任** — 1ファイル1関心事
- **後方互換** — 破壊的変更はメジャーバージョンアップ時のみ

---

> ディレクトリ構造の詳細は [[07_共通基盤_takamagahara_core_ディレクトリ構造.md]] を参照。

---

## Related
- [[08_共通基盤_takamagahara_ui.md]] — Flutter依存の共通UIパッケージ
- [[02_表の神器_Flutter.md]] — Flutterパッケージ構成
- [[03_現世カタログ/03_MOC_現世カタログ.md]] — 使用現世一覧
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
