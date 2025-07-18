---
id: patient-centric-byod-workflow
title: Patient-Centric BYOD ePRO Workflow
category: epro_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [epro, workflow, byod]
---

# Patient-Centric BYOD ePRO Workflow

## Purpose

Design a streamlined ePRO workflow that supports a BYOD model and maximizes patient compliance.

## Context

You are a clinical operations expert preparing a Phase II trial. The workflow should integrate with Interactive Web Response Systems and include training guides, automated reminders, range validation, and review/edit functionality. Data security must comply with HIPAA and GDPR and remain fully auditable.

## Instructions

1. List key setup steps for implementing BYOD ePRO.
1. Provide a mock screen flow and UX best practices.
1. Describe integration checkpoints with IWRS and other data systems.
1. Ensure patient data is secure and audit ready.

## Inputs

- `{{trial_phase}}` – trial phase and key objectives.
- `{{platform}}` – preferred ePRO platform or tools.

## Output Format

```
A. Key Steps in Setup
...
B. Mock Screen-Flow and UX Best Practices
...
C. Integration Checkpoints
...
```

## Additional Notes

Confirm any assumptions about platform capabilities or security requirements before finalizing the workflow.
