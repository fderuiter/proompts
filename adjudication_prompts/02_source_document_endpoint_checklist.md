---
id: adjudication-source-document-checklist
title: Source Document and Endpoint Checklist
category: adjudication_prompts
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: [adjudication, documentation]
---

# Source Document and Endpoint Checklist

## Purpose
Create a clear checklist of required documents and endpoint criteria for clinical adjudication.

## Context

- Draft adjudication charter lists seven primary endpoints but lacks detail on required source documents.
- Adjudicators previously received incomplete packages.

## Instructions
1. For each endpoint, build a checklist of required documents including imaging, labs, and narrative notes with formatting rules.
1. Convert each endpoint definition into binary inclusion or exclusion criteria.
1. Suggest concise form-field wording (≤50 characters) for EDC alignment.
1. Flag ambiguous language in the draft charter that needs clarification from the sponsor.

## Inputs

- `{{charter_excerpt}}` – relevant sections of the adjudication charter.

## Output Format

- Markdown table per endpoint with columns: *Doc Type*, *Required?*, *Acceptable Formats*, *Notes*.
- Numbered list of **Clarification Needed** items.

## Additional Notes

Ask any clarifying questions before generating the checklist.
