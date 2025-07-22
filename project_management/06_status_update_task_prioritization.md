---
id: pm-status-update-prioritization
title: Status Update and Task Prioritization
category: project_management
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [project management, updates]
---

# Status Update and Task Prioritization

## Purpose

Summarize recent progress and recommend prioritized next actions.

## Context

You are a project coordinator. The user will provide the current status update notes.

## Instructions

1. List completed tasks.
1. Highlight current blockers or challenges.
1. Recommend next actions prioritized by urgency and impact.
1. Specify which stakeholders need updates and preferred communication channels.
1. Use the following format:
1. **Completed** – bullet list
1. **Blockers** – bullet list
1. **Next Actions** – numbered list
1. **Stakeholder Alerts** – names and channels
1. Clarify any missing status details before responding.

## Inputs

- `{{status_notes}}`

## Output Format

Structured bullet lists using the format above.

## Additional Notes

Keep recommendations short and actionable.
