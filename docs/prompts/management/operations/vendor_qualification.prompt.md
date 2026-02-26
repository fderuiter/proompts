---
title: Vendor Qualification and Oversight
---

# Vendor Qualification and Oversight

Develop Vendor Oversight Plan and KPIs.

[View Source YAML](../../../../prompts/management/operations/vendor_qualification.prompt.yaml)

```yaml
---
name: Vendor Qualification and Oversight
version: 0.1.0
description: Develop Vendor Oversight Plan and KPIs.
metadata:
  domain: management
  complexity: low
  tags:
  - operations
  - vendor
  - qualification
  - oversight
  requires_context: false
variables:
- name: vendor_details
  description: The vendor details to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Vendor Manager. Develop a Vendor Oversight Plan for a CRO managing monitoring services, including five
    key performance indicators for quality tracking and a review of the transfer of sponsor obligations.
- role: user
  content: 'Develop a Vendor Oversight Plan for a CRO managing monitoring services, including five key performance indicators
    for quality tracking and a review of the transfer of sponsor obligations.


    Inputs:

    - `{{vendor_details}}`


    Output format:

    Markdown Vendor Oversight Plan.'
testData:
- input: 'vendor_details: CRO providing monitoring services.

    '
  expected: 'Vendor Oversight Plan

    '
evaluators:
- name: Key Performance Indicators
  string:
    contains: Key Performance Indicators
- name: Transfer of Obligations
  string:
    contains: Transfer of Obligations

```
