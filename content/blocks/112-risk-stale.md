+++
id = "risk.stale-truth"
kind = "risk"
title = "古い情報が有効な事実として残る"
summary = "正しかった記述が時間経過で変化し、更新日だけ新しい文書の中に残存する危険がある。"
order = 122
priority = 90
audience = ["both"]
tags = ["リスク", "鮮度", "期限", "事実", "更新", "失敗モード", "改善"]
status = "active"
trust = "reviewed"
depends_on = ["constraint.truth", "constraint.provenance"]
owner = "project"
updated = "2026-07-26"
+++
ファイルの更新日時は、各主張の鮮度を保証しない。軽微な編集で文書全体の日時が新しくなっても、内部の数値や外部仕様は古いまま残る。

変化し得る情報には`volatile = true`と`expires`を設定する。期限を過ぎた有効ブロックは検証エラーにし、公開前に再確認または状態変更を要求する。

恒久的な原則へ不要な期限を付けず、外部仕様、料金、役職、記録、予定日など、時間で変わる主張へ限定して使う。
