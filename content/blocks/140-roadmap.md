+++
id = "roadmap.v1"
kind = "roadmap"
title = "v1 から Claude Code ハーネス基盤へ"
summary = "初号機は README 生成に留まる。次はハーネス設定の生成へ拡張する。"
order = 150
priority = 55
audience = ["both"]
tags = ["ロードマップ", "次の開発"]
status = "active"
trust = "reviewed"
depends_on = ["purpose.meaning", "architecture.pipeline"]
owner = "project"
updated = "2026-07-26"
+++
初号機（v1）で実装する核は、型付きブロック、決定論的 README 生成、構造検証、意味グラフ、タスク文脈、意味差分、複数次元監査、検索ベンチマーク、テスト、CI である。これは README ビューに留まる。

次の段階では、同じ意味ブロックから Claude Code ハーネス設定を生成する。

1. 目的・禁止事項・前提ブロックから CLAUDE.md を生成
2. 手順ブロックから Skills を生成
3. 禁止事項ブロックから Hooks を生成
4. 役割ブロックから Subagents を生成
5. 他エージェント環境への移植ビューを生成

拡張は機能数ではなく、観測された引き渡し摩擦を減らす順に行う。
