---
id: 03-rbm-plan-builder
title: Risk-Based Monitoring (RBM) Plan Builder
category: cra_prompts
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: []
---

# Risk-Based Monitoring (RBM) Plan Builder

## Purpose

```

## Context

## Instructions

**System (role):** You are a clinical risk-management consultant.

**User instruction:** Develop a site-level RBM plan for a Phase II oncology study, focusing on proactive detection of high-impact risks.

Context:  
"""
• Study phase/indication: Phase II, metastatic NSCLC  
• Enrollment goal: 150 participants, 10 sites  
• Known risk factors: high AE rate, complex biomarker sampling, decentralized ePRO  
• Regulatory expectation: ICH E6 (R3) & FDA guidance on risk-based monitoring (2019)  
"""

**Deliverables (markdown):**  
1. **Risk Assessment Matrix** (table: Risk │ Root Cause │ Likelihood │ Impact │ Mitigation KPI)  
2. **Key Risk Indicators (KRIs)** (≤ 8, define calculation & alert threshold)  
3. **Adaptive Monitoring Strategy** – outline trigger logic for remote vs. on-site, including minimum visit frequency  
4. **Data-quality Checks** – list automated queries to run weekly with pseudo-SQL examples  
5. **Escalation Pathway** – who is notified and within what timeline  
```

## Inputs

## Output Format

## Additional Notes
