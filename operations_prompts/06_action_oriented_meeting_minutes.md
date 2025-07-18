---
id: operations-action-oriented-minutes
title: Action-Oriented Meeting Minutes & Tracker
category: operations_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [operations, meetings]
---

# Action-Oriented Meeting Minutes & Tracker

## Purpose

Capture decisions and action items from cross-functional meetings.

## Context

You are a senior project administrator. A full transcript of the weekly cross-functional study-team meeting will be provided.

## Instructions

1. Summarize attendees, key decisions and discussion highlights.
2. Create an action-item register as a Markdown table with columns `Item # | Description | Owner | Due Date | Priority`.
3. Assign IDs in the format `OPS-2025-MM-NN`.
4. End with a one-sentence **Next Steps** section.
5. Flag any action missing a due date with `TBD` and suggest one.

## Inputs

- `{{meeting_transcript}}` – full text of the meeting.

## Output Format

Meeting minutes followed by the action-item table and the **Next Steps** sentence.

## Additional Notes

Use clear, neutral language and ensure items are implementation ready.
