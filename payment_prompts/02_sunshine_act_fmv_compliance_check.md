---
id: payment-sunshine-act-compliance
title: Sunshine Act and FMV Compliance Check
category: payment_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [payments, audit]
---

# Sunshine Act and FMV Compliance Check

## Purpose

Audit site-payment data for Sunshine Act reporting and FMV adherence.

## Context

You are a compliance auditor reviewing a CSV ledger of payments for calendar year 2025.

## Instructions

1. Load the CSV and normalize currency to USD using the provided FX rates.
1. For each line item:
   - Determine if a single payment ≥ $13.46 or annual aggregate > $134.54.
   - Verify required Sunshine fields: NPI, address, payment nature, and related product.
   - Compare investigator fees to FMV benchmarks (±10 %).
1. Output two tables:
   - **Reportable Payments** – rows that must be reported to CMS.
   - **Compliance Exceptions** – missing data or FMV variance > 10 % with remediation notes.
1. Summarize lines reviewed, percent reportable, and percent exceptions.
1. Ask questions if thresholds or tables seem outdated.

## Inputs

- `{{payment_ledger_csv}}`
- `{{fx_rates}}`
- `{{fmv_table}}`

## Output Format

Two CSV-formatted tables followed by a short executive summary.

## Additional Notes

Use clear column headers so the tables can be imported without modification.
