---
title: Budget Variance Analysis
---

# Budget Variance Analysis

Identify top variances in a budget-to-actuals report and draft explanations for the Board.

[View Source YAML](../../../../prompts/business/cfo/variance_analysis.prompt.yaml)

```yaml
---
name: Budget Variance Analysis
version: 0.1.0
description: Identify top variances in a budget-to-actuals report and draft explanations for the Board.
metadata:
  domain: business
  complexity: medium
  tags:
  - finance
  - budget
  - variance
  - analysis
  requires_context: true
variables:
- name: report
  description: '`{{report}}`'
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
  content: 'Analyze the attached Q3 budget-to-actuals report. Identify the top 3 variances that had the largest negative impact
    on Net Income. For each variance, draft a 3-sentence explanation suitable for a Board of Directors deck that attributes
    the variance to either specific volume, rate, or mix changes. Avoid jargon; focus on operational drivers.


    Report:

    `{{report}}`'
testData:
- input: "report: |-\n  Item,Budget,Actual,Variance\n  Revenue,10M,9.5M,-0.5M\n  COGS,4M,4.2M,+0.2M\n  OpEx,3M,2.8M,-0.2M\n\
    \  Net Income,3M,2.5M,-0.5M"
  expected: Variance Explanation
evaluators:
- name: Output should contain variance explanations
  regex:
    pattern: (?i)variance

```
