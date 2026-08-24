---
type: strategy
title: 03_試験戦略_rpg-task特化
tags: [/, moc, red, 品質の門, 試験戦略, tdd循環, 全現世共通, green]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 03_試験戦略_rpg-task特化

**カテゴリ**: 06_品質と試練
**ソース**: test-strategy-tsukuyomi-rpg-task.md §一〜十
**最終更新**: 令和八年皐月八日（2026年5月8日）
---

## 和風化リブランディングに伴う試験戦略

rpg-taskの全UI和風化を、TDDで安全に実行するための特化戦略。
---

## 変更範囲と影響マッピング

| 変更対象 | 変更内容 | 既存試験への影響 |
|---------|---------|----------------|
| 全4画面AppBar | 和風タイトル変更 | 回帰なし（AppBarテキスト未検証） |
| BottomNav | label/icon変更 | 回帰なし（BottomNav未検証） |
| 色定義 | `game_themes.dart` 全変更 | 既存色テストなし→新規作成必要 |
| 背景画像 | 差し替え | 目視確認のみ（自動検証不可） |
| テキスト29箇所 | グレードA〜D分類 | A(UI)7件要変更、B(ロア)8件推奨 |
---

## 7フェーズTDD計画

| フェーズ | 内容 | 独立可否 |
|---------|------|---------|
| Phase 0 | 既存66試験の基线確認＋静的ゲート | — |
| Phase 1 | 色定義変更＋ThemeDataテスト | 最初に実行 |
| Phase 2 | player_status_header分割（416→7Widget） | Phase 1と並行可 |
| Phase 3 | AppBarタイトル変更 | Phase 1完了後 |
| Phase 4 | BottomNav label/icon変更 | Phase 3と連続可 |
| Phase 5 | ダイアログ・スナックバー変更 | Phase 3/4と並行可 |
| Phase 6 | 背景画像差し替え（非TDD・手動検証） | — |
| Phase 7 | 全試験回帰確認＋dart analyze | 最終ゲート |
---

## Widgetテスト文字列検証戦略

| パターン | メソッド | 使用場面 |
|---------|---------|---------|
| 完全一致 | `find.text('和風名称')` | AppBar、ボタンラベル |
| 部分一致 | `find.textContaining('...')` | 動的テキスト（変数埋め込み） |
| Widget述語 | `find.byWidgetPredicate(...)` | 複数Textから特定抽出 |
推奨: 期待値は `test/test_constants.dart` に定数化。

## 色のリグレッションテスト

- ThemeData色プロパティ網羅（`test/core/theme/theme_data_test.dart`）
- 4ジョブでscaffoldBackgroundColorが異なること
- アクセシビリティ輝度チェック（背景輝度 < 0.18）
## 実装参照

- 色定義: `utsushiyo/rpg-task/lib/core/theme/game_themes.dart`
- 分割設計: test-strategy-tsukuyomi-rpg-task.md §八
---

## Related
- [[02_試験戦略_汎用.md]] — 全現世共通の試験アーキテクチャ
- [[01_TDD循環_RED_GREEN_REFACTOR.md]] — TDD基本循環
- [[08_品質の門_全現世共通.md]] — 品質ゲート詳細
- [[06_MOC_品質と試練.md]] — カテゴリハブ
