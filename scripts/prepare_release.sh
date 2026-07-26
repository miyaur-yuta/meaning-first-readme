#!/usr/bin/env sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$ROOT"
export PYTHONPATH="$ROOT/src"

./scripts/quality.sh
python3 -m meaning_first_readme snapshot --output build/release-snapshot.json

printf '%s\n' \
  'Release preparation completed.' \
  'No remote operation was performed.' \
  'Review release/PR_BODY.md and request explicit human approval before creating a PR.'
