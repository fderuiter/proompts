---
id: regulatory-gap-analysis
title: Regulatory Gap Analysis
category: data_management_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [compliance, governance]
---

# Regulatory Gap Analysis

Title: Audit Data Governance vs Regulations

Role: Chief Data Officer

Task:

- Map each policy clause to GDPR Art.5 and EU AI Act Title IV.
- Flag partial or missing coverage.
- Rate risk severity and business impact.
- Recommend top five remediation actions in priority order.
- Clarify any missing details.

Context:
"""
Current policy excerpt provided separately.
Target regulations: GDPR Art.5 and EU AI Act Title IV.
Objective: deliver a compliance gap analysis and remediation roadmap.
"""

Constraints:

- Present findings in a table: Regulation article \| Current coverage \| Gap description \| Risk \| Recommended fix.
- Follow with a numbered action list.

## Output Format

Markdown
