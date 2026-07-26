+++
id = "evidence.retrieval-benchmark"
kind = "evidence"
title = "タスク別文脈検索ベンチマーク"
summary = "代表的な質問ごとに期待ブロックを宣言し、予算内の選択結果に対する再現率と適合率を測定する。"
order = 111
priority = 80
audience = ["both"]
tags = ["根拠", "ベンチマーク", "検索", "再現率", "適合率", "意味評価", "意味スコア"]
status = "active"
trust = "reviewed"
depends_on = ["purpose.meaning"]
supports = ["architecture.context-packer"]
owner = "project"
updated = "2026-07-26"
+++
`benchmarks/tasks.json`は、タスク名、自然言語クエリ、期待するブロックID、トークン予算を保持する。

各ケースで以下を測る。

- **再現率:** 期待ブロックのうち選択された割合。
- **適合率:** 選択ブロックのうち期待ブロックだった割合。
- **ケース合否:** 宣言された最小再現率を満たすか。
- **全体合否:** 全ケースの合格と、設定されたマクロ閾値を満たすか。

必須の目的・制約ブロックは多くのタスクへ入るため、適合率だけを最大化しない。検索器を変更した場合、同じケースで結果を比較して回帰を検出する。
