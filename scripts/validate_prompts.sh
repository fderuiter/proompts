#!/usr/bin/env bash
set -euo pipefail

# Validate prompt files and documentation index.
# Requires 'yamllint' and Python 3.

command -v yamllint >/dev/null 2>&1 || { echo "Error: yamllint is not installed" >&2; exit 1; }

# Ensure docs/index.md and docs/table-of-contents.md are current.
python3 scripts/update_docs_index.py --check

# Validate YAML prompt files
while IFS= read -r -d '' file; do
    yamllint -s "$file"
done < <(find . \( -name '*.prompt.yaml' -o -name '*.prompt.yml' \) -not -path './.git/*' -print0)

echo "All prompt files validated"
