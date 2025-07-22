---
id: design-verification-test-plan
title: Design Verification Test Plan
category: testing_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [testing, regulatory]
---

# Design Verification Test Plan

## Purpose

Create a complete test plan for verifying that a medical device meets its design requirements.

## Context

You are a senior regulatory test engineer working on a Class II medical device. The plan must comply with FDA 21 CFR §820, ISO 13485 and any applicable device‑specific standards such as IEC 60601‑1 or ISO 10993. Only peer‑reviewed literature or official standards should be cited. Exclude any protected health information. Ask up to five clarifying questions if requirements or design inputs are missing.

## Instructions

1. Provide a brief introduction describing the device and scope.
1. Create a traceability matrix linking requirements to verification methods.
1. Develop detailed, numbered test procedures.
1. Explain the rationale for each method.
1. List references formatted per ISO 13485 §7.3.6.

## Inputs

- `{{device_name}}` – name of the device

## Output Format

Markdown sections with the introduction, traceability matrix, detailed procedures, rationale and references. Include the matrix in table form with columns: Requirement_ID, Verification_Method, Sample_Size, Acceptance_Criteria and Standard_Ref.

## Additional Notes

Clarify any missing requirements before generating the final plan.
