---
type: spec
title: 01_lifelog-news_神想
tags: [/, 神想, moc, 個別道標, 新聞コラム, 現世カタログ, lifelog-news]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 01_lifelog-news_神想

**カテゴリ**: 03_現世カタログ
**ソース**: lifelog-shinso.md
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## LifeLog News — 日々の記録を新聞に編む

日々の出来事・気づきを「みことのり（メモ）」として記録し、AIが**新聞記事風ダイジェスト**として自動編纂。所在: `utsushiyo/lifelog-news/`

---

## 技術構成

| 要素 | 採用 |
|------|------|
| フレームワーク | Next.js 16（App Router） |
| スタイリング | Tailwind CSS v4 |
| 状態管理 | Zustand（localStorage永続化） |
| バックエンド | Supabase（Auth, Storage, Realtime） |
| AI連携 | Claude / DeepSeek / OpenAI |
| 画像生成 | pollinations.ai |

---

## 新聞構成

- **タイムライン面**: 日々のメモを時系列表示
- **ダイジェスト面**: AIがメモ群から自動生成する新聞記事
- **コラム面**: AIのアドバイス＋実践的タスク提案 → [[02_lifelog-news_新聞コラム]]
- デプロイ: 静的エクスポート済み

---

## Related
- [[02_lifelog-news_新聞コラム.md]] — コラム欄設計
- [[03_lifelog-news_個別道標.md]] — ロードマップ
- [[../03_MOC_現世カタログ.md]] — カテゴリハブへ戻る
