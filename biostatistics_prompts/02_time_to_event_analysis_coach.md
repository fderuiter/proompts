---
id: biostatistics-time-to-event-coach
title: Time-to-Event Analysis Coach
category: biostatistics_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [biostatistics, survival analysis]
# Time-to-Event Analysis Coach
---

## Purpose

Guide a junior analyst through performing a time-to-event analysis.

## Context

Dataset snapshot: 5 000 oncology patients with variables `t_event`, `event_flag`, `treatment`, `age`, `sex`, and `stage`.

## Instructions

1. Explain why a Cox proportional-hazards model is appropriate.
2. Provide commented R code to load data, check proportional hazards (Schoenfeld residuals and log-minus-log curves), fit the model `Surv(t_event, event_flag) ~ treatment + age + sex + stage`, and output hazard ratios in a `gt` table.
3. If the PH assumption fails, suggest two alternative modelling strategies with pros and cons.

## Inputs

- `{{dataset_path}}` — path to the patient dataset

## Output Format

Section A: conceptual walk-through (bullets). Section B: fenced R code block. Section C: interpretation and next steps (\u2264250 words).

## Additional Notes

Provide rationale before each major code chunk using comments.
