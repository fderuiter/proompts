---
title: AI Risk Mapper
---

# AI Risk Mapper

Create a quick-look risk register for a specified AI system.

[View Source YAML](../../../../prompts/regulatory/strategy/ai_risk_mapper.prompt.yaml)

```yaml
---
name: AI Risk Mapper
version: 0.1.0
description: Create a quick-look risk register for a specified AI system.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - regulatory-strategy
  - risk
  - mapper
  requires_context: false
variables:
- name: AI_SYSTEM
  description: the system being assessed
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'Regulatory frameworks such as the EU AI Act and NIST AI RMF guide responsible AI deployment.


    1. List up to six key risks, each no more than 12 words.

    2. Provide a table with columns *Risk*, *Likelihood H/M/L*, *Impact H/M/L*, and *Mitigation* (≤ 15 words).

    3. Conclude with a 25-word compliance note referencing the EU AI Act and NIST AI RMF.

    4. Keep total response under 150 words.


    Focus on brevity and clarity.


    References: Reuters, Osano'
- role: user
  content: '- `{{AI_SYSTEM}}` — the system being assessed.


    Output format: Markdown list, table, and concluding note.'
testData: []
evaluators: []

```
