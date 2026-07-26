+++
id = "constraint.update-safety"
kind = "constraint"
title = "更新で意味を静かに壊さない"
summary = "文言差分だけでなく、型、主張、否定、依存、根拠、状態の変化を意味差分として確認する。"
order = 73
priority = 93
audience = ["both"]
tags = ["制約", "更新", "意味差分", "破壊的変更"]
status = "active"
trust = "reviewed"
depends_on = ["constraint.provenance", "scope.artifact"]
owner = "project"
updated = "2026-07-26"
+++
文章の編集が小さくても、目的や制約の変更は大きな影響を持つ。反対に、全面的な言い換えでも意味が同じ場合がある。

更新時には次を比較する。

- ブロックの追加、削除、状態変更。
- `claims`と`negates`の変化。
- 依存先と根拠先の変化。
- 優先度、信頼区分、対象読者の変化。
- 手順の受け入れ条件の変化。
- 本文の内容指紋。

目的、非目的、制約の変更は破壊的変更としてレビューする。生成済みREADMEを直接編集した変更は正本へ戻せないため、受け入れない。
