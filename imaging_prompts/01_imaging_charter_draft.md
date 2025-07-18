<!-- markdownlint-disable MD029 -->

# Generate a Study-Specific Imaging Charter Draft

## Role

You are a senior Imaging Core Lab compliance specialist who has written 200+ FDA- and EMA-accepted Imaging Charters.

## Context

Trial synopsis ⟶ {{paste protocol synopsis}}
Imaging modalities & sequences ⟶ {{list}}
Primary/secondary imaging endpoints ⟶ {{list}}
Participating regions/sites ⟶ {{list}}
Key regulations to respect ⟶ 21 CFR Part 11, ICH E6(R2), ICH E17, GDPR/HIPAA

## Task

Draft a complete Imaging Charter (v0.1) that includes:

1. Standardized acquisition parameters per modality & site
1. Site QC workflow/checklists (pre-scan, real-time, post-upload)
1. De-identification & secure transfer specs (DICOM tags to scrub, sFTP/S3 details)
1. Central review paradigm (reader roles, blinding, adjudication rules)
1. Data storage/archiving plan (format, retention, disaster recovery)
1. Governance (version control, deviation handling, audit trail)
1. Appendices: abbreviations, document history, reference standards

## Process

First reason step-by-step off-screen; then output the charter in **Markdown** with H2 section headings.

## Output format

```markdown
## 1 Purpose …
## 2 Roles & Responsibilities …
…
## Appendix C – Revision History
```

If any information is missing, ask up to three concise follow-up questions **before** drafting.

<!-- markdownlint-enable MD029 -->
