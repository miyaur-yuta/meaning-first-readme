# 30秒で分かる入口

このリポジトリは **READMEを「長く書く」ためではなく、意味を壊さず伝えるため** のツールです。

## 何をするものか

1. `content/blocks/*.md` に型付きの意味ブロックを書く
2. `mfr build` で `README.md` を生成する
3. `mfr context --task '...'` で AI 向けに必要な文脈だけ取り出す

成功条件は文字数ではなく、読んだ人が **目的・境界・根拠・次の行動** を再現できることです。

## 最短コマンド

```bash
export PYTHONPATH=src   # Windows PowerShell: $env:PYTHONPATH='src'
python -m meaning_first_readme doctor
python -m meaning_first_readme validate
python -m meaning_first_readme build
python -m unittest discover -s tests -v
```

Windows で `make` が無い場合も、上の Python コマンドで十分です。`mfr` エントリがなくても `python -m meaning_first_readme` が使えます。

## レビューするとき見る順番

1. このファイル（全体像）
2. `content/blocks/001-purpose.md`（目的）
3. `release/VALIDATION_REPORT.md`（検証結果）
4. 必要なら生成物 `README.md` と差分対象 `build/`

詳細設計は `docs/architecture.md`、執筆ルールは `docs/authoring-guide.md` を見てください。
