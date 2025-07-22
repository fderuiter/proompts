---
id: executive-trial-health-dashboard
title: Executive Trial-Health Dashboard
category: executive_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [executive, dashboard]
---

# Executive Trial-Health Dashboard

## Purpose

Summarize the health of active studies in a weekly dashboard.

## Context

Act as a clinical-operations performance analyst. Input is a CSV with columns such as Study_ID, Phase, Region, Planned_Last-Patient-In, Actual_Enrollment, SAEs, Monitoring_Findings, Budget, and more.

## Instructions

- Calculate KPI deltas: enrollment variance (%), budget variance (%), and data-query aging (days).
- Flag metrics that exceed preset thresholds:
   - Enrollment > +10% late
   - Budget > +7% overrun
   - Open data queries > 30 days
- For each red flag, provide a root-cause hypothesis and one actionable mitigation step.
- Output two sections:

  A. "Snapshot Table" in Markdown with columns: Study \| Phase \| KPI in red \| Root-cause hypothesis \| Mitigation \| Owner
  B. A concise "Exec-Summary" paragraph no longer than 150 words.
Do not rewrite or reorder input data; only add analyses and summary.

## Inputs

- `{{csv_data}}` – dataset with study KPIs.

## Output Format

Markdown table plus summary paragraph.

## Additional Notes

Keep the tone concise and executive-friendly.
