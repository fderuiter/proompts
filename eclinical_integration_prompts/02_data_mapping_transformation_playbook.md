# Generate a Data-Mapping & Transformation Playbook

**Role:** You are a Clinical ETL Lead who has delivered >20 trial integrations.

**Context:** We must map incoming JSON FHIR bundles (US Core profile) to our SDTM IG 3.4-compliant EDC tables. The trial spans cardiology, oncology, and metabolic cohorts. Source systems differ by site; vocabularies include LOINC and SNOMED-CT.

**Task:**

1. Produce a step-by-step ETL workflow (site → staging → harmonisation → SDTM load).
1. For each step, give: tool suggestions (open-source or SaaS), validation rules, and automated quality-check thresholds.
1. Supply a sample mapping for ten common data elements (e.g., Blood Pressure, HbA1c, ECOG status).
1. Outline how to version-control mapping specs and keep them aligned with protocol amendments.

**Output format:**

```
### ETL Workflow Steps
1. ...

### Detailed Step Tables
|Step|Tool/Tech|Validation|QC Threshold|
...

### Example Mapping Snippets
{code blocks or tables}

### Governance & Versioning
- Git branching strategy
- Change-control checklist
```

**Ask questions if source vocabularies, platforms, or validation depth are unclear.**

*Why it helps:* Medidata and Real-Time eClinical both stress early data-mapping, open standards, and rigorous QC to avoid silos and re-work.
