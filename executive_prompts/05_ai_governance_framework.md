---
id: ai-governance-framework
title: FDA-Aligned AI Governance Framework
category: executive_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [executive, ai]
---

# FDA-Aligned AI Governance Framework

## Purpose

Draft an AI governance framework that satisfies regulators and sponsors.

## Context

You are a life-sciences compliance consultant specializing in AI. The FDA’s January 2025 draft guidance “Considerations for the Use of Artificial Intelligence to Support Regulatory Decision-Making” introduces a risk-based credibility framework. Our CRO plans to embed generative-AI tools in protocol authoring and TMF automation.

## Instructions

1. Summarize the five most relevant obligations from the 2025 FDA draft: model documentation, context of use, data quality, bias testing, and audit trail.
1. Map each obligation to concrete CRO policies, owners, and evidence artifacts.
1. Recommend a phased rollout plan (Pilot → Limited Production → Full Production) including success criteria and go/no-go gates.
1. Provide a one-page risk register with top five risks, likelihood, impact, and mitigation.

Only output a structured outline using Heading 2 for each major section and limit the response to 600 words.

## Inputs

- `{{existing_policies}}` – current AI or data governance policies.

## Output Format

Markdown outline with sections for obligations, policy mapping, rollout plan, and risk register.

## Additional Notes

Do not reveal your internal reasoning steps.
