PYTHON ?= python3
PYTHONPATH := src
export PYTHONPATH

.PHONY: help doctor validate build audit benchmark test context performance package quality clean

help:
	@printf '%s\n' \
	  'make doctor     - inspect runtime and repository' \
	  'make validate   - validate typed semantic blocks' \
	  'make build      - generate README and manifest' \
	  'make audit      - generate quality audit report' \
	  'make benchmark  - run context retrieval benchmark' \
	  'make test       - run the unittest suite' \
	  'make context    - generate an example AI context' \
	  'make performance - run a 2,000-block synthetic observation' \
	  'make package    - build an offline-installable wheel' \
	  'make quality    - run the complete local quality gate'

doctor:
	$(PYTHON) -m meaning_first_readme doctor

validate:
	$(PYTHON) -m meaning_first_readme validate

build: validate
	$(PYTHON) -m meaning_first_readme build --output README.md --manifest build/manifest.json

audit: validate
	$(PYTHON) -m meaning_first_readme audit --format markdown --output build/audit.md
	$(PYTHON) -m meaning_first_readme audit --format json --output build/audit.json

benchmark: validate
	$(PYTHON) -m meaning_first_readme benchmark --format markdown --output build/benchmark.md
	$(PYTHON) -m meaning_first_readme benchmark --format json --output build/benchmark.json

context: validate
	$(PYTHON) -m meaning_first_readme context \
	  --task '公開前に事実、根拠、秘密情報、リリース条件を確認する' \
	  --tokens 6500 \
	  --audience ai \
	  --output build/release-context.md

test:
	$(PYTHON) -m unittest discover -s tests -v

performance:
	$(PYTHON) benchmarks/performance.py --blocks 2000 --output build/performance.json

package:
	rm -rf dist src/meaning_first_readme.egg-info
	$(PYTHON) -m pip install --upgrade pip setuptools wheel
	$(PYTHON) -m pip wheel . --no-deps -w dist

quality: validate build audit benchmark context test
	@git diff --exit-code -- README.md build/manifest.json build/audit.md build/audit.json build/benchmark.md build/benchmark.json build/release-context.md 2>/dev/null || \
	  (printf '%s\n' 'Generated artifacts differ. Review and commit them.' && exit 1)

clean:
	rm -rf build/*.json build/*.md dist __pycache__ src/meaning_first_readme/__pycache__ tests/__pycache__ src/meaning_first_readme.egg-info
