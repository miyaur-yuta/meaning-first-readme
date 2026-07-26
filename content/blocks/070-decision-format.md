+++
id = "decision.markdown-toml"
kind = "decision"
title = "Markdown本文とTOML前置きを正本にする"
summary = "人間が編集しやすいMarkdownと、標準ライブラリで解析できるTOMLメタデータを一つのブロックに統合する。"
order = 80
priority = 84
audience = ["both"]
tags = ["意思決定", "Markdown", "TOML", "依存ゼロ"]
status = "active"
trust = "reviewed"
depends_on = ["scope.artifact", "principle.typed-claims"]
rationale = "Markdownは本文の可読性を保ち、TOMLはPython標準ライブラリで厳密に解析できるため、実行時依存を増やさず型付き文書を実現できる。"
owner = "project"
updated = "2026-07-26"
+++
各ソースブロックは`+++`で囲まれたTOML前置きとMarkdown本文からなる。

この形式により、タイトル、要約、型、優先度、依存、根拠、期限を機械的に読みながら、本文は通常のMarkdownとしてレビューできる。YAML専用ライブラリやデータベースを実行時必須にしないため、クローン直後でもPython 3.11以上だけで検証できる。

形式を変更する場合は、既存IDと意味スナップショットを保持できる移行器を先に用意する。
