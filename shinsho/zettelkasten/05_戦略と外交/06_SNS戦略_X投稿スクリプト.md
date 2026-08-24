---
type: strategy
title: 06_SNS戦略_X投稿スクリプト
tags: [/, moc, 戦略と外交, sns戦略, 投稿カテゴリ, x投稿スクリプト, 自動化パイプライン]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 06_SNS戦略_X投稿スクリプト

**カテゴリ**: 05_戦略と外交
**ソース**: sns-senryaku.md §十二
**最終更新**: 令和八年皐月九日（2026年5月9日）

---

## xurl CLIによる投稿自動化スクリプト設計

**認証**: yaoyorozu_bot アプリ使用、OAuth 2.0認証済み

---

## 基本コマンド

```bash
# 通常投稿
xurl post "本文"

# 画像付き投稿
xurl media upload /path/to/image.png
xurl post -m "media_key_1,media_key_2" "本文"
```

**制限**: X API v2 有償API（Basic $100/月）のレート制限に注意

---

## スクリプト配置案

```
scripts/sns/
├── post.sh                      # 汎用投稿
├── post_from_daily_report.sh    # 日報→X自動変換
├── post_weekly_summary.sh       # 週次まとめ
├── post_japanese_myth.sh        # 和風小ネタ（ストックから）
└── sns_state.sh                 # 状態確認（フォロワー数等）
```

---

## 日報連動スクリプト設計（post_from_daily_report.sh）

1. 直近の日報内容を取得
2. 進捗有無を判定（ゼロならスキップ）
3. 100字目安に要約
4. ハッシュタグ付与
5. xurl post で投稿

---

> 禁忌事項の詳細は [[06_SNS戦略_X投稿スクリプト_禁忌.md]] を参照。

---

## Related
- [[05_SNS戦略_自動化パイプライン.md]] — cron連動設計
- [[04_SNS戦略_投稿カテゴリ5種.md]] — 5種の神器
- [[05_MOC_戦略と外交.md]] — カテゴリハブ