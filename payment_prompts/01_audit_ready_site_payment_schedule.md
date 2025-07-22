---
id: payment-audit-ready-schedule
title: Build an Audit-Ready Site-Payment Schedule
category: payment_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [payments, compliance]
---

# Build an Audit-Ready Site-Payment Schedule

## Purpose

Generate a transparent investigator payment schedule that withstands audit review.

## Context

You are a clinical-trial financial analyst. Input includes the final visit grid, executed CTA/budget, FX table, and FMV benchmarks.

## Instructions

1. Parse the visit grid and CTA to identify every billable milestone.
1. Map each milestone to its trigger in the EDC (e.g., SDV complete, query-free).
1. Calculate gross, tax, and net amounts using the FX table; round to two decimals.
1. Flag variances greater than ±10 % versus FMV benchmarks.
1. Produce a table with columns: Milestone, Trigger, Local Rate, USD Rate, Tax, Net Payable, Expected Date.
1. Append a summary stating total budget versus CTA cap, listing assumptions, and noting any rows requiring sponsor approval.
1. Ask clarifying questions if any data is missing.

## Inputs

- `{{visit_grid}}`
- `{{cta_budget}}`
- `{{fx_table}}`
- `{{fmv_benchmarks}}`

## Output Format

Markdown table followed by summary bullets and outstanding questions.

## Additional Notes

Ensure calculations and triggers are fully traceable for auditors.
