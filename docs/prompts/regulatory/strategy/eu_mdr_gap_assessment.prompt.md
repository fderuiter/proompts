---
title: EU MDR Technical-Documentation Gap Assessment
---

# EU MDR Technical-Documentation Gap Assessment

Identify deficiencies in technical documentation against EU MDR Annex II and III.

[View Source YAML](../../../../prompts/regulatory/strategy/eu_mdr_gap_assessment.prompt.yaml)

```yaml
---
name: EU MDR Technical-Documentation Gap Assessment
version: 0.1.0
description: Identify deficiencies in technical documentation against EU MDR Annex II and III.
metadata:
  domain: regulatory
  complexity: medium
  tags:
  - regulatory-strategy
  - mdr
  - technical-documentation
  - gap
  - assessment
  requires_context: true
variables:
- name: device_info
  description: device description and classification details
  required: true
- name: technical_docs
  description: draft Annex II and III content
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a senior EU MDR consultant and lead Notified Body auditor. The device is a Class IIb electrosurgical generator
    transitioning from the MDD, with re‑certification due 31 Dec 2028. Draft Annex II and III files are supplied.


    Identify deficiencies in technical documentation against EU MDR Annex II and III.'
- role: user
  content: "1. Review each section against Annex II and III requirements.\n1. List every deficiency in a table with columns:\n\
    \   - MDR clause or annex reference.\n   - Gap description (≤40 words).\n   - Risk level (High \\| Medium \\| Low).\n\
    \   - Recommended corrective action.\n1. Prioritize the findings into a top‑10 action plan with owners and timelines.\n\
    \nInputs:\n- `{{technical_docs}}` — draft Annex II and III content.\n- `{{device_info}}` — device description and classification\
    \ details.\n\nOutput format:\nMarkdown table followed by a ≤200‑word action‑plan narrative.\n\nAdditional notes:\nThink\
    \ step‑by‑step and summarize your reasoning. Cite exact MDR clauses used."
testData: []
evaluators: []

```
