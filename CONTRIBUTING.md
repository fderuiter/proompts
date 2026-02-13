# Contributing to Proompts

Thank you for your interest in contributing to the Proompts repository! This guide will help you get started with adding new prompts, improving documentation, and submitting changes.

## Getting Started

1.  **Fork the repository** and clone it locally.
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
    Ensure you have Python 3 installed.
3.  **Explore the repository**:
    *   `prompts/` contains the prompt files, organized by category.
    *   `docs/` contains documentation.
    *   `tools/scripts/` contains utility scripts for validation and maintenance.

## Adding a New Prompt

1.  **Create a Prompt File**:
    *   Use the `.prompt.yaml` extension.
    *   Follow the schema defined in `docs/template_prompt.prompt.yaml`.
    *   Include required fields: `name`, `description`, `model`, `messages`.
    *   Include optional but recommended fields: `testData`, `evaluators`.

2.  **Choose the Right Category**:
    *   Place your file in the appropriate subdirectory under `prompts/`.
    *   If a suitable directory doesn't exist, create a new one using snake_case (e.g., `prompts/new_category/`).
    *   Add an `overview.md` file to any new directory describing its contents.

3.  **Validate Your Prompt**:
    Run the validation scripts to ensure your prompt meets the standards:
    ```bash
    # Run all checks
    python3 tools/scripts/test_all.py
    ```
    This will run:
    *   `check_prompts.py`: Checks naming conventions and file locations.
    *   `validate_prompt_schema.py`: Validates the YAML structure and required fields.
    *   `yamllint`: Checks for YAML syntax errors.

4.  **Sanitize and Standardize**:
    *   Ensure no sensitive information is included.
    *   **Naming Conventions**:
        *   **Standard Prompts**: use `snake_case.prompt.yaml` (e.g., `market_research.prompt.yaml`). Do not number them.
        *   **Workflow Prompts**:
            *   Create a dedicated subfolder for the workflow (e.g., `prompts/category/my_workflow/`).
            *   Number the prompts sequentially (e.g., `01_step_one.prompt.yaml`, `02_step_two.prompt.yaml`).

## Submitting Changes

1.  **Create a Branch**: Use a descriptive name for your branch (e.g., `add-feature-x`, `fix-bug-y`).
2.  **Commit Your Changes**: Write clear and concise commit messages.
3.  **Open a Pull Request**:
    *   Describe your changes in detail.
    *   Link to any relevant issues.
    *   Ensure all checks pass.

## Style Guide

*   **YAML**: Use 2 spaces for indentation.
*   **Markdown**: Use standard Markdown formatting.
*   **Prompts**: Be clear, concise, and explicit in your instructions. Use `{{variable}}` for placeholders.

## Reporting Issues

If you find a bug or have a feature request, please open an issue using the provided templates.

Thank you for contributing!
