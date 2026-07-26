+++
id = "principle.typed-claims"
kind = "principle"
title = "文章を型付きの主張へ分解する"
summary = "目的、事実、前提、制約、判断、根拠、手順を型で分け、同じ強さの文章として扱わない。"
order = 51
priority = 92
audience = ["both"]
tags = ["原則", "型", "事実", "判断", "根拠"]
status = "active"
trust = "reviewed"
depends_on = ["definition.meaning", "definition.context-contract"]
owner = "project"
updated = "2026-07-26"
+++
自然言語は柔軟だが、情報の身分を隠しやすい。そこで各ブロックに`kind`を持たせる。

- `fact`は根拠または情報源を要求する。
- `assumption`は検証前の前提として表示する。
- `decision`は選択理由を要求する。
- `constraint`は違反時の挙動を明確にする。
- `procedure`は受け入れ条件を要求する。
- `evidence`は支える対象への逆参照を持つ。
- `non_goal`は目的の拡大解釈を防ぐ。

型は文章表現を制限するためではなく、読者が主張の強さと扱い方を誤らないために使う。
