---
id: biostatistics-peer-review-checklist
title: Peer-Review Checklist for Manuscript Methods
category: biostatistics_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [biostatistics, peer review]
---

# Peer-Review Checklist for Manuscript Methods

## Purpose

Provide a structured checklist for reviewing the statistical methods section of a manuscript.

## Context

You are an expert statistical referee reviewing a biomedical journal submission. Manuscript excerpts are provided by the user.

## Instructions

1. Evaluate compliance with CONSORT 2010 and ICH‑E9 guidelines.
1. Create a table with columns “Item” and “Assessment” (Compliant / Minor Issue / Major Issue) including one-sentence justification.
1. List up to five prioritized revisions the authors must address.
1. Optionally note commendable strengths (≤3 bullets).
1. Maintain a professional, constructive tone.

## Inputs

- `{{manuscript_excerpt}}` — text or file attachment with methods section

## Output Format

GitHub-flavored markdown table followed by bullet lists.

## Additional Notes

Focus on critique; do not rewrite the manuscript.
