---
type: reference
title: 08_共通基盤_takamagahara_ui
tags: [/, ui, moc, 絶対掟, 共通基盤, core, コード適応, 神器と基盤]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 08_共通基盤_takamagahara_ui

**カテゴリ**: 02_神器と基盤
**ソース**: jingi.md §共通基盤
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## takamagahara_ui：共通UI基盤

全Flutter現世に共有されるFlutter依存UIパッケージ。

---

## 提供するもの

| カテゴリ | 内容 |
|---------|------|
| 共通テーマ | 和風・RPGテーマ（ThemeData） |
| 共通Widget | ボタン・カード・ダイアログ |
| SemanticHelper | `interactive()` 他 — 詳細 [[14_コード適応_Semantics体系.md]] |
| ErrorBoundary | 例外捕捉＋フォールバックUI — 詳細 [[15_コード適応_ErrorBoundary.md]] |
| AppKeys管理 | 全画面試練用Key一元管理 |

---

## 使い方

```yaml
dependencies:
  takamagahara_ui:
    path: ../../packages/takamagahara_ui
```

構造: `lib/src/{theme/, widgets/, accessibility/, error/, testing/}` → barrel export。

---

## 反映状況

rpg-task ✅ | tsundoku-quest-flutter ✅ | election-game ✅ | Kozuchi ✅ | book-review-app ✅

---

## Related
- [[07_共通基盤_takamagahara_core.md]] — 純粋Dartパッケージ
- [[14_コード適応_Semantics体系.md]] — SemanticHelper詳細
- [[15_コード適応_ErrorBoundary.md]] — ErrorBoundary詳細
- [[../01_大願と掟/07_絶対掟_試練可能コード.md]] — 試練可能コードの掟
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
