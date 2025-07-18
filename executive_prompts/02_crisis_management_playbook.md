---
id: crisis-management-playbook
title: Crisis-Management Playbook Generator
category: executive_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [executive, risk]
---

# Crisis-Management Playbook Generator

## Purpose
Provide a concise playbook for handling critical incidents affecting customer data.

## Context
Act as the Chief Risk Officer with experience in Fortune 100 crisis response. The scenario is a newly discovered vulnerability in our flagship SaaS platform that could expose customer data.

## Instructions
1. Create a decision-making tree indicating who approves what and in what timeframe.
1. Provide immediate communication templates for internal teams, media, and regulators.
1. Outline technical containment steps at a high level.
1. Define after-action review criteria and timeline.
Follow ISO 22361 terminology and maintain a calm, authoritative tone. Use bullet lists and tables for clarity.

## Inputs

- `{{incident_details}}` – short description of the security incident.

## Output Format

Markdown with sections for decision tree, communication templates, containment steps, and after-action review.
After each main section, add one question to confirm assumptions before finalization.

## Additional Notes
Limit the playbook to four pages and focus on actions that preserve customer trust.
