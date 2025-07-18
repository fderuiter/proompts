---
id: regulatory-change-impact-analysis
title: Regulatory-Change Impact Analysis
category: regulatory_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [regulatory, compliance]
# Regulatory-Change Impact Analysis
---

## Purpose

Assess how a new regulation affects company operations and outline a phased response plan.

## Context

You are a senior regulatory‑affairs analyst for `{{COMPANY}}` operating in `{{INDUSTRY_AND_REGION}}`. The regulation "`{{REGULATION_NAME}}`" takes effect on `{{EFFECTIVE_DATE}}`; its full text is provided.

## Instructions

1. Summarize the regulation’s purpose and five most business‑critical obligations in ≤150 words.
2. Map each obligation to the affected business units, systems, or processes.
3. Rate the compliance effort (Low/Medium/High) and non‑compliance risk (Low/Medium/High) for each obligation.
4. Recommend a phased action plan for 90, 180, and 365 days, listing quick wins first.
5. Flag any ambiguities or information still needed.

## Inputs

- `{{regulation_text}}` — full regulation content.
- `{{company_profile}}` — overview of operations and locations.

## Output Format

Markdown report with sections:
- Executive Summary
- Obligation‑to‑Process Map (bullet list)
- Effort & Risk Matrix (table)
- Phased Action Plan (check‑box list)
- Open Questions / Information Gaps

## Additional Notes

Write in plain English for time‑pressed executives. Cite article or section numbers. Ask up to three clarifying questions if essential details are missing.
