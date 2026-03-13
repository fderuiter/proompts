---
title: Supplier Quality Evaluation and SQA Architect
---

# Supplier Quality Evaluation and SQA Architect

Synthesizes supplier capability data, ISO certifications, and risk profiles to generate a comprehensive Supplier Quality Agreement (SQA) and evaluation report.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/regulatory/quality/supplier_quality_agreement_architect.prompt.yaml)

```yaml
---
name: Supplier Quality Evaluation and SQA Architect
version: 1.0.0
description: Synthesizes supplier capability data, ISO certifications, and risk profiles to generate a comprehensive Supplier Quality Agreement (SQA) and evaluation report.
metadata:
  domain: regulatory
  complexity: high
  tags:
  - quality
  - supplier
  - sqa
  - audit
  - onboarding
  requires_context: false
variables:
- name: supplier_type
  description: The category of the supplier (e.g., Contract Manufacturer, Critical Component Supplier, Service Provider).
  required: true
- name: supplied_materials
  description: A detailed list of materials, components, or services provided by the supplier.
  required: true
- name: iso_certifications
  description: A list of the supplier's active quality system certifications (e.g., ISO 13485:2016, ISO 9001:2015).
  required: true
- name: risk_level
  description: The identified risk level associated with the supplier (e.g., High, Medium, Low).
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.1
messages:
- role: system
  content: Act as a Principal Supplier Quality Architect and Regulatory Auditor. Your objective is to thoroughly evaluate prospective and existing suppliers based on capability and risk, and to engineer rigorous Supplier Quality Agreements (SQAs) that ensure strict compliance with ISO 13485:2016, FDA 21 CFR Part 820.50 (Purchasing Controls), and the EU MDR 2017/745. You must employ the "Vector" standard, focusing on clear responsibility matrices, rigorous acceptance criteria, change control notification requirements, and audit provisions.
- role: user
  content: |
    Please evaluate the following supplier and draft a comprehensive Supplier Quality Agreement (SQA) framework and evaluation summary.

    <supplier_type>{{supplier_type}}</supplier_type>
    <supplied_materials>{{supplied_materials}}</supplied_materials>
    <iso_certifications>{{iso_certifications}}</iso_certifications>
    <risk_level>{{risk_level}}</risk_level>

    Your output must include:
    1. **Supplier Evaluation Summary:** A risk-based assessment of the supplier's qualifications given their certifications and the critical nature of the supplied materials.
    2. **Audit Strategy:** Recommended frequency and type of audits (e.g., on-site, desktop) based on the risk level.
    3. **SQA Framework:** A structured outline of the Supplier Quality Agreement, specifically emphasizing:
        - Management Responsibility
        - Change Control Notification (e.g., raw material or process changes)
        - Nonconformance Handling & CAPA Responsibilities
        - Documentation and Record Retention
        - Traceability and Right of Access.
testData:
- input:
    supplier_type: Contract Manufacturer (PCBA Assembly)
    supplied_materials: Class II Medical Device Main Motherboards
    iso_certifications: ISO 13485:2016
    risk_level: High
  expected: "Supplier Evaluation Summary"
evaluators:
- name: Risk Assessment
  regex:
    pattern: (?i)Evaluation Summary
- name: Audit Strategy Check
  regex:
    pattern: (?i)Audit Strategy
- name: SQA Framework Check
  regex:
    pattern: (?i)SQA Framework
- name: Change Control Mention
  regex:
    pattern: (?i)Change Control Notification

```
