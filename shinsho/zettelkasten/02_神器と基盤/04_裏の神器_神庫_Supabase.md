---
type: reference
title: 04_裏の神器_神庫_Supabase
tags: [/, 神庫, moc, 全体図, rls, 表の神器, 安全保障, 裏の神器]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 04_裏の神器_神庫_Supabase

**カテゴリ**: 02_神器と基盤
**ソース**: jingi.md §神庫
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## 神庫（データベース）の全体構成

高天原のデータ永続化は三層構造。

---

## 三層の神庫

| 神器 | 種別 | 用途 |
|------|------|------|
| **Supabase**（`^2.8.0`） | クラウド神庫 | PostgreSQL + Auth + Realtime + Storage + Edge Functions |
| **Hive**（`^2.2.3`） | ローカル神庫 | 高速・オフライン構造データ |
| **SharedPreferences** | 簡易KV | 設定値・フラグ |

---

## Supabase（主神庫）

提供機能: PostgreSQL・Auth（メール/OAuth/匿名/マジックリンク）・Realtime（WebSocket）・Storage・Edge Functions（Deno）

> ⚠️ **RLS（Row Level Security）必須。** RLSなくしてSupabase連携は在り得ず。詳細: [[18_Supabase連携_安全保障_RLS.md]]

---

## Hive（ローカル補完）

型安全ローカルNoSQL。オフライン動作の要。Supabase非依存データはHiveに保存。

---

## 選択基準

| 条件 | 選択 |
|------|------|
| 複数端末同期 | Supabase |
| オフライン必須 | Hive |
| 簡易設定値 | SharedPreferences |
| 認証必要 | Supabase Auth |
| 大規模バイナリ | Supabase Storage |

---

## Related
- [[17_Supabase連携_全体図.md]] — Supabase連携全体像
- [[18_Supabase連携_安全保障_RLS.md]] — RLS必須設定
- [[02_表の神器_Flutter.md]] — Flutterパッケージ構成
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
