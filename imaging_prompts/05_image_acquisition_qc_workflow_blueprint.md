---
id: imaging-acquisition-qc-workflow
title: Image Acquisition QC Workflow Blueprint
category: imaging_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [imaging, workflow]
---

# Image Acquisition QC Workflow Blueprint

## Purpose
Design a site-facing SOP for image acquisition and quality control.

## Context
You are an imaging-operations director implementing an imaging core lab management system (ICTMS).

- Study description: <<<study_description>>>
- Modalities: MRI (3 T) and low-dose CT
- Sites involved: 30
- Standards: ISO 13485 documentation controls and decentralized-trial elements such as remote upload and eConsent

## Instructions
1. Produce a step-by-step SOP-style flowchart covering site qualification, scanner certification, phantom scans, real-time QC flags, re-acquisition triggers, data privacy safeguards, and KPI dashboards.
2. Present the flowchart as indented text with no more than 12 steps.
3. Provide a linked checklist in a Markdown table with columns **Owner**, **Timing**, and **Audit-Trail Field**.
4. Bold any automated ICTMS step.
5. Ask clarifying questions if needed.

## Inputs
- `<<<study_description>>>` – short trial overview
- `<<<modalities>>>` – modality details if different

## Output Format
Indented flowchart followed by a Markdown table checklist.

## Additional Notes
Focus on practical steps that sites can follow.
