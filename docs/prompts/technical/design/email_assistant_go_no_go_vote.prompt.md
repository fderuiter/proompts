---
title: AI Email Assistant Go/No-Go Vote
---

# AI Email Assistant Go/No-Go Vote

Personas: UX designer, data scientist, CFO. Objective: decide whether to move forward with the prototype AI email assistant.


[View Source YAML](../../../../prompts/technical/design/email_assistant_go_no_go_vote.prompt.yaml)

```yaml
---
name: AI Email Assistant Go/No-Go Vote
version: 0.1.0
description: 'Personas: UX designer, data scientist, CFO. Objective: decide whether to move forward with the prototype AI
  email assistant.

  '
metadata:
  domain: technical
  complexity: low
  tags:
  - design
  - email
  - assistant
  - no-go
  - vote
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
  content: 'Personas: UX designer, data scientist, CFO.

    Objective: decide whether to move forward with the prototype AI email assistant.

    '
- role: user
  content: '{{input}}

    '
testData:
- input: "Prototype feedback:\n  - UX designer impressed with usability.\n  - Data scientist concerned about privacy.\n  -\
    \ CFO notes high projected costs.\nShould we proceed with development?\n"
  expected: 'Summary of each persona''s vote and final Go or No-Go recommendation.

    '
evaluators:
- name: Mentions a Go or No-Go decision
  string:
    contains: Go

```
