+++
id = "scope.artifact"
kind = "scope"
title = "成果物の範囲"
summary = "README本文だけでなく、意味ブロック、検証器、文脈コンパイラ、ベンチマーク、変更履歴を一つの成果物として扱う。"
order = 21
priority = 92
audience = ["both"]
tags = ["成果物", "README", "CLI", "検証", "ベンチマーク"]
status = "active"
trust = "reviewed"
depends_on = ["purpose.meaning", "scope.readers"]
owner = "project"
updated = "2026-07-26"
+++
成果物は単一のMarkdownファイルに限定しない。正本は型付きの意味ブロック群であり、READMEはその人間可読ビューである。

成果物に含めるものは以下である。

- `content/blocks/`: 独立して参照できる意味ブロック。
- `README.md`: ブロックから決定論的に生成される標準ビュー。
- `mfr validate`: 構造、参照、矛盾、期限、根拠を検査する品質ゲート。
- `mfr context`: タスクと予算に応じて文脈を選択するコンパイラ。
- `mfr audit`: 単一スコアに潰さず、複数の品質次元を報告する監査器。
- `mfr benchmark`: 文脈検索が必要な意味を取り出せるか測るテスト。
- 意味スナップショットと差分: 文言ではなく、判断・主張・依存の変化を追跡する記録。

READMEだけを配布しても読めるが、リポジトリ全体を使うと更新可能で検証可能な知識基盤になる。
