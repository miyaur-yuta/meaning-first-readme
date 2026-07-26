+++
id = "constraint.truth"
kind = "constraint"
title = "未確認事項を事実として書かない"
summary = "記録、期限、性能、外部評価を断定する前に、根拠、確認日、測定方法を保持する。"
order = 70
priority = 100
audience = ["both"]
tags = ["制約", "事実", "根拠", "期限", "測定"]
status = "active"
trust = "authoritative"
depends_on = ["purpose.meaning", "principle.typed-claims"]
claims = ["未確認事項は事実として断定しない"]
owner = "project"
updated = "2026-07-26"
+++
次の内容は、出典または再現可能な測定なしに断定してはならない。

- 世界記録、業界最大、最高性能などの比較表現。
- 将来の達成日、作業時間、処理速度。
- ファイルサイズ、行数、章数、テスト数。
- 外部サービスの仕様、料金、制限。
- 誰かの承認、申請、公開状態。

測定値は生成時に実測し、比較値には確認日と対象範囲を付ける。根拠がない場合は`assumption`、`question`相当の説明、または未採用候補として扱い、見栄えのために数値を作らない。
