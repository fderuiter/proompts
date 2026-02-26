---
title: Scenario-Based Clinical-Trial Cash-Flow Forecast
---

# Scenario-Based Clinical-Trial Cash-Flow Forecast

Model 12-quarter cash flows under baseline, inflation, and recruitment slowdown scenarios.

[View Source YAML](../../../../../prompts/business/cfo/cfo_workflow/01_scenario_cash_flow_forecast.prompt.yaml)

```yaml
---
name: Scenario-Based Clinical-Trial Cash-Flow Forecast
version: 0.1.0
description: Model 12-quarter cash flows under baseline, inflation, and recruitment slowdown scenarios.
metadata:
  domain: business
  complexity: high
  tags:
  - finance
  - scenario-based
  - clinical-trial
  - cash-flow
  - forecast
  requires_context: false
variables:
- name: base_costs
  description: baseline quarterly costs (USD)
  required: true
- name: base_revenue
  description: baseline quarterly revenue (USD)
  required: true
- name: notes
  description: assumptions or upcoming events
  required: true
- name: starting_cash
  description: cash on hand at start (USD)
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are my senior FP&A analyst inside a mid-size global CRO. Rising Phase II/III costs and client delays are compressing
    margins. I need a 12-quarter cash-flow forecast under three scenarios (Base, +15% cost inflation, –20% patient-recruitment
    pace).
- role: user
  content: '- `{{base_revenue}}` – baseline quarterly revenue (USD).

    - `{{base_costs}}` – baseline quarterly costs (USD).

    - `{{starting_cash}}` – cash on hand at start (USD).

    - `{{notes}}` – assumptions or upcoming events.


    Start the response with **Scenario Forecast -**.

    Output format:

    1. Markdown table showing Base, Inflation, and Slow-Recruitment scenarios for 12 quarters with net and ending cash.

    2. Two bullet-point insights on liquidity risks or funding needs.'
testData:
- input: 'base_revenue: 20000000

    base_costs: 15000000

    starting_cash: 50000000

    notes: none'
  expected: Scenario Forecast -
evaluators:
- name: Output should start with 'Scenario Forecast -'
  string:
    startsWith: Scenario Forecast -

```
