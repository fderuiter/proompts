---
id: biostatistics-dual-language-figure
title: Dual-Language Figure Prompt
category: biostatistics_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [biostatistics, graphics]
# Dual-Language Figure Prompt
---

## Purpose

Generate a Kaplan–Meier figure in both R and SAS from ADaM ADTTE data.

## Context

You are a bilingual statistical programmer proficient in R and SAS.

## Instructions

1. Create Figure 15‑2 “Time‑to‑Progression” Kaplan–Meier plot using ADTTE.
2. Stratify by `TRT01P` with a risk table; censor marks are vertical ticks.
3. X‑axis: 0–1825 days, major tick every 180 days.
4. Y‑axis: Survival probability from 0 to 1.
5. Add hazard ratio (95 % CI) from a Cox model in the subtitle.
6. When `dual = TRUE`, output two code blocks labeled `R` and `SAS` only.

## Inputs

- `{{dual}}` — whether to output both languages
- `{{dataset_path}}` — path to ADTTE dataset

## Output Format

Two pristine code blocks: first in R, then in SAS.

## Additional Notes

Follow the same aesthetic for both languages to keep outputs consistent.
