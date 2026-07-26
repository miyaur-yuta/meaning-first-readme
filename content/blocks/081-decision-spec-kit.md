+++
id = "decision.spec-kit-integration"
kind = "decision"
title = "Spec Kit との関係：意味ブロックを Constitution/Spec に接続"
summary = "GitHub Spec Kit の SDD ライフサイクル（constitution/spec/clarify/plan/tasks/implement/converge）と意味ブロックを接続し、要件定義ファーストで運用する。"
order = 81
priority = 60
audience = ["human"]
tags = ["SpecKit", "SDD", "要件定義", "ClaudeCode", "決定"]
status = "active"
trust = "authoritative"
depends_on = ["thesis.frictionless-ai-handoff", "scope.explanation-vs-generation", "guide.claude-code-primitives"]
claims = [
  "Spec Kit の SDD ライフサイクルを採用し、意味ブロックをその前段・入力として使う",
  "constitution.md は意味ブロックの principle/constraint 層から生成する",
  "spec.md は purpose/scope/non_goal 層から生成する",
]
rationale = "ユーザーの『まず要件定義しない？Spec Kit 入れて』という指摘通り、意味ブロック単体では要件定義の工程順序がなく、Spec Kit がその欠けを埋める。意味ブロックは『正本』、Spec Kit は『工程』。"
owner = "project"
updated = "2026-07-26"
+++
GitHub Spec Kit（2026-07 時点 v0.12.5）の SDD ライフサイクルを採用し、本プロジェクトの意味ブロック層と接続する。

## Spec Kit とは

GitHub 製のオープンソース CLI・プロンプト群。自然言語の仕様書を一次産物とし、コードをそこから生成する「Spec-Driven Development」を Claude Code / Copilot / Cursor 等で実施するためのフレームワーク。

## SDD の9フェーズ

| フェーズ | コマンド | 役割 |
|---|---|---|
| Constitution | `/speckit.constitution` | プロジェクト原則・ガバナンス |
| Specify | `/speckit.specify` | 機能要件・ユーザーストーリー |
| Clarify | `/speckit.clarify` | 曖昧さ解消 |
| Plan | `/speckit.plan` | 技術アーキ・スタック |
| Checklist | `/speckit.checklist` | 仕様の完全性検証 |
| Tasks | `/speckit.tasks` | 実行可能なタスク分解 |
| Analyze | `/speckit.analyze` | 全アーティファクトの整合性検査 |
| Implement | `/speckit.implement` | コード生成 |
| Converge | `/speckit.converge` | 仕様・計画との収束確認 |

## 意味ブロックとの対応

| Spec Kit 入力 | 意味ブロック層 |
|---|---|
| `memory/constitution.md` | `principle` / `constraint` / `decision` |
| `spec.md` | `purpose` / `scope` / `non_goal` / `definition` |
| `plan.md` | `architecture` / `procedure` |
| `tasks.md` | `procedure`（具体化） |
| 検査入力 | `evidence` / `risk` / `fact` |

意味ブロックは**正本（single source of truth）**、Spec Kit は**工程（lifecycle）**。両者は競合せず、意味ブロックから Spec Kit の各 Markdown を生成し、Spec Kit が AI と協調して実装に落とす。

## 運用フロー

1. **ヒアリング（認知負荷低）:** 人間が要点だけ伝える
2. **意味ブロック化:** AI がヒアリング結果を `purpose`/`scope`/`non_goal`/`definition` に構造化
3. **Constitution/Spec 生成:** 意味ブロックから Spec Kit の Markdown を生成
4. **Clarify/Plan/Tasks:** Spec Kit のフェーズを順に進める
5. **Implement/Converge:** コード生成と収束検証

## v1 の範囲

- **作る:** 意味ブロック → Spec Kit Markdown の**生成ガイド**（説明資料）
- **作らない:** 自動生成機能・Spec Kit CLI のラッパー（次段階）

Spec Kit 自体の説明は `guide.spec-kit`（別ブロック）に譲る。
