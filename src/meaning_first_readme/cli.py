from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .audit import audit_repository, render_audit_markdown
from .benchmark import load_cases, render_benchmark_markdown, run_benchmark
from .compiler import build_readme
from .context import compile_context
from .diff import compare_snapshots, render_diff_markdown
from .errors import MeaningFirstError
from .graph import MeaningGraph
from .parser import load_repository
from .snapshot import load_snapshot, write_snapshot
from .validate import validate_repository


def _project_path(value: str) -> Path:
    return Path(value).resolve()


def _load(args: argparse.Namespace):
    return load_repository(_project_path(args.project))


def command_build(args: argparse.Namespace) -> int:
    config, blocks = _load(args)
    report = validate_repository(config, blocks)
    if not report.passed and not args.allow_invalid:
        print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2), file=sys.stderr)
        return 2
    rendered = build_readme(
        config,
        blocks,
        output=Path(args.output),
        manifest_output=Path(args.manifest) if args.manifest else None,
    )
    print(f"built {args.output}: {len(rendered.encode('utf-8'))} bytes, {len(rendered.splitlines())} lines")
    return 0


def command_validate(args: argparse.Namespace) -> int:
    config, blocks = _load(args)
    report = validate_repository(config, blocks)
    if args.json:
        print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(f"validation: {'PASS' if report.passed else 'FAIL'}")
        print(f"errors={len(report.errors)} warnings={len(report.warnings)}")
        for issue in report.issues:
            location = f" [{issue.block_id}]" if issue.block_id else ""
            print(f"{issue.severity.upper():7} {issue.code}{location}: {issue.message}")
    return 0 if report.passed else 2


def command_context(args: argparse.Namespace) -> int:
    config, blocks = _load(args)
    selection, rendered = compile_context(
        config,
        blocks,
        task=args.task,
        budget=args.tokens,
        audience=args.audience,
        output=Path(args.output) if args.output else None,
    )
    if not args.output:
        print(rendered, end="")
    else:
        print(
            f"context {args.output}: selected={len(selection.selected)} "
            f"estimated_tokens={selection.estimated_tokens}/{selection.budget}"
        )
    return 0


def command_audit(args: argparse.Namespace) -> int:
    config, blocks = _load(args)
    report = audit_repository(config, blocks)
    if args.format == "json":
        rendered = json.dumps(report.to_dict(), ensure_ascii=False, indent=2) + "\n"
    else:
        rendered = render_audit_markdown(report)
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
        print(f"audit written to {args.output}: {'PASS' if report.passed else 'FAIL'}")
    else:
        print(rendered, end="")
    return 0 if report.passed else 2


def command_benchmark(args: argparse.Namespace) -> int:
    config, blocks = _load(args)
    cases = load_cases(Path(args.cases))
    report = run_benchmark(config, blocks, cases)
    if args.format == "json":
        rendered = json.dumps(report.to_dict(), ensure_ascii=False, indent=2) + "\n"
    else:
        rendered = render_benchmark_markdown(report)
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
        print(f"benchmark written to {args.output}: {'PASS' if report.passed else 'FAIL'}")
    else:
        print(rendered, end="")
    return 0 if report.passed else 2


def command_snapshot(args: argparse.Namespace) -> int:
    _, blocks = _load(args)
    data = write_snapshot(Path(args.output), blocks)
    print(f"snapshot {args.output}: {data['repository_digest']}")
    return 0


def command_diff(args: argparse.Namespace) -> int:
    diff = compare_snapshots(load_snapshot(Path(args.left)), load_snapshot(Path(args.right)))
    if args.format == "json":
        rendered = json.dumps(diff.to_dict(), ensure_ascii=False, indent=2) + "\n"
    else:
        rendered = render_diff_markdown(diff)
    print(rendered, end="")
    return 1 if diff.changed and args.fail_on_change else 0


