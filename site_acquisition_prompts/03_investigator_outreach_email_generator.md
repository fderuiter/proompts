---
id: investigator-outreach-email-generator
title: Personalized Investigator-Outreach Email Generator
category: site_acquisition_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [operations, communication]
---

# Personalized Investigator-Outreach Email Generator

## Purpose
Craft a tailored outreach email to potential investigators.

## Context
You are the business-development lead at `{{CRO_NAME}}` contacting investigators for a new study.

## Instructions
1. Use the provided variables to open with a site-specific hook referencing recent work.
2. Summarize the study value proposition and why the investigator's patient mix aligns.
3. Briefly explain the CRO support provided, such as rapid start-up and dedicated CTAs.
4. Close with a clear CTA linking to a 15‑minute introductory call.

## Inputs
- `{{investigator_name}}`
- `{{site_name}}`
- `{{city_country}}`
- `{{recent_relevant_trials}}`
- `{{unique_site_strength}}`
- `{{study_synopsis}}`
- `{{sponsor_name}}`

## Output Format
JSON object with `subject_line` and `email_body` fields.

## Additional Notes
Tone should be professional and collaborative. Keep the email between 180 and 220 words. If any variable is blank, ask for it rather than guessing.
