+++
id = "procedure.build"
kind = "procedure"
title = "ローカルでビルドと検証を実行する"
summary = "標準ライブラリだけで正本を読み、README、監査報告、文脈例、ベンチマーク結果を再生成する。"
order = 102
priority = 90
audience = ["both"]
tags = ["手順", "ビルド", "CLI", "テスト"]
status = "active"
trust = "reviewed"
depends_on = ["architecture.pipeline", "decision.self-hosting"]
acceptance = ["validateが成功する", "READMEを再生成して意図しない差分がない", "auditの全ゲートが成功する", "benchmarkが設定閾値を満たす", "unittestが全件成功する"]
owner = "project"
updated = "2026-07-26"
+++
リポジトリ直下で以下を実行する。

```bash
python -m meaning_first_readme validate
python -m meaning_first_readme build
python -m meaning_first_readme audit --output build/audit.md
python -m meaning_first_readme benchmark --output build/benchmark.md
python -m unittest discover -s tests -v
```

パッケージをインストールせず実行する場合は、`PYTHONPATH=src`を設定する。`Makefile`の`make quality`は同じ品質ゲートをまとめて実行する。

生成後に`git diff --exit-code`を実行し、正本ブロックとREADMEが同期していることを確認する。
