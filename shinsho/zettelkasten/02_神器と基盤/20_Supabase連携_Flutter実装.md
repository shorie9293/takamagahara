---
type: reference
title: 20_Supabase連携_Flutter実装
tags: [/, moc, 全体図, rls, 安全保障, コード適応, 神器と基盤, 依存性注入]
status: active
timestamp: 2026-06-17T00:00:00Z
---
# 20_Supabase連携_Flutter実装

**カテゴリ**: 02_神器と基盤 | **ソース**: supabase-renkei-shinsho.md §三, §六 | **最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## Flutter側のSupabase実装パターン

Repositoryパターン＋DIを前提としたFlutter SDKの標準実装。

---

## 初期化

```dart
await Supabase.initialize(url: Env.supabaseUrl, anonKey: Env.supabaseAnonKey);
```

`lib/core/infrastructure/env.dart` で `.env` から読み出し（`flutter_dotenv`使用）。

---

## 三層構造

```
domain/repositories/book_repository.dart    ← 抽象IF（試練時Mock可能）
features/bookshelf/data/
  supabase_book_repository.dart             ← Supabase具象実装
```

- **抽象IF**: `abstract class BookRepository { Future<List<UserBook>> getMyBooks(); ... }`
- **具象**: `_client.from('user_books').select('*, books(*)').order('created_at')` 等
- **DI**: Riverpod `Provider<BookRepository>` で注入

RLSが自動でuser_idフィルタリング。`.eq('user_id', ...)` 明示も安全。
完全実装例: `utsushiyo/tsundoku-quest/lib/features/bookshelf/data/` 参照。

---

## 試練用Mock

`MockBookRepository implements BookRepository` → メモリ内リストで全操作模擬。

---

## 導入フェーズ

| Phase | 内容 |
|-------|------|
| 1 | 基盤（supabase_provider.dart, .env） |
| 2 | ドメイン層（モデル純粋Dart化＋抽象IF） |
| 3 | Feature実装（TDDで具象Repository） |
| 4 | 神庫定義（マイグレーション複製） |
| 5 | 試練（Mock＋flutter test --coverage） |

---

## Related
- [[17_Supabase連携_全体図.md]] — 全体アーキテクチャ
- [[18_Supabase連携_安全保障_RLS.md]] — RLS詳細
- [[19_Supabase連携_データフロー.md]] — データフロー
- [[16_コード適応_依存性注入.md]] — DIパターン
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
