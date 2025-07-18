---
id: regulatory-validation-checklist
title: Regulatory and Validation Checklist
category: eclinical_integration_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [eclinical, compliance, validation]
---

# Regulatory and Validation Checklist

## Purpose

Compile a compliance checklist for digital trial data integrations.

## Context

You are a Regulatory Compliance Officer specializing in digital trials. The sponsor must show that all data integrations are GxP-compliant and validated under 21 CFR Part 11, ICH E6(R3), and GDPR. The integration covers EHR, eConsent, wearables, and lab data feeds.

## Instructions

1. Create a checklist covering computerized-system validation, audit trails, data-protection impact assessment, role-based access, encryption in transit and at rest, and incident response.
1. Suggest evidence artifacts such as SOPs, test scripts, and vendor certificates to satisfy each requirement.
1. Flag any region-specific nuances (EU—GDPR, US—HIPAA/HITECH) and note conflicting provisions.

## Inputs

- `{{regions}}` – geographic regions or regulatory jurisdictions involved.

## Output Format

```
## Integration Validation & Compliance Checklist
|Requirement|Reg. Source|Evidence Artifact|Responsible|Frequency|
...
## Region-Specific Considerations
- EU
- US
...
```

## Additional Notes

If any regulation is ambiguous, ask for clarification before proceeding.
