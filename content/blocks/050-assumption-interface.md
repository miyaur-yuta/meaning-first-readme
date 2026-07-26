+++
id = "assumption.readme-interface"
kind = "assumption"
title = "READMEを主要なAI文脈インターフェースとして扱う"
summary = "現段階では、リポジトリ直下のREADMEが人間とAIの双方から最も発見されやすい文脈入口であると仮定する。"
order = 60
priority = 86
audience = ["both"]
tags = ["前提", "README", "AI", "入口", "発見性"]
status = "active"
trust = "reviewed"
depends_on = ["scope.readers", "scope.artifact"]
owner = "project"
updated = "2026-07-26"
+++
本プロジェクトは、READMEが常に全環境で最強の文脈形式であるとは断定しない。採用する前提は、リポジトリを開いた人間と、多くの開発支援AIが最初に参照しやすい入口としてREADMEを扱えることである。

この前提が成立しない環境では、同じ意味ブロックから別形式を生成する。例として、短い`AGENTS.md`、JSONマニフェスト、タスク専用コンテキスト、静的Webページがある。

READMEへ全情報を直接詰め込むのではなく、READMEを正本へ接続する標準ビューとすることで、入口の強さと構造化データの保守性を両立する。
