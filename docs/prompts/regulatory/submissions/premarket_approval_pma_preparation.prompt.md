---
title: Premarket Approval (PMA) Preparation
---

# Premarket Approval (PMA) Preparation

Draft a detailed summary of a PMA application, including clinical investigation results and manufacturing history.

[View Source YAML](../../../../prompts/regulatory/submissions/premarket_approval_pma_preparation.prompt.yaml)

```yaml
---
name: Premarket Approval (PMA) Preparation
version: 0.1.0
description: Draft a detailed summary of a PMA application, including clinical investigation results and manufacturing history.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - submissions
  - premarket
  - approval
  - pma
  - preparation
  requires_context: false
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

    21 CFR Part 814


    ## Objective

    Draft a detailed summary of a PMA application, including clinical investigation results and manufacturing history.


    ## Output Format

    Formal structured summary as per 21 CFR 814.20(b)(3).'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: Clinical results, nonclinical lab data, device characteristics, and marketing history. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Review

```
