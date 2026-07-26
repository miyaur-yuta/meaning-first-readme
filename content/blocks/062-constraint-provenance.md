+++
id = "constraint.provenance"
kind = "constraint"
title = "主張の来歴を失わない"
summary = "重要な主張は、所有者、更新日、根拠、依存、信頼区分のいずれかで追跡可能にする。"
order = 72
priority = 94
audience = ["both"]
tags = ["制約", "来歴", "所有者", "更新日", "根拠"]
status = "active"
trust = "reviewed"
depends_on = ["principle.typed-claims", "constraint.truth"]
owner = "project"
updated = "2026-07-26"
+++
コピーされた文章が正しく見えても、誰が、いつ、何を根拠に書いたか分からなければ更新できない。

各意味ブロックは安定したIDとソースパスを持つ。重要な判断には理由を、事実には根拠を、揮発情報には失効日を、手順には受け入れ条件を付ける。生成READMEにはブロックIDと内容指紋を埋め込み、ソースとの差異を検出できるようにする。

来歴情報は装飾ではない。矛盾が起きたときに、どちらを再確認すべきか決めるための最小情報である。
