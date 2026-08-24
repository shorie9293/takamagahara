---
type: rule
title: 禁忌① — Widget 1ファイル200行超を禁ず
tags: [feature-first, widget, code-quality, rule, 三大禁忌]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 禁忌①：Widget 1ファイル200行超を禁ず

**親ノート**: [[10_三大禁忌.md]]

## なぜ禁忌か

- 1ファイルが巨大化すると、試練の作成が困難になる
- 変更の影響範囲が読めず、禍津の温床となる
- 眷属神への委任時に「このファイルを修正して」と言えなくなる

## 検知方法

```bash
find lib/ -name "*.dart" -exec wc -l {} + | awk '$1 > 200 {print $0}'
```

## 分割の指針

- **画面全体**（Screen）→ **セクションWidget**（Section）→ **最小部品**（Atom）
- 200行を超えたら、その役割を考えて適切な単位で分割せよ
- 例：`game_screen.dart`（923行）→ `town_view` / `quest_list` / `player_status` に分割

## Related
- [[10_三大禁忌.md]] — 三大禁忌ハブ
- [[08_絶対掟_FeatureFirst構造.md]] — Feature-First構造の掟
- [[18_禁忌_Feature跨ぎimport.md]] — 禁忌②
- [[19_禁忌_ViewModel神クラス化.md]] — 禁忌③
