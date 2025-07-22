---
id: e2e-test-discovery
title: E2E Test Discovery Template
category: testing_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [testing, qa]
---

# E2E Test Discovery Template

## Purpose

Guide a model to analyze a codebase and produce a comprehensive end‑to‑end test plan.

## Context

This prompt is used with a repository URL or zipped source tree for **{{project_name}}**. Provide the primary tech stack and the high‑level business goal. The assistant acts as an expert test architect and senior software engineer.

## Instructions

1. Map the structure: apps, packages, routes, entry points and existing test frameworks.
1. Outline critical user journeys with triggers, expected behaviour, data mutations and side effects.
1. Catalogue REST/GraphQL endpoints, message queues and third‑party APIs with schemas and auth methods.
1. Identify state management and seed data needed for deterministic tests.
1. Capture non‑functional requirements such as performance, a11y, security and compliance.
1. List validation rules, error branches and retry logic.
1. Describe how to spin up the system locally or in CI and recommend tooling if needed.
1. Produce a table grouping E2E scenarios by theme with priority and test data.
1. Highlight coverage gaps and risk areas.
1. After the first pass, list any open questions before finalizing.

## Inputs

- `{{project_name}}` – name of the project
- `{{languages_frameworks}}` – tech stack
- `{{business_goal}}` – overall objective

## Output Format

Markdown report with sections:

1. Repository Overview
1. Critical User Journeys
1. API / Interface Catalogue
1. State & Data Requirements
1. Non‑Functional Requirements
1. Edge Cases & Negative Paths
1. Environment & Tooling
1. Proposed E2E Test Suite
1. Coverage Gaps & Risk Register

## Additional Notes

Aim for exhaustive coverage. Respond only with the open questions list until all unknowns are resolved.
