#!/usr/bin/env sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$ROOT"
export PYTHONPATH="$ROOT/src"

python3 -m meaning_first_readme validate
python3 -m meaning_first_readme build --output README.md --manifest build/manifest.json
python3 -m meaning_first_readme audit --format markdown --output build/audit.md
python3 -m meaning_first_readme audit --format json --output build/audit.json
python3 -m meaning_first_readme benchmark --format markdown --output build/benchmark.md
python3 -m meaning_first_readme benchmark --format json --output build/benchmark.json
python3 -m meaning_first_readme context \
  --task "公開前に事実、根拠、秘密情報、リリース条件を確認する" \
  --tokens 6500 \
  --audience ai \
  --output build/release-context.md
python3 -m compileall -q src tests
python3 -m unittest discover -s tests -v
