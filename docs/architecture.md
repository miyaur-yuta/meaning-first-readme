# Architecture

## Components

```text
content/blocks/*.md
        |
        v
     parser.py  ----> SemanticBlock
        |                 |
        v                 v
    validate.py       graph.py
        |                 |
        +--------+--------+
                 v
          compiler.py --------> README.md + build/manifest.json
                 |
                 +--------> context.py + rank.py ----> task context
                 |
                 +--------> audit.py ----------------> quality dimensions
                 |
                 +--------> benchmark.py ------------> retrieval report
                 |
                 +--------> snapshot.py + diff.py ---> semantic diff
```

## Dependency policy

実行時依存はありません。Python 3.11以上の標準ライブラリだけで、TOML解析、Markdown生成、グラフ検査、検索、JSON出力を行います。高度な形態素解析や埋め込み検索は、基準実装の再現性を壊さない任意拡張として扱います。

## Determinism

- ブロックは`order`、次にIDで安定ソートします。
- 指紋は正規化したJSONとSHA-256から生成します。
- 現在時刻をREADMEへ埋め込まず、ソースの更新日を使います。
- 同じ入力集合から同じREADMEとマニフェストを生成します。

## Retrieval

日本語の連続文字列から2文字・3文字特徴を、英数字から語特徴を作ります。小規模コーパス向けIDF、タイトル・タグの完全包含、優先度、信頼区分を組み合わせます。固定アンカーと依存閉包を先に確保し、残り予算へ関連ブロックを追加します。

この方式は埋め込みモデルより単純ですが、ネットワーク、外部モデル、秘密鍵なしで再現でき、ベンチマークによる回帰検出が可能です。
