---
title: Clinical ETL Pipeline Review
---

# Clinical ETL Pipeline Review

Review the clinical ETL pipeline for accuracy and efficiency.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/data_management/data_management_etl_workflow/03_clinical_etl_pipeline_review.prompt.yaml)

```yaml
---
name: Clinical ETL Pipeline Review
version: 0.1.0
description: Review the clinical ETL pipeline for accuracy and efficiency.
metadata:
  domain: clinical
  complexity: low
  tags:
  - data-management
  - clinical
  - etl
  - pipeline
  - review
  requires_context: false
variables:
- name: etl_qc_plan
  description: The etl qc plan to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a reviewer auditing clinical ETL pipelines for accuracy and

    efficiency.

    '
- role: user
  content: 'Here is the ETL Quality Check plan:

    {{etl_qc_plan}}


    Based on this QC plan, and the implied mapping specification, review the entire clinical ETL pipeline for accuracy, efficiency,
    and potential bottlenecks.'
testData:
- input: Assess pipeline stages for bottlenecks.
  expected: Identifies slow transformations and load issues.
evaluators:
- name: Output mentions pipeline
  string:
    contains: pipeline

```
