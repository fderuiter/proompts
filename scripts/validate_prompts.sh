#!/bin/bash
# validation script

# Ensure we are at the root of the repo
cd "$(dirname "$0")/.."

echo "Running test suite..."
uv run pytest || exit 1

echo "Checking prompt formats..."
uv run python3 tools/tools/scripts/check_prompts.py || exit 1

echo "Checking for dead code..."
uv run vulture promptops tools proompts_guard studio --min-confidence 70 || exit 1

echo "Validating prompt schemas..."
uv run python3 tools/tools/scripts/validate_prompt_schema.py || exit 1

echo "Validating workflows..."
uv run python3 tools/tools/scripts/test_workflows.py || exit 1

echo "Updating baseline governance manifest..."
uv run python3 tools/tools/scripts/governance_manifest_generator.py || exit 1

echo "All checks passed!"
