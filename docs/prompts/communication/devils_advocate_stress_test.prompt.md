---
title: Devil’s-Advocate Stress Test
---

# Devil’s-Advocate Stress Test

Act as a seasoned critic.

[View Source YAML](../../../prompts/communication/devils_advocate_stress_test.prompt.yaml)

```yaml
---
name: Devil’s-Advocate Stress Test
version: 0.1.0
description: Act as a seasoned critic.
metadata:
  domain: communication
  complexity: low
  tags:
  - devil
  - s-advocate
  - stress
  - test
  requires_context: false
variables:
- name: input
  description: The primary input or query text for the prompt
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: '1. Present the three strongest arguments against this idea: ‹DESCRIBE IDEA›.

    2. For each objection, cite a real or hypothetical example that illustrates the risk.

    3. Then propose one mitigation strategy per objection.'
- role: user
  content: '{{input}}'
testData:
- input: Launch a new social app
  expected: 'Objection 1: crowded market; Example: many apps fail.

    Mitigation: offer unique community.

    Objection 2: privacy risk; Example: data leaks.

    Mitigation: strong encryption.

    Objection 3: low retention; Example: early churn.

    Mitigation: gamified rewards.'
evaluators:
- name: Output lists mitigations
  string:
    contains: Mitigation

```
