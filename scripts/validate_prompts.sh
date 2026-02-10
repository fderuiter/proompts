#!/bin/bash
set -e

# Navigate to the root of the repository
cd "$(dirname "$0")/.."

echo "Running YAML linting..."
# Using 'yamllint .' as defined in test_all.py
if command -v yamllint >/dev/null 2>&1; then
    yamllint .
else
    echo "Warning: yamllint not found, skipping."
fi

echo "Validating prompt schemas..."
python3 tools/scripts/validate_prompt_schema.py

echo "Checking documentation index status..."
python3 tools/scripts/update_docs_index.py --check

echo "All validation checks passed!"
