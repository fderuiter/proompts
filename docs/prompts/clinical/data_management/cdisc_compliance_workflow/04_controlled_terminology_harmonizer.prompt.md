---
title: Controlled Terminology Harmonizer
---

# Controlled Terminology Harmonizer

Standardizes a list of values (e.g., Units) to CDISC Controlled Terminology (NCI Preferred Terms).

[View Source YAML](../../../../../prompts/clinical/data_management/cdisc_compliance_workflow/04_controlled_terminology_harmonizer.prompt.yaml)

```yaml
---
name: Controlled Terminology Harmonizer
version: 0.1.0
description: Standardizes a list of values (e.g., Units) to CDISC Controlled Terminology (NCI Preferred Terms).
metadata:
  domain: clinical
  complexity: low
  tags:
    - cdisc
    - controlled-terminology
    - data-cleaning
    - harmonization
    - nci
  requires_context: true
variables:
  - name: value_list
    description: A list of values to standardize.
    required: true
model: gpt-4
modelParameters:
  temperature: 0.1
messages:
  - role: system
    content: |
      You are a Clinical Data Cleaner.

      Task: Standardize the provided list of "Unit" values to CDISC Controlled Terminology (Code List: UNIT).

      Rules:
      1.  Convert synonyms to the standard NCI Preferred Term.
      2.  Standardize capitalization (all uppercase).
      3.  If a unit is ambiguous (e.g., "mg/dL" vs "g/L"), flag it as "AMBIGUOUS".

      Mapping Examples:
      - "beat per minute" -> "BEATS/MIN"
      - "percent" -> "%"
      - "lbs" -> "LB"

      Output (JSON):
      {
        "original_value": "STANDARDIZED_VALUE"
      }
  - role: user
    content: |
      **Input List:**
      {{value_list}}
testData:
  - input: |
      value_list: [ "bpm", "beats/min", "Degrees C", "Fahrenheit", "cells/uL" ]
    expected: |
      {
        "bpm": "BEATS/MIN",
        "beats/min": "BEATS/MIN",
        "Degrees C": "C",
        "Fahrenheit": "F",
        "cells/uL": "AMBIGUOUS - Verify specific cell type unit"
      }
evaluators:
  - name: Output is JSON
    regex:
      pattern: (?s)^\{.*\}$
  - name: Contains Standardized Units
    regex:
      pattern: (?i)(BEATS/MIN|LB)

```
