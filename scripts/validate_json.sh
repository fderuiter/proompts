#!/usr/bin/env bash
set -euo pipefail

# Validate JSON prompt files and documentation index.
# Requires 'jq' and Python 3.

command -v jq >/dev/null 2>&1 || { echo "Error: jq is not installed" >&2; exit 1; }

# Ensure docs/index.md and docs/table-of-contents.md are current.
python3 scripts/update_docs_index.py --check

# Verify each JSON file parses correctly
while IFS= read -r -d '' file; do
    jq -e '.' "$file" >/dev/null
done < <(find . -name '*.json' -not -path './.git/*' -print0)

echo "All JSON files validated"
