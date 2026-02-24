---
description: "Comprehensive guide for AI agents contributing to the Proompts repository."
tags: ["documentation", "developer-guide", "ai-context", "best-practices"]
---

# 🤖 AI Agent Guidelines

This document provides the tribal knowledge, technical constraints, and operational procedures required for AI agents to contribute effectively to this repository.

## 1. Project Overview & Stack

**Repository Type**: Prompt Engineering Library & Workflow Engine
**Core Technologies**:
- **Data Format**: YAML (`.prompt.yaml`, `.workflow.yaml`)
- **Validation**: Python 3.x
- **Documentation**: Jekyll (Markdown)
- **CI/CD**: GitHub Actions

**Key Dependencies**: `pyyaml`, `yamllint`, `pydantic`, `jinja2`, `pytest`

## 2. Executable Commands

Use these exact commands to build, test, and validate your work.

### Setup
```bash
# Install required Python dependencies
pip install -r requirements.txt
```

### Validation & Testing
```bash
# Run the full validation suite (includes schema, linting, docs check)
python3 tools/scripts/test_all.py

# Run specific schema validation for prompts
python3 tools/scripts/validate_prompt_schema.py

# Lint YAML files strictly
yamllint .
```

### Documentation
```bash
# Generate documentation indices and overviews
python3 tools/scripts/generate_docs.py
```

## 3. Testing & Validation

Testing in this repository means verifying **schema compliance** and **logic correctness** of prompts.

- **Schema Validation**: handled by `validate_prompt_schema.py`. Ensure all required fields (`name`, `model`, `messages`) are present.
- **Logic Verification**: use the `testData` field in your prompt file. This allows simulation tools to verify the prompt's output against expected results.
- **Workflow Simulation**: use `tools/scripts/run_workflow.py` to simulate complex multi-step prompt chains.

## 4. Code Style & Conventions

### File Naming
- **Prompts**: `snake_case.prompt.yaml` (e.g., `code_review.prompt.yaml`)
- **Workflows**: `snake_case.workflow.yaml`
- **Directories**: `snake_case/` (e.g., `prompts/technical/software_engineering/`)

### Prompt Structure (Example)
Your prompts **must** follow this structure. Do not invent new fields.

```yaml
name: Text Summarizer
version: "1.0.0"
description: Summarizes input text concisely.
metadata:
  domain: general
  complexity: low
  tags:
    - summarization
variables:
  - name: input
    description: The text to summarize.
    required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.5
messages:
  - role: system
    content: "You are a concise summarizer."
  - role: user
    content: "Summarize this: {{input}}"
testData:
  - input:
      input: "Long text here..."
    expected: "Short summary."
evaluators:
  - name: Length Check
    python: "len(output) < len(input)"
```

## 5. Strict Boundaries & Constraints

🛑 **CRITICAL RULES**:
1. **No JSON Prompts**: All prompts must be YAML (`.prompt.yaml`).
2. **Docs Integrity**: Do not manually edit auto-generated files in `docs/` unless you are fixing the generator script itself.
3. **Directory Hygiene**: Every new directory under `prompts/` **must** contain an `overview.md` file describing its contents.
4. **Workflow Numbering**: Prompts inside a workflow directory (e.g., `paw_workflow/`) must be numbered sequentially (e.g., `01_step_one.prompt.yaml`). Standalone prompts must **not** be numbered.

## 6. Git & PR Workflow

- **Commit Messages**: Use Conventional Commits.
  - `feat: add new summarization prompt`
  - `fix: correct typo in system message`
  - `docs: update usage guide`
- **Pull Requests**:
  - Must pass `tools/scripts/test_all.py` before submission.
  - Ensure no sensitive data (API keys, PII) is included in `testData`.
