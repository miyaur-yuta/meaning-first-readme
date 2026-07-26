+++
id = "example.typed-block"
kind = "example"
title = "型付き意味ブロックの最小例"
summary = "事実、判断、手順を同じ文章として混ぜず、メタデータと本文で役割を明示する例を示す。"
order = 130
priority = 62
audience = ["both"]
tags = ["例", "TOML", "ブロック", "執筆", "ID", "型", "根拠", "依存", "受け入れ条件"]
status = "active"
trust = "reviewed"
depends_on = ["decision.markdown-toml", "procedure.author"]
owner = "project"
updated = "2026-07-26"
+++
```markdown
+++
id = "decision.example"
kind = "decision"
title = "例示用の判断"
summary = "何を選び、なぜ選んだかを単独で理解できる要約。"
priority = 70
depends_on = ["purpose.meaning"]
rationale = "候補Aと候補Bを比較し、目的への適合が高いAを選んだ。"
updated = "2026-07-26"
+++

本文には適用範囲、選ばなかった候補、撤回条件を書く。
```

IDは表示順ではなく概念へ結び付ける。本文を移動してもIDを変えない。判断を撤回する場合は削除だけで履歴を消さず、状態または変更履歴で追跡可能にする。
