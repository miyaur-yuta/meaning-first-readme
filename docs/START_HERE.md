# 30秒で分かる入口

**ひとことで言うと:** Claude Code ハーネス（CLAUDE.md / Skills / Hooks / Subagents / MCP / Plugins）への引き渡し摩擦を、意味ブロックから限界まで減らすツール。**v1 は README ビューのみ**。

## Claude Code との関係（ここ大事）

README は Claude Code のハーネスのほんの一部。このプロジェクトは最終的に **全部のハーネス設定** を同じ意味ブロックから生成する体制を目指す。

| ハーネス要素 | 現状 | このプロジェクトの役割 |
|---|---|---|
| README / CLAUDE.md | v1 で生成 | 意味ブロック → README ビュー |
| Skills | 次段階 | 意味ブロックから知識を生成 |
| Hooks | 次段階 | 強制ルール（`deny` 相当）を生成 |
| Subagents | 次段階 | 独立コンテキスト用にブロックを分包 |
| MCP | 次段階 | 外部接続設定の記述 |
| 権限設定 | 次段階 | スコープ別に生成・検証 |

v1 の範囲と次段階は [`content/blocks/140-roadmap.md`](../content/blocks/140-roadmap.md) を参照。

## 「README生成器」って何が嬉しいの？

README は書きっぱなしにすると、こういう問題が起きます。

- 「手順」と「理由」が離れていて、手順だけ見て間違える
- 「禁止事項」が奥に埋もれて AI が無視する
- 更新するときに根拠が分からず、消していいか迷う
- 長くなりすぎて、読む人も AI も迷子になる

このツールは README を **「意味の部品（型付きブロック）」** として管理し、検証して、必要な分だけ取り出せるようにします。

### 具体例

```
リリース直前に AI で最終確認したい
→ 全文ではなく「事実・根拠・秘密情報・リリース条件」のブロックだけ渡す
→ トークンを節約しつつ、見落としを防ぐ
```

```
新しいメンバーが来た
→ 「目的・禁止事項・次の一手」だけ取り出した短縮版を見せる
→ 全部読ませない
```

```
README を書き換えた
→ 自動で「参照先が消えてないか」「未確認情報が事実として混ざってないか」検証
→ 見落としを機械が拾う
```

## 最短コマンド

```bash
export PYTHONPATH=src   # Windows PowerShell: $env:PYTHONPATH='src'
python -m meaning_first_readme doctor
python -m meaning_first_readme validate
python -m meaning_first_readme build
python -m unittest discover -s tests -v
```

Windows で `make` が無い場合も、上で十分です。

## レビューするとき見る順番

1. このファイル
2. `content/blocks/001-purpose.md`
3. `release/VALIDATION_REPORT.md`
4. 必要なら生成物 `README.md` と `build/`

詳細は `docs/architecture.md` と `docs/authoring-guide.md`。

## 説明会用スライド

| 対象 | ファイル | 所要 |
|---|---|---|
| 初学者（非エンジニア） | [`slides/for-beginners.html`](../slides/for-beginners.html) | 10分 |
| エンジニア | [`slides/for-engineers.html`](../slides/for-engineers.html) | 15分 |
| 台本（説明時のスクリプト） | [`slides/script.md`](../slides/script.md) | — |

初学者向けは比喩多用、エンジニア向けは7プリミティブ・権限モデル・SDD ライフサイクルを深く扱います。

## Spec Kit との関係（要件定義ファースト）

[GitHub Spec Kit](https://github.com/github/spec-kit) の SDD を採用。意味ブロックは**正本**、Spec Kit は**工程**。詳細は [`content/blocks/081-decision-spec-kit.md`](../content/blocks/081-decision-spec-kit.md)。
