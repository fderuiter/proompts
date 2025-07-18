# proompts

[![Update Docs Index](https://github.com/fderuiter/proompts/actions/workflows/update-docs.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/update-docs.yml)
[![Markdown Validation](https://github.com/fderuiter/proompts/actions/workflows/markdown-validation.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/markdown-validation.yml)
[![Deploy Jekyll site](https://github.com/fderuiter/proompts/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/deploy-pages.yml)

A curated set of Markdown prompts for AI-assisted product development, regulatory workflows, and general operations. Prompts are organized by topic—ranging from code reviews to market research—so you can mix and match them in your own agentic workflows.

## Validation

Check Markdown formatting and the docs index before committing:

```bash
./scripts/validate_markdown.sh
```

The script first runs `python3 scripts/update_docs_index.py --check` to ensure
`docs/index.md` and `docs/table-of-contents.md` are up to date, then runs `mdl`.
It requires both Python 3 and the `mdl` tool. Install the linter with
`gem install mdl` if it isn't already available. The same check runs in GitHub
Actions.
This repository also runs `.github/workflows/update-docs.yml` to automatically commit the index if it changes.

## Contributing

1. Add prompts as `.md` files in the appropriate folder.
1. Include an `overview.md` when creating a new directory.
1. Run `scripts/update_docs_index.py` to regenerate the index; the workflow will update it automatically.
1. Run the validation script above before committing.

## License

This project is licensed under the [Proompts Personal Use License](LICENSE.md).
Individuals may freely use, modify, and distribute the prompts for personal,
non-commercial purposes. Commercial entities must obtain written permission
from Frederick de Ruiter before using the material.
