+++
id = "procedure.author"
kind = "procedure"
title = "意味ブロックを追加する手順"
summary = "新しい文章を、目的との関係、型、根拠、依存、受け入れ条件を持つ更新可能な単位へ変換する。"
order = 100
priority = 82
audience = ["both"]
tags = ["手順", "執筆", "追加", "ブロック"]
status = "active"
trust = "reviewed"
depends_on = ["decision.markdown-toml", "constraint.provenance"]
acceptance = ["一意で安定したIDがある", "kindが主張の身分と一致する", "目的または既存ブロックへの依存がある", "事実には根拠、判断には理由、手順には受け入れ条件がある", "validateがエラーなしで完了する"]
owner = "project"
updated = "2026-07-26"
+++
1. 追加したい内容が、目的、判断、行動、検証のどれに影響するか一文で書く。
2. 内容の身分に合う`kind`を選ぶ。
3. 変更されにくい概念名からブロックIDを決める。章番号をIDにしない。
4. 単独で読める`summary`を書く。
5. 依存先、根拠、対象読者、信頼区分、更新日を宣言する。
6. 本文に適用範囲、例外、次の行動を含める。
7. 生成、検証、監査、ベンチマークを実行する。

既存ブロックと同じ意味を言い換えるだけの場合は、新規追加せず既存ブロックを改善する。
