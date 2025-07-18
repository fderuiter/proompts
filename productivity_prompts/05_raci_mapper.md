---
id: raci-mapper
title: "RACI Mapper"
category: productivity_prompts
author: codex
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.7
tags: [project management, roles]
---

<!-- markdownlint-disable MD029 -->

# RACI Mapper

## Purpose

Clarify team responsibilities using a RACI matrix.

## Context

The user specifies a project phase and key tasks with team member initials.

## Instructions

1. Build a markdown table with columns Task, R, A, C, I for up to six tasks.
1. After the table, add a 35-word reflection highlighting any overload and suggest one reassignment.

## Inputs

- `{{project_phase}}`: project phase description.
- `{{tasks}}`: list of tasks with assigned initials.

## Output Format

Markdown table followed by the reflection paragraph.

## Additional Notes

Keep the response under 130 words and avoid jargon.
