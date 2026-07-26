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

自動生成物は、実際に人間が Claude Code と対話したときに取り違え・迷子・停滞が起きない品質が必要。検証とベンチマークに加えて、代表ペルソナでの対話観察を `evidence` として残す。

---

## v1 の範囲（正直に）

**v1 は README ビューのみ**。CLAUDE.md, Skills, Hooks, Subagents の生成は次段階（[`roadmap`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/140-roadmap.md) 参照）。

それでも v1 には意味がある：
- 意味ブロック管理の基盤が完成
- 検証・監査・差分の仕組みが動く
- 次段階は同じ基盤から各種ハーネス設定を生やすだけ

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
