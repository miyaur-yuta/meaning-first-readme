# Meaning First README v1

## 思想（ここが一番大事）

**Claude Code ハーネス（CLAUDE.md, Skills, Hooks, Subagents, MCP）への引き渡し摩擦を、限界まで減らす。**

README を「正しく書く」ための道具ではない。README を含む **Claude Code ハーネス設定全体** を、意味ブロックから一貫して生成・検証する体制を目指す。

### Claude Code は README を超える

| プリミティブ | 役割 |
|---|---|
| CLAUDE.md / Rules | 常に効く文脈・指示 |
| Skills | オンデマンドの知識・ワークフロー |
| Hooks | 必ず発火する強制ルール |
| Subagents | 独立コンテキストで専門作業 |
| MCP | 外部システム接続 |
| Plugins | 上記を束ねて配布 |

### 権限スコープとモードも扱う

| スコープ | 場所 |
|---|---|
| ユーザー | `~/.claude/settings.json` |
| プロジェクト共有 | `.claude/settings.json` |
| プロジェクト個人 | `.claude/settings.local.json`（Git 除外） |
| 管理者 | OS 固定（上書き不可） |

モードは `default` / `acceptEdits` / `plan` / `auto` / `dontAsk` / `bypassPermissions`。`deny` はスコープ間で常に優先する。

### リアルな対話品質

「リアルな対話」とは、生成したハーネスを実際に読み込ませた Claude Code セッションで、**代表ペルソナの典型タスク**を実施したときの振る舞い。主観ではなく観察可能な基準（[`definition.real-conversation`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/030-definition-real-conversation.md) 参照）。

含むもの：目的・禁止事項・次の一手が最初の応答に反映されるか、禁止が機械的に守られるか、人間向けビューで俯瞰できるか。
含まないもの：「なんとなく自然」等の主観、サンプル1の印象。

---

## v1 の範囲（正直に）

**v1 は README ビューのみ**。CLAUDE.md, Skills, Hooks, Subagents の生成は次段階（[`roadmap`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/140-roadmap.md) 参照）。

詳細は [`content/blocks/016-scope-design-boundary.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/016-scope-design-boundary.md) に明示。

### v1 で作るもの

- 意味ブロック管理（`content/blocks/`）
- README 生成・検証・監査・ベンチマーク
- コンテキスト取り出し・差分・スナップショット
- 自己ホスト

### v1 では作らないもの（明示的に範囲外）

- CLAUDE.md / Skills / Hooks / Subagents / MCP 設定の生成
- 権限設定（`settings.json` 系）の生成
- 対話観察の自動化パイプライン
- ペルソナ全網羅検査

「作ってみたけど設計は後」を防ぐため、未設計部分は可視化したまま次段階に回す。

---

## ここだけ見ればOK（30秒）

1. ⭐ [`docs/START_HERE.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/docs/START_HERE.md)
2. 🎯 [`content/blocks/002-thesis-frictionless.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/002-thesis-frictionless.md) — 思想
3. 🔒 [`content/blocks/064-constraint-permission-scope.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/064-constraint-permission-scope.md) — 権限
4. ✅ [`release/VALIDATION_REPORT.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/release/VALIDATION_REPORT.md)

CI: 🟢 3.11 / 3.12 / 3.13 通過済み

---

## 既知の限界

- 日本語検索は簡易（同義語に弱い）
- 注入検査は補助（信頼境界の代替ではない）
- 外部 URL の到達性は未検証
- v1 は README ビューのみ（ハーネス設定生成は次段階）

## 公開境界

Draft のまま整備中。Ready / merge は人間の明示承認後。
