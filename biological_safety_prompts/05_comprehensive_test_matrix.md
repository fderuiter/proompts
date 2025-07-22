---
id: biological-safety-test-matrix
title: Comprehensive Biocompatibility Test Matrix
category: biological_safety_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [biological safety, testing]
---

# Comprehensive Biocompatibility Test Matrix

## Purpose

Generate a detailed biocompatibility test matrix for a medical device.

## Context

You are the lead biocompatibility scientist at an ISO 17025-accredited lab. Follow the FDA-modified ISO 10993 endpoint matrix.

## Instructions

1. For each endpoint, specify test type (in vitro, in vivo, or NAM).
1. List the relevant standard and edition (ISO/ASTM/USP).
1. Provide sample conditioning and extraction details per FDA guidance.
1. Note acceptance criteria and rationale.
1. Suggest potential NAM replacements to reduce animal use.

## Inputs

- `{{device_materials}}` — materials and clinical-use scenario

## Output Format

Two-level markdown table followed by concise explanatory notes.

## Additional Notes

Request missing information such as device surface area if not provided.
