+++
id = "principle.fail-closed"
kind = "principle"
title = "不足時は安全側に停止する"
summary = "根拠不足、参照切れ、矛盾、期限切れを検出した場合、もっともらしい補完ではなく失敗として扱う。"
order = 52
priority = 96
audience = ["both"]
tags = ["原則", "停止", "根拠不足", "矛盾", "安全"]
status = "active"
trust = "reviewed"
depends_on = ["definition.context-contract"]
owner = "project"
updated = "2026-07-26"
+++
AIは空白を自然な文章で補えるため、文書の不足が見えにくくなる。意味を守るには、不足を明示的な状態として扱う。

次の状態では品質ゲートを失敗させる。

- 必須ブロックがない。
- 参照先のIDが存在しない。
- 依存グラフに循環がある。
- 有効な事実に根拠がない。
- 有効な揮発情報が期限切れである。
- 同じ正規化主張が、別の有効ブロックで肯定と否定の両方に現れる。

失敗は欠陥の隠蔽ではなく、次の確認点を提供する出力である。
