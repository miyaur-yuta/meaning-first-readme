+++
id = "example.quickstart"
kind = "example"
title = "クイックスタート：3つの使い方"
summary = "リリース前確認、新メンバーオンボーディング、README更新検証という3つの典型ユースケースをコマンド付きで示す。"
order = 125
priority = 78
audience = ["both"]
tags = ["例", "クイックスタート", "使い方", "ユースケース", "コマンド"]
status = "active"
trust = "reviewed"
depends_on = ["purpose.meaning", "scope.artifact", "procedure.build", "procedure.context"]
owner = "project"
updated = "2026-07-26"
+++
このツールは「長いREADMEを書く道具」ではなく、README を **意味の部品** として管理し、人間にも AI にも取り違えが起きないようにする。典型ユースケースを3つ示す。

### 1. リリース前の最終確認（AI に渡す文脈を絞る）

```bash
export PYTHONPATH=src
python -m meaning_first_readme context \
  --task '公開前に事実、根拠、秘密情報、リリース条件を確認する' \
  --tokens 6500 \
  --audience ai \
  --output build/release-context.md
```

全文を食わせるのではなく、必要ブロックだけを取り出して AI に渡す。トークンを節約しつつ、見落としを防ぐ。

### 2. 新メンバーのオンボーディング（人間向け短縮版）

```bash
python -m meaning_first_readme context \
  --task '初見の人が目的と禁止事項を把握する' \
  --tokens 3000 \
  --audience human \
  --output build/onboarding.md
```

全部読ませず、目的・禁止事項・次の一手だけを渡す。

### 3. README 更新時の自動検証

```bash
python -m meaning_first_readme validate
python -m meaning_first_readme build
git diff README.md build/
```

参照先が消えていないか、未確認情報が事実として混ざっていないか、期限切れがないかを機械が検証する。

---

いずれも `make` が無い環境では `python -m meaning_first_readme ...` で動く。追加ライブラリは不要。
