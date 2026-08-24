---
type: reference
title: 15_コード適応_ErrorBoundary
tags: [/, moc, 全体図, 共通基盤, コード適応, 神器と基盤, semantics体系, takamagahara]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 15_コード適応_ErrorBoundary

**カテゴリ**: 02_神器と基盤
**ソース**: code-adaptation-shinsho.md §三⑥
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## ErrorBoundary：画面単位の例外安全

1Widgetの例外でアプリ全体をクラッシュさせない。仕様変更による禍津の影響を局所化する。

---

## 三層設定（配置: `lib/core/error/error_boundary.dart`）

| 層 | 設定箇所 | 捕捉対象 |
|----|---------|---------|
| ① Widget内 | `ErrorWidget.builder`（main.dart） | Widget構築時例外 |
| ② フレームワーク | `FlutterError.onError` | 非同期エラー |
| ③ Platform | `PlatformDispatcher.instance.onError` | ゾーン外例外 |

---

## 使用パターン

各画面を `ErrorBoundary` で囲う。エラー時はフォールバックUI（エラーアイコン＋再試行ボタン）表示。
開発時は詳細表示、本番時は簡易表示。

```dart
// 全画面をErrorBoundaryで囲う
ErrorBoundary(child: GuildScreen()),
ErrorBoundary(child: BattleScreen()),
```

---

## 恩恵

- 部分障害耐性：ギルド画面のバグでアプリ全体が落ちない
- 仕様変更耐性：新機能追加で一部が壊れても継続動作
- デバッグ容易性：エラー発生画面の特定が容易

---

## 落とし穴

- 開発中にエラーが飲み込まれないよう、開発ビルド時は詳細表示
- `dispose()` 時エラーは `FlutterError.onError` で捕捉

---

## Related
- [[14_コード適応_Semantics体系.md]] — Semantics+AppKeys
- [[11_コード適応_全体図.md]] — 三本柱の全体像
- [[08_共通基盤_takamagahara_ui.md]] — ErrorBoundaryの配布パッケージ
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
