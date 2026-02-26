---
title: M&A Target Evaluation
---

# M&A Target Evaluation

Evaluate a potential acquisition target based on financial statements.

[View Source YAML](../../../../prompts/business/cfo/ma_target_evaluation.prompt.yaml)

```yaml
---
name: M&A Target Evaluation
version: 0.1.0
description: Evaluate a potential acquisition target based on financial statements.
metadata:
  domain: business
  complexity: medium
  tags:
  - finance
  - target
  - evaluation
  requires_context: false
variables:
- name: financial_statements
  description: The financial statements to use for this prompt
  required: true
- name: target_description
  description: A description of the subject
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: Act as an investment banker advising a CFO. We are evaluating a potential acquisition of `{{target_description}}`.
- role: user
  content: 'Based on their attached financial statements for the last 3 years:

    1. Calculate their CAGR for Revenue and EBITDA.

    2. Flag any anomalies in their Working Capital trends (e.g., sudden spikes in DSOs or DPOs).

    3. List 5 distinct due diligence questions I should ask their CFO regarding their quality of earnings.


    Financial Statements:

    `{{financial_statements}}`'
testData:
- input: "target_description: a SaaS provider in the healthcare space\nfinancial_statements: |-\n  Year 1: Revenue 5M, EBITDA\
    \ 1M\n  Year 2: Revenue 6M, EBITDA 1.2M\n  Year 3: Revenue 7.5M, EBITDA 1.8M"
  expected: M&A Analysis
evaluators:
- name: Output should contain CAGR calculation
  regex:
    pattern: (?i)CAGR

```
