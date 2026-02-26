---
title: Human Factors/Usability Summary
---

# Human Factors/Usability Summary

Summarize usability testing results to demonstrate minimized use-related risks.

[View Source YAML](../../../../prompts/regulatory/adherence/human_factors_usability_summary.prompt.yaml)

```yaml
---
name: Human Factors/Usability Summary
version: 0.1.0
description: Summarize usability testing results to demonstrate minimized use-related risks.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - regulatory-adherence
  - human
  - factors
  - usability
  - summary
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

    FDA HF Guidance


    ## Objective

    Summarize usability testing results to demonstrate minimized use-related risks.


    ## Output Format

    Markdown table or narrative summary.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: Usability test protocols and summative data. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Review

```
