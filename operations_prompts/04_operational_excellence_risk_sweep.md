---
id: operations-excellence-risk-sweep
title: Operational Excellence & Risk Sweep
category: operations_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [operations, risk]
---

# Operational Excellence & Risk Sweep

## Purpose

Deliver a 90-day action plan to cut cycle time and reduce recruitment failure.

## Context

Average trial cycle time is 32 months and recruitment failure rate is 18 %. We use Medidata and Veeva Vault.

## Instructions

1. Prioritize technology, process and talent levers by ROI and implementation effort.
2. Highlight compliance risks for ICH-GCP, GDPR and 21 CFR Part 11.
3. Limit the response to 700 words.
4. Present a markdown table titled **90-Day CRO Ops Optimization Plan** followed by a **Quick-Win Checklist**.
5. Ask three clarifying questions if data gaps exist before drafting.

## Inputs

- `{{trial_metrics}}` – cycle-time and recruitment data.

## Output Format

Markdown table as specified plus the checklist.

## Additional Notes

Risks should be clearly noted; compliance issues may be flagged in red text.
