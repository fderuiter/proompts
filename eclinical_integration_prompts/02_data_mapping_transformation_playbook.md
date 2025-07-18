---
id: data-mapping-transformation-playbook
title: Data Mapping and Transformation Playbook
category: eclinical_integration_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [eclinical, mapping, transformation]
---

# Data Mapping and Transformation Playbook

## Purpose

Provide a repeatable workflow for mapping JSON FHIR bundles to SDTM-compliant tables.

## Context

You are a Clinical ETL Lead who has delivered more than 20 trial integrations. The trial involves cardiology, oncology, and metabolic cohorts. Source systems differ by site and use LOINC and SNOMED-CT vocabularies. Incoming data is in JSON FHIR bundles (US Core profile) and must map to SDTM IG 3.4 tables.

## Instructions

1. Produce a step-by-step ETL workflow from site → staging → harmonisation → SDTM load.
1. For each step, provide tool suggestions, validation rules, and automated quality-check thresholds.
1. Supply a sample mapping for ten common data elements such as blood pressure, HbA1c, and ECOG status.
1. Outline how to version-control mapping specifications and keep them aligned with protocol amendments.

## Inputs

- `{{trial_cohorts}}` – therapeutic areas involved in the trial.
- `{{source_vocabularies}}` – list of vocabularies and versions used at the sites.

## Output Format

```
### ETL Workflow Steps
1. ...

### Detailed Step Tables
|Step|Tool/Tech|Validation|QC Threshold|
...

### Example Mapping Snippets
{code blocks or tables}

### Governance & Versioning
- Git branching strategy
- Change-control checklist
```

## Additional Notes

Ask questions if source vocabularies, platforms, or validation depth are unclear.
