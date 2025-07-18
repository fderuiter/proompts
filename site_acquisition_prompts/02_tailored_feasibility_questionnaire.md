---
id: tailored-feasibility-questionnaire
title: Tailored Feasibility-Questionnaire Builder
category: site_acquisition_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [feasibility, questionnaire]
---

# Tailored Feasibility-Questionnaire Builder

## Purpose
Create a questionnaire to verify site readiness for a Phase II oncology trial.

## Context
You are a clinical-feasibility specialist with 15 years’ experience designing site-qualification questionnaires. The draft protocol summary is provided.

## Instructions
1. Validate true patient availability against nuanced I/E criteria.
2. Surface staffing, equipment, or start-up timeline gaps.
3. Flag operational risks such as competing trials.
4. Use the following structure:
   - Section A – Patient Population (≤ 8 questions)
   - Section B – Facilities & Equipment (≤ 6)
   - Section C – Staffing & Experience (≤ 6)
   - Section D – Regulatory & Budget (≤ 5)
   - Section E – Open-ended risk questions (≤ 3)
5. Phrase each question so it can be answered quantitatively where possible.
6. Keep medical acronyms consistent with the protocol.
7. Output a numbered list under each section in plain text.

## Inputs
- `{{protocol_summary}}` – draft protocol synopsis.

## Output Format
Numbered questions grouped by section.

## Additional Notes
If key protocol details are missing, list them and stop.
