# PR: Meaning First README v1

## 1行で言うと

READMEの成功条件を「長さ」から「意味の再現」へ移す、依存ゼロの意味ブロック・コンパイラ基盤。

## レビュー経路（この順だけ見れば足りる）

1. `docs/START_HERE.md`
2. `content/blocks/001-purpose.md`
3. `release/VALIDATION_REPORT.md`
4. CI の `meaning-quality` が green か

詳細ファイル全部を最初から読む必要はない。

## 何が入っているか

- 型付き意味ブロック → 決定論的 README 生成
- 検証 / 監査 / タスク文脈 / ベンチマーク / 意味差分
- 標準ライブラリのみの CLI（`python -m meaning_first_readme`）

## 検証の見方

| 見たいこと | 場所 |
|---|---|
| ゲート合否 | `release/VALIDATION_REPORT.md` |
| 生成物 | `README.md`, `build/` |
| 変更意図 | この PR 本文の Summary |

## 既知の限界

- 日本語検索は N-gram（同義語に弱い）
- 注入検査は補助（信頼境界の代替ではない）
- 外部 URL 到達性は未検証

## 公開境界

Draft のまま整備・検証してよい。Ready / merge は人間の明示承認後。
