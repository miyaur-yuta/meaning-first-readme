+++
id = "deliverable.explanation-slides"
kind = "scope"
title = "説明資料：HTML スライドと台本"
summary = "Spec Kit と Claude Code ハーネスの仕組みを、詳しい人向け・詳しくない人向けの2種類のHTMLスライドと、説明時のスクリプト（台本）として提供する。"
order = 19
priority = 30
audience = ["human"]
tags = ["説明資料", "スライド", "HTML", "台本", "引き継ぎ"]
status = "active"
trust = "authoritative"
depends_on = ["decision.claude-code-only", "decision.spec-kit-integration", "guide.claude-code-primitives"]
claims = [
  "Spec Kit / Claude Code ハーネスの説明資料をHTMLスライドで提供する",
  "詳しい人向けと詳しくない人向けの2種類を用意する",
  "説明時のスクリプト（台本）を併存させる",
]
owner = "project"
updated = "2026-07-26"
+++
ユーザーの要望に基づき、Spec Kit と Claude Code ハーネスの仕組みを **HTML スライド** で提供する。

## 提供物

| 対象 | 形式 | ファイル |
|---|---|---|
| 詳しい人（エンジニア・Claude Code 利用経験者） | HTML スライド | `slides/for-engineers.html` |
| 詳しくない人（非エンジニア・初学者） | HTML スライド | `slides/for-beginners.html` |
| 台本（説明時のスクリプト） | Markdown | `slides/script.md` |

## 2種類の違い

### 詳しい人向け
- Claude Code / Spec Kit の前提知識を仮定
- アーキテクチャ・ライフサイクル・権限体系を深く
- コード例・ファイル配置・移行手順を含む

### 詳しくない人向け
- AI エージェント・ハーネスの前提から解説
- 専門用語は避け、比喩と図解を多用
- 「何が嬉しいか」「何が変わるか」に集中

## HTML スライドの要件

- 単一の自己完結型 HTML ファイル
- 図解・構造・視覚表現を限界まで活用
- `context-to-html` スキルの基準に準拠
- レスポンシブ対応（スマホ・PC 両方で見える）

## 台本の要件

- 各スライドに対応する話す内容
- 想定質問と回答例
- 所要時間の目安
