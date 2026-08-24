---
type: analysis
title: Flutterハーネス分析（天目一箇神）
tags: [/, flutterハーネス分析]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# Flutterハーネス分析（天目一箇神）

- **奏上日**: 皐月四日（2026-05-04）
- **奏上者**: 天目一箇神（アメノマヒトツ）— 工匠神
- **対象**: tsundoku-quest-flutter
- **元神書**: `shinsho/flutter-harness-analysis-20260504.md`

## 対象現世の規模

- Flutter SDK 3.27.4 / lib: 30.dart / test: 18.dart / 依存: supabase_flutter, riverpod, go_router

## 各工程の実測時間（WSL2）

- `flutter analyze` → 3.8秒（軽量）
- `flutter test` → 8.3秒（軽量〜中量）
- `dart format --set-exit-if-changed` → 1〜2秒
- `flutter test <単一>` → 〜2秒
- `flutter build apk --debug` → 推定60〜180秒（**重量**）
- `flutter build web` → 推定30〜90秒（**重量**）

**合計（分析＋テスト）≈ 12秒**。delegate_taskタイムアウトの原因は単体テストではない。

## delegate_task限界分析

### 根本原因：全体コンテキスト問題

- 単一工程の重さではなく、**コンテキスト転送＋再構築の蓄積**でタイムアウト
- 眷属神が神書＋AGENTS.md＋全コードを読み込むオーバーヘッドが支配的

### 失敗パターン

1. 大規模変更時にコンテキストが詰まる
2. 眷属神が不必要なファイルを読み込みすぎる
3. 並列召喚（4神同時）でAPIレート制限

## 教訓

- delegate_taskは「小タスク×多段階」より「中タスク×少数」が適正
- 眷属神に渡すコンテキストは必要最小限に（`context`パラメータを厳選）
- 静的解析＋単体テストはdelegate_task不要、直接 `terminal` で十分

Related: [[03_UX監査.md]] [[07_ハーネス設計5原則.md]]
