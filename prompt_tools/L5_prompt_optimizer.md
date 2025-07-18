<!-- markdownlint-disable MD002 MD022 MD032 MD041 MD029 -->
---
id: prompt-optimizer-1-0
title: PromptOptimizer 1.0
category: prompt_tools
author: OpenAI
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [meta, improvement]
---
# PromptOptimizer 1.0


## Purpose
Iteratively refine an instruction set for a given task.

## Context
The tool helps create clearer, unbiased prompts by drafting, critiquing, and rewriting its own instructions.

## Instructions

1. Draft **V1** that solves `{{task}}`.
1. Critique V1 in ≤ 60 words on clarity, completeness, and bias.
1. Rewrite as **V2** addressing every issue.
1. If V2 self-scores ≥ 8/10, output it. Otherwise, repeat steps 2–3 once more, producing **V3**.
1. Present each version under headings `## V1`, `## Critique`, `## V2`, and `## V3` if needed. Limit each version to 150 words.
1. Conclude with a one-sentence reflection (≤ 15 words).

## Inputs

- `{{task}}` – description of the task to optimize.

## Output Format

Markdown sections for each version followed by the final reflection.

## Additional Notes

Use concise language and avoid introducing new objectives.

## References

Microsoft
