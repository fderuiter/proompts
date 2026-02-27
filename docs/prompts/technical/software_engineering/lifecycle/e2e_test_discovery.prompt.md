---
title: E2E Test Discovery Lifecycle Template
---

# E2E Test Discovery Lifecycle Template

Provide a system prompt template that guides an LLM to analyse a codebase and generate a comprehensive end-to-end test plan.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/technical/software_engineering/lifecycle/e2e_test_discovery.prompt.yaml)

```yaml
---
name: E2E Test Discovery Lifecycle Template
version: 0.1.0
description: Provide a system prompt template that guides an LLM to analyse a codebase and generate a comprehensive end-to-end
  test plan.
metadata:
  domain: technical
  complexity: medium
  tags:
  - software-engineering
  - sdlc
  - e2e
  - test
  - discovery
  requires_context: true
variables:
- name: BUSINESS_GOAL
  description: high-level goal of the system
  required: true
- name: LANGUAGES/FRAMEWORKS
  description: '`{{BUSINESS_GOAL}}`'
  required: true
- name: PROJECT_NAME
  description: '`{{LANGUAGES/FRAMEWORKS}}`'
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'Use this template with ChatGPT or another GPT-4 class model. Fill in placeholders for project specifics and supply
    repository access when prompted.


    After the first pass, list any open questions and wait for responses before finalising the plan. Aim for exhaustive coverage
    and actionable next steps.'
- role: user
  content: "1. Explain that the assistant acts as a Test Architect analysing the supplied codebase.\n1. Provide the following\
    \ context variables:\n   - `{{PROJECT_NAME}}`\n   - `{{LANGUAGES/FRAMEWORKS}}`\n   - `{{BUSINESS_GOAL}}`\n1. Direct the\
    \ assistant to map the structure, user journeys, interfaces, data fixtures, non-functional requirements, edge cases, environment\
    \ details, test plan skeleton, and coverage gaps.\n1. Instruct it to return a markdown report with numbered sections covering\
    \ each topic.\n1. Tell the assistant to ask clarifying questions first if information is missing.\nInputs:\n- `{{PROJECT_NAME}}`\
    \ – project identifier\n- `{{LANGUAGES/FRAMEWORKS}}` – primary tech stack\n- `{{BUSINESS_GOAL}}` – high-level goal of\
    \ the system\nOutput format:\nMarkdown report with sections:\n\n1. Repository Overview\n1. Critical User Journeys\n1.\
    \ API / Interface Catalogue\n1. State & Data Requirements\n1. Non-Functional Requirements\n1. Edge Cases & Negative Paths\n\
    1. Environment & Tooling\n1. Proposed E2E Test Suite\n1. Coverage Gaps & Risk Register"
testData:
- vars:
    LANGUAGES/FRAMEWORKS: example_LANGUAGES/FRAMEWORKS
    BUSINESS_GOAL: example_BUSINESS_GOAL
    PROJECT_NAME: example_PROJECT_NAME
  expected: 'Markdown report with sections:


    1. Repository Overview

    1. Critical User Journeys

    1. API / Interface Catalogue

    1. State & Data Requirements

    1. Non-Functional Requirements

    1. Edge Cases & Negative Paths

    1. Environment & Tooling

    1. Proposed E2E Test Suite

    1. Coverage Gaps & Risk Register'
evaluators:
- name: Output starts with 'Repository Overview'
  string:
    startsWith: Repository Overview

```
