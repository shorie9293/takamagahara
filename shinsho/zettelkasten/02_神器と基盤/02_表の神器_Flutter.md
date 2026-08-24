---
type: reference
title: 02_表の神器_Flutter
tags: [/, moc, 全体図, 絶対掟, 表の神器, コード適応, 神器と基盤, 神器選定の指針]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 02_表の神器_Flutter

**カテゴリ**: 02_神器と基盤
**ソース**: jingi.md §第一の神器
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## Flutter：高天原の主神器

高天原の主たる神器は **Flutter / Dart** なり。全現世の8割が此の神器にて鍛造さる。

---

## 全パッケージ構成

| 位 | 神器 | バージョン | 用途 |
|----|------|-----------|------|
| **器の枠** | Flutter | 3.27+（Dart SDK ^3.5.4） | iOS / Android 両開顕。単一コードベースで遍く世を征す |
| **心の在処（状態管理）** | Provider | ^6.1.5 | 小〜中規模の状態管理 |
| | Riverpod | ^2.6.0 | 大規模・複雑な依存関係 |
| **万物を納むる器（永続化）** | Hive | ^2.2.3 | 構造データのローカル保存 |
| | SharedPreferences | — | 簡易KV保存 |
| **神庫への通路** | Supabase Flutter SDK | ^2.8.0 | PostgreSQL + Auth + Realtime |
| **神機との縁** | Anthropic Claude / OpenAI API | — | Supabase Edge Functions経由 |
| **道案内（画面遷移）** | go_router | ^14.6.0 | 深層リンク対応、型安全ルーティング |
| **文様（フォント）** | Google Fonts | ^6.3.0 | 和風・RPGの装い |
| **符丁（ID生成）** | uuid | ^4.5.2 | 万物に一意の符丁 |

---

## 状態管理の選択基準

| 規模 | 推奨 | 理由 |
|------|------|------|
| 小（1〜3画面） | Provider | 学習コスト低・設定最小 |
| 中（4〜10画面） | Provider → Riverpod移行検討 | 依存関係が複雑化したら移行 |
| 大（10画面超） | Riverpod | コンパイル時安全・依存関係の明示 |

---

## 鍛造の規律（要約）

全Flutter現世は以下の規律に従う（詳細はコード適応ノート群 11〜16）：

1. **Feature-First構造** — 機能単位のディレクトリ構成
2. **試練可能なるUI** — Semantics + AppKeys + ErrorBoundary
3. **TDD** — RED → GREEN → REFACTOR
4. **依存性注入** — 外部依存の抽象化

---

## Related
- [[01_神器選定の指針.md]] — 新規現世の技術選定フロー
- [[../01_大願と掟/07_絶対掟_試練可能コード.md]] — Flutterコードの必須要件
- [[../01_大願と掟/08_絶対掟_FeatureFirst構造.md]] — Feature-Firstの掟
- [[11_コード適応_全体図.md]] — コード適応の全体像
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
