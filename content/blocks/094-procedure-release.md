+++
id = "procedure.release"
kind = "procedure"
title = "公開またはPR作成を最終判断する"
summary = "技術的準備が完了した後に、権限を持つ人間へ「PRを出すか」を一度だけ明確に確認し、承認時のみ公開操作へ進む。"
order = 104
priority = 100
audience = ["both"]
tags = ["手順", "PR", "公開", "最終判断", "承認"]
status = "active"
trust = "authoritative"
depends_on = ["procedure.review", "procedure.build", "constraint.truth", "constraint.boundary"]
acceptance = ["検証、監査、ベンチマーク、テストが成功している", "PRタイトルと本文が事実に基づいている", "秘密情報と未許諾素材が含まれない", "差分と既知の限界を提示した", "権限を持つ人間が明示的にPR作成を承認した"]
owner = "project"
updated = "2026-07-26"
+++
公開準備では、ブランチ、コミット、PRタイトル、説明、検証結果、既知の限界を揃える。ここまでは承認前に実施できる。

最後に権限を持つ人間へ、次の二択を提示する。

- **出す:** PRを作成し、取得できた公開URLと結果を報告する。
- **出さない:** 公開操作を行わず、指定された修正へ戻る。

「公開してよいか」と「PRを出すか」を別々の曖昧な質問に分けない。PR作成が公開行為に当たる前提を明示し、最終確認は一つの実行判断にする。承認されていない状態で外部リポジトリへ送信しない。
