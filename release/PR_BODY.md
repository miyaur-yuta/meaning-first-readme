# Meaning First README v1

> **30秒サマリ:** Claude Code ハーネス（CLAUDE.md/Skills/Hooks/Subagents/MCP）への引き渡し摩擦を限界まで減らす道具。**v1 は README ビューのみ**。CI 🟢 3.11/3.12/3.13 通過済み。Draft で整備中。

---

## ⭐ ここだけ見ればOK（所要30秒）

1. ⭐ [`docs/START_HERE.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/docs/START_HERE.md) — 入口
2. 🎯 [`content/blocks/002-thesis-frictionless.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/002-thesis-frictionless.md) — 思想
3. 🔒 [`content/blocks/064-constraint-permission-scope.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/064-constraint-permission-scope.md) — 権限
4. ✅ [`release/VALIDATION_REPORT.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/release/VALIDATION_REPORT.md) — 検証結果

---

## 一言で言うと

README を「正しく書く」ための道具ではない。README を含む **Claude Code ハーネス設定全体** を、意味ブロックから一貫して生成・検証する体制を目指す。

## v1 の範囲（正直に）

**v1 は README ビューのみ**。詳細は [`016-scope-design-boundary`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/016-scope-design-boundary.md)。

**作る:** 意味ブロック管理、README 生成・検証・監査・ベンチマーク、コンテキスト/差分/スナップショット、自己ホスト

**作らない（明示的に範囲外）:**
- CLAUDE.md / Skills / Hooks / Subagents / MCP 設定の生成
- 権限設定（`settings.json` 系）の生成
- 対話観察の自動化パイプライン
- ペルソナ全網羅検査

---

## 思想（詳細）

### Claude Code は README を超える

| プリミティブ | 役割 |
|---|---|
| CLAUDE.md / Rules | 常に効く文脈・指示 |
| Skills | オンデマンドの知識・ワークフロー |
| Hooks | 必ず発火する強制ルール |
| Subagents | 独立コンテキストで専門作業 |
| MCP | 外部システム接続 |
| Plugins | 上記を束ねて配布 |

### 権限スコープ

| スコープ | 場所 |
|---|---|
| ユーザー | `~/.claude/settings.json` |
| プロジェクト共有 | `.claude/settings.json` |
| プロジェクト個人 | `.claude/settings.local.json`（Git 除外） |
| 管理者 | OS 固定（上書き不可） |

モードは `default` / `acceptEdits` / `plan` / `auto` / `dontAsk` / `bypassPermissions`。`deny` はスコープ間で常に優先。

### リアルな対話品質

生成したハーネスを実際に読み込ませた Claude Code セッションで、**代表ペルソナの典型タスク**を実施した振る舞い。主観ではなく観察可能な基準（[`definition`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/030-definition-real-conversation.md) 参照）。

---

## 既知の限界

- 日本語検索は簡易（同義語に弱い）
- 注入検査は補助（信頼境界の代替ではない）
- 外部 URL の到達性は未検証
- v1 は README ビューのみ

## 公開境界

Draft のまま整備中。Ready / merge は人間の明示承認後。
