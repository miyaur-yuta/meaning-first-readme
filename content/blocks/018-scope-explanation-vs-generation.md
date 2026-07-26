+++
id = "scope.explanation-vs-generation"
kind = "scope"
title = "「生成しない」と「説明しない」は別物"
summary = "v1 では各ハーネス要素（CLAUDE.md/Skills/Hooks/Subagents/MCP）の自動生成はしないが、概念・使い方・引き継ぎ資料は提供する。"
order = 18
priority = 65
audience = ["human"]
tags = ["スコープ", "説明", "引き継ぎ", "区別"]
status = "active"
trust = "authoritative"
depends_on = ["scope.design-boundary", "thesis.frictionless-ai-handoff"]
claims = ["生成機能が範囲外でも、概念・使い方の説明は範囲内"]
owner = "project"
updated = "2026-07-26"
+++
「v1 では作らない」と「v1 では説明しない」を混同しない。自動生成機能が範囲外でも、読者が対象を理解するための説明は必須である。

## 区別

| 対象 | v1 の位置付け |
|---|---|
| CLAUDE.md / Skills / Hooks / Subagents / MCP の**自動生成機能** | 範囲外（次段階） |
| それぞれの**概念・役割・使い方の説明** | 範囲内（この README/ドキュメント群に含む） |
| 権限設定の**自動生成機能** | 範囲外（次段階） |
| 権限スコープとモードの**解説** | 範囲内（`constraint.permission-scope` 参照） |

## なぜ区別するか

ハーネス要素を「範囲外」とだけ書くと、読者は「このプロジェクトは Claude Code の何も分かっていない」と誤解する。目的は **生成自動化を後回しにすること** であって、**読者を放置すること** ではない。

## v1 で提供する説明資産

- Claude Code の7プリミティブと役割（`thesis.frictionless-ai-handoff`）
- 権限スコープとモード（`constraint.permission-scope`）
- ペルソナと典型タスク（`scope.personas`）
- 対話観察フォーマット（`decision.observation-format`）
- このプロジェクトが v1 で扱う範囲（`scope.design-boundary`）

これらにより、読者は「何が自動化され、何が手動か」を含めて全体を理解できる。

## 引き継ぎ資料

次段階で各種生成機能を追加する前提で、v1 の時点で次を整備する。

- 各ハーネス要素の「現在の状態」と「理想状態」の差分
- 次段階で生成する際の出力イメージ
- 手動で設定する場合の最小構成例

これらは `roadmap` と連動して整備する。
