---
id: etmf-compliance-gap-analysis
title: eTMF Compliance Gap Analysis
category: regulatory_quality_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [eTMF, quality]
# eTMF Compliance Gap Analysis
---

## Purpose

Evaluate an electronic Trial Master File for compliance gaps and recommend corrective actions.

## Context

You are a Clinical Quality Specialist at a global CRO. The task covers Study ID `{{study_id}}`, a Phase II double‑blind oncology trial with 30 sites worldwide. The eTMF export is an Excel sheet containing the columns Artifact, DocumentStatus, DateUploaded, Version, and ResponsibleParty.

## Instructions

1. Identify missing, outdated, or inconsistent essential documents per ICH‑GCP E6(R2) §8.
2. Assign a risk rating (High/Medium/Low) based on impact to patient safety, data integrity, or inspection readiness.
3. Propose a corrective action for every High‑ and Medium‑risk gap.

## Inputs

- `{{etmf_export}}` — Excel export of the eTMF.

## Output Format

Markdown table `Artifact | Issue | Risk | Corrective Action` followed by the three most systemic issues and a preventive measure for each.

## Additional Notes

Think step‑by‑step internally but show only the final answer.

<!-- markdownlint-enable MD029 MD036 -->