def command_explain(args: argparse.Namespace) -> int:
    _, blocks = _load(args)
    graph = MeaningGraph(blocks)
    try:
        result = graph.explain(args.block_id)
    except KeyError:
        print(f"unknown block: {args.block_id}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def command_query(args: argparse.Namespace) -> int:
    config, blocks = _load(args)
    from .rank import rank_blocks

    ranked = rank_blocks(config, blocks, task=args.text, audience=args.audience)
    for item in ranked[: args.limit]:
        print(f"{item.score:8.3f}  {item.block.id:36}  {item.block.title}")
        if args.verbose:
            print(f"          {'; '.join(item.reasons)}")
    return 0


def command_doctor(args: argparse.Namespace) -> int:
    config, blocks = _load(args)
    report = validate_repository(config, blocks)
    print("Meaning First README doctor")
    print(f"python={sys.version.split()[0]}")
    print(f"project={config.name}")
    print(f"content_dir={config.content_dir}")
    print(f"blocks={len(blocks)}")
    print(f"validation={'PASS' if report.passed else 'FAIL'}")
    return 0 if report.passed else 2


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mfr",
        description="意味を壊さない README を生成・検証する。長いことより、判断を取り違えないことが成功条件。",
    )
    parser.add_argument(
        "--project",
        default="content/project.toml",
        help="project.toml のパス（既定: content/project.toml）",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    build = sub.add_parser("build", help="正本の README を生成する")
    build.add_argument("--output", default="README.md")
    build.add_argument("--manifest", default="build/manifest.json")
    build.add_argument("--allow-invalid", action="store_true", help="検証エラーがあっても生成を続ける")
    build.set_defaults(func=command_build)

    validate = sub.add_parser("validate", help="構造と意味の検証を行う")
    validate.add_argument("--json", action="store_true", help="結果を JSON で出す")
    validate.set_defaults(func=command_validate)

    context = sub.add_parser("context", help="トークン予算内でタスク向け文脈を組み立てる")
    context.add_argument("--task", required=True, help="今やりたいこと（検索クエリ）")
    context.add_argument("--tokens", type=int, default=8000, help="トークン予算")
    context.add_argument("--audience", choices=("human", "ai"), default="ai", help="想定読者")
    context.add_argument("--output", help="出力ファイル（省略時は標準出力）")
    context.set_defaults(func=command_context)

    audit = sub.add_parser("audit", help="単一スコアにしない品質監査を行う")
    audit.add_argument("--format", choices=("json", "markdown"), default="markdown")
    audit.add_argument("--output", help="出力ファイル")
    audit.set_defaults(func=command_audit)

    benchmark = sub.add_parser("benchmark", help="期待ブロックを拾えるか検索ベンチを測る")
    benchmark.add_argument("--cases", default="benchmarks/tasks.json", help="ベンチケース JSON")
    benchmark.add_argument("--format", choices=("json", "markdown"), default="markdown")
    benchmark.add_argument("--output", help="出力ファイル")
    benchmark.set_defaults(func=command_benchmark)

    snapshot = sub.add_parser("snapshot", help="意味スナップショットを書き出す")
    snapshot.add_argument("--output", default="build/snapshot.json")
    snapshot.set_defaults(func=command_snapshot)

    diff = sub.add_parser("diff", help="意味スナップショットを比較する")
    diff.add_argument("left", help="比較元スナップショット")
    diff.add_argument("right", help="比較先スナップショット")
    diff.add_argument("--format", choices=("json", "markdown"), default="markdown")
    diff.add_argument("--fail-on-change", action="store_true", help="差分があれば終了コード 1")
    diff.set_defaults(func=command_diff)

    explain = sub.add_parser("explain", help="ブロックとその依存関係を表示する")
    explain.add_argument("block_id", help="ブロック ID")
    explain.set_defaults(func=command_explain)

    query = sub.add_parser("query", help="文脈生成せずに関連ブロックを順位付けする")
    query.add_argument("text", help="検索テキスト")
    query.add_argument("--audience", choices=("human", "ai"), default="ai")
    query.add_argument("--limit", type=int, default=10, help="表示件数")
    query.add_argument("--verbose", action="store_true", help="スコア理由も出す")
    query.set_defaults(func=command_query)

    doctor = sub.add_parser("doctor", help="実行環境とリポジトリを点検する")
    doctor.set_defaults(func=command_doctor)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = make_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except (MeaningFirstError, OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
