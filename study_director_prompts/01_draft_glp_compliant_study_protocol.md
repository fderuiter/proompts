---
id: draft-glp-compliant-study-protocol
title: Draft a GLP-Compliant Study Protocol
category: study_director_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [study design, glp]
---

# Draft a GLP-Compliant Study Protocol

## Purpose
Produce a detailed study plan that satisfies OECD and FDA GLP regulations.

## Context
You are a senior toxicologist preparing a 28‑day oral toxicity study (OECD TG 407) in Sprague‑Dawley rats for Test Article X to support an IND.

## Instructions
1. Outline objectives and scientific rationale.
2. Specify dose groups with rationale and mg kg⁻¹ day⁻¹ levels.
3. Describe experimental design—n/group, randomization, critical endpoints, and interim kills.
4. Provide a Gantt-style timeline of milestones.
5. List quality-assurance checkpoints and record-keeping requirements.
6. Summarize potential protocol pitfalls with up to five mitigation bullet points.

## Inputs
- `{{protocol_basics}}` – any additional study parameters.

## Output Format
Numbered outline followed by a CSV-ready risk-mitigation table with columns: Phase, Risk, Impact, Mitigation.

## Additional Notes
Reason step-by-step before writing but reveal only the final protocol.
