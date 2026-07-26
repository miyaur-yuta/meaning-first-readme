+++
id = "constraint.permission-scope"
kind = "constraint"
title = "Claude Code の権限スコープと権限モードを正しく扱う"
summary = "個人・プロジェクト・管理の各スコープと、default/acceptEdits/plan/auto/dontAsk/bypassPermissions の各モードの違いを、生成するハーネス設定に反映する。"
order = 76
priority = 55
audience = ["human"]
tags = ["権限", "スコープ", "ClaudeCode", "安全"]
status = "active"
trust = "reviewed"
depends_on = ["constraint.boundary", "thesis.frictionless-ai-handoff"]
claims = ["権限スコープと権限モードの違いを正しく反映しなければならない"]
owner = "project"
updated = "2026-07-26"
+++
Claude Code の権限体系は、単一の設定ファイルでは表現できない。生成するハーネス設定は、次の区別を正しく扱う必要がある。

## 権限スコープ（誰の設定か）

| スコープ | 場所 | 性質 |
|---|---|---|
| ユーザー | `~/.claude/settings.json` | 全プロジェクトで共通 |
| プロジェクト（共有） | `.claude/settings.json` | チーム共有、Git 管理対象 |
| プロジェクト（個人） | `.claude/settings.local.json` | 個人 override、Git 除外 |
| 管理者（エンタープライズ） | OS 固定パス | 上書き不可 |

`allow` / `deny` / `ask` リストはスコープ間で **マージ** される。`deny` は常に優先する（ユーザー deny がプロジェクト allow に勝つ）。

## 権限モード（どの程度自動か）

| モード | 挙動 | 想定用途 |
|---|---|---|
| `default`（Manual） | 初回は毎回確認 | 通常開発 |
| `acceptEdits` | 編集を自動許可 | 作業中 |
| `plan` | 読み取りのみ、編集不可 | 探索・計画 |
| `auto` | 分類器で自動承認 | 高頻度作業 |
| `dontAsk` | 未承認は自動拒否 | CI |
| `bypassPermissions` | 全スキップ | 隔離コンテナ・VM のみ |

`bypassPermissions` は `rm -rf /` 等のサーキットブレーカを除き、`.git` や `.claude` 等への書き込みも含めほぼ全てをスキップする。隔離環境以外で使ってはならない。

## このプロジェクトが守ること

1. 生成するハーネス設定は、スコープ（共有か個人か）を明示する
2. 強制ルール（Hooks）は `deny` 相当、推奨は `ask` 相当と区別する
3. `bypassPermissions` 向けの設定は生成しない（隔離環境専用のため）
4. 個人設定（`settings.local.json`）は Git に含めない

これらを満たさない生成物は検証段階で不合格とする。
