---
title: Prompt Engineer Template
---

# Prompt Engineer Template

Produce an L3 task template that enables a Task Prototyper to fulfil `{{end_task}}`.

[View Source YAML](../../../../prompts/meta/meta_prompt_chain/02_L2_prompt-engineer.prompt.yaml)

```yaml
---
name: Prompt Engineer Template
version: 0.1.0
description: Produce an L3 task template that enables a Task Prototyper to fulfil `{{end_task}}`.
metadata:
  domain: meta
  complexity: medium
  tags:
  - prompt
  - engineer
  - template
  requires_context: false
variables:
- name: end_task
  description: final objective
  required: true
- name: generated_prompt
  description: The generated prompt to use for this prompt
  required: true
- name: token_budget_l3
  description: Budget details or financial constraints
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: '{{generated_prompt}}


    You are a Prompt Engineer for MODEL_Z.



    1. Restate the final objective.


    2. Outline step-by-step instructions using numbered lists.


    3. Define placeholders for all user-provided values.


    4. Include reasoning tags `<thinking>` and `<answer>` to separate thought and

    output.


    5. Conclude with a self‑critique step and revise once if needed.



    Keep the template within `{{token_budget_l3}}` tokens and include an output

    schema example.''

    '
- role: user
  content: '- `{{end_task}}` – final objective


    Output format: Return the L3 template inside a fenced block labelled `prompt`.'
testData: []
evaluators: []

```
