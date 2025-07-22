---
id: payment-global-regulatory-tax
title: Global Regulatory and Tax Matrix for Site Payments
category: payment_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [payments, compliance]
---

# Global Regulatory and Tax Matrix for Site Payments

## Purpose

Summarize key payment compliance requirements across major regions.

## Context

You are a senior regulatory payments expert compiling rules for the U.S., EU (CTR 536/2014), U.K., Japan, and Australia.

## Instructions

1. Create a table with columns: Region, Timing Rule, Mandatory Reports, Tax Docs, FX/Banking Notes, Record Retention, Recent Updates (≤ 12 months).
1. Provide a short commentary (≤150 words) on emerging trends such as heightened scrutiny of cross-border payments.
1. Ask clarifying questions if any requirement is ambiguous.

## Inputs

- `{{regional_guidelines}}` – any additional region-specific documents.

## Output Format

Markdown table plus a short commentary paragraph.

## Additional Notes

Keep language concise and reference official guidance where possible.
