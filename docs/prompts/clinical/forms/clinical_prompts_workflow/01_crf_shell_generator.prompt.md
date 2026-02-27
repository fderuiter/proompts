---
title: CRF Shell Generator
---

# CRF Shell Generator

- Read the protocol summary inside the triple quotes.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/forms/clinical_prompts_workflow/01_crf_shell_generator.prompt.yaml)

```yaml
---
name: CRF Shell Generator
version: 0.1.0
description: '- Read the protocol summary inside the triple quotes.'
metadata:
  domain: clinical
  complexity: low
  tags:
  - forms
  - crf
  - shell
  - generator
  requires_context: false
variables:
- name: input
  description: The primary input or query text for the prompt
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: '- Working section-by-section, list the CRF pages you would create.

    - Under each page, list every field with: • CDASH variable • question text • data type • permitted values • SDTM mapping.

    - Flag any data the protocol requests that is not essential for primary/secondary endpoints.

    - Output a Markdown table grouped by CRF page.

    - Think step-by-step before writing the final table.'
- role: user
  content: '{{input}}'
testData:
- input: 'Study collects age and sex.

    '
  expected: '| CRF Page | Field | CDASH Variable | Data Type | Permitted Values | SDTM Mapping |

    | Demographics | Age | AGE | integer | >=0 | DM.AGE |

    '
evaluators:
- name: Output should include AGE mapping
  string:
    contains: DM.AGE

```
