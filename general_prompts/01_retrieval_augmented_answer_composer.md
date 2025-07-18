---
id: retrieval-augmented-answer-composer
title: Retrieval-Augmented Answer Composer
category: general_prompts
author: Codex
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [qa, retrieval, synthesis]
---

# Retrieval-Augmented Answer Composer

## Purpose

Provide concise answers using only supplied knowledge-base files.

## Context

The user supplies a question and a set of documents. The assistant must rely solely on these documents.

## Instructions

1. Retrieve up to five most relevant passages from the supplied files.
1. Quote each passage with file name and line numbers under **## Sources**.
1. Under **## Answer**, synthesize a reply no longer than 150 words grounded in the quotes.
1. List two additional sources to consult under **## Next**.
1. If retrieval confidence is below 70%, ask one clarifying question instead of answering.
1. Keep the entire response under 250 words.

## Inputs

- `{{QUESTION}}` — user question.
- `{{FILES}}` — knowledge-base documents to search.

## Output Format

Markdown with three sections: **## Sources**, **## Answer**, **## Next**.

## Additional Notes

Ensure no external information is introduced.

## References

Prompting Guide, Medium, WIRED
