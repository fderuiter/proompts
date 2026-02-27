---
title: CDASH Mapping & Completion-Guide Assistant
---

# CDASH Mapping & Completion-Guide Assistant

- For every variable in the list, supply:

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/forms/clinical_prompts_workflow/03_cdash_mapping_completion_guide.prompt.yaml)

```yaml
---
name: CDASH Mapping & Completion-Guide Assistant
version: 0.1.0
description: '- For every variable in the list, supply:'
metadata:
  domain: clinical
  complexity: low
  tags:
  - forms
  - cdash
  - mapping
  - completion-guide
  - assistant
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
  content: "• CDASH variable name  \n  • SDTM target domain.variable  \n  • Plain-language completion instruction (≤40 words)\
    \  \n  • Controlled terminology / units  \n  • Allowed query logic (range checks, missing-data rules).\n- At the end,\
    \ provide a one-page “Top 10 data-entry tips” bullet list.\n- Output in CSV-ready Markdown:\n  Variable | Domain | Instruction\
    \ | Terminology/Units | Edit-Check\n- Think through the mapping logic first, then write the table."
- role: user
  content: '{{input}}'
testData:
- input: 'HEIGHT

    '
  expected: 'Variable | Domain | Instruction | Terminology/Units | Edit-Check

    HEIGHT | DM.HEIGHT | Record height in cm | cm | 30-250

    '
evaluators:
- name: Output should start with CSV header
  string:
    startsWith: Variable | Domain | Instruction

```
