---
id: investigator-outreach-email-generator
title: Investigator Outreach Email Generator
category: site_acquisition_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [communication, outreach]
---

# Investigator Outreach Email Generator

## Purpose
Draft a personalized first-contact email to potential investigators.

## Context
You are the business-development lead at `{{cro_name}}`.

## Instructions
1. Use the provided JSON variables:
   ```json
   {
     "investigator_name": "",
     "site_name": "",
     "city_country": "",
     "recent_relevant_trials": "",
     "unique_site_strength": "",
     "study_synopsis": "",
     "sponsor_name": ""
   }
   ```
2. Open with a site-specific hook referencing recent work.
3. Summarize the study value proposition and alignment with their patient mix.
4. Briefly explain CRO support provided (e.g., rapid start-up, dedicated CTAs).
5. Close with a clear call to action linking to a 15-min intro call.
6. Keep the tone professional and collaborative (180–220 words).

## Inputs
- JSON block above

## Output Format
```json
{
  "subject_line": "",
  "email_body": ""
}
```

## Additional Notes
If any variable is blank, ask for it rather than guessing.
