+++
id = "decision.observation-format"
kind = "decision"
title = "対話観察の記録フォーマット"
summary = "ペルソナ別典型タスクの対話観察を evidence ブロックとして残すための標準フォーマットを定める。"
order = 80
priority = 58
audience = ["human"]
tags = ["観察", "evidence", "フォーマット", "決定"]
status = "active"
trust = "reviewed"
depends_on = ["scope.personas", "definition.real-conversation", "constraint.real-conversation-quality"]
claims = ["対話観察は標準フォーマットで evidence ブロックに記録する"]
rationale = "フォーマットが固定されていないと観察の蓄積と比較ができず、回帰検出が主観にすり替わる。"
owner = "project"
updated = "2026-07-26"
+++
「リアルな対話品質」を回帰検出可能にするため、対話観察は `evidence` 種別の意味ブロックとして記録する。フォーマットを固定することで、蓄積と比較を可能にする。

## フロントマター

```toml
+++
id = "evidence.observation.<連番>-<persona>"
kind = "evidence"
title = "対話観察：<ペルソナ> / <タスク>"
summary = "1行で結果。成功か失敗かを含む。"
order = <連番>
priority = 40
audience = ["human"]
tags = ["観察", "evidence", "<persona>"]
status = "active"
trust = "observed"
depends_on = ["scope.personas", "<関連ブロック>"]
claims = ["<観察から導かれる主張>"]
owner = "project"
updated = "<YYYY-MM-DD>"
+++
```

## 本文

本文は次の4セクションを含む。

### 条件
- 日時、Claude Code バージョン、モデル、対象コミット

### セッション記録
- プロンプトと応答の要点（全文ではなく要点で良い）
- 目的・禁止事項・次の一手が反映されたか

### 結果
- 成功基準（`scope.personas` で定義）に対する合否
- 失敗時は失敗モード（`constraint.real-conversation-quality` 参照）を明示

### 次の改善
- 失敗した場合、どのブロックを変えれば再発を防げるか
- 成功した場合、再現性を上げるためのメモ

## 運用ルール

- サンプルサイズ1で判定しない（少なくとも2回の観察で傾向を扱う）
- 主観表現（「良かった」「自然だった」）は避け、観察事実を書く
- `trust="observed"` を必ず付ける（事実であることの明示）
- 失敗観察も等しく残す（隠さない）

このフォーマットは v1 の範囲外（観察自動化）に属するが、手動観察から使えるように v1 で導入する。
