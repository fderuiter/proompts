---
title: Foreign Supplier Verification Program (FSVP) Audit
---

# Foreign Supplier Verification Program (FSVP) Audit

Draft a summary report of an onsite audit for a foreign food supplier including conclusions and corrective actions.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/regulatory/food_safety/foreign_supplier_verification_program_fsvp_audit.prompt.yaml)

```yaml
---
name: Foreign Supplier Verification Program (FSVP) Audit
version: 0.1.0
description: Draft a summary report of an onsite audit for a foreign food supplier including conclusions and corrective actions.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - food-safety
  - foreign
  - supplier
  - verification
  - program
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

    21 CFR Part 1 Subpart L


    ## Objective

    Draft a summary report of an onsite audit for a foreign food supplier including conclusions and corrective actions.


    ## Output Format

    Formal audit report in Markdown format.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: Audit procedures, dates, findings on processes, and records of deficiencies. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Cross\-reference

```
