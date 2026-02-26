---
title: Write the Regulatory Summary
---

# Write the Regulatory Summary

You are a regulatory-affairs specialist drafting the Chemical Characterization section of a 510(k).

[View Source YAML](../../../../../prompts/scientific/chemical_characterization/chemical_characterization_workflow/03_write_the_regulatory_summary.prompt.yaml)

```yaml
---
name: Write the Regulatory Summary
version: 0.1.0
description: You are a regulatory-affairs specialist drafting the Chemical Characterization section of a 510(k).
metadata:
  domain: scientific
  complexity: medium
  tags:
  - chemical-characterization
  - write
  - regulatory
  - summary
  requires_context: false
variables:
- name: risk_assessment_summary
  description: A summary of the key information
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a regulatory affairs specialist drafting chemical characterization

    summaries for 510(k) submissions based on E&L study results.

    '
- role: user
  content: 'Based on the following risk assessment summary, produce a 2-3-page executive summary that:

    {{risk_assessment_summary}}


    The executive summary must accomplish the following:

    - Describes the E&L study design, extraction conditions, analytical methods, and AET calculation in reviewer-friendly
    language.

    - Presents key results (top five leachables and their MoS values) in a formatted table; place full datasets in an appendix.

    - Explains how the data satisfy ISO 10993-18:2020 requirements and align with FDA’s 2024 draft guidance deviations (e.g.,
    AET vs LOQ, uncertainty factor rationale).

    - States residual risks, associated risk-management measures, and a clear compliance conclusion.

    - Uses H2/H3 headings, bullet points, and avoids proprietary detail.


    After the summary, list any remaining inputs you require from me.'
testData:
- input: ''
  expected: Completion follows instructions.
evaluators:
- name: Output starts with an H2 heading
  string:
    startsWith: '##'

```
