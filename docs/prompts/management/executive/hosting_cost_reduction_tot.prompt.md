---
title: Hosting Cost Reduction ToT Plan
---

# Hosting Cost Reduction ToT Plan

Develop a tree-of-thought plan to reduce hosting costs.

[View Source YAML](../../../../prompts/management/executive/hosting_cost_reduction_tot.prompt.yaml)

```yaml
---
name: Hosting Cost Reduction ToT Plan
version: 0.1.0
description: Develop a tree-of-thought plan to reduce hosting costs.
metadata:
  domain: management
  complexity: low
  tags:
  - executive
  - hosting
  - cost
  - reduction
  - plan
  requires_context: false
variables:
- name: input
  description: The primary input or query text for the prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a cost-optimization strategist using structured tree-of-thought

    reasoning to reduce hosting expenses.

    '
- role: user
  content: '{{input}}'
testData:
- input: ''
  expected: ''
evaluators:
- name: Output is non-empty
  string:
    startsWith: ''

```
