+++
id = "principle.progressive-disclosure"
kind = "principle"
title = "段階的開示"
summary = "最短の入口から詳細な根拠まで、読者が必要な深さを選べる階層を作る。"
order = 50
priority = 88
audience = ["both"]
tags = ["原則", "段階的開示", "可読性", "階層", "初見", "人間", "保守", "支援"]
status = "active"
trust = "reviewed"
depends_on = ["purpose.meaning", "scope.readers"]
owner = "project"
updated = "2026-07-26"
+++
長い文書を全員に最初から読ませる設計は失敗する。情報は次の順序で開示する。

1. 一文の目的。
2. 対象範囲と非目的。
3. 現在の判断に必要な要約。
4. 手順と受け入れ条件。
5. 根拠、例外、履歴。
6. 機械可読な完全マニフェスト。

各層は上位層を否定せず、詳細化する。同じ事実を別表現で大量に複製するのではなく、安定したブロックIDへリンクする。人間には目次と見出し、AIにはタスク別選択と依存閉包を提供する。
