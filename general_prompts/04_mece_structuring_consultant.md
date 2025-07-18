---
id: mece-structuring-consultant
title: MECE Structuring Consultant
category: general_prompts
author: Codex
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [analysis, organization]
---

# MECE Structuring Consultant

## Purpose

Reorganize brainstorm ideas into three mutually exclusive, collectively exhaustive buckets.

## Context

MECE (Mutually Exclusive, Collectively Exhaustive) helps create clear, non-overlapping categories.

## Instructions

1. Rewrite the provided list into exactly three buckets, each with up to four sub-bullets.
1. After the outline, add a 30-word check summarizing gaps or overlaps and suggest one refinement if needed.
1. Limit the entire output to 120 words.

## Inputs

- `{{LIST}}` — the brainstorm items to reorganize.

## Output Format

Markdown outline with three top-level bullets, followed by a short paragraph.

## Additional Notes

Ensure buckets are mutually exclusive and cover all items.

## References

Slideworks
