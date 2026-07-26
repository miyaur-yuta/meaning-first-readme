+++
id = "constraint.real-conversation-quality"
kind = "constraint"
title = "整備後にリアルに人間がやり取りする想定の品質を出す"
summary = "自動生成されたハーネス設定と README は、実際に人間が Claude Code と対話したときに、取り違え・迷子・停滞が起きない品質でなければならない。"
order = 77
priority = 55
audience = ["human"]
tags = ["品質", "対話", "人間", "ClaudeCode"]
status = "active"
trust = "reviewed"
depends_on = ["constraint.truth", "constraint.permission-scope", "thesis.frictionless-ai-handoff"]
claims = ["自動生成物は実際の人間との対話で取り違えが起きない品質が必要"]
owner = "project"
updated = "2026-07-26"
+++
検証とベンチマークを通過した生成物でも、実際の人間が Claude Code と対話したときに役立たなければ、意味を達成したとは呼ばない。

## リアルな対話で起きる失敗モード

1. **取り違え:**禁止事項を読み飛ばして AI が勝手に実行する
2. **迷子:**目的がぼやけて AI が脱線する
3. **停滞:**次の一手が分からず AI が止まるか、推測で埋める
4. **権限の誤認:**個人設定と共有設定を混同して、チームに無断でルールが変わる
5. **文脈の欠落:**トークン予算で前提が削られ、AI が誤判断する

## 受け入れ条件

生成物は次を満たす。

- 目的・禁止事項・次の一手が、AI の最初の応答に反映される
- 禁止事項は Hooks または `deny` ルールで機械的に担保される
- 人間向け README ビューは、AI に何を渡しているかを俯瞰できる
- 個人設定と共有設定の区別が、ファイル構造と文面の両方で明示される

## 検証方法

ベンチマークと監査に加えて、代表ペルソナによる対話観察を記録する。観察結果は意味ブロックの `evidence` として残し、回帰検出に使う。
