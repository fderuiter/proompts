---
id: optimize-epro-form-design
title: Optimize ePRO Form Design
category: epro_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [epro, design]
---

# Optimize ePRO Form Design

## Purpose

Improve ePRO form usability and data quality.

## Context

You are a user-experience researcher. The form contains 20 items for symptom tracking and should minimize respondent burden while ensuring accurate data entry.

## Instructions

1. Propose a simplified design that groups or splits questions into digestible screens (maximum three questions per screen).
1. Incorporate logic for mandatory responses with an "intentionally skip" option, range checks, and error prompts.
1. Suggest onboarding content such as screenshots and tooltips.
1. Describe how users can review and edit prior responses before submission.
1. Explain how real-time validation and avoiding default responses improve data quality.

## Inputs

- `{{form_items}}` – list of survey questions or data items.

## Output Format

Bullet list or short paragraphs covering each instruction.

## Additional Notes

Focus on clarity and ease of use to maximize patient compliance.
