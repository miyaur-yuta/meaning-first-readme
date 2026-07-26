+++
id = "guide.spec-kit"
kind = "procedure"
title = "Spec Kit：概念・使い方・最小構成"
summary = "GitHub Spec Kit の概念・CLI・最小構成を整理する。本プロジェクトの意味ブロックを前段として接続するための引き継ぎ資料。"
order = 91
priority = 60
audience = ["human"]
tags = ["ガイド", "SpecKit", "SDD", "使い方", "最小構成"]
status = "active"
trust = "reviewed"
depends_on = ["decision.spec-kit-integration", "thesis.frictionless-ai-handoff"]
claims = ["Spec Kit の概念と最小構成を文書化する"]
acceptance = [
  "Spec Kit の位置付けと9フェーズをカバーしている",
  "インストールから最初の spec までの手順がある",
  "このプロジェクトとの関係が明記されている",
]
owner = "project"
updated = "2026-07-26"
+++
GitHub Spec Kit（v0.12.5, 2026-07）の概念・使い方・最小構成を整理する。

## 概念

Spec Kit は GitHub 製のオープンソース CLI・プロンプト群。自然言語の仕様書を一次産物とする **Spec-Driven Development（SDD）** を、Claude Code / Copilot / Cursor / Gemini 等の AI エージェントで実施するためのフレームワーク。

従来の「コードが王」ではなく、**「仕様が王、コードは仕様から生成される」** という転倒。

## 使い方

### インストール

```bash
uv tool install specify-cli
# または pipx install specify-cli
```

### 初期化

```bash
specify init <project-name>
cd <project-name>
```

### 主要コマンド

```bash
/speckit.constitution   # プロジェクト原則を定義
/speckit.specify        # 機能要件・ユーザーストーリー
/speckit.clarify        # 曖昧さをAIが質問して解消
/speckit.plan           # 技術アーキ・スタック決定
/speckit.checklist      # 仕様の完全性検証
/speckit.tasks          # 実行可能タスクに分解
/speckit.analyze        # 全アーティファクトの整合性検査
/speckit.implement      # コード生成
/speckit.converge       # 仕様・計画との収束確認
```

## 最小構成

Spec Kit が生成する主要 Markdown：

```
project/
├── memory/
│   └── constitution.md   # プロジェクト原則（不変）
├── specs/
│   └── <feature>/
│       ├── spec.md       # 機能要件
│       ├── plan.md       # 技術計画
│       └── tasks.md      # タスク分解
└── .speckit/
    └── config.yml        # 設定
```

## このプロジェクトとの関係

本プロジェクト（Meaning First README）の**意味ブロックは Spec Kit の前段**：

- `principle` / `constraint` → `constitution.md`
- `purpose` / `scope` / `non_goal` / `definition` → `spec.md`
- `architecture` / `procedure` → `plan.md` / `tasks.md`
- `evidence` / `risk` / `fact` → 検査入力

詳細は [`decision.spec-kit-integration`](081-decision-spec-kit.md) を参照。

## 認知負荷の低い運用

ユーザーの要望「認知負荷の低いヒアリングを一度やって、AI エージェントが走り続ける」は次のフローで実現する：

1. 人間が要点を伝える（認知負荷低）
2. AI が意味ブロックに構造化
3. Spec Kit の Markdown を生成
4. Spec Kit のフェーズを AI が自動進行
5. 人間は要所で承認のみ

このフローの具体化は次段階の実装課題。
