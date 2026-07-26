+++
id = "guide.claude-code-primitives"
kind = "procedure"
title = "Claude Code ハーネス要素：概念・使い方・最小構成"
summary = "Claude Code の7プリミティブ（CLAUDE.md/Skills/Hooks/Subagents/MCP/Plugins/権限）について、概念・使い方・最小構成を整理する。"
order = 90
priority = 60
audience = ["human"]
tags = ["ガイド", "ClaudeCode", "ハーネス", "使い方", "最小構成"]
status = "active"
trust = "reviewed"
depends_on = ["thesis.frictionless-ai-handoff", "constraint.permission-scope", "scope.explanation-vs-generation"]
claims = ["各ハーネス要素の概念と最小構成を文書化する"]
acceptance = [
  "CLAUDE.md/Skills/Hooks/Subagents/MCP/Plugins/権限の7要素すべてをカバーしている",
  "各要素に概念・使い方・最小構成の3点が揃っている",
  "このプロジェクトとの関係が明記されている",
]
owner = "project"
updated = "2026-07-26"
+++
Claude Code のハーネス要素について、概念・使い方・最小構成を整理する。v1 では自動生成しないが、読者・保守者・引き継ぎ担当が全体を把握するために必要な資産。

## CLAUDE.md / Rules

**概念:** セッションで常に読み込まれる文脈・指示。プロジェクトの「常に効く前提」を書く。

**使い方:** リポジトリルートに `CLAUDE.md` を置く。グローバルは `~/.claude/CLAUDE.md`。

**最小構成:**

```markdown
# CLAUDE.md

## 目的
<プロジェクトの目的を1行で>

## 禁止事項
- <やってはいけないこと>

## 次の一手
- <現在の優先タスク>
```

**このプロジェクトとの関係:** v1 の README は、CLAUDE.md に相当する情報を人間向けビューで出力する。

## Skills

**概念:** オンデマンドで読み込まれる知識・ワークフロー。`/` コマンドや自動判定で発動。

**使い方:** `.claude/skills/<name>/SKILL.md` に配置。

**最小構成:**

```markdown
---
name: <skill-name>
description: 何をするスキルか
---

# スキル本文
<手順・知識>
```

**このプロジェクトとの関係:** 次段階で意味ブロックから Skill 定義を生成する。

## Hooks

**概念:** ライフサイクルイベントで必ず発火する強制ルール。`deny` 相当。

**使い方:** `.claude/settings.json` の `hooks` セクションに定義。

**最小構成:**

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{"type": "command", "command": "echo 'check'"}]
      }
    ]
  }
}
```

**このプロジェクトとの関係:** 次段階で「禁止事項」ブロックから Hooks を生成する。

## Subagents

**概念:** 独立コンテキストで専門作業を行うエージェント。

**使い方:** `.claude/agents/<name>.md` に定義。

**最小構成:**

```markdown
---
name: <agent-name>
description: 何をさせるエージェントか
tools: [Read, Grep]
---

# エージェント指示
<役割・手順>
```

**このプロジェクトとの関係:** 次段階で「手順」ブロックから Subagent 定義を生成する。

## MCP

**概念:** 外部システム接続。ファイルシステム・DB・API 等をツールとして暴露。

**使い方:** `.claude/mcp.json`（プロジェクト）または `~/.claude.json`（ユーザー）に定義。

**最小構成:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path"]
    }
  }
}
```

**このプロジェクトとの関係:** 次段階で外部連携設定を意味ブロックから生成する。

## Plugins

**概念:** 上記を束ねて配布する単位。

**使い方:** マーケットプレイスまたはローカルパスからインストール。

**このプロジェクトとの関係:** 最終段階でハーネス設定一式を Plugin として配布可能にする。

## 権限

**概念:** 誰の設定か（スコープ）、どの程度自動か（モード）。

**詳細:** `constraint.permission-scope` を参照。

**このプロジェクトとの関係:** v1 では解説のみ。次段階でスコープ別に権限設定を生成する。
