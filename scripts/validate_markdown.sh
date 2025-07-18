#!/usr/bin/env bash
set -euo pipefail

# Validate documentation and formatting
# Requires the 'markdownlint' package (provides the 'mdl' command)
# and Python 3 for the docs index check.

# Ensure docs/index.md and docs/table-of-contents.md are current.
python3 scripts/update_docs_index.py --check

# Skip the license file as it mirrors the original text and doesn't
# conform to all markdownlint rules.
find . -name "*.md" ! -name LICENSE.md | xargs mdl -r ~MD013
