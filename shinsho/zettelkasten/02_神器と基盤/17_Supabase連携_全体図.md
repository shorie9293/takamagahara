---
type: reference
title: 17_Supabase連携_全体図
tags: [/, moc, 全体図, rls, 安全保障, 裏の神器, 神器と基盤, データフロー]
status: active
timestamp: 2026-06-17T00:00:00Z
---
# 17_Supabase連携_全体図

**カテゴリ**: 02_神器と基盤 | **ソース**: supabase-renkei-shinsho.md §二 | **最終更新**: 令和八年皐月二十六日（2026年5月26日）

---
## Supabase連携の全体アーキテクチャ

全Flutter現世がSupabase神庫と連携する際のデータの流れと安全保障の全体像。

---

## 鍵の使い分け——最も肝要

| 鍵 | 渡す相手 | 権能 | 漏洩時の禍 |
|----|---------|------|-----------|
| `anon key` | 現世（Flutter） | RLS制約下のみ | RLSあれば限定的 |
| `service_role key` | Edge Functionsのみ | RLS迂回・全能 | 神庫全データ漏洩 |

> `service_role` 鍵は決して現世コード・Gitに含めるべからず。必要時はEdge Functions（Deno）経由。

---

## 認証の型

| 神器 | 推奨用途 |
|------|---------|
| メール/パスワード | 標準入り口 |
| OAuth（Google/Apple） | 簡便入り口として併用 |
| マジックリンク | 低摩擦入門用 |
| 匿名認証 | 試遊・チュートリアル用 |

環境変数は `.env`（Git管理外）で管理：`SUPABASE_URL`, `SUPABASE_ANON_KEY`

---

## 初期化（main.dart）

```dart
await Supabase.initialize(url: Env.supabaseUrl, anonKey: Env.supabaseAnonKey);
```

実装詳細: `lib/core/infrastructure/supabase_provider.dart`, `lib/core/infrastructure/env.dart`

---

## データフローの三型

| 型 | 特徴 | 用途 |
|----|------|------|
| 直接対話型 | Flutter SDKで直接CRUD | 単純CRUD |
| 実体化同期型 | Hive（即時）+ Supabase（真実源）同期 | オフライン対応 |
| 神事仲介型 | Edge Functionsがservice_roleで仲介 | 課金・集計・管理 |

詳細: [[19_Supabase連携_データフロー.md]]

---

## Related
- [[18_Supabase連携_安全保障_RLS.md]] — RLSの完全詳細
- [[19_Supabase連携_データフロー.md]] — 三型の詳細
- [[20_Supabase連携_Flutter実装.md]] — Flutter SDK実装
- [[04_裏の神器_神庫_Supabase.md]] — 神庫選定
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
