+++
id = "scope.personas"
kind = "scope"
title = "中心ペルソナの典型タスク"
summary = "ペルソナA/B/C の典型タスクを明記し、対話観察の再現性を担保する。"
order = 17
priority = 58
audience = ["human"]
tags = ["ペルソナ", "典型タスク", "対話観察"]
status = "active"
trust = "reviewed"
depends_on = ["thesis.frictionless-ai-handoff", "definition.real-conversation"]
claims = ["代表ペルソナの典型タスクは観察の再現に必要"]
owner = "project"
updated = "2026-07-26"
+++
「リアルな対話品質」を観察可能にするため、中心ペルソナの典型タスクを固定する。

## ペルソナA：Claude Code を使い始めた人

**状況:** 初めてリポジトリを Claude Code で開く。

**典型タスク:**
1. 「このプロジェクトの目的は？」と聞く
2. 「次に何をすべき？」と聞く
3. 「やってはいけないことは？」と聞く

**成功基準:** いずれも README の目的・次の一手・禁止事項が最初の応答に反映される。

## ペルソナB：ハーネス設定を保守する人

**状況:** 既存の意味ブロックを更新する。

**典型タスク:**
1. 変更したいブロックの根拠（`evidence`/`depends_on`）を確認する
2. 変更後 `mfr validate` を走らせる
3. `mfr audit` で整合性を確認する

**成功基準:** 根拠が欠けている変更は検証で弾かれ、怖くなく更新できる。

## ペルソナC：初見でリポジトリを見る人

**状況:** GitHub で README を開く。

**典型タスク:**
1. 目次から関心セクションへ飛ぶ
2. AI に何を渡しているか把握する
3. 必要なら `docs/START_HERE.md` から深掘りする

**成功基準:** 人間向けビューで全体を俯瞰でき、AI 文脈との違いが分かる。

## 観察の記録

各タスクの実施結果は `evidence` 種別ブロックとして残し、回帰検出に使う。サンプルサイズ1の印象は採用しない。
