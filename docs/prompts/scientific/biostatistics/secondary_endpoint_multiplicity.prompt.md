---
title: Secondary Endpoint Multiplicity Adjuster
---

# Secondary Endpoint Multiplicity Adjuster

Apply Bonferroni-Holm (step-down) procedure to secondary efficacy endpoints.

[View Source YAML](../../../../prompts/scientific/biostatistics/secondary_endpoint_multiplicity.prompt.yaml)

```yaml
---
name: Secondary Endpoint Multiplicity Adjuster
version: 0.1.0
description: Apply Bonferroni-Holm (step-down) procedure to secondary efficacy endpoints.
metadata:
  domain: scientific
  complexity: medium
  tags:
  - biostatistics
  - secondary
  - endpoint
  - multiplicity
  - adjuster
  requires_context: false
variables:
- name: endpoints
  description: The endpoints to use for this prompt
  required: true
- name: p_values
  description: The p values to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.1
messages:
- role: system
  content: "You are a Biostatistician and Regulatory Affairs Specialist. Your task is to calculate adjusted p-values using\
    \ the Bonferroni-Holm (step-down) procedure for a family of secondary efficacy endpoints.\n\nFollow these steps and format\
    \ the output as a Markdown report:\n1.  **## Order:** Arrange the raw p-values from smallest to largest.\n2.  **## Calculate:**\
    \ Apply the Holm step-down correction:\n    *   Adjusted p-value = min(1, (k - rank + 1) * raw_p), where k is the number\
    \ of endpoints.\n    *   Ensure monotonicity (adjusted p-values cannot decrease as rank increases).\n3.  **## Conclusion:**\
    \ State which endpoints are statistically significant at a family-wise alpha of 0.05 per ICH E9 (R1) standards.\n"
- role: user
  content: '<secondary_endpoints>

    {{endpoints}}

    </secondary_endpoints>


    <raw_p_values>

    {{p_values}} (Corresponding to endpoints)

    </raw_p_values>


    Generate the adjustment report.

    '
testData:
- input: 'endpoints: Fatigue, Pain, Sleep Quality

    p_values: 0.002, 0.015, 0.04

    '
  expected: Report showing ordered p-values, adjusted calculation, and conclusion on significance at 0.05 level.
evaluators:
- name: Calculation Check
  regex:
    pattern: (?i)(step-down|Holm)
- name: Significance Check
  regex:
    pattern: (?i)(significant|reject)

```
