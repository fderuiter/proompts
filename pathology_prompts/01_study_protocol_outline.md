---
id: pathology-study-protocol-outline
title: Design a Robust Preclinical Pathology Study Protocol
category: pathology_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [pathology, protocol]
---

# Design a Robust Preclinical Pathology Study Protocol

## Purpose
Outline a GLP-compliant pathology study plan for a medical device evaluation.

## Context
You are a senior preclinical pathologist. The study must comply with FDA 21 CFR 58 and ISO 10993-6.

## Instructions
1. Provide risk-based selection of species, sample sizes, and timepoints.
2. Describe necropsy procedures, macro- and histopathology endpoints.
3. List staining techniques, scoring criteria, and acceptance thresholds.
4. Explain imaging modalities such as micro-CT or SEM.
5. Include QA steps to maintain GLP compliance.
6. Organize the output under these headings:
   - Study Overview
   - In-life Procedures
   - Pathology Assessments
   - Imaging
   - Quality Assurance
7. Use bullet points under each section.

## Inputs
- `{{study_details}}` – summary of the device and objectives.

## Output Format
Markdown outline using the sections above.

## Additional Notes
Keep language concise and suitable for protocol drafting.
