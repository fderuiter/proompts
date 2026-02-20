#!/bin/bash
# validation script
#
# This script is a convenience wrapper around 'tools/scripts/test_all.py'.
# It ensures all validation checks (YAML linting, schema validation, broken links)
# are run before committing changes.

# Ensure we are at the root of the repo
cd "$(dirname "$0")/.."

echo "Running full validation suite via tools/scripts/test_all.py..."
python3 tools/scripts/test_all.py
