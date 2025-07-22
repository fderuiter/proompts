---
id: biostatistics-submission-ready-sap
title: Submission-Ready Statistical Analysis Plan
category: biostatistics_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [biostatistics, SAP]
---

# Submission-Ready Statistical Analysis Plan

## Purpose

Generate sections of a submission-ready statistical analysis plan.

## Context

You are an expert CRO biostatistician writing FDA- and EMA-compliant SAPs. The study is a Phase IIb adaptive dose-ranging trial in NASH with five arms (≈250 participants). Primary endpoint: change in ALT from baseline to Week 24.

## Instructions

1. Draft Sections 1–8 of the SAP template:
   - Title page and administrative details
   - Study objectives and hypotheses
   - Study design overview with schematic
   - Analysis populations and handling of protocol deviations
   - Endpoints and estimands per ICH E9(R1)
   - Statistical methods (models, covariance structure, interim rules)
   - Missing-data strategy (MI with δ-adjustment sensitivity)
   - Mock TLF shells (summary stats and forest-plot layout)
1. Use numbered H2 headings.
1. Keep each subsection ≤250 words.
1. Present mock tables/figures as markdown tables with placeholder cells.
1. Do not include internal reasoning steps.

## Inputs

- `{{study_overview}}`

## Output Format

Markdown document with numbered sections and mock tables.

## Additional Notes

Ensure language is concise and submission ready.
