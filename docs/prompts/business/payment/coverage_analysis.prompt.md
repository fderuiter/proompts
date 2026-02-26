---
title: Medicare Coverage Analysis
---

# Medicare Coverage Analysis

Determine qualifying status and billing justification.

[View Source YAML](../../../../prompts/business/payment/coverage_analysis.prompt.yaml)

```yaml
---
name: Medicare Coverage Analysis
version: 0.1.0
description: Determine qualifying status and billing justification.
metadata:
  domain: business
  complexity: low
  tags:
  - payment
  - medicare
  - coverage
  - analysis
  requires_context: false
variables:
- name: schedule_of_events
  description: The schedule of events to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Reimbursement Analyst. Compare the study protocol's schedule of events with Medicare routine care guidelines
    to determine which labs should be billed to the research account vs. patient insurance. Adhere to Medicare NCD 310.1.
- role: user
  content: 'Compare the study protocol''s schedule of events with Medicare routine care guidelines to determine which labs
    should be billed to the research account vs. patient insurance.


    Inputs:

    - `{{schedule_of_events}}`


    Output format:

    Markdown Coverage Analysis Matrix.'
testData:
- input: 'schedule_of_events: Routine CBC and Chemistry.

    '
  expected: 'Coverage Analysis

    '
evaluators:
- name: Billing Justification
  string:
    contains: Billing Justification
- name: Medicare Guidelines
  string:
    contains: Medicare Guidelines

```
