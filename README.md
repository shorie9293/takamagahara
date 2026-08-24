# 高天原（Takamagahara）

**AIエージェント8柱による自律型アプリ開発システム — 「朝起きたら、AIが開発を進めてくれている状態」を実現する**

高天原は、役割を分担した複数のAIエージェント（八百万の神々）が、**人間の指示なしに自律的にアプリを開発し続ける**システムです。PM・開発・UX・QA・監査という役割を神話の神々に割り当て、共通の知識庫（神書）と掟（開発規律）で品質を機械的に担保します。

---

## 特徴

- **8柱のAIが役割分担** — 天照大神（統括）・思兼神（PM）・天目一箇神（開発）・天宇受賣命（UX）・月読命（QA）・直毘神（監察）・事代主神（生活管理）・須佐之男命（宣伝）
- **1日4回の自律開発サイクル** — cronによる自動トリガーで、Kanbanからタスクを取得 → 仕様相談 → コード生成 → テスト実行 → 日報まで自動で行う
- **神書（Zettelkasten知識庫）** — 190件近い仕様書・設計書・履歴を、すべてのAIが仕事の前に検索する
- **三つの絶対掟** — ①四神相談なくコードを書くな ②TDDなくコードを書くな ③試練可能でないコードを書くな
- **監査性** — AIが何をしたか、日報・記録としてすべて可視化される

## なぜ神話なのか

「PM」より「思兼神」——知恵を司る神——のほうが、役割への自覚が湧きます。
バグは「禍津（まがつ）」、「デプロイ」は「現世への降臨」。
**たったこれだけの言い換えで、AIのアウトプットの質が変わりました。**
神話は遊び心ではなく、設計上の判断です。

---

## リポジトリ構成

```
takamagahara/
├── AGENTS.md              # 高天原 神勅（エージェントの行動規範・三つの絶対掟）
├── SOUL.md                # 天照大神の神魂（核となる理・境界）
├── IDENTITY.md            # 天照大神の名鑑
├── USER.md                # 創造主様について（大願・好み・運用の掟）
└── shinsho/
    └── zettelkasten/      # 神書（Zettelkasten知識庫・9カテゴリ）
        ├── 01_大願と掟/       # 憲法級の不変の掟
        ├── 02_神器と基盤/     # 技術スタック・設計原則
        ├── 03_現世カタログ/   # アプリ群の仕様・設計
        ├── 04_自律運営/       # cron体系・自律開発の仕組み
        ├── 05_戦略と外交/     # 市場戦略・SNS戦略
        ├── 06_品質と試練/     # TDD・E2E試練手順
        ├── 07_記録と歴史/     # 古事記・Note連載・時系列索引
        ├── 08_分析と監査/     # ハーネス分析・UX監査
        ├── 99_索引と横断/     # 全ファイル索引・用語集
        ├── Takamagahara_MOC.md
        ├── query_zettelkasten.py   # 神書検索ツール（AND+同義語検索）
        ├── link_linter.py          # リンク健全性チェック
        ├── schema_linter.py        # スキーマ整合チェック
        ├── graph_metrics.py        # 知識グラフ計測
        ├── fix_dead_links.py       # デッドリンク修復
        └── synonyms.json           # 同義語辞書
```

---

## 使い方 — リポジトリを読み込ませると、即高天原システムが動き出す

このリポジトリは、**エージェント（AI）に読み込ませることで高天原システムとして機能する**ように設計されています。

### 1. クローン

```bash
git clone https://github.com/shorie9293/takamagahara
cd takamagahara
```

### 2. エージェントの作業ディレクトリに指定

Hermes Agent（または AGENTS.md を自動ロードするエージェント）で、このディレクトリを作業ディレクトリとして指定します。

```bash
# Hermes Agent の場合の例
hermes config set workdir /path/to/takamagahara
# または
cd /path/to/takamagahara && hermes
```

### 3. 動き出すもの

- **AGENTS.md（神勅）** が自動ロードされ、エージェントは「四神相談」「TDD」「試練可能コード」の掟に従って行動します
- **shinsho/zettelkasten/**（神書）が知識庫として機能し、エージェントは仕事の前に必ず検索します
- **query_zettelkasten.py** で神書を横断検索できます（AND検索・同義語展開対応）

```bash
python3 shinsho/zettelkasten/query_zettelkasten.py "タスク管理 rpg"
```

### 4. 必要な環境（自律運用する場合）

完全な自律運用（1日4回の開発サイクル・日報・監査）には、以下を別途構成します。

- **Hermes Agent**（エージェント基盤）
- **cronジョブ**（トリガー: 朝の宣言・開発サイクル・日報）
- **Notion**（タスク管理・Kanban・記録）
- **Flutter / Supabase / GitHub Actions**（アプリ開発・CI/CD）

---

## 実証データ（2026年8月時点）

| 項目 | 数値 |
|---|---|
| 自律運用の連続日数 | 49日間以上・一度も停止なし |
| 神書（知識庫ノート） | 189件 |
| 開発サイクル | 1日4回（6:30 / 11:30 / 16:45 / 21:15） |
| 代表アプリ rpg-task | 自動テスト1,132件・クローズドα版 |
| Flutter全アプリの自動試験 | 2,898件（毎日実行） |

---

## 関連リポジトリ

高天原から生まれたアプリ（現世）は、それぞれ個別のリポジトリで公開しています。

- [rpg-task](https://github.com/shorie9293/lifequestslayer-of-procrastination) — RPG風タスク管理アプリ
- [tsundoku-quest](https://github.com/shorie9293/tsundoku-quest) — 積読を冒険にする読書習慣化アプリ
- [kozuchi](https://github.com/shorie9293/kozuchi) — 家計見える化アプリ
- [election-game](https://github.com/shorie9293/election-game) — 選挙体験シミュレーション
- [book-review-app](https://github.com/shorie9293/book-review-app) — 書評アプリ

---

## ライセンス

ライセンス未定（連絡先: リポジトリオーナーまで）
