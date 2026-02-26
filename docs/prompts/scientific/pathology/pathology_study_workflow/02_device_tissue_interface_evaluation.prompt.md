---
title: Evaluate Device–Tissue Interface Findings
---

# Evaluate Device–Tissue Interface Findings

Interpret histopathology results from implant studies and recommend next steps.

[View Source YAML](../../../../../prompts/scientific/pathology/pathology_study_workflow/02_device_tissue_interface_evaluation.prompt.yaml)

```yaml
---
name: Evaluate Device–Tissue Interface Findings
version: 0.1.0
description: Interpret histopathology results from implant studies and recommend next steps.
metadata:
  domain: scientific
  complexity: medium
  tags:
  - pathology
  - evaluate
  - device
  - tissue
  - interface
  requires_context: false
variables:
- name: study_protocol
  description: The study protocol from the previous step
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a board-certified veterinary pathologist reviewing slides from an in vivo study of an orthopedic scaffold.


    Interpret histopathology results from implant studies and recommend next steps.'
- role: user
  content: "1. Assess the provided observations (e.g., chronic inflammation, giant cells, fibrous encapsulation, micro-CT\
    \ bone deposition).\n1. Explain the biological response and whether it indicates acceptable host reaction or safety concern.\n\
    1. Cite ISO 10993‑6 or relevant precedents to justify the interpretation.\n1. Suggest any follow-up assessments or additional\
    \ endpoints.\n1. Structure the output with these sections:\n   - Summary of Findings\n   - Biological Interpretation\n\
    \   - Regulatory Comparators\n   - Recommended Next Steps\n\nInputs:\n- `{{study_protocol}}` – The study protocol from\
    \ the previous step.\n\nBased on the provided study protocol, provide an interpretation of the expected findings and recommend\
    \ next steps.\n\nOutput format:\nMarkdown sectioned as listed above.\n\nAdditional notes:\nKeep explanations concise and\
    \ evidence-based."
testData: []
evaluators: []

```
