---
title: Investigator-Site Payment Forecast
---

# Investigator-Site Payment Forecast

Produce a month-by-month cash-flow forecast for site payments.

[View Source YAML](../../../../prompts/business/payment/investigator_site_payment_forecast.prompt.yaml)

```yaml
---
name: Investigator-Site Payment Forecast
version: 0.1.0
description: Produce a month-by-month cash-flow forecast for site payments.
metadata:
  domain: business
  complexity: medium
  tags:
  - payment
  - investigator-site
  - forecast
  requires_context: false
variables:
- name: enrollment_curve
  description: expected enrollment percentage per month
  required: true
- name: fx_rates
  description: FX rate sheet name
  required: true
- name: site_data
  description: Site ID, country, contract currency, enrollment target, and milestone amounts
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a senior clinical payments analyst planning for the Phase III oncology study "Onco-1234." The CTA defines
    Start-up, Per-Visit, Close-out, and Screen-Failure fees. FPFV is 15 Sep 2025 and the planned duration is 30 months.


    Produce a month-by-month cash-flow forecast for site payments.'
- role: user
  content: '1. Convert milestone amounts to USD using the provided FX rates.

    1. Build a table showing monthly and cumulative totals per site and overall.

    1. Highlight any month with >20 % variance versus the previous forecast in **red**.

    1. Summarize key drivers such as seasonality or enrollment ramp-up in a short narrative.

    1. Clarify any assumptions before starting if needed.


    Inputs:

    - `{{site_data}}` – Site ID, country, contract currency, enrollment target, and milestone amounts.

    - `{{enrollment_curve}}` – expected enrollment percentage per month.

    - `{{fx_rates}}` – FX rate sheet name.


    Output format:

    Markdown table followed by a narrative summary.


    Additional notes:

    Keep the table easy to import into spreadsheets.'
testData:
- site_data: 'Site_ID,Country,Currency,Enrollment,Start-up

    S1,US,USD,10,1000'
  enrollment_curve: 'Month,Percent

    1,10'
  fx_rates: 'Currency,USD

    USD,1'
  expected: '| Site ID |'
evaluators:
- name: Contains site ID column
  string:
    contains: '| Site ID |'

```
