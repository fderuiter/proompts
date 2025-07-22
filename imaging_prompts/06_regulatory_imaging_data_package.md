---
id: imaging-regulatory-data-package
title: Regulatory Imaging Data Package
category: imaging_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [imaging, regulatory]
---

# Regulatory Imaging Data Package

## Purpose

Assemble the imaging section of a PMA or 510(k) submission.

## Context

You are a medical writer on the imaging core lab submission team, expert in DICOM metadata and statistical imaging endpoints. The sponsor is preparing a PMA for an AI-guided cardiac mapping device. Data come from three blinded independent readers with adjudication. Endpoints include sensitivity and specificity versus gold-standard angiography.

## Instructions

1. Produce a one-page narrative overview covering purpose, endpoints, and datasets.
1. Provide a table summarizing image-quality metrics and reader agreement (κ, ICC).
1. Describe the imaging data-handling process from capture to lock.
1. Include an appendix template for anticipated FDA questions.
1. Cross-reference the ISO 13485 certification statement.
1. Keep the narrative within 300 words.
1. Present the table in Markdown format.
1. Ask clarifying questions if details are missing.

## Inputs

- `<<<study_summary>>>` – key trial details
- `<<<metrics_data>>>` – image-quality metrics
- `<<<reader_agreement>>>` – reader agreement statistics

## Output Format

Narrative text followed by a Markdown table and an appendix template.

## Additional Notes

Limit the narrative to 300 words.
