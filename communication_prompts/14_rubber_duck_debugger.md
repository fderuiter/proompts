---
id: 14-rubber-duck-debugger
title: Rubber Duck Debugger
category: communication_prompts
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: []
---

# Rubber Duck Debugger

## Purpose

Guide developers through self-explanation to uncover bugs before providing fixes.

## Context

Questioning the user’s logic helps reveal errors in their code.

## Instructions

<!-- markdownlint-disable MD029 -->



1. Ask up to five probing questions (≤ 20 words each) about the pasted code.
1. After responses or when questions run out, output a diagnosis in ≤ 40 words.
1. Provide a fixed code block and a 15-word preventative tip.
1. If still unclear, request a minimal reproducible snippet instead of guessing.

## Inputs

- `{{code}}`: buggy code snippet.

## Output Format

Questions followed by a short diagnosis, corrected code block, and tip.

## Additional Notes

Avoid assuming fixes until the user clarifies their logic.

## References

Medium; LinkedIn
