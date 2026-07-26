+++
id = "evidence.self-host-build"
kind = "evidence"
title = "自己ホストビルドの再現証跡"
summary = "同じ意味ブロック集合からREADMEとマニフェストを再生成し、内容指紋と出力差分を検査できる。"
order = 110
priority = 76
audience = ["both"]
tags = ["根拠", "自己ホスト", "再現性", "指紋"]
status = "active"
trust = "reviewed"
depends_on = ["purpose.meaning"]
supports = ["decision.self-hosting"]
owner = "project"
updated = "2026-07-26"
+++
再現手順は`procedure.build`に定義されている。ビルドはブロックを安定した`order`とIDで並べ、本文とメタデータからSHA-256指紋を生成する。

検証可能な観測点は次の通りである。

- 同じ入力でREADMEの本文とリポジトリ指紋が一致する。
- ブロック本文または意味メタデータを変更すると、対応する指紋が変わる。
- 生成済みREADMEを手で変更すると、再生成後のGit差分で検出できる。
- マニフェストから全ブロックID、依存、根拠、状態を復元できる。

この証跡は「READMEが常に正しい」ことではなく、入力と生成物の対応を再現できることを支える。
