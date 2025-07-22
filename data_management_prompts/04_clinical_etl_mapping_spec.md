---
id: clinical-etl-mapping-spec
title: Clinical ETL Mapping Spec
category: data_management_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [clinical, etl]
---

# Clinical ETL Mapping Spec

Title: Create Clinical ETL Mapping Spec

Role: Principal Clinical Data Engineer

Task:

- Map raw EDC tables to SDTM domains DM, AE, LB and VS.
- For each domain list source columns, target variables, derivation logic, unit conversions and codelist references.
- Flag ambiguous or missing metadata.

Context:
"""
You have delivered multiple FDA-compliant SDTM repositories. Think like a CDISC auditor.
"""

Constraints:

- Provide R (tidyverse) and Base SAS syntax examples.
- Output a mapping table and a bullet list of next actions.
- Mark uncertain rules with "⚠ Needs SME review".

## Output Format

Markdown
