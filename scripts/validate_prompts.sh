#!/bin/bash
# validation script

# Ensure we are at the root of the repo
cd "$(dirname "$0")/.."

echo "Running test suite..."
uv run pytest || exit 1

echo "Validating prompts and workflows with CLI..."
uv run promptops validate --strict || exit 1

echo "Validating CLI documentation is synchronized..."
uv run promptops generate-cli-docs
if ! git diff --exit-code docs/CLI.md > /dev/null; then
    echo "ERROR: CLI documentation is out of sync. Please run 'uv run promptops generate-cli-docs' and commit the changes."
    exit 1
fi

echo "Checking for dead code..."
uv run vulture || exit 1

echo "Updating tools script inventory..."
uv run python3 tools/tools/scripts/update_readme_map.py || exit 1

echo "Updating baseline governance manifest..."
uv run python3 tools/tools/scripts/governance_manifest_generator.py || exit 1

echo "Validating documentation snippets..."
uv run python3 tools/tools/scripts/validate_docs_snippets.py docs/USAGE.md docs/BEST_PRACTICES.md || exit 1

echo "All checks passed!"
