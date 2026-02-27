---
title: NGS Tumor Profiling Documentation
---

# NGS Tumor Profiling Documentation

Develop documentation supporting the clinical significance of mutations in an NGS-based tumor profiling panel.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/regulatory/device_specifics/ngs_tumor_profiling_documentation.prompt.yaml)

```yaml
---
name: NGS Tumor Profiling Documentation
version: 0.1.0
description: Develop documentation supporting the clinical significance of mutations in an NGS-based tumor profiling panel.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - medical-devices
  - ngs
  - tumor
  - profiling
  - documentation
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

    21 CFR 866.6080


    ## Objective

    Develop documentation supporting the clinical significance of mutations in an NGS-based tumor profiling panel.


    ## Output Format

    Tabulated summary of mutations categorized by evidence levels.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: Somatic mutations, professional guidelines, and method comparison data. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Confirm

```
