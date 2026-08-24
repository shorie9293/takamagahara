---
type: history
title: kozuchi改名の詳細 — 遺跡救出時
tags: [kojiki, restructuring, kozuchi, daikoku, rename, 遺跡救出]
status: active
timestamp: 2026-06-07T00:00:00Z
---

# kozuchi改名の詳細

**親ノート**: [[06_古事記_遺跡からの現世救出.md]]

daikoku → kozuchi への改名にあたり、以下の修正を実施：

## 修正内容

- `pubspec.yaml`: `name: daikoku` → `name: kozuchi`
- 全Dartファイルの `import 'package:daikoku/` → `import 'package:kozuchi/`（46ファイル）
- アプリ名表示: title, label, window title → `kozuchi`（10ファイル）
- Android: `AndroidManifest.xml` label
- iOS: `Info.plist` CFBundleDisplayName
- Web: `manifest.json`, `index.html`
- Linux: `CMakeLists.txt`（BINARY_NAME, APPLICATION_ID）
- macOS: `AppInfo.xcconfig`（PRODUCT_NAME, PRODUCT_BUNDLE_IDENTIFIER）
- Windows: `CMakeLists.txt`（BINARY_NAME）
- **未変更**: `GuardianDeity.daikokuten`（大黒天——神の名でありアプリ名ではない）

## Related
- [[06_古事記_遺跡からの現世救出.md]] — 親ノート
- [[03_現世カタログ/📁_kozuchi/01_kozuchi_神想_コア体験.md]] — kozuchi神想
- [[05_古事記_時系列索引.md]] — 時系列索引
