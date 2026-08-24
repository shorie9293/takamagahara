---
type: reference
title: 06_現世降臨_CI_CD
tags: [/, ci, cd, moc, 表の神器, 現世降臨, 開闢の手順, 神器と基盤]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 06_現世降臨_CI_CD

**カテゴリ**: 02_神器と基盤
**ソース**: jingi.md §現世降臨
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## 現世降臨（CI/CD）の仕組み

GitHub Actionsによる自動ビルド・自動降臨が、全Flutter現世の標準配信パイプライン。

---

## 降臨の流れ

1. `pubspec.yaml` の `version` を更新（**最初に！重複で降臨失敗**）
2. `git commit` → `git push`
3. GitHub Actions 発火：`flutter pub get` → `flutter test --no-pub` → `dart analyze` → `flutter build appbundle`（署名付きAAB）→ Play Console自動配信

---

## 降臨前の絶対掟

> **必ず先にバージョンを上げよ。** `versionCode`（`+`の後ろ）単調増加。詳細は [[../01_大願と掟/15_開闢の手順_バージョン上げ.md]]。

---

## 署名設定

- キーストアファイルとパスワードは **GitHub Secrets** に保存（クライアントコード非含有）
- 設定例: `android/app/build.gradle` 参照（`signingConfigs { release { ... } }`）

---

## Play Store配信パイプライン

| 段階 | 用途 | 審査 |
|------|------|------|
| 内部テスト | 開発者限定 | なし（即時配信） |
| クローズドテスト | 限定ユーザー | あり（初回） |
| 本番 | 一般公開 | あり |

---

## Related
- [[../01_大願と掟/15_開闢の手順_バージョン上げ.md]] — バージョン上げの絶対掟
- [[02_表の神器_Flutter.md]] — Flutterパッケージ構成
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
