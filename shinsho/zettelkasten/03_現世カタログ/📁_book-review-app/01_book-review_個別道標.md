---
type: reference
title: 01_book-review_個別道標
tags: [/, moc, 表の神器, 個別道標, 現世カタログ, flutter, book-review, tsundoku-quest]
status: active
timestamp: 2026-07-22T00:00:00Z
---

# 01_book-review_個別道標

**カテゴリ**: 03_現世カタログ
**ソース**: utsushiyo/book-review-app/docs/roadmap.md
**最終更新**: 令和八年文月22日（実態同期）

---

## book-review-app ロードマップ

所在: `utsushiyo/book-review-app/docs/roadmap.md`

---

## 現状

| 要素 | 状態 |
|------|------|
| Flutter雛形 | ✅ Feature-First構造 |
| 版 | 1.0.0+2 |
| 本棚画面 | ✅ ISBN検索＋蔵書CRUD＋バーコードスキャン |
| レビュー機能 | ✅ 星評価＋テキスト＋追加・編集・削除（Hive永続化） |
| 蔵書API連携 | ✅ OpenBD API連携＋HiveBookRepository |
| 試験 | 62/62通過 ✅ |
| dart analyze | clean ✅ |

---

## 技術構成

Flutter + Provider + Hive。ISBNバーコードスキャン（MobileScanner + scanWindow + debounce + 確認ダイアログ）実装済み。

---

## Related
- [[../📁_tsundoku-quest/01_tsundoku-quest_神想.md]] — 姉妹アプリ（積読）
- [[../../02_神器と基盤/02_表の神器_Flutter.md]] — Flutter全体方針
- [[../03_MOC_現世カタログ.md]] — カテゴリハブへ戻る
