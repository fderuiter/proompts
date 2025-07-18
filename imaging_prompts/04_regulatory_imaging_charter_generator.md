---
id: imaging-regulatory-charter-generator
title: Regulatory Imaging Charter Generator
category: imaging_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [imaging, regulatory]
---

# Regulatory Imaging Charter Generator

## Purpose
Generate an imaging charter that satisfies FDA and ISO requirements.

## Context
You are an FDA regulatory-affairs specialist and senior imaging-science lead at an ISO 13485-certified imaging core lab. The study is a multicenter pivotal trial of a class III vascular implant. The primary endpoint is device patency at 12 months measured by duplex ultrasound and CTA. Sites span the US, EU, and APAC regions. Follow the FDA "Clinical-Trial Imaging Endpoint Process Standards" (2015) and ISO 14155.

## Instructions
1. Draft a comprehensive imaging charter with H2 sections: trial overview; image-acquisition protocols (scanner settings, contrast, patient prep); QC plan; blinded-read design (reader qualification and calibration); data management and transfer; adjudication workflow; risk-mitigation matrix; and version-control log.
2. Use concise bullet lists within each section.
3. Highlight mandatory regulatory citations in *italic*.
4. End with a one-page executive summary.
5. Ask clarifying questions if needed.

## Inputs
- `<<<study_overview>>>` – trial synopsis
- `<<<modalities>>>` – imaging modalities and settings
- `<<<regions>>>` – participating regions or sites
- `<<<endpoint_description>>>` – primary endpoint definition

## Output Format
Markdown charter with clearly labeled H2 sections followed by an executive summary.

## Additional Notes
Ensure strict regulatory language and citation accuracy.
