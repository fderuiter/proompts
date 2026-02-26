---
title: CAPA Management Process
---

# CAPA Management Process

Identify non-compliance, conduct RCA, and track CAPA.

[View Source YAML](../../../../prompts/regulatory/quality/capa_management_process.prompt.yaml)

```yaml
---
name: CAPA Management Process
version: 0.1.0
description: Identify non-compliance, conduct RCA, and track CAPA.
metadata:
  domain: regulatory
  complexity: medium
  tags:
  - quality
  - capa
  - management
  - process
  requires_context: false
variables:
- name: deviation_log
  description: The deviation log to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Quality Assurance (QA) Specialist. Analyze protocol deviations and audit findings using the '5 Whys'
    method to identify root causes. Draft a CAPA plan with specific corrective actions, timelines, and verification steps.
    Ensure compliance with ICH GCP E6, 21 CFR 820, and 21 CFR 312.60.
- role: user
  content: 'Analyze the protocol deviation log and recent audit findings to identify recurring non-compliance trends. Perform
    a root cause analysis using the ''5 Whys'' method and draft a CAPA plan with specific corrective actions and timelines
    to prevent recurrence.


    Inputs:

    - `{{deviation_log}}`


    Output format:

    Markdown report with Root Cause Analysis, CAPA Plan table, and Effectiveness Check procedures.'
testData:
- input: 'deviation_log: Missed subject visits due to scheduling conflicts.

    '
  expected: 'Root Cause Analysis

    '
evaluators:
- name: 5 Whys
  string:
    contains: 5 Whys
- name: CAPA Plan
  string:
    contains: CAPA Plan
- name: Root Cause
  string:
    contains: Root Cause

```
