+++
id = "definition.real-conversation"
kind = "definition"
title = "「リアルな対話」の定義"
summary = "整備後のハーネス設定と README が、実際の人間と Claude Code の対話で取り違え・迷子・停滞を起こさない状態を指す。装飾ではなく観察可能な基準。"
order = 30
priority = 58
audience = ["human"]
tags = ["定義", "対話", "品質", "用語"]
status = "active"
trust = "reviewed"
depends_on = ["constraint.real-conversation-quality", "thesis.frictionless-ai-handoff"]
claims = ["「リアルな対話」は観察可能な基準であり、主観ではない"]
owner = "project"
updated = "2026-07-26"
+++
「リアルな対話」とは、生成したハーネス設定と README を実際に読み込ませた Claude Code セッションで、**代表ペルソナの典型タスク**を実施したときの振る舞いを指す。

## 含むもの

- ペルソナ（A/B/C）の典型タスクをセッションで再現すること
- AI の最初の応答に目的・禁止事項・次の一手が反映されているか
- 禁止事項が Hooks または `deny` で機械的に守られるか
- 人間向けビューで何を渡しているか俯瞰できるか

## 含まないもの

- 「なんとなく自然に話せた」等の主観
- サンプルサイズ1の印象
- 本番環境以外での再現のない成果

## 観察の記録

対話観察の結果は `evidence` 種別の意味ブロックとして残す。これにより、再現性・回帰検出・根拠提示が可能になる。

## なぜ定義が必要か

「リアルな対話品質」を主観のまま放置すると、整備が思い込みにすり替わる。用語を固定することで、何を測るかを共通にする。
