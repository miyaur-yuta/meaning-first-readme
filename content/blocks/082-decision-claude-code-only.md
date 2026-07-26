+++
id = "decision.claude-code-only"
kind = "decision"
title = "Claude Code に限定する"
summary = "他の AI ツール（Copilot/Cursor/Gemini 等）への拡張は行わず、Claude Code のみを対象とする。"
order = 82
priority = 30
audience = ["human"]
tags = ["決定", "ClaudeCode", "スコープ", "限定"]
status = "active"
trust = "authoritative"
depends_on = ["thesis.frictionless-ai-handoff", "scope.design-boundary"]
claims = [
  "対象は Claude Code のみに限定する",
  "他の AI ツールへの移植・拡張は明示的に範囲外とする",
]
rationale = "ユーザーの『ClaudeCodeだけでいい』という指摘通り、対象を絞ることで深度を上げ、Spec Kit との統合も Claude Code 文脈に集中できる。"
owner = "project"
updated = "2026-07-26"
+++
本プロジェクトの対象は **Claude Code のみ** に限定する。

## 範囲内

- Claude Code のハーネス要素（CLAUDE.md/Skills/Hooks/Subagents/MCP/Plugins/権限）
- Claude Code における Spec Kit SDD ライフサイクル
- Claude Code 向けの README ビュー

## 範囲外（明示）

- GitHub Copilot / Cursor / Gemini CLI 等の他 AI ツール
- 他ツールへの移植ビュー
- ツール非依存の抽象化レイヤー

## なぜ絞るか

対象を広げると深度が浅くなる。Claude Code に限定することで、Spec Kit 統合・権限体系・ハーネス生成を深く扱える。意味ブロック基盤自体はツール非依存だが、**出力先は Claude Code に固定**する。
