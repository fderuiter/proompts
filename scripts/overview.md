# Scripts Overview

Utility scripts for repository maintenance live here. The `validate_json.sh` script verifies JSON formatting across the project.

The `update_docs_index.py` script regenerates `docs/index.md` and
`docs/table-of-contents.md` by scanning all prompt folders. Use the
`--check` flag in CI to ensure the documentation is up to date.
