---
id: imaging-central-reading-design
title: Central Reading Paradigm Design
category: imaging_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [imaging, bicr]
---

# Central Reading Paradigm Design

## Purpose

Recommend an efficient central reading model for an oncology trial.

## Context

You are a blinded independent central review architect.

- Disease: `<<<disease>>>`
- Imaging time-points: `<<<timepoints>>>`
- Target endpoints: `<<<endpoints>>>`
- Available reader pool: `<<<reader_pool_size>>>`
- Budget constraint: `<<<budget>>>`

## Instructions

1. Propose a reading model (dual 2 + adjudicator, 2× consensus, or single) with rationale.
1. Outline reader training and calibration schedule including dry runs and kappa targets.
1. Define ongoing variability monitoring KPIs and retraining triggers.
1. Specify tie-breaker and adjudication rules with decision timelines.
1. Estimate FTE and cost impact versus alternatives.
1. Cite empirical variability data when relevant.
1. Ask clarifying questions if trial details are insufficient.

## Inputs

- `<<<disease>>>` – indication
- `<<<timepoints>>>` – imaging schedule
- `<<<endpoints>>>` – target endpoints
- `<<<reader_pool_size>>>` – number of available readers
- `<<<budget>>>` – cost constraint per read

## Output Format

Two-column Markdown table: **Component \| Recommendation**.

## Additional Notes

Think step by step before producing the table.
