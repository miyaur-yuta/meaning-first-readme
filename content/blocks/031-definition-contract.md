+++
id = "definition.context-contract"
kind = "definition"
title = "文脈契約"
summary = "文脈契約は、目的・優先順位・境界・信頼区分・不足時の挙動を読者とAIへ明示する。"
order = 41
priority = 94
audience = ["both"]
tags = ["定義", "文脈契約", "優先順位", "不足"]
status = "active"
trust = "reviewed"
depends_on = ["definition.meaning", "scope.readers"]
owner = "project"
updated = "2026-07-26"
+++
文脈契約は、READMEを単なる説明文から実行可能なインターフェースへ変える規約である。

文脈契約には次を含める。

- **目的:** 最終的に何を達成するか。
- **優先順位:** 衝突した情報のどちらを採用するか。
- **境界:** 対象外、禁止事項、権限の限界。
- **信頼区分:** authoritative、reviewed、unverified、external_untrusted。
- **根拠:** 主張を支える資料または実験。
- **停止条件:** 情報不足、矛盾、期限切れを検出した際の挙動。
- **更新方法:** 変更を検証し、意味差分を残す方法。

AI向けのタスク文脈を生成するとき、この契約は省略可能な補足ではなく、最初に含める実行条件となる。
