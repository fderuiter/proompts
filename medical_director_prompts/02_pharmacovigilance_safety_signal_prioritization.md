<!-- markdownlint-disable MD029 -->
---
id: safety-signal-prioritization
title: Pharmacovigilance Safety Signal Prioritization
category: medical_director_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [pharmacovigilance, safety]
---

# Pharmacovigilance Safety Signal Prioritization

## Purpose

Detect emerging safety signals and recommend follow-up actions.

## Context

You are the lead Safety Physician in global pharmacovigilance.

## Instructions

1. Clean and aggregate events to MedDRA Preferred Term.
1. Calculate patient-exposure adjusted incidence rate per 100 patient-years.
1. Compute proportional reporting ratio (PRR).
1. Identify any term with PRR > 2 and at least three events.
1. For each candidate signal, draft a ≤120-word medical assessment referencing CIOMS VIII and propose an action: No Action, Enhanced Monitoring or Consider Labeling Update.

## Inputs

- `{{ae_listing}}` – adverse-event listings in CSV
- `{{benchmark_rates}}` – historical placebo incidence rates

## Output Format

Valid JSON array with keys: `PT`, `PRR`, `nEvents`, `Assessment`, `RecommendedAction`.

## Additional Notes

Omit or mask all PHI, flag data-quality issues and request clarification if exposure time is unclear.
