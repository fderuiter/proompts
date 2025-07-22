---
id: sop-gap-analysis
title: SOP Gap Analysis
category: data_management_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [compliance, sop]
---

# SOP Gap Analysis

Title: Analyse SOPs Against Regulations

Role: Regulatory Compliance Auditor

Task:

- Compare our Data-Management SOP suite with ICH E6(R3), FDA Data Integrity Guidance, GDPR and CDISC GCDMP v4.0.
- Produce a gap-analysis table with risk rating and recommended action.
- Provide a 90-day remediation roadmap listing owners and success metrics.

Context:
"""
Current SOPs:

1. DM-001 Database Build v4.2 (Jan 2022)
1. DM-002 Data Cleaning v3.1 (Jun 2022)
1. DM-003 Vendor Data Reconciliation v2.0 (Aug 2021)
1. DM-004 Database Lock v1.0 (Mar 2021)

"""

Constraints:

- Focus on gaps affecting data integrity, patient safety or submission readiness.
- Limit output to two tables and a bullet-list roadmap with ≤ 1 000 words total.

## Output Format

Markdown
