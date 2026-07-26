+++
id = "scope.design-boundary"
kind = "scope"
title = "v1 の設計境界：作り出さず、範囲を固定する"
summary = "v1 は README ビューの生成・検証のみ。ハーネス要素生成・対話観察・全ペルソナ網羅は明示的に範囲外とし、未設計部分を作り出さない。"
order = 16
priority = 60
audience = ["human"]
tags = ["スコープ", "境界", "v1", "設計"]
status = "active"
trust = "authoritative"
depends_on = ["thesis.frictionless-ai-handoff", "constraint.real-conversation-quality", "definition.real-conversation"]
claims = ["v1 は README ビューのみ", "未設計のハーネス生成は範囲外"]
owner = "project"
updated = "2026-07-26"
+++
この PR（v1）は、思い込みで機能を膨らませないために、明示的な設計境界を設ける。

## v1 の範囲（作る）

1. `content/blocks/` の意味ブロック管理
2. README ビューの生成（`mfr build`）
3. 検証（`validate`）、監査（`audit`）、ベンチマーク（`benchmark`）
4. コンテキスト取り出し（`context`）、差分（`diff`）、スナップショット（`snapshot`）
5. 自己ホスト（この README は自分で生成）

## 範囲外（作らない、この PR では）

- CLAUDE.md / Skills / Hooks / Subagents / MCP 設定の生成
- 権限設定（`settings.json` 系）の生成
- 対話観察の自動化パイプライン
- ペルソナ全網羅の網羅的検査
- Claude Code 本体の機能改変

これらは [`roadmap`](140-roadmap.md) の次段階以降で、同じ意味ブロック基盤から段階的に生やす。v1 で作り出さないことが、後から間違って前提にしないための境界である。

## なぜ固定するか

「作ってみたけど設計は後」は、取り違えの温床になる。v1 では範囲を明示し、範囲外のものは「未設計」として可視化する。
