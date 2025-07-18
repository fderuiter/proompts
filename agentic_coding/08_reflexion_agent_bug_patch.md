<!-- markdownlint-disable MD029 -->
---
id: reflexion-agent-bug-patch
title: "Reflexion Agent Bug Patch"
category: agentic_coding
author: "OpenAI"
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.7
tags: [debugging, reflexion]
---

# Reflexion Agent Bug Patch

## Purpose

Locate and fix a bug using a structured reflexion workflow.

## Context

The user provides code snippet `{{code}}`. Follow Reflexion Agent v1.3 practices.

## Instructions

1. Hypothesize the root cause in 50 words or fewer.
1. Self-evaluate confidence and list any knowledge gaps in ≤ 30 words.
1. Reflect and revise the hypothesis once.
1. If confidence is ≥ 70%, output the corrected code block plus a 20-word rationale.
1. If confidence is below 70%, ask one clarifying question instead.

## Inputs

- `{{code}}`: code containing the bug.

## Output Format

Markdown with code fences for the patch and a short rationale. Entire reply ≤ 120 words.

## References

- Prompting Guide
- Taylor & Francis Online
