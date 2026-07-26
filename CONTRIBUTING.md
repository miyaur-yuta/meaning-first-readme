# Contributing

このリポジトリでは、文章量ではなく**意味の変化**をレビューします。`README.md`は生成物です。直接編集せず、`content/blocks/*.md`を変更してください。

## 変更の最小単位

意味ブロックはTOML前置きとMarkdown本文で構成します。

```markdown
+++
id = "decision.example"
kind = "decision"
title = "判断のタイトル"
summary = "単独で意味が分かる要約。"
priority = 70
depends_on = ["purpose.meaning"]
rationale = "この選択を採用した理由。"
updated = "2026-07-26"
+++
本文。
```

## 必須ルール

1. IDは概念へ結び付け、表示順やファイル番号を意味に含めない。
2. `fact`には`evidence`または`source`を付ける。
3. `decision`には`rationale`を付ける。
4. `procedure`には検証可能な`acceptance`を付ける。
5. 新しいブロックを目的または既存ブロックへ接続する。
6. 外部文章を取り込む場合は信頼区分を宣言する。
7. 揮発情報には`volatile = true`と`expires`を付ける。

## 品質ゲート

```bash
make quality
```

このコマンドは検証、README生成、監査、検索ベンチマーク、テスト、生成物差分確認を実行します。

## レビューで説明すること

- 何の目的または失敗モードに対応する変更か。
- 追加、削除、変更された主張は何か。
- 根拠と依存関係はどう変わるか。
- 人間向け表示とAI向け文脈の両方にどの影響があるか。
- 破壊的変更または既知の限界があるか。
