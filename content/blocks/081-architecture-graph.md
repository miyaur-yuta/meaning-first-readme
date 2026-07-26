+++
id = "architecture.semantic-graph"
kind = "architecture"
title = "意味グラフ"
summary = "ブロックIDをノード、依存・根拠・支持を辺として扱い、文書の関係を本文の並び順から独立させる。"
order = 91
priority = 90
audience = ["both"]
tags = ["構造", "グラフ", "依存", "根拠", "ID", "差分", "レビュー", "主張"]
status = "active"
trust = "reviewed"
depends_on = ["principle.typed-claims", "architecture.pipeline"]
owner = "project"
updated = "2026-07-26"
+++
Markdownの見出し順だけでは、どの判断がどの前提に依存するか表現できない。意味グラフでは、各ブロックを安定したIDで参照する。

- `depends_on`: 理解または成立に必要なブロック。
- `evidence`: 主張を支える根拠ブロック。
- `supports`: 根拠側から対象への逆参照。

グラフは参照切れと循環を検出し、タスク文脈を作る際には選択ブロックの依存閉包を含める。これにより、結論だけが選ばれて前提が欠落する問題を減らす。
