---
title: Liquidity Stress Test
---

# Liquidity Stress Test

Run a stress test on cash flow forecast assuming a drop in collections.

[View Source YAML](../../../../prompts/business/cfo/liquidity_stress_test.prompt.yaml)

```yaml
---
name: Liquidity Stress Test
version: 0.1.0
description: Run a stress test on cash flow forecast assuming a drop in collections.
metadata:
  domain: business
  complexity: medium
  tags:
  - finance
  - liquidity
  - stress
  - test
  requires_context: false
variables:
- name: drop_percentage
  description: The drop percentage to use for this prompt
  required: true
- name: forecast
  description: '`{{forecast}}`'
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are the Chief Financial Officer of a mid-cap company. You are pragmatic, data-driven, and focused on value
    creation.

    * **Communication Style:** Concise (BLUF - Bottom Line Up Front), professional, and risk-aware but not risk-averse.

    * **Priority:** Always prioritize cash flow and ROI in your recommendations.

    * **Formatting:** Use bullet points and bold text for key metrics to make your responses scannable.'
- role: user
  content: 'Review the attached cash flow forecast. Run a ''Stress Test'' assuming a sudden `{{drop_percentage}}` drop in
    collections next month due to a macroeconomic downturn.

    * **Output:** Calculate our resulting runway in months.

    * **Action Plan:** Suggest 5 immediate liquidity preservation levers we could pull (e.g., delaying capex, stretching payables),
    ranked by speed of implementation vs. negative impact on operations.


    Forecast:

    `{{forecast}}`'
testData:
- input: "drop_percentage: 20%\nforecast: |-\n  Month 1: Inflow 1M, Outflow 0.8M, Cash 2M\n  Month 2: Inflow 1M, Outflow 0.8M,\
    \ Cash 2.2M"
  expected: Stress Test Analysis
evaluators:
- name: Output should contain runway calculation
  regex:
    pattern: (?i)runway

```
