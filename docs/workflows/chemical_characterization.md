---
title: Chemical Characterization and Biocompatibility Assessment
---

# Chemical Characterization and Biocompatibility Assessment

A workflow to design a chemical characterization study, assess the risks from the results, and write a regulatory summary. This follows the sequence in the chemical_characterization_prompts directory.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:#0d3a4d,stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:#183b27,stroke-width:2px,color:#ffffff;
    INPUT_device_description([Input: device_description]):::inputNode
    INPUT_body_weight_kg([Input: body_weight_kg]):::inputNode
    INPUT_device_dose_ug_day([Input: device_dose_ug_day]):::inputNode
    design_study[design_study<br><i>01_design_the_study.prompt.md</i>]:::stepNode
    INPUT_device_description -. device_description .-> design_study
    design_study -->|sequential| assess_risk
    assess_risk[assess_risk<br><i>02_interpret_the_chemistry_assess_risk.prompt.md</i>]:::stepNode
    design_study -. study_results .-> assess_risk
    INPUT_body_weight_kg -. body_weight .-> assess_risk
    INPUT_device_dose_ug_day -. device_dose .-> assess_risk
    assess_risk -->|sequential| write_summary
    write_summary[write_summary<br><i>03_write_the_regulatory_summary.prompt.md</i>]:::stepNode
    assess_risk -. risk_assessment_summary .-> write_summary
    linkStyle default stroke:#767676,stroke-width:2px;
```


