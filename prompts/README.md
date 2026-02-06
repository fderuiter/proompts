# Prompt Library 📚

Welcome to the Prompt Library! This directory is the core of our agentic framework, containing structured prompts that drive our AI agents across various domains.

## Directory Map 🗺️

The prompts are organized by domain to ensure easy navigation and specialized context.

| Directory | Domain | Description |
| :--- | :--- | :--- |
| **[`business/`](./business)** | Business | Corporate functions including **Finance**, **HR**, and **Market Research**. |
| **[`clinical/`](./clinical)** | Clinical | Comprehensive clinical trial operations, covering **Adjudication**, **CRA** tasks, **Data Management**, **Protocols**, **Safety**, and **Trial Execution**. |
| **[`general/`](./general)** | General | Utility prompts for **Personal Productivity**, **Brainstorming**, **Communication**, and Self-Improvement. |
| **[`management/`](./management)** | Management | High-level decision-making prompts for **Leadership**, **Project Management**, and **Executive** roles. |
| **[`meta/`](./meta)** | Meta | "Prompts for Prompts" - The engine room for **Prompt Engineering**, **Agent Creation**, and self-improving workflows. |
| **[`regulatory/`](./regulatory)** | Regulatory | Critical frameworks for **Compliance**, **Quality Assurance**, and **Regulatory Strategy**. |
| **[`scientific/`](./scientific)** | Scientific | Lab-focused prompts for **Biosafety**, **Microbiology**, **Pathology**, and **Sterility**. |
| **[`technical/`](./technical)** | Technical | Engineering excellence: **Software Architecture**, **DevOps**, **Testing**, and **Codebase Analysis**. |

## Prompt Structure 🏗️

All prompts in this repository follow a strict YAML schema (`*.prompt.yaml`) to ensure they are machine-readable and testable.

### Key Fields

- **`name`**: A unique, human-readable identifier for the prompt.
- **`description`**: A clear explanation of the prompt's purpose.
- **`messages`**: The sequence of messages (System, User) that form the prompt context. Variables are denoted with Jinja2 syntax (e.g., `{{ input_variable }}`).
- **`inputs`**: Definitions of expected variables, including types and descriptions.
- **`testData`**: A list of test cases (inputs and expected outputs) used for validation.

### Example

```yaml
name: "Code Reviewer"
description: "Reviews code for best practices."
inputs:
  - name: "code_snippet"
    description: "The code to review."
messages:
  - role: "system"
    content: "You are an expert code reviewer."
  - role: "user"
    content: "Review this code:\n\n{{ code_snippet }}"
```

## Usage 🚀

Prompts are rarely used in isolation. They are typically chained together in **Workflows**.

- **Workflows**: Defined in the [`../workflows/`](../workflows) directory, workflows orchestrate multiple prompts to achieve complex goals (e.g., "Take a product idea -> Generate Brief -> Create Epics").
- **Execution**: You can run workflows using the `run_workflow.py` script.

```bash
# Example: Run the Agentic Coding workflow
python3 tools/scripts/run_workflow.py workflows/agentic_coding.workflow.yaml -i product_concept="A new time-tracking app"
```

## Tools 🛠️

We maintain a suite of tools in [`../tools/scripts/`](../tools/scripts) to manage this library:

- **[`check_prompts.py`](../tools/scripts/check_prompts.py)**: Validates that all prompt files follow the required schema and naming conventions.
- **[`generate_overviews.py`](../tools/scripts/generate_overviews.py)**: Automatically generates `overview.md` files for subdirectories.
- **[`run_workflow.py`](../tools/scripts/run_workflow.py)**: The engine that executes workflows and prompts.

## Contributing 🤝

1.  **Create**: Add your new `.prompt.yaml` file in the appropriate subdirectory.
2.  **Document**: Ensure you provide a clear `description` and `inputs`.
3.  **Test**: Add at least one test case in the `testData` field.
4.  **Verify**: Run `python3 tools/scripts/check_prompts.py` to ensure your prompt is valid.
