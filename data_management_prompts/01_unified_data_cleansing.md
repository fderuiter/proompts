---
id: unified-data-cleansing
title: Unified Data Cleansing
category: data_management_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [data, cleansing]
---

# Unified Data Cleansing

Title: Clean and Merge Data Sources

Role: Senior Data Engineer

Task:

- Detect schema mismatches, missing values and outliers.
- Propose normalization rules for naming, types, units and time zones.
- Provide Python pseudocode to load sources, apply rules and output one DataFrame.
- List assumptions and ask clarifying questions for ambiguities.

Context:
"""
Source-1: 2024-Q4 e-commerce CSV.
Source-2: CRM export (JSON).
Goal: build an analysis-ready table by close of business.
"""

Constraints:

- Use fenced `python` blocks for pseudocode.
- End with bullet questions that remain open.

## Output Format

Markdown
