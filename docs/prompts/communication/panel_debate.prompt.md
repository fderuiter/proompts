---
title: Panel Debate
---

# Panel Debate

Host a simulated debate among three experts on a chosen topic.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/communication/panel_debate.prompt.yaml)

```yaml
---
name: Panel Debate
version: 0.1.0
description: Host a simulated debate among three experts on a chosen topic.
metadata:
  domain: communication
  complexity: low
  tags:
  - panel
  - debate
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
  content: 'Participants are [Proponent], [Opponent], and a neutral Moderator. The user supplies the topic.


    <!-- markdownlint-disable MD002 MD022 MD041 MD029 -->


    1. Each expert delivers an opening statement (≤ 60 words each).

    2. Run two rebuttal rounds (≤ 40 words per speaker per round).

    3. After debates, the Moderator provides a table summarizing consensus and disputes. Columns: *Point* and *Agreement?*
    (Yes/No).

    4. End with a 100-word balanced takeaway including one actionable recommendation.


    Label each section clearly and use plain language.


    Keep responses concise and avoid bias.'
- role: user
  content: '{{input}}'
testData:
- input: Remote work
  expected: 'Proponent: boosts flexibility.

    Opponent: lowers team cohesion.

    Moderator: notes key points.

    Rebuttal round 1...

    Rebuttal round 2...

    Moderator Table:

    Point | Agreement?

    Flex time | Yes

    Takeaway: balance office days with remote options.'
evaluators:
- name: Output references moderator
  string:
    contains: Moderator

```
