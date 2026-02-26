---
title: Generate an Executive Summary for the Final Report
---

# Generate an Executive Summary for the Final Report

Write a concise executive summary of a non-clinical study report.

[View Source YAML](../../../../../prompts/management/study_director/study_director_workflow/03_executive_summary_final_report.prompt.yaml)

```yaml
---
name: Generate an Executive Summary for the Final Report
version: 0.1.0
description: Write a concise executive summary of a non-clinical study report.
metadata:
  domain: management
  complexity: medium
  tags:
  - study-director
  - generate
  - executive
  - summary
  - final
  requires_context: true
variables:
- name: report_sections
  description: draft CTD modules and tables
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a regulatory medical writer specializing in CTD submissions. Input includes draft report sections (Modules 4.2.3
    and 4.2.5) plus statistical tables for Study DEF.


    Keep the summary under 800 words and follow the CTD heading hierarchy. Plan internally and reveal only the finished summary.'
- role: user
  content: '1. Succinctly describe study design, methodology, and key findings.

    2. State the NOAEL and justify it with reference to dose‑response data.

    3. Highlight deviations and explain how they were resolved.

    4. Provide a bullet list supporting the proposed first-in-human dose with links to ICH M3(R2) expectations.

    5. End with a four-item checklist the Study Director must sign.


    Inputs:

    - `{{report_sections}}` – draft CTD modules and tables


    Output Format:

    1. Two-page summary in formal language aligned with CTD headings

    2. Final four-item sign-off checklist for the Study Director'
testData:
- input: "report_sections: |\n  Module 4.2.3: Study design and dose levels\n  Module 4.2.5: Results and discussion\n"
  expected: 'NOAEL: 50 mg/kg

    Checklist:

    - Sign protocol

    - Review deviations

    - Confirm NOAEL

    - Approve submission

    '
evaluators:
- name: Mentions NOAEL
  string:
    contains: NOAEL

```
