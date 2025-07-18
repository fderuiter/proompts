---
id: 02-interpret-the-chemistry-assess-risk
title: Interpret the Chemistry & Assess Risk
category: chemical_characterization_prompts
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: []
---

# Interpret the Chemistry & Assess Risk

## Purpose

Act as a board-certified toxicologist.

## Context

## Instructions

I will supply the extractables/leachables results table that was generated per ISO 10993-18. Using those data:

- Calculate the Analytical Evaluation Threshold (AET) given:
   - Patient body weight = {BW} kg
   - Clinical dose = {DEVICE-DOSE} µg day⁻¹
   - Show equations and intermediate steps.
- Tag each compound as:
   - “Below AET”
   - “Above AET – identified”
   - “Above AET – unknown”
- For compounds above the AET, retrieve toxicological reference values (e.g., TTC or DNEL), calculate the Margin of Safety (MoS), and flag any MoS < 1.
- Summarize overall patient risk and recommend next actions (further ID work, in-vivo testing, justification memo, etc.).

Return a markdown table of results followed by a concise narrative. If any required inputs are missing, list the specific questions **before** performing the assessment.
\n<!-- markdownlint-enable MD007 -->

## Inputs

## Output Format

## Additional Notes
