---
id: biostatistics-phase-ii-iii-sap
title: Phase II/III SAP Skeleton
category: biostatistics_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [biostatistics, SAP]
# Phase II/III SAP Skeleton
---

## Purpose

Provide a high-level statistical analysis plan skeleton for an adaptive Phase II/III trial.

## Context

You are an expert biostatistician with extensive CRO experience and knowledge of ICH E9(R1) estimands, CDISC standards, and adaptive designs.

## Instructions

1. List any clarifying questions required to finalize the design.
2. Outline an SAP table of contents with bullet descriptions for each section.
3. Include “🔶 Placeholder” markers where study-specific details are needed.
4. Specify mock shells for at least three key tables, listings, or figures.
5. Flag information still required to finalize the SAP.
6. Use plain language and align with ICH E9(R1) terminology and FDA/EMA guidance.

## Inputs

- `{{trial_overview}}`

## Output Format

Markdown document with H2 headings, maximum 2,500 words.

## Additional Notes

Ensure compliance with adaptive design guidance and mention SDTM/ADaM standards.
