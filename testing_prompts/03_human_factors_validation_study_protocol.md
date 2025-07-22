---
id: human-factors-validation-protocol
title: Human Factors Validation Study Protocol
category: testing_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [testing, human factors]
---

# Human Factors Validation Study Protocol

## Purpose

Draft a user validation study protocol for a medical device.

## Context

You are a human‑factors specialist preparing the design validation protocol for **{{device_name}}**. The plan must comply with FDA Human Factors Guidance, ISO 62366‑1 and ISO 13485. Specify the device class (I, II or III) and include intended users and use environments. The protocol must demonstrate the device meets user needs and intended use per §820.30(g). Maintain a formal tone suitable for a regulatory submission. Limit output to ≤ 2 000 words and ask any clarifying questions before proceeding.

## Instructions

1. Outline the purpose and regulatory basis.
1. Define study objectives and success metrics.
1. Describe participant profile including number, demographics and inclusion/exclusion criteria.
1. Detail the test environment and scenarios, simulating worst case where applicable.
1. Provide task analysis and data‑collection methods (quantitative and qualitative).
1. Specify risk‑mitigation triggers and stop rules.
1. Present the data analysis plan.
1. List deliverables and acceptance criteria.

## Inputs

- `{{device_name}}` – name of the device
- `{{class}}` – device class

## Output Format

Structured Markdown outline with numbered sections corresponding to the instructions.

## Additional Notes

Confirm any missing design inputs before finalizing the protocol.
