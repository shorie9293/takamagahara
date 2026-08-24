---
type: guide
title: TDD Flutter実践 — コマンドと試練の種類
tags: [tdd, flutter, test, commands, 実践編]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# TDD Flutter実践編

**親ノート**: [[06_絶対掟_TDD.md]]

## FlutterでのTDD実行コマンド

```bash
# 全試練の実行
flutter pub get && flutter test --no-pub

# 特定ファイルの試練
flutter test test/path/to/test_file.dart

# 静的解析
flutter analyze

# 試練網羅率の確認
flutter test --coverage
```

## 試練の種類

| 種類 | 対象 | ツール |
|------|------|--------|
| 単位試練（Unit Test） | ViewModel・UseCase・Model | flutter_test |
| Widget試練 | 個別Widgetの表示・操作 | flutter_test |
| 統合試練（Integration Test） | 画面遷移・実機操作 | integration_test |

## Related
- [[06_絶対掟_TDD.md]] — 親ノート（TDD三段階と掟）
- [[../06_品質と試練/01_TDD循環_RED_GREEN_REFACTOR.md]] — TDDの詳細作法
- [[../06_品質と試練/02_試験戦略_汎用.md]] — 試験戦略の全体像
