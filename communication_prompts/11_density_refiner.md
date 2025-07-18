---
id: communication-density-refiner
title: Density Refiner
category: communication_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [communication, summary]
---

<!-- markdownlint-disable MD029 -->

# Density Refiner

## Purpose

Craft a concise yet information-rich summary of provided text.

## Context

Use Chain-of-Density summarization to tighten coverage without length creep.

## Instructions

1. Produce an entity-sparse gist in 120 words or fewer.
1. List missing key nouns in 40 words or fewer.
1. Rewrite a denser summary under 120 words using those nouns.
1. End with a 15-word reflection on what detail improved.
1. Label sections **Gist**, **Missing Entities**, **Dense Summary**, and **Reflection**.

## Inputs

- `{{text}}`: passage to summarize.

## Output Format

Markdown with four labeled sections.

## Additional Notes

Chain-of-Density helps retain key entities while keeping the summary short.

## References

Analytics Vidhya; Prompthub
