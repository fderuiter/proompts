---
id: eisenhower-matrix-coach
title: "Eisenhower Matrix Coach"
category: productivity_prompts
author: codex
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.7
tags: [productivity, prioritization]
---

<!-- markdownlint-disable MD029 -->

# Eisenhower Matrix Coach

## Purpose

Triage a to-do list using the Eisenhower Matrix.

## Context

The user provides a list of tasks and wants them sorted by urgency and importance.

## Instructions

1. Create a markdown table with headers: ✅ Do Now, 📅 Schedule, ↗ Delegate, 🗑 Delete.
1. Place each task in the appropriate quadrant and add a short reason.
1. End with a 40-word focus plan referencing two Do Now tasks, one Schedule item and a delegation tip.

## Inputs

- `{{tasks}}`: list of tasks to triage.

## Output Format

Markdown table followed by the focus plan.

## Additional Notes

Keep the entire reply under 150 words.
