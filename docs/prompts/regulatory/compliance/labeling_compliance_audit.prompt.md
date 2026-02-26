---
title: Labeling Compliance Audit
---

# Labeling Compliance Audit

Audit device labeling for compliance with mandatory elements (Manufacturer, UDI, date formats).

[View Source YAML](../../../../prompts/regulatory/compliance/labeling_compliance_audit.prompt.yaml)

```yaml
---
name: Labeling Compliance Audit
version: 0.1.0
description: Audit device labeling for compliance with mandatory elements (Manufacturer, UDI, date formats).
metadata:
  domain: regulatory
  complexity: low
  tags:
  - compliance
  - labeling
  - audit
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

    21 CFR Part 801


    ## Objective

    Audit device labeling for compliance with mandatory elements (Manufacturer, UDI, date formats).


    ## Output Format

    Gap analysis report.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: Product labels, symbols glossary, and 21 CFR 801 text. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Inspect

```
