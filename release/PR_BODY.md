# Meaning First README v1

## ひとことで言うと

README を「正しく伝わる構造データ」として管理し、人間にも AI にも取り違えが起きないようにするツール。

---

## 「README生成器」って何が嬉しいの？（具体例）

| 状況 | これがないと | これがあると |
|---|---|---|
| リリース前確認 | 全文を AI に食わせて迷子 | 必要ブロックだけ渡して確実 |
| 新メンバー | 長い README を全部読ませる | 目的・禁止・次手だけ取り出す |
| README 更新 | 根拠が分からず怖い | 参照・根拠・未確認情報を自動検証 |

---

## ここだけ見ればOK（所要30秒）

1. ⭐ [`docs/START_HERE.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/docs/START_HERE.md)
2. 🎯 [`content/blocks/001-purpose.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/001-purpose.md)
3. ✅ [`release/VALIDATION_REPORT.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/release/VALIDATION_REPORT.md)

CI: 🟢 3.11 / 3.12 / 3.13 通過済み

---

## 何ができる？

- 意味の部品（型付きブロック）から README を自動生成
- 参照・根拠・未確認情報・重複・期限を **自動検証**
- AI に渡すときは **タスク別に必要な文脈だけ** 取り出す（トークン節約）
- 追加ライブラリなし（Python 標準ライブラリのみ）

---

## スマホから見る時のヒント

- 上の 3 リンクだけ開けば理解できる
- 細かい差分は見なくてよい（生成物は自動）
- コメントあれば順次対応します

## 既知の限界

- 日本語検索は簡易（同義語に弱い）
- 注入検査は補助（信頼境界の代替ではない）
- 外部 URL の到達性は未検証

## 公開境界

Draft のまま整備中。Ready / merge は人間の明示承認後。
