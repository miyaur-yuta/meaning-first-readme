権限スコープとリアルな対話品質を制約ブロックとして追加しました。

## 追加した制約

**1. 権限スコープ（`constraint.permission-scope`）**
- ユーザー / プロジェクト共有 / プロジェクト個人 / 管理者の4スコープを明示
- 権限モード（default/acceptEdits/plan/auto/dontAsk/bypassPermissions）の違い
- `deny` はスコープ間で常に優先する仕様
- `bypassPermissions` 向け設定は生成しない（隔離環境専用）

**2. リアルな対話品質（`constraint.real-conversation-quality`）**
- 取り違え・迷子・停滞・権限誤認・文脈欠落の5つの失敗モードを定義
- 自動生成物が満たすべき受け入れ条件
- 代表ペルソナでの対話観察を evidence として残す方針

どちらも現状は `audience=human` で運用し、AI 文脈の予算を圧迫しないよう調整済み。ベンチマーク全ケース PASS。
