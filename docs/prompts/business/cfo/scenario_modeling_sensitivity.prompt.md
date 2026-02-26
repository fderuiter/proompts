---
title: Scenario Modeling & Sensitivity Analysis
---

# Scenario Modeling & Sensitivity Analysis

Create three financial scenarios (Conservative, Base, and Aggressive) based on historical data and market trends.

[View Source YAML](../../../../prompts/business/cfo/scenario_modeling_sensitivity.prompt.yaml)

```yaml
---
name: Scenario Modeling & Sensitivity Analysis
version: 0.1.0
description: Create three financial scenarios (Conservative, Base, and Aggressive) based on historical data and market trends.
metadata:
  domain: business
  complexity: medium
  tags:
  - finance
  - scenario
  - modeling
  - sensitivity
  - analysis
  requires_context: false
variables:
- name: cac
  description: The cac to use for this prompt
  required: true
- name: churn
  description: The churn to use for this prompt
  required: true
- name: decision
  description: The decision to use for this prompt
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
  content: 'I am considering `{{decision}}`. Based on the attached historical financial data and current market trends in
    that region, please create three financial scenarios: Conservative, Base, and Aggressive.

    * **Inputs:** Assume a customer acquisition cost of `{{cac}}` and a churn rate of `{{churn}}`.

    * **Variables:** Vary the revenue growth rate and operational leverage for each scenario.

    * **Output:** A table comparing EBITDA, Net Cash Flow, and Payback Period for each scenario, followed by a summary of
    the biggest risks associated with the Aggressive scenario.'
testData:
- input: 'decision: expanding into the APAC market

    cac: $500

    churn: 5%'
  expected: Scenario Analysis
evaluators:
- name: Output should contain scenario table
  regex:
    pattern: \|.*EBITDA.*\|.*Net Cash Flow.*\|

```
