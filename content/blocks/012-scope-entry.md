+++
id = "scope.entry"
kind = "scope"
title = "最初の30秒でやること"
summary = "全体を読む前に、ひとこと説明と最短コマンドだけ通す。"
order = 15
priority = 97
audience = ["both"]
tags = ["入口", "最短", "オンボーディング", "レビュー", "コマンド"]
status = "active"
trust = "reviewed"
depends_on = ["purpose.meaning", "scope.readers"]
claims = ["初見は入口ドキュメントと最短コマンドから入る"]
owner = "project"
updated = "2026-07-26"
+++
ひとことで言うと: 長いREADMEを書く道具ではない。読んだ人とAIが、目的・禁止事項・次の一手を取り違えないためのREADME生成器。

レビューや初見で、最初に全部の章を読む必要はない。

1. 入口: [`docs/START_HERE.md`](docs/START_HERE.md)
2. 目的の正本: [`content/blocks/001-purpose.md`](content/blocks/001-purpose.md)
3. 検証結果: [`release/VALIDATION_REPORT.md`](release/VALIDATION_REPORT.md)

ローカル確認は次の3コマンドで足りる。

```bash
export PYTHONPATH=src
python -m meaning_first_readme doctor
python -m meaning_first_readme validate
```

`README.md` は生成物なので直接編集しない。変更は `content/blocks/` に入れる。
