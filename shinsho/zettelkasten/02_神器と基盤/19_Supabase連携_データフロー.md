---
type: rule
title: 19_Supabase連携_データフロー
tags: [/, moc, 全体図, rls, 安全保障, 神器と基盤, データフロー, flutter実装]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 19_Supabase連携_データフロー

**カテゴリ**: 02_神器と基盤
**ソース**: supabase-renkei-shinsho.md §五, §七
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## Supabaseとのデータフロー

認証からCRUDまでの完全なデータフロー設計とテーブル命名の掟。

---

## データフロー三型

| 型 | 特徴 | 用途 |
|----|------|------|
| **直接対話型** | Flutter SDKで直接CRUD。`_client.from('tbl').select()` | 単純CRUD |
| **実体化同期型** | Hive即時保存→Supabaseバックグラウンド同期。競合は最終書き込み優先 | オフライン対応 |
| **神事仲介型** | Edge Functions（Deno）が `service_role` で仲介 | 課金・集計・管理 |

Edge Functionsの実装例: `supabase/functions/admin-stats/index.ts`

---

## テーブル命名の掟

- スネークケース: `reading_sessions`
- 主キーUUID: `id UUID PRIMARY KEY DEFAULT gen_random_uuid()`
- ユーザー所有: `user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE`
- 作成時刻: `created_at TIMESTAMPTZ DEFAULT NOW()`

---

## Flutterモデル対応

Supabaseカラム名（`user_id`）とDartフィールド名（`userId`）は異なるため、`fromJson`/`toJson`で変換。
モデルは純粋Dart（Flutter非依存）で `lib/domain/models/` に配置。

```dart
factory UserBook.fromJson(Map<String, dynamic> json) => UserBook(
  id: json['id'], userId: json['user_id'], ...
);
```

---

## 環境変数

- `.env`（Git管理外）: `SUPABASE_URL`, `SUPABASE_ANON_KEY`
- 読み出し: `lib/core/infrastructure/env.dart`（`flutter_dotenv`使用）

---

## Related
- [[17_Supabase連携_全体図.md]] — 全体アーキテクチャ
- [[18_Supabase連携_安全保障_RLS.md]] — RLS詳細
- [[20_Supabase連携_Flutter実装.md]] — Flutter側具象実装
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
