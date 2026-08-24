---
type: reference
title: 18_Supabase連携_安全保障_RLS
tags: [/, moc, 全体図, rls, 安全保障, 神器と基盤, データフロー, flutter実装]
status: active
timestamp: 2026-06-17T00:00:00Z
---
# 18_Supabase連携_安全保障_RLS

**カテゴリ**: 02_神器と基盤 | **ソース**: supabase-renkei-shinsho.md §四 | **最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## RLS（Row Level Security）——行ごとの結界

SupabaseのPostgRESTは `anon key` ひとつで全世界に神庫が晒され得る。
**RLSなくしてSupabase連携は在り得ず。**

---

## RLSの三大鉄則

1. **全テーブルに `ALTER TABLE <name> ENABLE ROW LEVEL SECURITY;`**
2. **`(SELECT auth.uid())` と括弧で包め** — 直に使うと行ごとに再評価され致命的な性能劣化
3. **ポリシーは `TO authenticated` を明示** — 省略すると匿名ユーザーにも適用

---

## 基本形（全CRUDポリシー）

全ユーザー所有テーブルは以下4ポリシーを定義：

- `FOR SELECT TO authenticated USING ((SELECT auth.uid()) = user_id)`
- `FOR INSERT TO authenticated WITH CHECK ((SELECT auth.uid()) = user_id)`
- `FOR UPDATE` + `FOR DELETE` も同様

マスターテーブルは `FOR SELECT USING (true)`、登録は `FOR INSERT WITH CHECK (auth.role() = 'authenticated')`。
JOIN経由の所有権検証は `EXISTS (SELECT 1 FROM parent WHERE id = child.parent_id AND user_id = (SELECT auth.uid()))`。

完全なSQL実装例: `utsushiyo/tsundoku-quest/supabase/migrations/001_initial_schema.sql`

---

## 性能最適化

| 技法 | 必須度 |
|------|--------|
| `(SELECT auth.uid())` 括弧化 | 🔴 必須 |
| `user_id` インデックス | 🔴 必須 |
| アプリ側 `.eq('user_id', ...)` | 🟡 推奨 |

---

## 七つの安全保障検め

| # | 検め | 致命度 |
|---|------|--------|
| ① | `grep -r "eyJ" lib/` → anon keyハードコードなし | 🔴 |
| ② | `SELECT ... WHERE rowsecurity=false;` → 0行 | 🔴 |
| ③ | `grep -r "service_role" lib/` → 空 | 🔴 |
| ④〜⑦ | ポリシー網羅性・他者不可視・性能・MFA | 🟡〜🟢 |

---

## Related
- [[17_Supabase連携_全体図.md]] — 全体アーキテクチャ
- [[19_Supabase連携_データフロー.md]] — データフロー
- [[20_Supabase連携_Flutter実装.md]] — Flutter実装
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
