---
title: Chemical Characterization and Biocompatibility Assessment
---

# Chemical Characterization and Biocompatibility Assessment

A workflow to design a chemical characterization study, assess the risks from the results, and write a regulatory summary. This follows the sequence in the chemical_characterization_prompts directory.

## Workflow Diagram

```mermaid
graph TD
    INPUT_device_description([Input: device_description])
    INPUT_body_weight_kg([Input: body_weight_kg])
    INPUT_device_dose_ug_day([Input: device_dose_ug_day])
    design_study[design_study<br><i>01_design_the_study.prompt.md</i>]
    INPUT_device_description -. device_description .-> design_study
    design_study -->|sequential| assess_risk
    assess_risk[assess_risk<br><i>02_interpret_the_chemistry_assess_risk.prompt.md</i>]
    design_study -. study_results .-> assess_risk
    INPUT_body_weight_kg -. body_weight .-> assess_risk
    INPUT_device_dose_ug_day -. device_dose .-> assess_risk
    assess_risk -->|sequential| write_summary
    write_summary[write_summary<br><i>03_write_the_regulatory_summary.prompt.md</i>]
    assess_risk -. risk_assessment_summary .-> write_summary
```


