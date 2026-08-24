---
type: rule
title: 絶対掟④ — Feature-First構造
tags: [feature-first, architecture, rule, 絶対掟]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 絶対掟 ④：Feature-First構造

## 掟

**全Flutter現世はFeature-First構造に従うべし。**
型分類（models/widgets/screens/viewmodelsの横断的ディレクトリ）は禁ず。
機能単位でディレクトリを切り、その中に data / domain / presentation の三層を配置せよ。

## 正しき構造

```
lib/
├── core/                      # 共有基盤（全Featureから参照）
│   ├── theme/
│   ├── utils/
│   ├── accessibility/         # Semantics helper
│   ├── testing/               # AppKeys管理
│   └── error/                 # ErrorBoundary
│
├── features/                  # 機能単位のディレクトリ
│   ├── <機能名A>/
│   │   ├── data/              # 神庫アクセス層（Repository）
│   │   ├── domain/            # 神想（UseCase, Entity）
│   │   └── presentation/      # 神楽（Screen, Widget, ViewModel）
│   │
│   └── <機能名B>/
│       ├── data/
│       ├── domain/
│       └── presentation/
│
└── main.dart
```

## 三大禁忌（要約）

Feature-First構造を守る上での三大禁忌。詳細は各ノートを参照：
1. [[17_禁忌_Widget200行超.md]] — Widget 1ファイル200行超禁止
2. [[18_禁忌_Feature跨ぎimport.md]] — Feature跨ぎimport統一
3. [[19_禁忌_ViewModel神クラス化.md]] — ViewModel神クラス化禁止

> 完全な禁忌集は [[10_三大禁忌.md]] を参照。

## 検証

```bash
scripts/verify-feature-first.sh
```
詳細構造は `shinsho/code-adaptation-shinsho.md` 第五章を参照。

## Related
- [[10_三大禁忌.md]] — 三大禁忌ハブ
- [[../02_神器と基盤/13_コード適応_FeatureFirst詳細.md]] — Feature-Firstの完全詳細
- [[../02_神器と基盤/11_コード適応_全体図.md]] — コード適応の全体像
- [[01_MOC_大願と掟.md]] — カテゴリハブ
