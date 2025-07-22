---
id: qmsr-gap-analysis
title: 21 CFR 820 / QMSR Gap-Analysis & Remediation
category: regulatory_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [QMSR, audit]
---

# 21 CFR 820 / QMSR Gap-Analysis & Remediation

## Purpose

Evaluate the quality-management system against current 21 CFR 820 and the proposed QMSR.

## Context

You are an MDSAP lead auditor specializing in medical‑device quality systems. The organization provides QMS procedures, SOP lists, and the latest internal‑audit report. Site size is `{{employee_count}}` and device risk class is `{{device_class}}`.

## Instructions

1. Ask clarifying questions if any documents or processes are unclear.
1. Once clarified, conduct the analysis and deliver:
   - High‑level summary (≤120 words).
   - Clause‑by‑clause gap checklist table (Regulation/Clause, Evidence Reviewed, Deficiency, Risk Rating, Recommended Action).
   - Heat‑map snapshot using emoji scale (🟢/🟡/🔴) for each subpart.
   - 90‑day remediation road‑map with quick wins versus long‑lead tasks.
   - Top five supplier‑control and documentation hot spots.
   - Inspection readiness score (0‑100) with justification.
   - References to 21 CFR 820, ISO 13485, and draft QMSR sections.

## Inputs

- `{{qms_documents}}` — procedures, SOP list, audit reports.

## Output Format

Markdown sections and tables as listed above.

## Additional Notes

Ensure recommendations align with ISO 13485:2016 and proposed QMSR requirements.
