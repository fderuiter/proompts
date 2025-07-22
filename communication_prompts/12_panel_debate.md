---
id: 12-panel-debate
title: Panel Debate
category: communication_prompts
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: []
---

# Panel Debate

## Purpose

Host a simulated debate among three experts on a chosen topic.

## Context

Participants are [Proponent], [Opponent], and a neutral Moderator. The user supplies the topic.

## Instructions

<!-- markdownlint-disable MD002 MD022 MD041 MD029 -->

1. Each expert delivers an opening statement (≤ 60 words each).
1. Run two rebuttal rounds (≤ 40 words per speaker per round).
1. After debates, the Moderator provides a table summarizing consensus and disputes. Columns: *Point* and *Agreement?* (Yes/No).
1. End with a 100-word balanced takeaway including one actionable recommendation.

Label each section clearly and use plain language.

## Inputs

- `{{topic}}` – the subject of the debate.

## Output Format

Structured sections for opening statements, rebuttal rounds, table summary, and final takeaway.

## Additional Notes

Keep responses concise and avoid bias.

## References

Tom's Guide
