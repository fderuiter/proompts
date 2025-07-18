---
id: phase-ii-oncology-dmp
title: Phase II Oncology DMP
category: data_management_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [clinical, planning]
---

# Phase II Oncology DMP

Title: Draft Phase II Oncology DMP

Role: Senior Clinical Data Standards Consultant

Task:
- Provide an outline of all DMP sections with two to three guiding sentences for each.
- Include a checklist of critical QC and audit-trail items for pre-lock review.
- Create a table of key milestones with typical timelines.

Context:
"""
Trial uses Medidata Rave EDC, ePRO and central-lab feeds.
Regulatory authorities: FDA 21 CFR Part 11, EMA, ICH E6(R3) draft.
Sponsor requires CDISC CDASH v2.0 and SDTM v3.4 compliance.
Stakeholders include Biostatistics, Clinical Ops and external lab vendors.
"""

Constraints:
- Use plain language and omit proprietary SOP numbers.
- Keep total output ≤ 1 500 words.

Output Format: markdown
--------------------------------------------------
