---
title: Technical Writer Workflow
---

# Technical Writer Workflow

A workflow for drafting a CSR results and safety section, an Investigator's Brochure summary of changes, and an SAE reporting SOP.

## Workflow Diagram

```mermaid
graph TD
    INPUT_study_context([Input: study_context])
    INPUT_sponsor_requirements([Input: sponsor_requirements])
    csr_section[csr_section<br><i>01_csr_results_safety_section.prompt.md</i>]
    csr_section -->|sequential| ib_summary
    ib_summary[ib_summary<br><i>02_ib_detailed_soc.prompt.md</i>]
    ib_summary -->|sequential| sae_sop
    sae_sop[sae_sop<br><i>03_sae_reporting_sop.prompt.md</i>]
    INPUT_study_context -. study_context .-> sae_sop
    INPUT_sponsor_requirements -. sponsor_requirements .-> sae_sop
```


