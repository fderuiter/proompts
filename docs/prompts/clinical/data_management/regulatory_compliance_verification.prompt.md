---
title: Regulatory Compliance Verification
---

# Regulatory Compliance Verification

Verify electronic records and signatures against 21 CFR Part 11.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/data_management/regulatory_compliance_verification.prompt.yaml)

```yaml
---
name: Regulatory Compliance Verification
version: 0.1.0
description: Verify electronic records and signatures against 21 CFR Part 11.
metadata:
  domain: clinical
  complexity: medium
  tags:
  - data-management
  - regulatory
  - compliance
  - verification
  requires_context: false
variables:
- name: audit_logs
  description: The audit logs to use for this prompt
  required: true
- name: system_specs
  description: 'Audit Trail Logs (sample): `{{audit_logs}}`'
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Regulatory Compliance Officer. Ensure electronic records and signatures comply with requirements for
    technical and procedural controls. Focus on 21 CFR Part 11.
- role: user
  content: 'Analyze the system specifications and verify if the audit trail captures the printed name of the signer, the timestamp,
    and the meaning of the signature as required by 21 CFR Part 11.


    Inputs:

    - System Specifications: `{{system_specs}}`

    - Audit Trail Logs (sample): `{{audit_logs}}`


    Output format:

    Markdown Compliance Verification Checklist.'
testData:
- input: 'system_specs: "Signatures include name and date."

    audit_logs: "Signed by John Doe at 2023-01-01."

    '
  expected: 'Compliance Verification Checklist

    '
evaluators:
- name: Printed Name Check
  string:
    contains: Printed Name
- name: Timestamp Check
  string:
    contains: Timestamp

```
