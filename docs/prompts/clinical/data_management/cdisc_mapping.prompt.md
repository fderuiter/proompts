---
title: CDISC SDTM/ADaM Mapping
---

# CDISC SDTM/ADaM Mapping

Map raw clinical data to standardized CDISC SDTM and ADaM domains.

[View Source YAML](../../../../prompts/clinical/data_management/cdisc_mapping.prompt.yaml)

```yaml
---
name: CDISC SDTM/ADaM Mapping
version: 0.1.0
description: Map raw clinical data to standardized CDISC SDTM and ADaM domains.
metadata:
  domain: clinical
  complexity: high
  tags:
  - data-management
  - cdisc
  - sdtm
  - ada
  - mapping
  requires_context: false
variables:
- name: curation_guidelines
  description: 'Metadata definitions: `{{metadata_defs}}`'
  required: true
- name: metadata_defs
  description: 'Predefined Metadata Rules: `{{metadata_rules}}`'
  required: true
- name: metadata_rules
  description: The data or dataset to analyze
  required: true
- name: raw_data
  description: 'Data curation internal guidelines: `{{curation_guidelines}}`'
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Clinical Data Standards Specialist. Apply variable mapping to the provided raw datasets for each domain
    following CDISC standards and internal curation guidelines to generate SDTM-compliant datasets. Adhere to CDISC SDTM/ADaM
    standards.
- role: user
  content: 'Apply variable mapping to the provided raw datasets for each domain following CDISC standards and internal curation
    guidelines to generate SDTM-compliant datasets.


    Inputs:

    - Raw datasets (schema/sample): `{{raw_data}}`

    - Data curation internal guidelines: `{{curation_guidelines}}`

    - Metadata definitions: `{{metadata_defs}}`

    - Predefined Metadata Rules: `{{metadata_rules}}`


    Output format:

    Markdown Mapping Specifications Table (Source Variable -> Target Domain/Variable -> Transformation Logic).'
testData:
- input: 'raw_data: "PatientID, DOB, Gender"

    curation_guidelines: "Use DM domain"

    metadata_defs: "DM.USUBJID, DM.BRTHDTC, DM.SEX"

    metadata_rules: "ISO 8601 dates"

    '
  expected: '| Source Variable | Target Variable | Transformation |

    '
evaluators:
- name: Mapping Table
  string:
    contains: '| Source Variable |'
- name: SDTM Domain
  string:
    contains: DM

```
