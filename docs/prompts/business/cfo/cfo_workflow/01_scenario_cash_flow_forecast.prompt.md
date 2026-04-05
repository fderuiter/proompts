---
title: Scenario-Based Clinical-Trial Cash-Flow Forecast
---

# Scenario-Based Clinical-Trial Cash-Flow Forecast

Model 12-quarter cash flows under baseline, inflation, and recruitment slowdown scenarios.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/business/cfo/cfo_workflow/01_scenario_cash_flow_forecast.prompt.yaml)

```yaml
name: Scenario-Based Clinical-Trial Cash-Flow Forecast
version: 0.1.0
description: Model 12-quarter cash flows under baseline, inflation, and recruitment
  slowdown scenarios.
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
  content: "You are my senior FP&A analyst inside a mid-size global CRO. Rising Phase\
    \ II/III costs and client delays are compressing margins. I need a 12-quarter\
    \ cash-flow forecast under three scenarios (Base, +15% cost inflation, \u2013\
    20% patient-recruitment pace)."
- role: user
  content: "Start the response with **Scenario Forecast -**.\n\nOutput format:\n\n\
    1. Markdown table showing Base, Inflation, and Slow-Recruitment scenarios for\
    \ 12 quarters with net and ending cash.\n\n2. Two bullet-point insights on liquidity\
    \ risks or funding needs.\n\nInputs:\n\n- <base_revenue>{{base_revenue}}</base_revenue>\
    \ \u2013 baseline quarterly revenue (USD).\n- <base_costs>{{base_costs}}</base_costs>\
    \ \u2013 baseline quarterly costs (USD).\n- <starting_cash>{{starting_cash}}</starting_cash>\
    \ \u2013 cash on hand at start (USD).\n- <notes>{{notes}}</notes> \u2013 assumptions\
    \ or upcoming events.\n"
testData:
- base_revenue: '20000000'
  base_costs: '15000000'
  starting_cash: '50000000'
  notes: none
  expected: Scenario Forecast -
evaluators:
- name: Output should start with 'Scenario Forecast -'
  string:
    startsWith: Scenario Forecast -

```
