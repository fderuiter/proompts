---
title: Prompt-Writing Best-Practice Checklist
---

# Prompt-Writing Best-Practice Checklist

Summarize key elements of effective prompt design.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/regulatory/strategy/prompt_best_practices.prompt.yaml)

```yaml
---
name: Prompt-Writing Best-Practice Checklist
version: 0.1.0
description: Summarize key elements of effective prompt design.
metadata:
  domain: regulatory
  complexity: medium
  tags:
  - regulatory-strategy
  - prompt-writing
  - best-practice
  - checklist
  requires_context: true
variables: []
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'Use these tips when crafting regulatory prompts or other instructions for AI assistants.


    Summarize key elements of effective prompt design.'
- role: user
  content: '- **Clear role and expertise** – narrows style and vocabulary.

    - **Rich context placeholders** – `<<< … >>>` signals the user to supply project‑specific data.

    - **Explicit clarifying‑question step** – prevents hallucinations and promotes iterative accuracy.

    - **Structured output instructions** – headings, tables, word limits, risk registers, etc.

    - **Citation request** – encourages verifiable answers.

    - **Concise, actionable deliverables** – aligns with consultant workflows.


    Inputs:

    None.


    Output format:

    N/A – this file is informational.


    Additional notes:

    Adapt these points to fit the specific regulatory context.'
testData: []
evaluators: []

```
