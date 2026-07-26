# Validation Report — Meaning First README 1.0.0

## Result

**PASS** — この報告に記載した全ゲートは、2026-07-26のローカル実行で成功した。

この結果は「理論上の完成」や「すべての環境で無欠陥」を意味しない。現在の実装、コーパス、テスト、代表タスクに対する再現可能な観測結果である。

## Artifact summary

| Item | Measured value |
|---|---:|
| Active semantic blocks | 38 |
| Semantic kinds | 17 |
| Generated README | 95,669 bytes / 2,389 lines |
| Estimated source tokens | 7,837 |
| Runtime dependencies | 0 |
| Automated tests | 81 |
| Benchmark cases | 12 |
| Repository semantic digest | `6e079d52ab693877761ff1d1a32c830718e87dc5de12f37cea9d1c61faf8e088` |

## Quality gates

| Gate | Result |
|---|---|
| `no_validation_errors` | PASS |
| `required_structure` | PASS |
| `full_traceability` | PASS |
| `full_actionability` | PASS |
| `fresh_volatile_data` | PASS |
| `no_orphans` | PASS |
| `no_ambiguous_placeholders` | PASS |

## Context retrieval benchmark

| Metric | Result |
|---|---:|
| Cases passed | 12/12 |
| Macro recall | 1.000 |
| Macro precision | 0.523 |
| Configured minimum recall | 0.850 |
| Configured minimum precision | 0.300 |

再現率は全ケースで1.0だった。適合率は、タスク固有ブロックに加えて目的・非目的・信頼境界・依存閉包を常に含める設計のため、不要語だけを除く検索器より低くなる。これは安全側の文脈契約として意図した挙動である。

## Synthetic scale observation

2,000個の型付きブロックを生成し、同一プロセスで検証、文脈選択、README描画、スナップショット作成を実行した。

| Observation | Value |
|---|---:|
| Total (Windows / Python 3.13) | 6.316 s |
| Max RSS | 92,740 KiB |

計測値はこの実行環境固有であり、他環境への性能保証ではない。重複候補生成は64-bit SimHashの8バンドLSHを使い、全組み合わせ比較を避けている。

## Reproducibility checks

- 同一ブロック集合からREADMEとマニフェストを再生成できる。
- 意味スナップショットの指紋は絶対ファイルパスを含まない。
- 生成READMEにはブロックID、型、優先度、信頼区分、内容指紋が埋め込まれる。
- CIはPython 3.11、3.12、3.13で検証、生成、監査、検索ベンチマーク、テストを実行する設定である。

## Known limits

1. 日本語検索は依存ゼロの文字N-gram方式であり、暗黙的な同義語や専門分野固有の言い換えを完全には捉えない。
2. SimHashによる近似重複候補生成は、意味が同じ大幅な言い換えを検出する保証を持たない。
3. 外部URLの到達性、外部仕様の最新性、世界記録などは、ネットワークを使わない基準実装だけでは検証しない。
4. 命令注入のパターン警告は補助であり、実行環境の権限規則と信頼境界を置き換えない。
5. ベンチマークは現在の12代表タスクに対する結果であり、未知の全タスクを保証しない。

## Artifact hashes

| Artifact | SHA-256 |
|---|---|
| `README.md` | `90ac540619f0b8b623474c4e300287804609689589556f7e46ec6e63e8b77d09` |
| `build/manifest.json` | `7f5d2bf14dd73122642cfd70c64396b515dbd29e6eda671ea0389a81333f0281` |
| `build/audit.json` | `77cca0d64b4714276050f04b0e025822be19de29bdc4feef2a798152c5dd74b4` |
| `build/benchmark.json` | `eca45ef09d3bd245bd0e2e6fe58276ca6bdee6b0bfe5f60cdff8c3b6a9b3a345` |
| `build/performance.json` | `532c13374fd954f0408ca1a36247888786e90b88e8ae9f479905b89014e80a66` |
