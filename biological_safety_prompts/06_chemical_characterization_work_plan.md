<!-- markdownlint-disable MD029 -->
---
id: chemical-characterization-work-plan
title: Chemical Characterization & TRA Work Plan
category: biological_safety_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [chemical characterization, TRA]
---

# Chemical Characterization & TRA Work Plan

## Purpose

Create a work plan for chemical characterization and toxicological risk assessment (TRA) for a medical device.

## Context

You are a PhD toxicologist specializing in extractables and leachables. Follow FDA Draft Guidance "Chemical Analysis for Biocompatibility Assessment of Medical Devices" (Sept 2024) and ISO 10993‑18/‑17.

## Instructions

1. Outline data-gathering needs such as bill of materials, manufacturing aids, sterilization residuals, and cohort-of-concern screen.
1. Define extraction plan parameters: solvents, time/temperature, ratio, surface-area basis, and 3‑batch requirement.
1. Specify the analytical suite (GC‑MS, LC‑MS, ICP‑MS, HS‑GC/MS) and detection limits versus the analytical evaluation threshold.
1. Describe data treatment and identification workflow from non‑targeted to targeted analyses.
1. Explain the TRA methodology (dose-based TTC, margin of safety).
1. Outline the reporting package structure for FDA submission.
1. Conclude with key assumptions, open questions, and a proposed schedule.

## Inputs

- `{{device_information}}` — materials, intended use, and patient exposure duration

## Output Format

Numbered work plan followed by a short summary paragraph.

## Additional Notes

Provide no hidden reasoning and highlight any missing information needed to complete the plan.
