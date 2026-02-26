---
title: Post-Market Safety Signal Trending
---

# Post-Market Safety Signal Trending

Analyze post-market data to identify emerging safety signals.

[View Source YAML](../../../../../prompts/clinical/safety/clinical_safety_workflow/03_post_market_safety_signal_trending.prompt.yaml)

```yaml
---
name: Post-Market Safety Signal Trending
version: 0.1.0
description: Analyze post-market data to identify emerging safety signals.
metadata:
  domain: clinical
  complexity: low
  tags:
  - safety
  - post-market
  - signal
  - trending
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
  content: 'You are a safety analyst reviewing post-market surveillance data to trend and

    surface emerging safety signals.

    '
- role: user
  content: '{{input}}'
testData:
- input: 'Complaints of rash increased from 2 to 8 between Q1 and Q2 2024.

    '
  expected: 'Post-Market Safety Signal Trending: Rash complaints increased fourfold from Q1 to Q2 2024.'
evaluators:
- name: Output starts with 'Post-Market Safety Signal Trending'
  string:
    startsWith: Post-Market Safety Signal Trending

```
