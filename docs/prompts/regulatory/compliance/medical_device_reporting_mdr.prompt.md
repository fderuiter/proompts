---
title: Medical Device Reporting (MDR)
---

# Medical Device Reporting (MDR)

Summarize an adverse event for mandatory electronic submission or develop an MDR SOP.

[View Source YAML](../../../../prompts/regulatory/compliance/medical_device_reporting_mdr.prompt.yaml)

```yaml
---
name: Medical Device Reporting (MDR)
version: 0.1.0
description: Summarize an adverse event for mandatory electronic submission or develop an MDR SOP.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - compliance
  - medical
  - device
  - reporting
  - mdr
  requires_context: true
variables:
- name: input
  description: The primary input or query text for the prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.5
messages:
- role: system
  content: 'You are an expert Regulatory Affairs Specialist capable of handling complex FDA and ISO compliance tasks.


    ## Context

    21 CFR Part 803


    ## Objective

    Summarize an adverse event for mandatory electronic submission or develop an MDR SOP.


    ## Output Format

    Structured summary (eMDR) or numbered SOP document.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: Incident reports, outcome data, and device identification. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Review

```
