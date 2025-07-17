#!/usr/bin/env bash
set -euo pipefail

# Validate formatting of all Markdown files using mdl (Markdown lint)
# Requires the 'markdownlint' package (provides the 'mdl' command)

# Skip the license file as it mirrors the original text and doesn't
# conform to all markdownlint rules.
find . -name "*.md" ! -name LICENSE.md | xargs mdl -r ~MD013
