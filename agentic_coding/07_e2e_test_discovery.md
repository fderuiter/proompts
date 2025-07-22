---
id: agentic-e2e-test-discovery
title: E2E Test Discovery Template
category: agentic_coding
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: [testing, planning]
---

# E2E Test Discovery Template

## Purpose

Provide a system prompt template that guides an LLM to analyse a codebase and generate a comprehensive end-to-end test plan.

## Context

Use this template with ChatGPT or another GPT-4 class model. Fill in placeholders for project specifics and supply repository access when prompted.

## Instructions

1. Explain that the assistant acts as a Test Architect analysing the supplied codebase.
1. Provide the following context variables:
   - `{{PROJECT_NAME}}`
   - `{{LANGUAGES/FRAMEWORKS}}`
   - `{{BUSINESS_GOAL}}`
1. Direct the assistant to map the structure, user journeys, interfaces, data fixtures, non-functional requirements, edge cases, environment details, test plan skeleton, and coverage gaps.
1. Instruct it to return a markdown report with numbered sections covering each topic.
1. Tell the assistant to ask clarifying questions first if information is missing.

## Inputs

- `{{PROJECT_NAME}}` – project identifier
- `{{LANGUAGES/FRAMEWORKS}}` – primary tech stack
- `{{BUSINESS_GOAL}}` – high-level goal of the system

## Output Format

Markdown report with sections:

1. Repository Overview
1. Critical User Journeys
1. API / Interface Catalogue
1. State & Data Requirements
1. Non-Functional Requirements
1. Edge Cases & Negative Paths
1. Environment & Tooling
1. Proposed E2E Test Suite
1. Coverage Gaps & Risk Register

## Additional Notes

After the first pass, list any open questions and wait for responses before finalising the plan. Aim for exhaustive coverage and actionable next steps.
