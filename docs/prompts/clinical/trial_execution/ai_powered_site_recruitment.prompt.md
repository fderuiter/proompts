---
title: AI-Powered Site and Recruitment Strategy
---

# AI-Powered Site and Recruitment Strategy

Select optimal sites and anticipate dropout risks using simulated EHR insights.

[View Source YAML](../../../../prompts/clinical/trial_execution/ai_powered_site_recruitment.prompt.yaml)

```yaml
---
name: AI-Powered Site and Recruitment Strategy
version: 0.1.0
description: Select optimal sites and anticipate dropout risks using simulated EHR insights.
metadata:
  domain: clinical
  complexity: medium
  tags:
  - trial-execution
  - ai-powered
  - site
  - recruitment
  - strategy
  requires_context: false
variables:
- name: criteria
  description: inclusion and exclusion criteria
  required: true
- name: target_enrollment
  description: desired participant count
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a strategic enrollment planner experienced with EHR databases and predictive AI tools. Provided with inclusion
    and exclusion criteria and the target enrollment size, use simulated data to prioritise potential sites and plan mitigations.


    Use transparent assumptions when estimating projections.'
- role: user
  content: '1. Rank the top five potential sites by predicted enrollment speed and retention probability.

    2. Identify common patient dropout reasons.

    3. Propose mitigation strategies for each risk.


    Inputs:

    - `{{criteria}}` – inclusion and exclusion criteria

    - `{{target_enrollment}}` – desired participant count


    Output Format:

    Markdown sections:


    - **Site Ranking Table** – site, enrollment projection, retention rate

    - **Dropout Risks** – list with explanations

    - **Mitigation Plan** – bullet points per risk'
testData:
- input: 'criteria: age 18-65

    target_enrollment: 200

    '
  expected: 'Site Ranking Table

    '
evaluators:
- name: Lists mitigation strategies
  string:
    contains: Mitigation Plan

```
