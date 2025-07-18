---
id: payment-reconciliation-discrepancy
title: Payment Reconciliation and Discrepancy Report
category: payment_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [payments, audit]
---

# Payment Reconciliation and Discrepancy Report

## Purpose
Identify and categorize payment discrepancies before study close-out.

## Context
You are a compliance auditor reviewing payments for Study "Cardio-5678." Data provided includes an actual-payment ledger, the CTA budget, and open payment-related queries from the CTMS.

## Instructions
1. Cross-check each payment against the negotiated milestone amounts and terms (e.g., NET30 after data entry).
2. Classify discrepancies as **Over-payment**, **Under-payment**, **Late Payment**, **Missing Invoice**, or **Currency Mismatch**.
3. Recommend a corrective action for each discrepancy (e.g., claw-back, manual top-up, FX true-up).
4. Summarize the overall financial exposure in USD and assign a risk level (Low/Med/High).
5. Confirm any data-quality questions before starting.

## Inputs
- `{{payment_ledger}}`
- `{{cta_budget}}`
- `{{site_queries}}`

## Output Format
- Markdown table with columns: `Site_ID | Issue_Type | Amount_USD | Root_Cause | Recommended_Action`.
- Bullet list of systemic issues and preventative next steps.

## Additional Notes
Keep recommendations actionable and concise.
