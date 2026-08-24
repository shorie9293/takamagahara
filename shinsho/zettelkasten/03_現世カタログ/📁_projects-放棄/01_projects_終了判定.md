---
type: reference
title: 01_projects_終了判定
tags: [/, moc, 共通基盤, 終了判定, core, 現世カタログ, projects, takamagahara]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 01_projects_終了判定

**カテゴリ**: 03_現世カタログ
**ソース**: utsushiyo/projects/docs/roadmap.md
**最終更新**: 令和八年皐月二十五日（2026年5月25日）

---

## utsushiyo/projects/ — 共有パッケージ構想の現状と判断

所在: `utsushiyo/projects/docs/roadmap.md`

---

## 調査結果

`utsushiyo/projects/` には `takamagahara/test/features/town/viewmodels/shop_view_model_test.dart`（52行）のみが存在。
当初「全現世の共通パッケージ置き場」として想定されたが、実装が進まず放棄。

---

## 判定

- ❌ **放棄（Abandoned）** — 共通パッケージは `takamagahara_core` / `takamagahara_ui` に一本化
- 各現世のコードは `utsushiyo/<現世名>/` 直下で管理
- 残存ファイルは参照価値なし（`shop_view_model_test.dart` のみ）

---

## Related
- [[../../02_神器と基盤/07_共通基盤_takamagahara_core.md]] — 実質的な共通基盤
- [[../../02_神器と基盤/08_共通基盤_takamagahara_ui.md]] — UI共通基盤
- [[../03_MOC_現世カタログ.md]] — カテゴリハブへ戻る
