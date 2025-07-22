---
id: agentic-coding-session-guidelines
title: Coding Session Guidelines
category: agentic_coding
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: [coding, workflow]
---

# Coding Session Guidelines

## Purpose

Provide step-by-step guidance for running productive coding sessions.

## Context

Use these guidelines while developing a project with automated testing and persistent memory.

## Instructions

1. Write tests first for each task.
1. Implement code to satisfy the tests.
1. Run `dotnet test` or filtered tests to verify success and fix failures immediately.
1. After each task:
   - run tests again
   - update the to-do list
   - update `memory.md` with key state changes
   - capture lessons learned
   - end the chat session cleanly
1. Always reference `memory.md` to maintain context between sessions.

## Inputs

None

## Output Format

Clear Markdown checklist of steps completed during the session.

## Additional Notes

Maintain the to-do list and memory file to ensure continuity across sessions.
