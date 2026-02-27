---
title: To-Do List Template
---

# To-Do List Template

Track pending and completed development tasks.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/technical/software_engineering/lifecycle/todo_generation.prompt.yaml)

```yaml
---
name: To-Do List Template
version: 0.1.0
description: Track pending and completed development tasks.
metadata:
  domain: technical
  complexity: low
  tags:
  - software-engineering
  - sdlc
  - to-do
  - list
  - template
  requires_context: false
variables: []
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'Use this list to manage work derived from the technical implementation plan.


    Update frequently to reflect current project priorities.'
- role: user
  content: '1. Maintain an up-to-date list of actionable tasks.

    1. Record completed tasks separately.

    1. Keep descriptions short and clear for efficient AI execution.

    Inputs:

    None

    Output format:

    Markdown checklist under **To-Do** and **Completed Tasks** sections.'
testData:
- vars: {}
  expected: Markdown checklist under **To-Do** and **Completed Tasks** sections.
evaluators:
- name: Output starts with 'To-Do'
  string:
    startsWith: To-Do

```
