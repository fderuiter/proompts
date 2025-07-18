---
id: decentralized-trial-risk-matrix
title: Decentralized Trial Risk Matrix
category: data_management_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [clinical, risk]
---

# Decentralized Trial Risk Matrix

Title: Evaluate Decentralized Trial Data Risks

Role: CRO Director

Task:
- Produce a risk matrix listing Risk, Source, Likelihood, Impact, Mitigation and Owner.
- Summarise the three highest residual risks with escalation triggers in ≤ 300 words.

Context:
"""
Study: Hybrid Phase III oncology, 120 sites, BYOD ePRO, wearables and home nursing.
Data sources: Rave EDC, eConsent, wearable JSON API and central lab.
Regulations: ICH E6(R2), FDA Decentralized Trials Guidance (May 2023), GDPR.
Scoring uses 1–5 for likelihood and impact.
"""

Constraints:
- Use quantitative scores.
- Mitigations must be actionable and vendor-oversight ready.

Output Format: markdown
--------------------------------------------------
