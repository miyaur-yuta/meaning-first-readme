+++
id = "decision.self-hosting"
kind = "decision"
title = "プロジェクト自身のREADMEを自身で生成する"
summary = "説明対象と実装対象を一致させ、READMEコンパイラの欠陥を日常の変更で露出させる。"
order = 82
priority = 86
audience = ["both"]
tags = ["意思決定", "自己ホスト", "README", "検証"]
status = "active"
trust = "reviewed"
depends_on = ["architecture.pipeline", "decision.markdown-toml"]
evidence = ["evidence.self-host-build"]
rationale = "サンプルだけで動く実装は実運用の複雑さを検証できない。正本READMEを同じ仕組みで生成すれば、構文、順序、参照、再現性を継続的に試せる。"
owner = "project"
updated = "2026-07-26"
+++
`README.md`は手書きの宣伝文ではなく、`content/blocks/`から生成する。CIでは再生成後にGit差分がないことを確認する。

自己ホストにより、次の欠陥が早期に分かる。

- 見出しや目次が壊れる。
- メタデータが人間の可読性を損なう。
- マニフェストが過大になる。
- ブロック順序が不安定になる。
- 内容指紋が再現されない。

生成物を正本にしないため、機械的な再構築と人間によるレビューを両立する。
