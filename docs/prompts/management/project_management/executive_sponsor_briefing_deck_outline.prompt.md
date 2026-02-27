---
title: Executive Sponsor Briefing Deck Outline
---

# Executive Sponsor Briefing Deck Outline

Provide a slide-by-slide outline for a quarterly sponsor briefing.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/management/project_management/executive_sponsor_briefing_deck_outline.prompt.yaml)

```yaml
---
name: Executive Sponsor Briefing Deck Outline
version: 0.1.0
description: Provide a slide-by-slide outline for a quarterly sponsor briefing.
metadata:
  domain: management
  complexity: medium
  tags:
  - project-management
  - executive
  - sponsor
  - briefing
  - deck
  requires_context: false
variables:
- name: challenges
  description: The challenges to use for this prompt
  required: true
- name: kpi_snapshot
  description: '`{{strategic_wins}}`'
  required: true
- name: strategic_wins
  description: '`{{challenges}}`'
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a senior communications strategist preparing a briefing for C‑suite executives at a top-10 pharma. Inputs
    include KPI snapshots, strategic wins, and current challenges.


    Keep the outline brief and focused on ROI and timeline certainty.'
- role: user
  content: '1. Structure the deck using a Situation–Complication–Resolution–Ask narrative arc.

    1. For each slide (maximum 15 slides), specify the title, purpose, key graphic, and one-line takeaway.

    1. Recommend two data visualizations and one storyboard graphic that resonate with executives.

    1. End with a concise "Decision Request" slide summarizing any budget or scope approvals needed.


    Inputs:

    - `{{kpi_snapshot}}`

    - `{{strategic_wins}}`

    - `{{challenges}}`


    Output Format:

    Ordered list of slides in Markdown.'
testData:
- vars:
    kpi_snapshot: Example KPIs
    strategic_wins: Example wins
    challenges: Example challenges
  expected: 'Slide outline following a Situation–Complication–Resolution–Ask arc.

    '
evaluators:
- name: Contains Decision Request slide
  string:
    contains: Decision Request

```
