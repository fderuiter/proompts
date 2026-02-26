---
title: Fishbone Facilitator
---

# Fishbone Facilitator

Identify possible root causes of a problem using a fishbone diagram.

[View Source YAML](../../../../prompts/management/operations/fishbone_facilitator.prompt.yaml)

```yaml
---
name: Fishbone Facilitator
version: 0.1.0
description: Identify possible root causes of a problem using a fishbone diagram.
metadata:
  domain: management
  complexity: low
  tags:
  - operations
  - fishbone
  - facilitator
  requires_context: false
variables:
- name: problem
  description: The problem to use for this prompt
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.7
messages:
- role: system
  content: 'Ask for the main effect statement if it is not provided.


    Identify possible root causes of a problem using a fishbone diagram.'
- role: user
  content: '1. Generate a text-based fishbone with six categories: Methods, Machines, People, Materials, Environment and Measurement.

    1. Under each category, list two concise possible causes.

    1. End with a 30-word note on which cause to probe first and why.


    Inputs:

    - `{{problem}}`: main effect statement describing the problem.


    Output format:

    Bullet list or table representing the fishbone followed by the investigation note.


    Additional notes:

    Limit the entire reply to 120 words.'
testData:
- vars:
    problem: production line downtime
  expected: "- Methods:\n  - ...\n- Machines:\n  - ..."
evaluators:
- name: Mentions Methods category
  string:
    contains: Methods

```
