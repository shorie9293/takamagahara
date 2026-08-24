---
type: reference
title: 23_八百万拡張_SSH連携作法
tags: [/, moc, 八百万拡張, 天浮橋計画, 神器と基盤, 端末神構成, ssh連携作法]
status: active
timestamp: 2026-06-17T00:00:00Z
---
# 23_八百万拡張_SSH連携作法

**カテゴリ**: 02_神器と基盤 | **ソース**: yaoyorozu-kakucho.md §三 §十 | **最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## 契りの儀：SSH経由の遠隔契り作法

天照大神がSSH経由で端末に宿る神に直接タスクを移譲する神聖なる儀式。
うきはし計画の核心は此の契りの道により実現す。

---

## 通信の五層

| 層 | 経路 | 用途 |
|----|------|------|
| ① SSH | `ssh susanoo`（鍵認証） | 全遠隔操作の基本経路 |
| ② ADB over TCP | `adb connect 192.168.0.18:5555` | 画面操作（tap/swipe/keyevent） |
| ③ Discord | 八百万サーバー | 創造主様↔全神の神託通路 |
| ④ GDrive | rclone経由 | ログ・スクショ長期保存（第三段階） |
| ⑤ 契り | SSH + `hermes -z` | 端末神への直接的タスク委譲 |

---

## 契りの神咒

```bash
ssh susanoo "~/.hermes/hermes-agent/venv/bin/hermes -z '【契り】天照大神より須佐之男命へ。
<指令>。完了時はsend_messageでDiscordの専用通路（#スサノオ）に奏上せよ。'"
```

---

## 契りの掟

1. 受けたる神は自律的に端末操作を実行す
2. 完了時はDiscord（専用通路）に奏上する義務
3. 端末内の物理的操作（カメラ・マイク・TTS・ADB等）に用いる
4. **端末上で直接実行できることは端末神に任せるべし**（教訓）

---

## SSH設定（~/.ssh/config）

```
Host susanoo
    HostName 192.168.0.18 / Port 8022
    IdentityFile ~/.ssh/id_ed25519_susanoo
```

- 公開鍵認証（パスワード認証廃止済み）✅
- ADB: Android 10のため再起動後 `adb tcpip 5555` 再接続必須

---

## Related
- [[21_八百万拡張_天浮橋計画.md]] — 全体構想
- [[22_八百万拡張_端末神構成.md]] — 端末構成詳細

- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
