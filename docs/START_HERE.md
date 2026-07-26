# 30秒で分かる入口

**ひとことで言うと:** 長いREADMEを書く道具ではない。読んだ人とAIが、目的・禁止事項・次の一手を取り違えないためのREADME生成器。

## 何をするものか

1. `content/blocks/*.md` に「意味の部品」を書く
2. `python -m meaning_first_readme build` で `README.md` を作る
3. 必要なら `context` で、AI向けに今の作業に要る部分だけ取り出す

成功の見分け方は「長いこと」ではなく、「読んだ人が判断を間違えないこと」。

## 最短コマンド

```bash
export PYTHONPATH=src   # Windows PowerShell: $env:PYTHONPATH='src'
python -m meaning_first_readme doctor
python -m meaning_first_readme validate
python -m meaning_first_readme build
python -m unittest discover -s tests -v
```

Windows で `make` が無い場合も、上で十分です。

## レビューするとき見る順番

1. このファイル
2. `content/blocks/001-purpose.md`
3. `release/VALIDATION_REPORT.md`
4. 必要なら生成物 `README.md` と `build/`

詳細は `docs/architecture.md` と `docs/authoring-guide.md`。
