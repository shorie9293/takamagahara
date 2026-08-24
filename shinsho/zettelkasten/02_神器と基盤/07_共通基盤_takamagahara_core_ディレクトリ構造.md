---
type: reference
title: 07_共通基盤_takamagahara_core_ディレクトリ構造
tags: [/, moc, 表の神器, 共通基盤, core, 神器と基盤, 現世カタログ, flutter]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 07_共通基盤_takamagahara_core_ディレクトリ構造

**カテゴリ**: 02_神器と基盤 | **ソース**: jingi.md §共通基盤 | **親ノート**: [[07_共通基盤_takamagahara_core.md]]

---

## ディレクトリ構造

```
packages/takamagahara_core/
├── lib/
│   ├── src/
│   │   ├── types/        # 共通型定義
│   │   ├── constants/    # 定数
│   │   ├── utils/        # 汎用関数
│   │   └── errors/       # エラー型
│   └── takamagahara_core.dart  # barrel export
├── test/
├── pubspec.yaml
└── README.md
```

---

## Related
- [[07_共通基盤_takamagahara_core.md]] — 親ノート（概要・使い方・設計原則）
- [[08_共通基盤_takamagahara_ui.md]] — Flutter依存の共通UIパッケージ
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
