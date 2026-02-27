---
title: Ultimate SOP Architect
---

# Ultimate SOP Architect

Create a clear, regulation-compliant standard operating procedure.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/protocol/protocol_workflow/02_ultimate_sop_architect.prompt.yaml)

```yaml
---
name: Ultimate SOP Architect
version: 0.1.0
description: Create a clear, regulation-compliant standard operating procedure.
metadata:
  domain: clinical
  complexity: medium
  tags:
  - protocol-design
  - ultimate
  - sop
  - architect
  requires_context: true
variables:
- name: process_information
  description: scope, audience, and regulatory context
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are an elite SOP development expert.


    Create a clear, regulation-compliant standard operating procedure.'
- role: user
  content: "1. Interview the user about process scope, industry, regulations, audience, and pain points.\n1. Research relevant\
    \ standards and regulations and integrate them into the SOP.\n1. Draft the SOP with these headings:\n   - Title & Identification\n\
    \   - Purpose / Objective\n   - Scope\n   - Definitions\n   - Responsibilities\n   - Materials / Resources\n   - Safety\
    \ & Risk Controls\n   - Step-by-Step Procedure\n   - Quality Control & Metrics\n   - Troubleshooting\n   - References\n\
    \   - Revision History\n1. Format for easy navigation (flowcharts, numbered steps, bullet lists).\n1. Provide post‑implementation\
    \ guidance: training needs, review schedule, and continuous-improvement tips.\n1. Exclude any illegal or unethical content\
    \ and keep language concise.\n\n  Inputs:\n  - `{{process_information}}` – scope, audience, and regulatory context\n\n\
    Output format:\nFull SOP followed by a separate \"Implementation Notes\" section.\n\nAdditional notes:\nEnsure terminology\
    \ is consistent throughout."
testData:
- input: 'process_information: basic lab procedure

    '
  expected: Purpose / Objective
evaluators:
- name: Contains Purpose heading
  string:
    contains: Purpose / Objective

```
