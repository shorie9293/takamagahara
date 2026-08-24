---
type: reference
title: 10_神文の書式_Markdown規約
tags: [/, moc, 古事記, 神文の書式, 神聖語彙集, 時系列索引, 神器と基盤, markdown規約]
status: active
timestamp: 2026-06-17T00:00:00Z
---

# 10_神文の書式_Markdown規約

**カテゴリ**: 02_神器と基盤
**ソース**: jingi.md §神文の書式
**最終更新**: 令和八年皐月二十六日（2026年5月26日）

---

## 神文（ドキュメント）の書式規約

高天原の全ての文書はMarkdownにて記す。

---

## 文書種別と所在

| 文書種別 | 所在 | 更新タイミング |
|---------|------|--------------|
| 神想（仕様書） | `shinsho/*.md`, `utsushiyo/<現世>/shinso.md` | 仕様変更時 |
| 古事記（意思決定記録） | `shinsho/kojiki.md` | 意思決定の都度 |
| 変遷（CHANGELOG） | 各現世 `CHANGELOG.md` | リリース時 |
| 個別道標（ロードマップ） | `utsushiyo/<現世>/docs/roadmap.md` | タスク完了時 |
| Zettelkastenノート | `shinsho/zettelkasten/*/` | 随時 |

---

## Zettelkastenノート規約

- ファイル名: `XX_内容.md`（XXはノード番号）
- メタデータブロック: タイトル / カテゴリ / ソース / 最終更新日 を冒頭に
- リンク: `` 形式
- Relatedセクションにカテゴリハブ（MOC）への帰還リンクを必ず含める

---

## CHANGELOG形式

```markdown
## [1.2.0] - YYYY-MM-DD
### Added / Changed / Fixed
- 項目
```

---

## 禁忌
- ❌ バイナリ（.docx/.pdf）での神想管理
- ❌ 口頭のみの意思決定（古事記必須）
- ❌ 重複道標（個別道標が正）

---

## Related
- [[../01_大願と掟/09_神聖語彙集.md]] — 神聖語の統一
- [[../07_記録と歴史/05_古事記_時系列索引.md]] — 古事記の書式
- [[02_MOC_神器と基盤.md]] — カテゴリハブへ戻る
