# JSON Schemas for Tooling

This directory contains JSON Schemas generated from the repository's validation scripts. These schemas can be used to configure IDEs (like VS Code, IntelliJ, etc.) to provide validation, autocompletion, and hover documentation for your YAML files.

## Available Schemas

| Schema File | Description | Source Script |
| :--- | :--- | :--- |
| [`prompt.schema.json`](./prompt.schema.json) | Validates `.prompt.yaml` files. | `tools/scripts/validate_prompt_schema.py` |

## How to Configure VS Code

To enable schema validation and Intellisense in VS Code for `.prompt.yaml` files:

1.  Open your workspace settings (`.vscode/settings.json`) or global settings.
2.  Add the `yaml.schemas` configuration:

```json
{
  "yaml.schemas": {
    "docs/schemas/prompt.schema.json": "**/*.prompt.yaml"
  }
}
```

*Note: You may need to install the [Red Hat YAML extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) for this to work.*

## How to Configure JetBrains IDEs (IntelliJ, PyCharm)

1.  Go to **Settings/Preferences** > **Languages & Frameworks** > **Schemas and DTDs** > **JSON Schema Mappings**.
2.  Click `+` to add a new mapping.
3.  **Name**: "Prompt Schema".
4.  **Schema file or URL**: Select the `docs/schemas/prompt.schema.json` file in your project.
5.  **Schema version**: JSON Schema version 7.
6.  **File path pattern**: `**/*.prompt.yaml`.

## Updating the Schema

If you modify the `PromptSchema` class in `tools/scripts/validate_prompt_schema.py`, you must regenerate the schema file:

```bash
python3 tools/scripts/validate_prompt_schema.py --json-schema > docs/schemas/prompt.schema.json
```
