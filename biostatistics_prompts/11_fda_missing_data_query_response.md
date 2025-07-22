---
id: biostatistics-fda-missing-data
title: FDA Missing-Data Query Response
category: biostatistics_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [biostatistics, regulatory]
---

# FDA Missing-Data Query Response

## Purpose

Draft a response letter to an FDA information request about missing data.

## Context

You are a senior regulatory statistician preparing a Type C meeting package. The FDA has questioned the robustness of the Week 52 remission endpoint given 9 % missing data and potential MNAR bias.

## Instructions

1. Summarize the agency’s concerns in plain English.
1. Present planned sensitivity analyses (MI under MNAR, tipping point, δ-adjusted worst-case).
1. Justify the primary estimand choice (treatment policy) per ICH E9(R1).
1. Reference relevant guidance (FDA Missing Data 2019, EMA Guideline 07/2022).
1. Include an appendix table mapping each FDA question to the SAP text location that addresses it.
1. Draft in formal, concise regulatory style (≤8 pages) using numbered sections matching the FDA’s bullets.
1. Highlight any additional data or simulations proposed.
1. Conclude with a request for the agency’s confirmation that the approach is adequate.

## Inputs

- `{{fda_questions}}`
- `{{sap_references}}`

## Output Format

Word-style Markdown outline with H1/H2 sections plus the appendix table.

## Additional Notes

Ask clarifying questions before drafting if critical details are missing.
