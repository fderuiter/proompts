# Prompt Library 📚

Welcome to the Prompt Library! This directory is the core of our agentic framework, containing structured prompts that drive our AI agents across various domains.

## Discovery Model 🧭

We are moving away from deep folder nesting as the primary way to classify prompts.
Use prompt metadata/tags for discovery and categorization:

- `domain:<value>` — primary grouping (examples: `domain:technical`, `domain:clinical`)
- `topic:<value>` — subject area (examples: `topic:architecture`, `topic:qa`)
- `capability:<value>` — intended task style (examples: `capability:analysis`, `capability:generation`)

Directory layout can stay shallow/flat; docs and index tooling now derive categories from this taxonomy first.

## Prompt Structure 🏗️

All prompts in this repository follow a strict YAML schema (`*.prompt.yaml`) to ensure they are machine-readable and testable.

### Key Fields

- **`name`**: A unique, human-readable identifier for the prompt.
- **`description`**: A clear explanation of the prompt's purpose.
- **`model`**: The AI model to use (e.g., `gpt-4o`, `gpt-4o-mini`).
- **`modelParameters`**: Model configuration including `temperature`.
- **`messages`**: The sequence of messages (System, User, Assistant) that form the prompt context. Variables are denoted with `{{variable_name}}` syntax.
- **`testData`**: A list of test cases with sample inputs and expected outputs used for validation.
- **`evaluators`**: Validation rules to check output quality and format.

### Example

```yaml
name: "Code Reviewer"
description: "Reviews code for best practices."
model: "gpt-4o-mini"
modelParameters:
  temperature: 0.3
messages:
  - role: "system"
    content: "You are an expert code reviewer."
  - role: "user"
    content: |-
      Review this code:
      
      {{code_snippet}}
testData:
  - code_snippet: "function add(a,b){return a+b}"
    expected: "Review noting missing type safety and documentation"
evaluators:
  - name: "Output includes suggestions"
    string:
      contains: "suggest"
```

For detailed guidance, see [Best Practices Guide](../docs/BEST_PRACTICES.md).

## Usage 🚀

Prompts are rarely used in isolation. They are typically chained together in **Workflows**.

- **Workflows**: Defined in the [`../workflows/`](../workflows) directory (organized by domain), workflows orchestrate multiple prompts to achieve complex goals.
- **Simulation**: You can simulate workflows using the `run_workflow.py` script to test logic without API costs.

```bash
# Example: Simulate the Agentic Coding workflow
python3 tools/scripts/run_workflow.py workflows/technical/agentic_coding.workflow.yaml -i product_concept="A new time-tracking app"
```

## Tools 🛠️

We maintain a suite of tools in [`../tools/scripts/`](../tools/scripts) to manage this library:

- **[`check_prompts.py`](../tools/scripts/check_prompts.py)**: Validates that all prompt files follow the required schema and naming conventions.
- **[`generate_overviews.py`](../tools/scripts/generate_overviews.py)**: Automatically generates `overview.md` files for subdirectories.
- **[`run_workflow.py`](../tools/scripts/run_workflow.py)**: The engine that executes workflows and prompts.

## Contributing 🤝

1.  **Create**: Add your new `.prompt.yaml` file under `prompts/` (prefer a shallow/flat layout).
2.  **Document**: Ensure you provide a clear `description` and `inputs`.
3.  **Tag**: Add namespaced tags (`domain:`, `topic:`, `capability:`) in metadata where possible.
4.  **Test**: Add at least one test case in the `testData` field.
5.  **Verify**: Run `python3 tools/scripts/check_prompts.py` to ensure your prompt is valid.
