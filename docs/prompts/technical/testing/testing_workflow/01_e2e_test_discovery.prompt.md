---
title: E2E Test Discovery Template
---

# E2E Test Discovery Template

Guide a model to analyze a codebase and produce a comprehensive end‑to‑end test plan.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/technical/testing/testing_workflow/01_e2e_test_discovery.prompt.yaml)

```yaml
---
name: E2E Test Discovery Template
version: 0.1.0
description: Guide a model to analyze a codebase and produce a comprehensive end‑to‑end test plan.
metadata:
  domain: technical
  complexity: high
  tags:
  - testing
  - e2e
  - test
  - discovery
  - template
  requires_context: true
variables:
- name: business_goal
  description: overall objective
  required: true
- name: languages_frameworks
  description: The programming or natural language to use
  required: true
- name: project_name
  description: name of the project
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'This prompt is used with a repository URL or zipped source tree for **{{project_name}}**. Provide the primary
    tech stack and the high‑level business goal. The assistant acts as an expert test architect and senior software engineer.


    Aim for exhaustive coverage. Respond only with the open questions list until all unknowns are resolved.'
- role: user
  content: '1. Map the structure: apps, packages, routes, entry points and existing test frameworks.

    2. Outline critical user journeys with triggers, expected behaviour, data mutations and side effects.

    3. Catalogue REST/GraphQL endpoints, message queues and third‑party APIs with schemas and auth methods.

    4. Identify state management and seed data needed for deterministic tests.

    5. Capture non‑functional requirements such as performance, a11y, security and compliance.

    6. List validation rules, error branches and retry logic.

    7. Describe how to spin up the system locally or in CI and recommend tooling if needed.

    8. Produce a table grouping E2E scenarios by theme with priority and test data.

    9. Highlight coverage gaps and risk areas.

    10. After the first pass, list any open questions before finalizing.


    Inputs:

    - `{{project_name}}` – name of the project

    - `{{languages_frameworks}}` – tech stack

    - `{{business_goal}}` – overall objective


    Output Format:

    Markdown report with sections:


    1. Repository Overview

    2. Critical User Journeys

    3. API / Interface Catalogue

    4. State & Data Requirements

    5. Non‑Functional Requirements

    6. Edge Cases & Negative Paths

    7. Environment & Tooling

    8. Proposed E2E Test Suite

    9. Coverage Gaps & Risk Register'
testData:
- input: 'project_name: Cartify

    languages_frameworks: Django, React

    business_goal: Enable online shopping for users

    '
  expected: 'Repository Overview

    '
evaluators:
- name: Output starts with 'Repository Overview'
  string:
    startsWith: Repository Overview

```
