---
id: clinical-etl-transformation-qc
title: Clinical ETL Transformation QC
category: data_management_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [clinical, qc]
---

# Clinical ETL Transformation QC

Title: Produce Clinical ETL Code with QC

Role: Senior Statistical Programming Mentor

Task:

- Transform raw Lab Results into ADLB using identical logic in R and SAS.
- Include unit tests confirming the outputs match byte-for-byte.
- Add inline comments for regulatory traceability.

Context:
"""
Write production-ready code with R tidyverse and Base SAS.
"""

Constraints:

- R code uses tidyverse with `vctrs::vec_c` type safety.
- SAS code employs PROC SQL and DATA step macros with log checks.
- Provide testthat and `%assert_compare` examples.
- Column order must match ADaM IG v2.2 and dates use ISO 8601.

## Output Format

Markdown
