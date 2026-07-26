「まず要件定義しない？Spec Kit 入れて？」へ回答しました。

## Spec Kit（GitHub 製 SDD フレームワーク）を採用決定

[`content/blocks/081-decision-spec-kit.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/081-decision-spec-kit.md)

Spec Kit（v0.12.5, 2026-07）は自然言語の仕様書を一次産物とする **Spec-Driven Development** を Claude Code/Copilot/Cursor 等で実施するフレームワーク。9フェーズ（constitution → specify → clarify → plan → checklist → tasks → analyze → implement → converge）。

## 意味ブロックとの関係

**意味ブロックは正本、Spec Kit は工程。** 競合しません。

| Spec Kit 入力 | 意味ブロック層 |
|---|---|
| `constitution.md` | `principle` / `constraint` |
| `spec.md` | `purpose` / `scope` / `non_goal` / `definition` |
| `plan.md` | `architecture` / `procedure` |
| `tasks.md` | `procedure`（具体化） |

## 認知負荷の低いヒアリング後に走るフロー

[`guide.spec-kit`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/091-guide-spec-kit.md) に記載：

1. **人間が要点を伝える（認知負荷低）**
2. AI が意味ブロックに構造化
3. Spec Kit の Markdown（constitution/spec/plan/tasks）を生成
4. Spec Kit のフェーズを AI が自動進行
5. 人間は要所で承認のみ

## ヒアリング、いつでも始められます

ユーザーが「認知負荷の低いヒアリングを一度やって」と指示すれば、Spec Kit の clarify フェーズを模して要点だけ伺い、意味ブロック化 → SDD フェーズ自動進行、の順で走ります。

ベンチマーク PASS、CI は次 tick で確認します。
