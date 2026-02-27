---
title: Product Brief Template
---

# Product Brief Template

Outline the high-level vision, features, and architecture for a new software project.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/technical/software_engineering/lifecycle/agentic_coding_workflow/01_product_brief.prompt.yaml)

```yaml
---
name: Product Brief Template
version: 0.1.0
description: Outline the high-level vision, features, and architecture for a new software project.
metadata:
  domain: technical
  complexity: high
  tags:
  - software-engineering
  - sdlc
  - product
  - brief
  - template
  requires_context: false
variables:
- name: architecture
  description: overview of proposed architecture
  required: true
- name: context_notes
  description: constraints or risks
  required: true
- name: features
  description: feature list organised by phase
  required: true
- name: vision
  description: short statement of the desired end state
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'Use this brief when kicking off a new application or clarifying scope with collaborators.


    This template helps align teams before development begins.'
- role: user
  content: '1. Describe the overall product vision.

    1. List key features with associated phases or milestones.

    1. Summarize the chosen architectural style and component interactions.

    1. Capture additional context, constraints, or stakeholder expectations.

    Inputs:

    - `{{vision}}` – short statement of the desired end state

    - `{{features}}` – feature list organised by phase

    - `{{architecture}}` – overview of proposed architecture

    - `{{context_notes}}` – constraints or risks

    Output format:

    Markdown sections titled **Vision**, **Key Features and Roadmap**, **Overall Architecture**, and **Additional Context**.'
testData:
- vars:
    vision: example_vision
    architecture: example_architecture
    features: example_features
    context_notes: example_context_notes
  expected: Markdown sections titled **Vision**, **Key Features and Roadmap**, **Overall Architecture**, and **Additional
    Context**.
evaluators:
- name: Output starts with 'Vision'
  string:
    startsWith: Vision

```
