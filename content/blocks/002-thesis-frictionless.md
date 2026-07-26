+++
id = "thesis.frictionless-ai-handoff"
kind = "purpose"
title = "思想：Claude Code ハーネスへの引き渡し摩擦を限界まで減らす"
summary = "README を整備する道具ではなく、Claude Code ハーネス（CLAUDE.md, Skills, Hooks, Subagents, MCP）への引き渡しを、意味ブロックから一貫して生成・検証する体制にする。"
order = 9
priority = 70
audience = ["human"]
tags = ["思想", "ClaudeCode", "ハーネス", "CLAUDE.md", "Skills", "Hooks", "Subagents", "MCP"]
status = "active"
trust = "reviewed"
depends_on = ["purpose.meaning"]
claims = ["Claude Code は README を超える包括ハーネスである", "README は人間向けビューの一つにすぎない"]
owner = "project"
updated = "2026-07-26"
+++
このプロジェクトの思想は、「README を正しく書く」ことではなく、**Claude Code ハーネスへのリポジトリ引き渡し摩擦を限界まで減らす**ことにある。

## Claude Code は README を超える

Claude Code（2026-07 時点）は、README を含む包括的なエージェントハーネスである。主な拡張プリミティブは次の7つ。

| プリミティブ | 役割 | 読込タイミング |
|---|---|---|
| CLAUDE.md / Rules | 常に効く文脈・指示 | セッション毎に常に |
| Skills | オンデマンドの知識・ワークフロー | `/` や自動判定 |
| Hooks | ライフサイクル事件で必ず発火 | 毎回必ず |
| Subagents | 独立コンテキストで専門作業 | タスク委譲時 |
| Agent Teams | 複数セッション協調 | 並列処理時 |
| MCP | 外部システム接続 | ツール呼び出し時 |
| Plugins | 上記を束ねて配布 | インストール時 |

README は **CLAUDE.md の一部** にすぎない。「README を整備する道具」という位置付けでは、Claude Code 本体の機能のほんの一部しか支えない。

## このプロジェクトが目指す状態

意味ブロック（`content/blocks/`）を正本とし、そこから Claude Code ハーネス設定を一貫して生成・検証する。

- `CLAUDE.md` を意味ブロックから生成する
- Skills 用の YAML/markdown を同じブロックから生成する
- 「禁止事項」ブロックから Hooks（モデル依存しない強制ルール）を生成する
- 「手順」ブロックから Subagent 定義を生成する
- README は人間向けビューの1つにすぎない

## 中心ペルソナ

### ペルソナA：Claude Code を使い始めた人（中心）
- **苦痛:** CLAUDE.md, Skills, Hooks の設定がバラバラで、AI が方針を取り違える
- **解く:** 意味ブロックを正本にし、各種ハーネス設定を一貫生成する

### ペルソナB：ハーネス設定を保守する人
- **苦痛:** 「このルール消していい？根拠どこ？」が分からない
- **解く:** ブロックに根拠・依存・来歴を強制し、怖くなく更新できる

### ペルソナC：初見でリポジトリを見る人
- **苦痛:** 何を Claude Code に渡しているか把握できない
- **解く:** 人間向け README ビューで全体を俯瞰できる

## 成功の測り方

成果物の価値は「機能の数」ではなく、**対象ペルソナの摩擦がどれだけ減ったか**で測る。
