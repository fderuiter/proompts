#!/usr/bin/env bash
set -euo pipefail

# Validate formatting of all Markdown files using mdl (Markdown lint)
# Requires the 'markdownlint' package (provides the 'mdl' command)

find . -name "*.md" | xargs mdl -r ~MD013
