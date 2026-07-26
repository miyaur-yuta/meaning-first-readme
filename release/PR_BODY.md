# Meaning First README v1

## 思想（ここが一番大事）

**AIコーディング環境（ClaudeCode, Cursor 等）にリポジトリを渡す摩擦を、限界まで減らす。**

README を「正しく書く」ための道具ではない。README を **AI に渡しやすい構造** に再編成し、人間にも AI にも取り違えが起きないようにする。

### 誰の、どんな苦痛を消すか

| ペルソナ | 苦痛 | これが解くこと |
|---|---|---|
| ClaudeCode/Cursor 利用者 | README が古い/長い/矛盾で AI が迷子 | タスク別に必要文脈だけ渡す |
| README 保守者 | 「消していい？根拠どこ？」が分からない | 根拠・依存・来歴を強制 |
| 初見読者 | 長い README から目的を探すのがつらい | 短縮版を機械生成 |

---

## ここだけ見ればOK（所要30秒）

1. ⭐ [`docs/START_HERE.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/docs/START_HERE.md)
2. 🎯 [`content/blocks/002-thesis-frictionless.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/002-thesis-frictionless.md) — 思想
3. ✅ [`release/VALIDATION_REPORT.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/release/VALIDATION_REPORT.md)

CI: 🟢 3.11 / 3.12 / 3.13 通過済み

---

## 何ができる？

- 意味の部品（型付きブロック）から README を自動生成
- 参照・根拠・未確認情報・重複・期限を **自動検証**
- AI に渡すときは **タスク別に必要な文脈だけ** 取り出す（トークン節約）
- 追加ライブラリなし（Python 標準ライブラリのみ）

### 具体例：リリース前の AI 最終確認

```bash
python -m meaning_first_readme context \
  --task '公開前に事実、根拠、秘密情報、リリース条件を確認する' \
  --tokens 6500 --audience ai
```

全文を AI に食わせず、必要ブロックだけ渡す。

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
