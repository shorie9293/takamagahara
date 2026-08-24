---
type: rule
title: 禁忌② — Feature跨ぎimportの統一を乱すな
tags: [feature-first, import, architecture, rule, 三大禁忌]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 禁忌②：Feature跨ぎimportの統一を乱すな

**親ノート**: [[10_三大禁忌.md]]

## なぜ禁忌か

- 相対パス `../../features/other/...` はFeature間の密結合を生む
- リファクタ時にパスが破綻し、修正コストが爆発する
- Feature間の依存関係が暗黙的になり、アーキテクチャが崩壊する

## 正しきimport

```dart
// ✅ 正：パッケージ名でimport
import 'package:my_app/features/guild/data/guild_repository.dart';

// ❌ 誤：相対パスでのFeature跨ぎ
import '../../guild/data/guild_repository.dart';
```

## 許容されるimport

- `core/` からのimport（全Featureの共通基盤のため）
- 同一Feature内の相対パス（`../domain/entity.dart` 等）
- パッケージ名による他Featureへの明示的import

## Related
- [[10_三大禁忌.md]] — 三大禁忌ハブ
- [[08_絶対掟_FeatureFirst構造.md]] — Feature-First構造の掟
- [[17_禁忌_Widget200行超.md]] — 禁忌①
- [[19_禁忌_ViewModel神クラス化.md]] — 禁忌③
