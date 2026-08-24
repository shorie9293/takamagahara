---
type: guide
title: 17_Kanban_PWA
tags: [/, moc, 全体像, pwa, 大国主命, 召喚作法, 自律運営, 戦略監視神]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 17_Kanban_PWA

**カテゴリ**: 04_自律運営
**ソース**: kanban-pwa-implementation.md（新規創生）
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## Kanban PWA — スマホ対応カンバンボード

Flask + vanilla JS製。`hermes kanban` CLIをREST APIでラップ。スマホからPWAとしてインストール可。

所在: `~/Takamagahara/kanban-pwa/`

---

## 技術構成

| 層 | 技術 |
|----|------|
| バックエンド | Flask（`server.py`） — `hermes kanban` CLIのwrapper |
| フロントエンド | Vanilla JS（`app.js`） — ビルド不要・単一ファイル |
| スタイル | インラインCSS（ダークテーマ #0f172a） |
| PWA | Service Worker（cache-first） + manifest.json |
| 起動 | `./start.sh` → `http://192.168.2.103:8765` |

---

## API

`GET/POST/PUT /api/tasks` で Kanban CRUD。ステータスマッピングに注意（`running`≠`in_progress`）。
実装詳細: `kanban-pwa-implementation.md`（kanban-orchestrator スキル）

---

## デスクトップ＋モバイル デュアルレイアウト

- **デスクトップ**（≥769px）: 6列Kanbanボード（Todo/Ready/Running/Done/Blocked/Archived）
- **モバイル**（≤768px）: RPG風カード一覧。アバター＋XPバー＋フィルタータブ＋大国主命（👴）アドバイスボタン

---

## 注意点

- FlaskサーバーはHermes Gatewayの子プロセス。Gateway再起動時に死ぬ → 要再起動
- HTTPS（PWAインストール要件）: `tailscale serve --bg https://localhost:8765` で対応

---

## Related
- [[12_戦略監視神_全体像.md]] — Kanbanと連携する監視システム
- [[../05_戦略と外交/09_大国主命_召喚作法.md]] — 大国主命との連携
- [[04_MOC_自律運営.md]] — カテゴリハブ
