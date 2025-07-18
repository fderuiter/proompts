---
id: fishbone-facilitator
title: "Fishbone Facilitator"
category: productivity_prompts
author: codex
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.7
tags: [root cause analysis]
---

<!-- markdownlint-disable MD029 -->

# Fishbone Facilitator

## Purpose

Identify possible root causes of a problem using a fishbone diagram.

## Context

Ask for the main effect statement if it is not provided.

## Instructions

1. Generate a text-based fishbone with six categories: Methods, Machines, People, Materials, Environment and Measurement.
1. Under each category, list two concise possible causes.
1. End with a 30-word note on which cause to probe first and why.

## Inputs

- `{{problem}}`: main effect statement describing the problem.

## Output Format

Bullet list or table representing the fishbone followed by the investigation note.

## Additional Notes

Limit the entire reply to 120 words.
