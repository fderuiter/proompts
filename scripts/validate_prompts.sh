#!/bin/bash
# validation script

# Ensure we are at the root of the repo
cd "$(dirname "$0")/.."

echo "Running test suite..."
uv run playwright install --with-deps chromium || exit 1
uv run pytest || exit 1

echo "Building static HTML docs..."
uv run mkdocs build --clean --strict || exit 1

echo "Installing Node.js dependencies..."
npm install || exit 1

echo "Running static accessibility scanner..."
node scripts/accessibility-scan.js || exit 1

echo "Running YAML syntax validation..."
uv run yamllint --strict . || exit 1

echo "Validating prompts and workflows with CLI..."
uv run promptops validate --strict || exit 1

echo "Validating CLI documentation is synchronized..."
uv run promptops generate-cli-docs
if ! git diff --exit-code docs/CLI.md > /dev/null; then
    echo "ERROR: CLI documentation is out of sync. Please run 'uv run promptops generate-cli-docs' and commit the changes."
    exit 1
fi

echo "Validating schemas are synchronized..."
uv run promptops export-schemas --out-dir docs/schemas
if ! git diff --exit-code docs/schemas > /dev/null; then
    echo "ERROR: Schema files are out of sync. Please run 'uv run promptops export-schemas --out-dir docs/schemas' and commit the changes."
    exit 1
fi

echo "Validating prompt documentation is synchronized..."
uv run promptops docs --check || {
    echo "ERROR: Prompt documentation is out of sync. Please run 'uv run promptops docs' and commit the changes."
    exit 1
}

echo "Checking for unpruned imports and variables (check-only)..."
uv run ruff check --select F401,F841 . || exit 1

echo "Checking for dead code..."
uv run vulture || exit 1

echo "Testing documentation snippets simulation..."
uv run python3 tools/tools/scripts/test_docs_snippets.py || exit 1

echo "Updating baseline governance manifest..."
uv run python3 tools/tools/scripts/governance_manifest_generator.py || exit 1

echo "Checking for explicit file encodings in Python scripts..."
uv run python3 tools/tools/scripts/check_file_encoding.py || exit 1

echo "Checking for broken links..."
uv run python3 tools/tools/scripts/check_broken_links.py || exit 1

echo "All checks passed!"
