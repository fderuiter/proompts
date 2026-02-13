---
layout: default
title: System Architecture
nav_order: 2
---

# System Architecture & Design

This document details the technical design of the **Proompts** repository. It explains how prompts are structured, how workflows are simulated, and how the validation pipeline ensures quality.

## 1. Philosophy: Prompts as Code

The core philosophy of this repository is that **Prompts are Software**. They should be:
- **Versioned**: Stored in Git.
- **Structured**: Defined in YAML with a strict schema, not just free text.
- **Tested**: Validated with test cases and evaluators.
- **Modular**: Composable into workflows.

This approach allows for rigorous engineering practices (Code Review, CI/CD, Testing) to be applied to Prompt Engineering.

## 2. The Prompt Engine (Simulation Mode)

Currently, the repository acts as a **Library** and a **Simulation Engine**. The execution script (`run_workflow.py`) does **not** make live API calls to LLM providers (like OpenAI or Anthropic) by default. Instead, it **simulates** execution using defined `testData`.

### Simulation Data Flow

```mermaid
graph LR
    User[User / Developer] -->|Run Workflow| Runner[run_workflow.py]
    Runner -->|Load| Workflow[Workflow YAML]
    Workflow -->|Step 1| Prompt1[Prompt YAML]
    Prompt1 -->|Input Vars| Simulator[Simulation Logic]
    Simulator -->|Lookup| TestData[testData Block]
    TestData -->|Return| Output[Expected Output]
    Output -->|Pass to| Workflow
    Workflow -->|Step 2| Prompt2[Prompt YAML]
    Prompt2 -->|...| FinalResult[Final Result]
```

This design allows developers to:
1.  **Test Logic Rapidly**: Verify variable substitution and workflow chaining without latency or cost.
2.  **Ensure Determinism**: Tests always pass if the logic is correct, regardless of model stochasticity.
3.  **Work Offline**: No internet connection required for development.

To run this in production, you would swap the `simulate_prompt_execution` function in `run_workflow.py` with a real API client (e.g., `openai.ChatCompletion.create`).

## 3. Workflow Engine Architecture

Workflows orchestrate multiple prompts. They manage **State** and **Dependencies**.

### Workflow State Machine

```mermaid
stateDiagram-v2
    [*] --> Initialized
    Initialized --> Step1_Executing: Input Variables Injected
    Step1_Executing --> Step1_Completed: Prompt Simulation
    Step1_Completed --> Step2_Executing: Output Mapped to Step 2 Input
    Step2_Executing --> Step2_Completed: Prompt Simulation
    Step2_Completed --> Finished: Final Output Generated
    Finished --> [*]
```

- **Global Inputs**: Defined in `workflow.yaml` under `inputs`.
- **Step Inputs**: Mapped using Jinja2 syntax (e.g., `{{steps.step_id.output}}`).
- **Context**: The `workflow_state` dictionary grows as steps complete.

## 4. Validation Pipeline (`test_all.py`)

Every commit is verified by a strict validation pipeline.

```mermaid
graph TD
    Commit[Git Commit] --> TestAll[test_all.py]

    subgraph Checks
    TestAll --> Clean[Cleanup Mac Files]
    TestAll --> Schema[validate_prompt_schema.py]
    TestAll --> Links[check_broken_links.py]
    TestAll --> Index[update_docs_index.py]
    TestAll --> Lint[yamllint]
    end

    Schema -->|Validates| Prompts[*.prompt.yaml]
    Links -->|Scans| Docs[docs/*.md]
    Index -->|Generates| Site[docs/index.md]

    Checks --> Result{Pass / Fail}
```

### Key Scripts

| Script | Purpose |
| :--- | :--- |
| `validate_prompt_schema.py` | Enforces the Pydantic schema (required fields, valid YAML). |
| `check_prompts.py` | Enforces naming conventions and file locations. |
| `update_docs_index.py` | Regenerates the documentation index and table of contents. |
| `generate_docs.py` | Builds the static documentation site structure. |

## 5. Directory Map

A high-level view of the repository structure:

```text
.
├── docs/                   # Documentation Site (Jekyll)
│   ├── workflows/          # Generated workflow docs
│   └── *.md                # Category pages and guides
├── prompts/                # The Prompt Library
│   ├── business/           # Domain: Business
│   ├── clinical/           # Domain: Clinical
│   ├── technical/          # Domain: Technical
│   └── ...                 # Other domains
├── tools/                  # Developer Tools
│   ├── scripts/            # Python maintenance scripts
│   └── prompt_tools/       # Meta-prompts for repo maintenance
└── workflows/              # Workflow Definitions
    ├── clinical/           # Clinical workflows
    └── ...                 # Other workflow domains
```
