---
title: Regulatory Filing Draft Builder
---

# Regulatory Filing Draft Builder

Produce a regulator‑ready draft document using provided financials and risk data.

[View Source YAML](../../../../prompts/regulatory/strategy/regulatory_filing_draft_builder.prompt.yaml)

```yaml
---
name: Regulatory Filing Draft Builder
version: 0.1.0
description: Produce a regulator‑ready draft document using provided financials and risk data.
metadata:
  domain: regulatory
  complexity: high
  tags:
  - regulatory-strategy
  - regulatory
  - filing
  - draft
  - builder
  requires_context: false
variables:
- name: DATE
  description: The DATE to use for this prompt
  required: true
- name: DOCUMENT_TYPE
  description: The DOCUMENT TYPE to use for this prompt
  required: true
- name: REGULATOR
  description: The REGULATOR to use for this prompt
  required: true
- name: SPECIFIC_GUIDELINE
  description: The SPECIFIC GUIDELINE to use for this prompt
  required: true
- name: financial_data
  description: Data Sheet 1
  required: true
- name: prior_filing
  description: previous submission
  required: true
- name: risk_memo
  description: risk factors
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a compliance‑documentation specialist writing for `{{REGULATOR}}` and following `{{SPECIFIC_GUIDELINE}}`.
    Tone is formal and objective. Financials come from Data Sheet 1, risk factors from the memo dated `{{DATE}}`, and prior
    filings from Appendix C.


    Produce a regulator‑ready draft document using provided financials and risk data.'
- role: user
  content: "1. Draft the `{{DOCUMENT_TYPE}}` using the structure:\n\n   I. Cover Page\n   II. Business Overview\n   III. Management’s\
    \ Discussion & Analysis\n   IV. Financial Statements (summarized tables)\n   V. Risk Factors (ranked)\n   VI. Compliance\
    \ Declarations\n\n1. Cross‑check figures against Data Sheet 1 and flag discrepancies over 1 %.\n1. Insert `Reviewer-Comment`\
    \ placeholders wherever data is missing.\n1. Conclude with a self‑assessment table rating Accuracy, Completeness, Clarity,\
    \ and Timeliness on a 1‑5 scale.\n1. Deliver in GitHub‑Flavored Markdown so teams can redline easily.\n1. Do not fabricate\
    \ numbers; leave blank if data is absent.\n1. Keep each section ≤400 words unless otherwise noted.\n1. Provide three follow‑up\
    \ questions that would improve accuracy.\n\nInputs:\n- `{{financial_data}}` — Data Sheet 1.\n- `{{risk_memo}}` — risk\
    \ factors.\n- `{{prior_filing}}` — previous submission.\n\nOutput format:\nGFM document with clearly marked sections and\
    \ the final self‑assessment table.\n\nAdditional notes:\nMaintain a regulator‑friendly tone and highlight missing information."
testData: []
evaluators: []

```
