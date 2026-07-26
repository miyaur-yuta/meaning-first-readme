# Validation Report — Meaning First README 1.0.0

## Result

**PASS** — この報告に記載した全ゲートは、2026-07-26のローカル実行で成功した。

この結果は「理論上の完成」や「すべての環境で無欠陥」を意味しない。現在の実装、コーパス、テスト、代表タスクに対する再現可能な観測結果である。

## Artifact summary

| Item | Measured value |
|---|---:|
| Active semantic blocks | 36 |
| Semantic kinds | 17 |
| Generated README | 90,120 bytes / 2,235 lines |
| Estimated source tokens | 9,781 |
| Runtime dependencies | 0 |
| Python source | 1,899 lines |
| Test source | 703 lines |
| Automated tests | 81 |
| Benchmark cases | 12 |
| Repository semantic digest | `3e7d56c34a4957b414211bffef9610005e87152aa2a77549b21ff1b098b0c894` |

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
| Validation | 2.466404 s |
| Context selection | 0.373166 s |
| README rendering | 0.147123 s |
| Snapshot | 0.029351 s |
| Total | 3.023834 s |
| Generated README | 3,317,631 bytes |
| Max RSS | 182,192 KiB |

計測値はこの実行環境固有であり、他環境への性能保証ではない。重複候補生成は64-bit SimHashの8バンドLSHを使い、全組み合わせ比較を避けている。

## Package verification

- Wheel: `meaning_first_readme-1.0.0-py3-none-any.whl`
- Wheel SHA-256: `bbd1aedef0ad757573a7c995970ab3f04b568df67ebcf22a5a7bf57f21d5ebda`
- 新規仮想環境へ依存なしでインストールした。
- インストールされた`mfr`コマンドから、実リポジトリの`validate`が成功した。

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
| `README.md` | `0e9ff0ef95a83c80adb2042bba123c6448e980b951393b1c7934042bc1436c2e` |
| `build/manifest.json` | `fb639e4c9b46b0559d7c9040b5cbffd9aca23c52b49d8fe283ab04287533eebd` |
| `build/audit.json` | `ca7551df492a7b6afa60ffeba83782d19152b905c69f4b6c345b947dbad40666` |
| `build/benchmark.json` | `eca45ef09d3bd245bd0e2e6fe58276ca6bdee6b0bfe5f60cdff8c3b6a9b3a345` |
| `build/performance.json` | `1c1593cba1df02dd6d49541771bd12c60035cbf840dcd676a7e5ee6ddd208052` |
| `meaning_first_readme-1.0.0-py3-none-any.whl` | `bbd1aedef0ad757573a7c995970ab3f04b568df67ebcf22a5a7bf57f21d5ebda` |
