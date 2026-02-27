---
title: Site Landscape Mapping & Prioritization
---

# Site Landscape Mapping & Prioritization

Rank investigative sites for an upcoming study.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/site_acquisition/site_acquisition_workflow/01_site_landscape_mapping.prompt.yaml)

```yaml
---
name: Site Landscape Mapping & Prioritization
version: 0.1.0
description: Rank investigative sites for an upcoming study.
metadata:
  domain: clinical
  complexity: medium
  tags:
  - site-acquisition
  - site
  - landscape
  - mapping
  - prioritization
  requires_context: true
variables:
- name: protocol_summary
  description: final study synopsis
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a senior clinical-operations strategist at a global CRO. Use the provided study synopsis.


    Rank investigative sites for an upcoming study.'
- role: user
  content: '1. Ask up to three clarifying questions if details are missing.

    1. Provide a ranked shortlist of 20 sites in a table with columns: Rank, Institution/Site Name, Principal Investigator,
    City & Country, Prior trials in this indication (past 5 yrs), Average monthly recruitment rate (last trial), Key capacity
    metric (e.g., open beds), Contact e-mail/phone, and Source links.


    Inputs:

    - `{{protocol_summary}}` – final study synopsis.


    Output format:

    Markdown table listing recommended sites.


    Additional notes:

    - Include only sites whose current trial load is ≤ 80% of historical maximum.

    - Cover at least three geographic regions.

    - Base recommendations on public registries and sponsor data.

    - Cite every data source in column 9.'
testData:
- input: 'protocol_summary: Example Phase II oncology study synopsis'
  expected: Rank
evaluators:
- name: Output starts with 'Rank'
  string:
    startsWith: Rank

```
