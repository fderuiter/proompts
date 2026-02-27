---
title: Cyber Device Security Plan
---

# Cyber Device Security Plan

Draft a postmarket cybersecurity plan and Software Bill of Materials (SBOM).

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/regulatory/compliance/cyber_device_security_plan.prompt.yaml)

```yaml
---
name: Cyber Device Security Plan
version: 0.1.0
description: Draft a postmarket cybersecurity plan and Software Bill of Materials (SBOM).
metadata:
  domain: regulatory
  complexity: low
  tags:
  - compliance
  - cyber
  - device
  - security
  - plan
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

    FD&C Act 524B


    ## Objective

    Draft a postmarket cybersecurity plan and Software Bill of Materials (SBOM).


    ## Output Format

    Technical documentation for eSTAR.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: Software architecture and list of components. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Check

```
