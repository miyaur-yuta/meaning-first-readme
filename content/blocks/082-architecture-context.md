+++
id = "architecture.context-packer"
kind = "architecture"
title = "トークン予算付き文脈コンパイラ"
summary = "タスク関連度、優先度、信頼区分、必須型、依存閉包を使い、予算内でAI向け文脈を組み立てる。"
order = 92
priority = 95
audience = ["both"]
tags = ["構造", "コンテキスト", "トークン", "トークン予算", "検索", "AI", "タスク専用", "外部命令"]
status = "active"
trust = "reviewed"
depends_on = ["architecture.semantic-graph", "scope.readers", "constraint.boundary"]
evidence = ["evidence.retrieval-benchmark"]
owner = "project"
updated = "2026-07-26"
+++
`mfr context`は全文を単純に切り詰めない。まず目的、対象範囲、非目的、重要制約を固定アンカーとして選ぶ。次にタスク文から日本語文字特徴と英数字語を抽出し、タイトル、要約、タグ、本文との関連度を計算する。

候補を選ぶ際は、そのブロックが依存する前提と根拠も同時に予算へ入れる。予算を超える候補は、前提だけを欠落させて入れず、候補単位で見送る。

出力には選択ID、省略ID、推定トークン、信頼区分、内容指紋を含める。外部未信頼ブロックは引用として明示し、命令として実行しない契約を先頭に置く。
