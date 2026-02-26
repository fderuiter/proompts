---
title: MECE Structuring Consultant
---

# MECE Structuring Consultant

Reorganize brainstorm ideas into three mutually exclusive, collectively exhaustive buckets.

[View Source YAML](../../../../prompts/meta/meta_prompt_chain/05_L5_mece_structuring.prompt.yaml)

```yaml
---
name: MECE Structuring Consultant
version: 0.1.0
description: Reorganize brainstorm ideas into three mutually exclusive, collectively exhaustive buckets.
metadata:
  domain: meta
  complexity: low
  tags:
  - mece
  - structuring
  - consultant
  requires_context: true
variables:
- name: LIST
  description: the brainstorm items to reorganize
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'MECE (Mutually Exclusive, Collectively Exhaustive) helps create clear, non-overlapping categories.


    1. Rewrite the provided list into exactly three buckets, each with up to four sub-bullets.

    2. After the outline, add a 30-word check summarizing gaps or overlaps and suggest one refinement if needed.

    3. Limit the entire output to 120 words.


    Ensure buckets are mutually exclusive and cover all items.


    References: Slideworks'
- role: user
  content: '- `{{LIST}}` — the brainstorm items to reorganize.


    Output format: Markdown outline with three top-level bullets, followed by a short paragraph.'
testData: []
evaluators: []

```
