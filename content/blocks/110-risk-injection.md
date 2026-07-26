+++
id = "risk.prompt-injection"
kind = "risk"
title = "外部文書による命令注入"
summary = "READMEへ引用した外部データが、AIに対する命令として解釈され、目的や制約を上書きする危険がある。"
order = 120
priority = 96
audience = ["both"]
tags = ["リスク", "プロンプトインジェクション", "AI", "外部データ"]
status = "active"
trust = "reviewed"
depends_on = ["constraint.boundary", "architecture.context-packer"]
owner = "project"
updated = "2026-07-26"
+++
攻撃者または偶発的な文章は、資料の中に実行指示を埋め込める。人間には引用に見えても、AIが同じコンテキスト内の命令として扱う可能性がある。

対策は次の通りである。

- 外部データへ`external_untrusted`を付ける。
- 文脈生成時に警告と引用記号で隔離する。
- 信頼区分をランキング理由と出力メタデータへ含める。
- 未信頼ブロックから目的・制約への上書き関係を作らない。
- 指示らしい既知パターンを監査で警告する。

文字列パターンだけで完全には防げないため、信頼境界を構造として保持する。
