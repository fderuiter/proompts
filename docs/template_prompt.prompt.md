---
name: Text Summarizer
version: 1.0.0
description: Summarizes input text concisely
metadata:
  domain: general
  complexity: low
  tags:
  - summarization
  - text-processing
  - skill
  requires_context: false
variables:
- name: input
  description: The text to summarize.
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.5
testData:
- input: |
    The quick brown fox jumped over the lazy dog.
    The dog was too tired to react.
  expected: Summary - A fox jumped over a lazy, unresponsive dog.
evaluators:
- name: Output should start with 'Summary -'
  string:
    startsWith: Summary -
---

## Purpose
You are a text summarizer. Your only job is to summarize text given to you.

## Instructions
Summarize the given text, beginning with "Summary -":
<input>
{{ input }}
</input>
