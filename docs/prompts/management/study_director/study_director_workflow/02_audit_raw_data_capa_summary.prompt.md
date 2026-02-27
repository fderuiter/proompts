---
title: Audit Raw Data and Draft a CAPA Summary
---

# Audit Raw Data and Draft a CAPA Summary

Review study data for deviations and produce a corrective-action plan.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/management/study_director/study_director_workflow/02_audit_raw_data_capa_summary.prompt.yaml)

```yaml
---
name: Audit Raw Data and Draft a CAPA Summary
version: 0.1.0
description: Review study data for deviations and produce a corrective-action plan.
metadata:
  domain: management
  complexity: medium
  tags:
  - study-director
  - audit
  - raw
  - data
  - draft
  requires_context: false
variables:
- name: data_csv
  description: raw study data
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'Assume the role of a GLP Quality‑Assurance auditor examining raw body‑weight and clinical‑signs data from Day 15
    of dermal toxicity Study ABC.


    - Ignore trivial rounding differences.

    - Cite the line numbers or record IDs inspected so the Study Director can cross‑verify.

    - Think silently first; output only the table and memo.'
- role: user
  content: '1. Identify protocol deviations, data gaps, or statistical outliers that could affect study integrity.

    2. For each issue, rate the potential impact (Low/Med/High) and propose a corrective‑action/preventive‑action (CAPA).

    3. Draft a CAPA memo addressed to the Study Director in no more than 300 words.


    Inputs:

    - `{{data_csv}}` – raw study data


    Output Format:

    1. Markdown table with columns: Issue ID | Impact | CAPA

    2. CAPA memo addressed to the Study Director (≤300 words)'
testData:
- input: "data_csv: |\n  id,weight\n  1,200\n  2,150\n  3,250\n"
  expected: '| Issue ID | Impact | CAPA |

    | 1 | Low | ... |

    '
evaluators:
- name: Includes CAPA memo
  string:
    contains: CAPA memo

```
