---
id: capa-plan-generator
title: CAPA Plan Generator
category: regulatory_quality_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [CAPA, quality]
# CAPA Plan Generator
---

## Purpose

Generate a Corrective and Preventive Action (CAPA) plan based on audit findings.

## Context

You are a GxP audit consultant for a CRO. A draft sponsor audit report lists five major findings.

## Instructions

1. For each finding, conduct root-cause analysis using the 5 Whys method.
2. Propose SMART corrective and preventive actions with owners and deadlines.
3. Describe effectiveness checks.
4. Present results as a CAPA tracker table ready for Excel import.
5. Conclude with one sentence on how the plan prevents recurrence.

## Inputs

- `{{audit_findings}}` — list of major findings.

## Output Format

Markdown table plus short concluding sentence.

## Additional Notes

Ensure alignment with FDA 21 CFR 820.100 and ISO 13485:2016.

<!-- markdownlint-enable MD029 MD036 -->
