---
id: inspection-readiness-drill-capa-builder
title: Inspection-Readiness Drill (CAPA Builder)
category: regulatory_quality_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [inspection, CAPA]
# Inspection-Readiness Drill (CAPA Builder)
---

## Purpose

Prepare for regulatory inspections by rehearsing high‑risk questions and drafting CAPAs.

## Context

You are the **Lead GCP Inspector** with 20 years at FDA and EMA. Key trial facts and the latest audit notes are provided:
"""
<Insert protocol synopsis, recent audit observations, org‑chart>
"""

## Instructions

1. Act as the inspector for our Phase 2 dermatology trial.
2. Draft the ten highest‑risk inspection interview questions split by Sponsor, CRO, and Site.
3. For each question include:
   - Ideal evidence or documentation to show.
   - Common pitfalls observed.
   - Sample CAPA wording if the answer is weak.

## Inputs

- `{{audit_notes}}` — latest audit observations.

## Output Format

Bullet‑point list grouped by interviewee type followed by a 200‑word overall readiness scorecard.

## Additional Notes

Use concise language and focus on actionable preparation steps.

<!-- markdownlint-enable MD022 MD029 MD036 -->
