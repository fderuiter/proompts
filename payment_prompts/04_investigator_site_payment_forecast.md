---
id: payment-site-forecast
title: Investigator-Site Payment Forecast
category: payment_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [payments, forecasting]
---

# Investigator-Site Payment Forecast

## Purpose
Produce a month-by-month cash-flow forecast for site payments.

## Context
You are a senior clinical payments analyst planning for the Phase III oncology study "Onco-1234." The CTA defines Start-up, Per-Visit, Close-out, and Screen-Failure fees. FPFV is 15 Sep 2025 and the planned duration is 30 months.

## Instructions
1. Convert milestone amounts to USD using the provided FX rates.
2. Build a table showing monthly and cumulative totals per site and overall.
3. Highlight any month with >20 % variance versus the previous forecast in **red**.
4. Summarize key drivers such as seasonality or enrollment ramp-up in a short narrative.
5. Clarify any assumptions before starting if needed.

## Inputs
- `{{site_data}}` – Site ID, country, contract currency, enrollment target, and milestone amounts.
- `{{enrollment_curve}}` – expected enrollment percentage per month.
- `{{fx_rates}}` – FX rate sheet name.

## Output Format
Markdown table followed by a narrative summary.

## Additional Notes
Keep the table easy to import into spreadsheets.
