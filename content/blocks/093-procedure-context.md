+++
id = "procedure.context"
kind = "procedure"
title = "タスク専用AI文脈を生成する"
summary = "AIへ全文を渡す代わりに、実行するタスク、対象、トークン予算を指定して必要な意味を選択する。"
order = 103
priority = 89
audience = ["both"]
tags = ["手順", "AI", "コンテキスト", "タスク", "トークン"]
status = "active"
trust = "reviewed"
depends_on = ["architecture.context-packer", "constraint.boundary"]
acceptance = ["目的と重要制約が出力に含まれる", "タスク固有の期待ブロックが含まれる", "選択ブロックの依存が含まれる", "推定トークンが記録される", "未信頼データが引用として隔離される"]
owner = "project"
updated = "2026-07-26"
+++
例として、公開前レビュー用の文脈は次のように生成する。

```bash
python -m meaning_first_readme context   --task "公開前に事実、根拠、秘密情報、リリース条件を確認する"   --tokens 6000   --audience ai   --output build/release-context.md
```

出力は会話の絶対的な指示ではなく、プロジェクト側の文脈資料である。ユーザーの現在の明示指示、実行環境の権限、安全規則と合わせて使用する。

予算が小さすぎて必須アンカーだけで超過する場合、必須情報を削らず超過を明示する。
