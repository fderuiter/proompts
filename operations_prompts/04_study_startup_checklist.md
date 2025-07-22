---
id: operations-study-startup-checklist
title: Study Start-Up Checklist & Timeline
category: operations_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [operations, startup]
---

# Study Start-Up Checklist & Timeline

## Purpose

Provide an actionable checklist and timeline for Phase IIb study start-up.

## Context

You are an experienced clinical-operations specialist. The therapeutic area, regions, target first-patient-in date and regulations are provided.

## Instructions

1. Detail workstreams for regulatory submissions, site contracts, vendor onboarding, IMP supply and staff training.
1. Include a Gantt-style timeline.
1. List at least three common start-up risks with mitigations.

## Inputs

- `{{therapeutic_area}}` – indication for the study.
- `{{regions}}` – participating regions.
- `{{fpi_date}}` – first-patient-in target date.
- `{{regulations}}` – key regulatory references.

## Output Format

Markdown table with columns `Workstream \| Key Activities \| Owner \| Start \| Finish \| Dependencies \| Notes/Risks`.

## Additional Notes

All critical-path tasks should take no longer than 15 business days and align with the FPI date. Ask clarifying questions if information is missing.
