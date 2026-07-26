+++
id = "architecture.pipeline"
kind = "architecture"
title = "意味を壊さないビルドパイプライン"
summary = "解析、検証、グラフ構築、生成、監査、検索ベンチマークを決定論的な順序で実行する。"
order = 90
priority = 96
audience = ["both"]
tags = ["構造", "パイプライン", "ビルド", "検証", "CI"]
status = "active"
trust = "reviewed"
depends_on = ["scope.artifact", "constraint.update-safety", "decision.markdown-toml"]
owner = "project"
updated = "2026-07-26"
+++
標準パイプラインは次の順序を持つ。

```text
意味ブロックの探索
  -> TOML前置きとMarkdown本文の解析
  -> ID・型・参照・期限・根拠・矛盾の検証
  -> 依存グラフと内容指紋の構築
  -> READMEと機械可読マニフェストの生成
  -> 品質次元の監査
  -> タスク別文脈検索ベンチマーク
  -> テストと再生成差分の確認
  -> リリース判断
```

前段が失敗した場合、後段で見栄えの良い成果物を作って成功扱いにしない。CLIは失敗を終了コードで返し、CIが公開を止められるようにする。
