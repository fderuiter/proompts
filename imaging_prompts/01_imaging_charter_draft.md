---
id: imaging-charter-draft
title: Imaging Charter Draft
category: imaging_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [imaging, charter]
---

# Imaging Charter Draft

## Purpose
Create a study-specific imaging charter compliant with global regulations.

## Context
You are a senior imaging core lab compliance specialist with extensive FDA and EMA experience.

- Trial synopsis: <<<protocol synopsis>>>
- Imaging modalities & sequences: <<<list>>>
- Primary and secondary imaging endpoints: <<<list>>>
- Participating regions/sites: <<<list>>>
- Key regulations: 21 CFR Part 11, ICH E6(R2), ICH E17, GDPR/HIPAA.

## Instructions
1. Draft the charter in Markdown using H2 headings.
2. Specify standardized acquisition parameters per modality and site.
3. Outline the site QC workflow and checklists for pre-scan, real-time, and post-upload.
4. Describe de-identification and secure transfer specifications.
5. Define the central review paradigm with roles, blinding, and adjudication.
6. Detail data storage and archiving plans.
7. Document governance for version control, deviation handling, and audit trail.
8. Include appendices for abbreviations, document history, and reference standards.
9. Ask up to three clarifying questions if information is incomplete.

## Inputs
- `<<<protocol_synopsis>>>` – study overview
- `<<<modalities>>>` – imaging modalities and sequences
- `<<<endpoints>>>` – imaging endpoints
- `<<<sites>>>` – participating regions or sites
- `<<<regulations>>>` – key regulations to follow

## Output Format
Markdown charter with numbered H2 sections, for example:

```markdown
## 1 Purpose
## 2 Roles & Responsibilities
...
## Appendix C – Revision History
```

## Additional Notes
Reason step by step before writing the charter.
