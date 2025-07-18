<!-- markdownlint-disable MD029 -->

# TMF Gap-Analysis & Audit Readiness Check

**"You are a regulatory compliance auditor specializing in ICH-GCP.
Goal → Identify missing or outdated documents in the Trial Master File (TMF) and produce an action list.

Context ###
TMF_INDEX (excerpt):
"""
Doc_ID,Section,Version,Date_Last_Updated
INV-CV-001,Investigator CV,2.0,2024-12-01
IRB-APPROVAL-MAIN,Ethics/IRB,1.0,2024-11-15
SITE_INIT_REPORT-102,Site Mgmt,,
2255-RAD-SAE-FORM-04,Safety,4.0,2025-06-30
...
"""

## Instructions

1. Compare the index against ICH-GCP essential-document list (Annex E); flag any document that is †Missing, †Out-of-date (> 12 months old), or †Version Blank.
1. Return a table with columns: `Doc_ID`, `Gap_Type`, `Corrective Action`.
1. Provide a numbered plan to close the gaps within 10 business days.

## Output: Markdown table + numbered action plan

"**
