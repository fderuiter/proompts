---
title: Build an Audit-Ready Site-Payment Schedule
---

# Build an Audit-Ready Site-Payment Schedule

Generate a transparent investigator payment schedule that withstands audit review.

[View Source YAML](../../../../prompts/business/payment/audit_ready_site_payment_schedule.prompt.yaml)

```yaml
---
name: Build an Audit-Ready Site-Payment Schedule
version: 0.1.0
description: Generate a transparent investigator payment schedule that withstands audit review.
metadata:
  domain: business
  complexity: high
  tags:
  - payment
  - build
  - audit-ready
  - site-payment
  - schedule
  requires_context: false
variables:
- name: cta_budget
  description: executed clinical trial agreement budget
  required: true
- name: fmv_benchmarks
  description: fair market value benchmarks
  required: true
- name: fx_table
  description: foreign-exchange rate table
  required: true
- name: visit_grid
  description: visit schedule with milestones and triggers
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a clinical-trial financial analyst. Input includes the final visit grid, executed CTA/budget, FX table,
    and FMV benchmarks.


    Generate a transparent investigator payment schedule that withstands audit review.'
- role: user
  content: "1. Parse the visit grid and CTA to identify every billable milestone.\n1. Map each milestone to its trigger in\
    \ the EDC (e.g., SDV complete, query-free).\n1. Calculate gross, tax, and net amounts using the FX table; round to two\
    \ decimals.\n1. Flag variances greater than ±10 % versus FMV benchmarks.\n1. Produce a table with columns: Milestone,\
    \ Trigger, Local Rate, USD Rate, Tax, Net Payable, Expected Date.\n1. Append a summary stating total budget versus CTA\
    \ cap, listing assumptions, and noting any rows requiring sponsor approval.\n1. Ask clarifying questions if any data is\
    \ missing.\n\n  Inputs:\n  - `{{visit_grid}}` – visit schedule with milestones and triggers\n  - `{{cta_budget}}` – executed\
    \ clinical trial agreement budget\n  - `{{fx_table}}` – foreign-exchange rate table\n  - `{{fmv_benchmarks}}` – fair market\
    \ value benchmarks\n\nOutput format:\nMarkdown table followed by summary bullets and outstanding questions.\n\nAdditional\
    \ notes:\nEnsure calculations and triggers are fully traceable for auditors."
testData:
- visit_grid: 'Milestone,Trigger,Local Rate

    V1,SDV complete,100'
  cta_budget: 1000 USD
  fx_table: 'Currency,USD

    USD,1'
  fmv_benchmarks: 'Milestone,USD

    V1,90'
  expected: '| Milestone | Trigger | Local Rate | USD Rate | Tax | Net Payable | Expected Date |'
evaluators:
- name: Contains payment schedule table
  string:
    contains: '| Milestone | Trigger |'

```
