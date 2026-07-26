# Meaning First README v1

## 思想（ここが一番大事）

**Claude Code ハーネス（CLAUDE.md, Skills, Hooks, Subagents, MCP）への引き渡し摩擦を、限界まで減らす。**

README を「正しく書く」ための道具ではない。README を含む **Claude Code ハーネス設定全体** を、意味ブロックから一貫して生成・検証する体制を目指す。

### Claude Code は README を超える

Claude Code は README を含む包括ハーネスです（2026-07 時点で7つの拡張プリミティブ）。

| プリミティブ | 役割 |
|---|---|
| CLAUDE.md / Rules | 常に効く文脈・指示 |
| Skills | オンデマンドの知識・ワークフロー |
| Hooks | 必ず発火する強制ルール |
| Subagents | 独立コンテキストで専門作業 |
| MCP | 外部システム接続 |
| Plugins | 上記を束ねて配布 |

README は CLAUDE.md の一部にすぎません。「README 整備道具」という位置付けでは Claude Code 本体の機能のほんの一部しか支えません。

### 誰の、どんな苦痛を消すか

| ペルソナ | 苦痛 | これが解くこと |
|---|---|---|
| Claude Code 利用者 | 設定がバラバラで AI が方針を取り違える | 意味ブロックから一貫生成 |
| 設定保守者 | 「消していい？根拠どこ？」が分からない | 根拠・依存・来歴を強制 |
| 初見読者 | 何を AI に渡しているか分からない | 人間向けビューで俯瞰 |

---

## v1 の範囲（正直に）

**v1 は README ビューのみ** です。CLAUDE.md, Skills, Hooks, Subagents の生成は次段階（ロードマップ参照）。

それでも v1 には意味があります：
- 意味ブロック管理の基盤ができている
- 検証・監査・差分の仕組みが動いている
- 次段階は同じ基盤から各種ハーネス設定を生やすだけ

---

## ここだけ見ればOK（所要30秒）

1. ⭐ [`docs/START_HERE.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/docs/START_HERE.md)
2. 🎯 [`content/blocks/002-thesis-frictionless.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/002-thesis-frictionless.md) — 思想
3. 🗺️ [`content/blocks/140-roadmap.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/content/blocks/140-roadmap.md) — 次段階
4. ✅ [`release/VALIDATION_REPORT.md`](https://github.com/miyaur-yuta/meaning-first-readme/blob/release/v1.0.0/release/VALIDATION_REPORT.md)

CI: 🟢 3.11 / 3.12 / 3.13 通過済み

---

## スマホから見る時のヒント

- 上のリンクだけ開けば理解できる
- 細かい差分は見なくてよい（生成物は自動）
- コメントあれば順次対応します

## 既知の限界

- 日本語検索は簡易（同義語に弱い）
- 注入検査は補助（信頼境界の代替ではない）
- 外部 URL の到達性は未検証
- v1 は README ビューのみ（ハーネス設定生成は次段階）

## 公開境界

Draft のまま整備中。Ready / merge は人間の明示承認後。
