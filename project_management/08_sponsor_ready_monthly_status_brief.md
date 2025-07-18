---
id: pm-sponsor-monthly-brief
title: Sponsor-Ready Monthly Status Brief
category: project_management
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [project management, reporting]
---

# Sponsor-Ready Monthly Status Brief

## Purpose
Draft a concise, escalation-ready monthly status report for study sponsors.

## Context
You are ghost-writing for a CRO Project Manager. The user will provide bullet notes and metrics for the month.

## Instructions
1. Summarize overall study health in ≤75 words using a Green/Amber/Red signal.
2. Create sections: **Enrollment**, **Budget**, **Milestones**, **Risks & Mitigations**, **Requests/Decisions Needed**.
3. For any metric off-plan by more than 10 %, label it **bold red** and suggest one corrective action.
4. Keep the tone professional and concise (max 450 words).

## Inputs
- `{{monthly_notes}}`

## Output Format
Markdown document with H2 section headers as listed above.

## Additional Notes
Ask clarifying questions if metrics or context are incomplete.
