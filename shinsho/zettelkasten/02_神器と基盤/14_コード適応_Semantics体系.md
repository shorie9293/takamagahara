---
type: guide
title: 14_コード適応_Semantics体系
tags: [/, moc, 絶対掟, 共通基盤, 設計原則, コード適応, 神器と基盤, 試練可能コード]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 14_コード適応_Semantics体系

**カテゴリ**: 02_神器と基盤
**ソース**: code-adaptation-shinsho.md §三③④
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## Semantics + AppKeys：試練可能UIの二重網

コード適応の中核。Flutterの `Semantics` ウィジェットと `Key` により、あらゆる試練経路からUI要素を安定特定可能にする。

---

## SemanticHelper（`lib/core/accessibility/semantic_helper.dart`）

| メソッド | 用途 | testId命名 |
|---------|------|-----------|
| `interactive()` | ボタン・タップ可能要素 | `btn_add_task` |
| `container()` | 領域区切り。`explicitChildNodes` で子制御 | `sec_header` |
| `toggle()` | スイッチ・チェックボックス | `tgl_notifications` |
| `textField()` | テキスト入力 | `txt_task_title` |
| `listItem()` | リスト項目（`sortKey` で序数付与） | `item_task_0` |

型プレフィックス: `btn`, `tgl`, `txt`, `sec`, `nav`, `item`, `dlg`, `ico`

---

## AppKeys（`lib/core/testing/widget_keys.dart`）

全画面の試練用Keyを一元管理するstatic constクラス。Keyの重複をコンパイル時に防止。
画面ごとに命名: `guildScreen`, `guildFab`, `taskCardCheck` 等。

---

## Key vs SemanticsLabel 使い分け

| 観点 | Key | SemanticsLabel |
|------|-----|---------------|
| 保証 | Widgetのインスタンス同一性 | Widgetの意味的役割 |
| Finder | `find.byKey()` | `find.bySemanticsLabel()` |
| ADB連携 | ❌ 不可 | ✅ content-desc経由 |

**掟：重要Widgetには両方付与せよ。** Keyで同一性＋SemanticsLabelで意味＋ADB連携。

---

## アンチパターン

- ❌ レイアウト専用Widget（Padding, SizedBox）にSemantics付与 → ノイズ
- ❌ 情報過多ラベル（`addToCartButton__enabled__Add_to_Cart`）
- ✅ 操作可能要素・データ表示・領域区切りにのみ付与

---

## Related
- [[12_コード適応_8設計原則.md]] — 全8原則
- [[15_コード適応_ErrorBoundary.md]] — ErrorBoundary
- [[08_共通基盤_takamagahara_ui.md]] — SemanticHelperの配布パッケージ
- [[../01_大願と掟/07_絶対掟_試練可能コード.md]] — 試練可能コードの掟
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
