---
layout: default
title: System Architecture
nav_order: 1
has_children: false
---

# System Architecture

## Overview

Proompts is a "Prompts as Code" repository. It treats prompts as software artifacts with versioning, testing, and automated documentation. This approach ensures that prompts are reproducible, testable, and maintainable, just like traditional code.

## Core Concepts

### 1. Prompts as Code
Prompts are defined in YAML files (`.prompt.yaml`) following a strict schema. This allows for:
- **Structured Metadata**: Fields like `name`, `description`, `model`, and `parameters` provide clear context.
- **Templating**: Jinja2 syntax (`{{variable}}`) enables dynamic content injection.
- **Test Data**: Embedded test cases (`testData`) with expected outputs allow for deterministic validation.
- **Evaluators**: Rules for validating model outputs (e.g., regex checks, python scripts) ensure quality.

### 2. Workflows (The Orchestrator)
Workflows chain multiple prompts together to achieve complex, multi-step goals. They are defined in `.workflow.yaml` files.
- **Steps**: Define a sequential execution of prompts.
- **State Management**: Outputs from one step can be passed as inputs to subsequent steps using `{{steps.step_id.output}}`.
- **Visualizations**: Workflow diagrams are automatically generated to visualize the flow of data.

### 3. The Simulation Engine (`run_workflow.py`)
A unique feature of this repository is the ability to **simulate** workflow execution without incurring LLM costs or requiring API keys.
- **Deterministic Replay**: The engine uses the `testData` field in prompt files to mock LLM responses.
- **Validation**: This allows developers to verify variable mapping, conditional logic, and overall workflow integrity before deploying to a live model.
- **Usage**: `python3 tools/scripts/run_workflow.py path/to/workflow.workflow.yaml`

### 4. The Validation Pipeline (`test_all.py`)
A comprehensive suite of scripts ensures repository health and consistency.
- **`validate_prompt_schema.py`**: Enforces strict Pydantic schemas on all prompt YAML files.
- **`check_prompts.py`**: Verifies file naming conventions and ensures every directory has an `overview.md`.
- **`yamllint`**: Checks for YAML syntax errors and formatting consistency.
- **`check_broken_links.py`**: Scans documentation for broken internal links.

### 5. Documentation Generation
Documentation is treated as a first-class build artifact, automatically generated from the source code.
- **`generate_docs.py`**: Scans the repository to build the static site structure in `docs/`.
- **`update_docs_index.py`**: Regenerates the main `docs/index.md` based on current prompt metadata.
- **Workflow Diagrams**: Integrated into the documentation generation process, visualizing `.workflow.yaml` files using Mermaid.js.

## Directory Structure

- **`prompts/`**: The source of truth for all prompt definitions, organized by domain.
- **`workflows/`**: Workflow definitions that orchestrate prompts.
- **`tools/scripts/`**: The build, validation, and maintenance toolchain.
- **`docs/`**: The generated documentation site (Jekyll-ready).
