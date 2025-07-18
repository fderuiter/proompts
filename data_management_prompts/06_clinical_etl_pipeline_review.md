---
id: clinical-etl-pipeline-review
title: Clinical ETL Pipeline Review
category: data_management_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [clinical, performance]
---

# Clinical ETL Pipeline Review

Title: Optimise Clinical ETL Pipeline

Role: Performance-Tuning Specialist

Task:
- Review ETL code from the provided gist.
- List the top five maintainability issues and any CDISC compliance risks.
- Outline a benchmark plan using tools like `bench::mark` or `/fullstimer` to isolate slow steps.
- Recommend refactors such as vectorisation, hash joins and partitioned loads with estimated runtime savings.

Context:
"""
Files: ingest_raw.R, transform.sas and load_to_db.sql. Current peak runtime is 4 h.
"""

Constraints:
- Solutions must stay portable to on-prem SAS 9.4 and Posit Workbench.
- Avoid proprietary libraries.
- Present reasoning first, then recommendations.

Output Format: markdown
--------------------------------------------------
