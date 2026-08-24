---
type: reference
title: 03_lifelog-news_個別道標
tags: [/, moc, 個別道標, 新聞コラム, 現世カタログ, lifelog-news]
status: active
timestamp: 2026-07-22T00:00:00Z
---

# 03_lifelog-news_個別道標

**カテゴリ**: 03_現世カタログ
**ソース**: utsushiyo/lifelog-news/docs/roadmap.md
**最終更新**: 令和八年文月22日（実態同期）

---

## lifelog-news ロードマップ

所在: `utsushiyo/lifelog-news/docs/roadmap.md`

---

## 現状

| 要素 | 状態 |
|------|------|
| フレームワーク | Next.js（App Router） |
| 機能 | ライフログ＋ニュース表示 |
| デプロイ | 静的エクスポート済み |
| 試験 | なし（未整備） |

---

## 完了タスク（皐月二十五日）

| 項目 | 状態 |
|------|------|
| レスポンシブ対応強化 | ✅ セマンティックカラー化＋Tailwind全BP適用 |
| ダークモード | ✅ システム検出＋手動トグル |
| ローディング・エラー改善 | ✅ Skeleton＋ErrorBoundary |
| メタタグ最適化 | ✅ Metadata API＋keywords+canonical |
| OGP設定 | ✅ og:title/description/image＋Twitter Card |
| サイトマップ | ✅ sitemap.ts＋robots.ts動的生成 |

---

## Related
- [[01_lifelog-news_神想.md]] — コア設計
- [[02_lifelog-news_新聞コラム.md]] — コラム設計
- [[../03_MOC_現世カタログ.md]] — カテゴリハブへ戻る
