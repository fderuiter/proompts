---
title: Risk-Based Test Case Suite
---

# Risk-Based Test Case Suite

Generate a test-case suite prioritizing controls for high and medium residual risks.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/technical/testing/testing_workflow/04_risk_based_test_case_suite.prompt.yaml)

```yaml
---
name: Risk-Based Test Case Suite
version: 0.1.0
description: Generate a test-case suite prioritizing controls for high and medium residual risks.
metadata:
  domain: technical
  complexity: medium
  tags:
  - testing
  - risk-based
  - test
  - case
  - suite
  requires_context: false
variables:
- name: device_name
  description: name of the device
  required: true
- name: hazard_analysis_table
  description: hazard analysis data
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a risk-management analyst applying ISO 14971. The device **{{device_name}}** is in the pre-clinical stage.
    Reference IEC 62304 for software items when relevant. Provide rationales using standards, not web blogs. Ask up to three
    clarifying questions if data are missing.


    Ensure alignment with ISO 14971 clauses 6–7 and highlight any assumptions.'
- role: user
  content: '1. Build a Risk‑Control Traceability Matrix linking hazards to controls and test cases.

    2. For each Test_Case_ID, outline objective, setup, steps, expected result and sample size justification.

    3. Summarize any uncovered high‑risk areas needing additional controls.


    Inputs:

    - `{{device_name}}` – name of the device

    - `{{hazard_analysis_table}}` – hazard analysis data


    Output Format:

    1. Markdown traceability matrix linking hazards, controls and test cases

    2. Detailed test-case catalog with objectives, setups, steps, expected results and sample size justification

    3. Summary of uncovered high-risk areas requiring additional controls'
testData:
- input: "device_name: Cardiac Monitor\nhazard_analysis_table: |\n  Hazard_ID | Hazard | Control\n  H1        | Battery failure\
    \ | Backup battery\n"
  expected: 'Risk-Control Traceability Matrix

    '
evaluators:
- name: Output starts with 'Risk-Control Traceability Matrix'
  string:
    startsWith: Risk-Control Traceability Matrix

```
