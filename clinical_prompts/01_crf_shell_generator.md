---
id: 01-crf-shell-generator
title: CRF Shell Generator
category: clinical_prompts
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: []
---

# CRF Shell Generator

## Purpose

- Read the protocol summary inside the triple quotes.

## Context

## Instructions

- Working section-by-section, list the CRF pages you would create.
- Under each page, list every field with: • CDASH variable • question text • data type • permitted values • SDTM mapping.
- Flag any data the protocol requests that is not essential for primary/secondary endpoints.
- Output a Markdown table grouped by CRF page.
- Think step-by-step before writing the final table.

## Inputs

## Output Format

## Additional Notes
