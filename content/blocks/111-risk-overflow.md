+++
id = "risk.context-overflow"
kind = "risk"
title = "長文化による文脈飽和"
summary = "重要情報が存在していても、入力上限、注意の分散、検索失敗によって実質的に利用不能になる危険がある。"
order = 121
priority = 91
audience = ["both"]
tags = ["リスク", "長文化", "トークン", "検索", "注意", "失敗モード", "改善", "タスク専用"]
status = "active"
trust = "reviewed"
depends_on = ["non_goal.length", "principle.progressive-disclosure", "architecture.context-packer"]
owner = "project"
updated = "2026-07-26"
+++
全文を常にAIへ渡す設計では、上限を超えた部分が切り捨てられたり、重要な制約が大量の説明に埋もれたりする。

対策は、目的と制約を固定アンカーにし、タスク関連度で候補を選び、依存閉包を維持して予算へ詰めることである。さらに、選択されなかったIDを出力し、「全文を理解した」という誤認を防ぐ。

長さを増やす変更では、READMEの総容量だけでなく、代表タスクの検索再現率と生成文脈の推定トークンを確認する。
