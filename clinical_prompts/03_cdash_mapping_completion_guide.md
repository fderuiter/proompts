---
id: 03-cdash-mapping-completion-guide
title: CDASH Mapping & Completion-Guide Assistant
category: clinical_prompts
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: []
---

# CDASH Mapping & Completion-Guide Assistant

## Purpose

- For every variable in the list, supply:

## Context

## Instructions

  • CDASH variable name  
  • SDTM target domain.variable  
  • Plain-language completion instruction (≤40 words)  
  • Controlled terminology / units  
  • Allowed query logic (range checks, missing-data rules).
- At the end, provide a one-page “Top 10 data-entry tips” bullet list.
- Output in CSV-ready Markdown:
  Variable | Domain | Instruction | Terminology/Units | Edit-Check
- Think through the mapping logic first, then write the table.

## Inputs

## Output Format

## Additional Notes
