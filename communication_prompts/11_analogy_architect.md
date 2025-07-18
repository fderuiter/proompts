<!-- markdownlint-disable MD029 -->
---
id: analogy-architect
title: "Analogy Architect"
category: communication_prompts
author: "OpenAI"
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.7
tags: [communication, analogies]
---

# Analogy Architect

## Purpose

Help the user grasp a complex topic through everyday analogies.

## Context

The caller supplies `{{complex_topic}}`. The reply must stay under 120 words.

## Instructions

1. Create three analogies linking everyday objects to `{{complex_topic}}`.
1. **Bold** each object and map its parts to the concept in 40 words or fewer.
1. Provide one real-life scenario showing the analogy's usefulness.
1. After all three, write a 30-word accuracy check noting each comparison's limits.

## Inputs

- `{{complex_topic}}`: subject to explain.

## Output Format

Bulleted analogies followed by a short accuracy check.

## References

- Medium
- Lewis C. Lin
- Tom's Guide
