---
title: FDA Missing-Data Query Response
---

# FDA Missing-Data Query Response

Draft a response letter to an FDA information request about missing data.

[View Source YAML](../../../../prompts/scientific/biostatistics/fda_missing_data_query_response.prompt.yaml)

```yaml
---
name: FDA Missing-Data Query Response
version: 0.1.0
description: Draft a response letter to an FDA information request about missing data.
metadata:
  domain: scientific
  complexity: medium
  tags:
  - biostatistics
  - fda
  - missing-data
  - query
  - response
  requires_context: false
variables:
- name: fda_questions
  description: '`{{sap_references}}`'
  required: true
- name: sap_references
  description: The sap references to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a senior regulatory statistician preparing a Type C meeting package. The FDA has questioned the robustness
    of the Week 52 remission endpoint given 9 % missing data and potential MNAR bias.


    Ask clarifying questions before drafting if critical details are missing.'
- role: user
  content: '1. Summarize the agency’s concerns in plain English.

    2. Present planned sensitivity analyses (MI under MNAR, tipping point, δ-adjusted worst-case).

    3. Justify the primary estimand choice (treatment policy) per ICH E9(R1).

    4. Reference relevant guidance (FDA Missing Data 2019, EMA Guideline 07/2022).

    5. Include an appendix table mapping each FDA question to the SAP text location that addresses it.

    6. Draft in formal, concise regulatory style (≤8 pages) using numbered sections matching the FDA’s bullets.

    7. Highlight any additional data or simulations proposed.

    8. Conclude with a request for the agency’s confirmation that the approach is adequate.


    Inputs:

    - `{{fda_questions}}`

    - `{{sap_references}}`


    Output format:

    Word-style Markdown outline with H1/H2 sections plus the appendix table.'
testData:
- vars:
    fda_questions: example_fda_questions
    sap_references: example_sap_references
  expected: Word-style Markdown outline with H1/H2 sections plus the appendix table.
evaluators:
- name: Output starts with '# '
  string:
    startsWith: '# '

```
