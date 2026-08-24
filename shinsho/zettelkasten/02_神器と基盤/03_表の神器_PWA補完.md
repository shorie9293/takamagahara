---
type: reference
title: 03_表の神器_PWA補完
tags: [/, moc, 表の神器, pwa補完, 神器と基盤, 神器選定の指針, flutter, lifelog-news]
status: active
timestamp: 2026-06-17T00:00:00Z
---
# 03_表の神器_PWA補完

**カテゴリ**: 02_神器と基盤 | **ソース**: jingi.md §第二の神器 | **最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## PWA：Flutterの補完

Flutterの及ばぬ速さを求める時、PWAにて先に検証す。
ただし、**Flutterこそ第一。PWAは補完。**

---

## PWAの神器構成

| 位 | 神器 | 用途 |
|----|------|------|
| **器の枠** | Next.js 16（App Router） | サーバーサイドレンダリング・静的生成 |
| **装いの法** | Tailwind CSS | ユーティリティファーストCSS |
| **心の在処** | Zustand | 軽量状態管理 |
| **神機との縁** | Claude / DeepSeek / OpenAI API | AI機能連携 |

---

## PWAを用いる現世

現在、唯一のNext.js現世：

| 現世 | 用途 | PWA採用理由 |
|------|------|------------|
| **lifelog-news** | ライフログ新聞 | Web即時性・SSR・SEO・ブラウザ共有 |

---

## PWA採用の判断基準

PWAを採用してよい場合：
- Webブラウザでの即時アクセスが必須
- SEO・OGP対応が必要
- 共有URLでのアクセスが主用途
- Flutter Webのパフォーマンスが不十分

PWAを採用すべきでない場合：
- モバイルアプリとしての配信が主目的 → Flutter
- オフライン機能が重要な場合 → Flutter（Hiveで強力なオフライン対応）
- カメラ・センサー等のネイティブ機能が必要 → Flutter

---

## アーカイブ済みPWA

| 現世 | 状態 | 理由 |
|------|------|------|
| tsundoku-quest（旧PWA） | 🪦 アーカイブ | Flutter版に全機能移行完了。**今後改訂予定なし**（皐月一日神託） |

---

## Related
- [[01_神器選定の指針.md]] — 技術選定フロー
- [[02_表の神器_Flutter.md]] — 主力のFlutter
- [[../03_現世カタログ/📁_lifelog-news/01_lifelog-news_神想.md]] — PWA現世の詳細
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
