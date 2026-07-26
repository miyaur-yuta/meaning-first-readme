$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root
$env:PYTHONPATH = Join-Path $Root 'src'

python -m meaning_first_readme validate
python -m meaning_first_readme build --output README.md --manifest build/manifest.json
python -m meaning_first_readme audit --format markdown --output build/audit.md
python -m meaning_first_readme audit --format json --output build/audit.json
python -m meaning_first_readme benchmark --format markdown --output build/benchmark.md
python -m meaning_first_readme benchmark --format json --output build/benchmark.json
python -m meaning_first_readme context `
  --task '公開前に事実、根拠、秘密情報、リリース条件を確認する' `
  --tokens 6500 `
  --audience ai `
  --output build/release-context.md
python -m compileall -q src tests
python -m unittest discover -s tests -v
