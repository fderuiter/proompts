<!-- markdownlint-disable MD029 -->
---
id: comprehensive-task-template
title: Comprehensive Task Template
category: meta_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [meta, planning]
---

# Comprehensive Task Template

## Purpose

Provide a reusable prompt that guides an AI through planning, execution and self-checking for any complex task.

## Context

Copy the template and fill in the bracketed sections to suit your use case.

## Instructions

1. Begin with the role line: “You are [expert role]. Your mission is to perform [task] thoroughly.”
1. Enumerate all sub‑topics and edge cases before starting work.
1. For each item, dig until all relevant detail is addressed or further detail would be redundant.
1. Deliver an executive summary, detailed walkthrough, assumptions and sources, and a self-audit checklist.
1. Use plain language and prefer bullets or tables when helpful.

## Inputs

- `{{expert_role}}` – role the agent should assume
- `{{task}}` – description of the task

## Output Format

Markdown with clearly labelled sections matching the instructions.

## Additional Notes

Highlight gaps or unknowns and suggest how to obtain missing information.
