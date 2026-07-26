# PR: Meaning First README v1

## ひとことで言うと

長いREADMEを書く道具ではない。読んだ人とAIが、目的・禁止事項・次の一手を取り違えないためのREADME生成器。

## レビュー経路（この順だけ）

1. `docs/START_HERE.md`
2. `content/blocks/001-purpose.md`
3. `release/VALIDATION_REPORT.md`
4. CI の `meaning-quality` が green か

全部を最初から読む必要はない。

## 何が入っているか

- 意味の部品（ブロック）から README を自動生成
- 検証・監査・タスク別文脈・ベンチマーク・差分
- 追加ライブラリなしの CLI（`python -m meaning_first_readme`）

## 検証の見方

| 見たいこと | 場所 |
|---|---|
| 合否 | `release/VALIDATION_REPORT.md` |
| 生成物 | `README.md`, `build/` |

## 既知の限界

- 日本語検索は簡易（同義語に弱い）
- 注入検査は補助
- 外部 URL は未検証

## 公開境界

Draft のまま整備してよい。Ready / merge は人間の明示承認後。
