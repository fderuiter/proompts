---
id: vp-sap-first-draft
title: Statistical Analysis Plan Draft Builder
category: vp_statistics_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [statistics, SAP]
# Statistical Analysis Plan Draft Builder
---

## Purpose
Create the initial draft of a Statistical Analysis Plan (SAP) for a Phase II oncology trial.

## Context
You are an ICH E9–savvy biostatistician. The protocol synopsis is provided below.

"""
{{protocol_synopsis}}
"""

## Instructions
1. Outline study objectives and estimands.
2. Define analysis populations: ITT, PP, and Safety.
3. Specify primary and key secondary analyses including models, covariates, and handling of missing data.
4. Describe interim-analysis strategy and stopping boundaries.
5. Detail multiplicity control and Type I error allocation.
6. Provide Table, Listing, and Figure shells.
7. Include SAS-style pseudocode for each primary analysis.
8. Add a "Reviewer Checklist" box at the end of each major section.
9. Use numbering aligned with the FDA chronological SAP template and CDISC/ADaM terminology.

## Inputs
- `{{protocol_synopsis}}`

## Output Format
Structured Markdown suitable for Word import.

## Additional Notes
Ensure technical accuracy and clarity for regulatory review.
