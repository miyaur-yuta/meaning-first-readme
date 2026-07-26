+++
id = "scope.entry"
kind = "scope"
title = "最初の30秒でやること"
summary = "全体を読む前に、ひとこと説明と最短コマンドだけ通す。"
order = 15
priority = 60
audience = ["human"]
tags = ["入口", "最短", "オンボーディング"]
status = "active"
trust = "reviewed"
depends_on = ["purpose.meaning", "scope.readers"]
claims = ["初見は入口ドキュメントと最短コマンドから入る"]
owner = "project"
updated = "2026-07-26"
+++
ひとことで言うと: Claude Code ハーネス（CLAUDE.md, Skills, Hooks, Subagents, MCP）への引き渡し摩擦を、意味ブロックから限界まで減らすツール。v1 は README ビューのみ。

レビューや初見で、最初に全部の章を読む必要はない。

1. 入口: [`docs/START_HERE.md`](docs/START_HERE.md)
2. 目的の正本: [`content/blocks/001-purpose.md`](content/blocks/001-purpose.md)
3. 思想: [`content/blocks/002-thesis-frictionless.md`](content/blocks/002-thesis-frictionless.md)
4. 検証結果: [`release/VALIDATION_REPORT.md`](release/VALIDATION_REPORT.md)
5. 説明資料（HTML スライド + 台本）: [`slides/`](slides/)
   - 詳しくない人向け: [`slides/for-beginners.html`](slides/for-beginners.html)
   - 詳しい人向け: [`slides/for-engineers.html`](slides/for-engineers.html)
   - 説明台本: [`slides/script.md`](slides/script.md)

ローカル確認は次の3コマンドで足りる。

```bash
export PYTHONPATH=src
python -m meaning_first_readme doctor
python -m meaning_first_readme validate
```

`README.md` は生成物なので直接編集しない。変更は `content/blocks/` に入れる。
