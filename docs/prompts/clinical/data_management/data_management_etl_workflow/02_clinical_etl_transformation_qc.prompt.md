---
title: Clinical ETL Transformation QC
---

# Clinical ETL Transformation QC

Define quality checks for clinical ETL transformations.

[View Source YAML](../../../../../prompts/clinical/data_management/data_management_etl_workflow/02_clinical_etl_transformation_qc.prompt.yaml)

```yaml
---
name: Clinical ETL Transformation QC
version: 0.1.0
description: Define quality checks for clinical ETL transformations.
metadata:
  domain: clinical
  complexity: low
  tags:
  - data-management
  - clinical
  - etl
  - transformation
  requires_context: false
variables:
- name: etl_mapping_spec
  description: The etl mapping spec to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a quality engineer establishing validation checks for clinical ETL

    transformations.

    '
- role: user
  content: 'Here is the ETL mapping specification:

    {{etl_mapping_spec}}


    Based on this specification, define a comprehensive set of quality checks for the clinical ETL transformations.'
testData:
- input: List QC checks for transforming lab results data.
  expected: Mentions range validations and format consistency.
evaluators:
- name: Output mentions validation
  string:
    contains: validation

```
