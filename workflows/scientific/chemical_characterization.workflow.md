# Chemical Characterization and Biocompatibility Assessment

A workflow to design a chemical characterization study, assess the risks from the results, and write a regulatory summary. This follows the sequence in the chemical_characterization_prompts directory.

## Visual Flow

```mermaid
flowchart TD
    subgraph Inputs [Global Inputs]
        inp_device_description((device_description))
        inp_body_weight_kg((body_weight_kg))
        inp_device_dose_ug_day((device_dose_ug_day))
    end
    design_study["design_study<br/><small>prompts/scientific/chemical_characterization/chemical_characterization/01_design_the_study.prompt.yaml</small>"]
    assess_risk["assess_risk<br/><small>prompts/scientific/chemical_characterization/chemical_characterization/02_interpret_the_chemistry_assess_risk.prompt.yaml</small>"]
    write_summary["write_summary<br/><small>prompts/scientific/chemical_characterization/chemical_characterization/03_write_the_regulatory_summary.prompt.yaml</small>"]
    inp_device_description -->|device_description| design_study
    design_study -->|study_results| assess_risk
    inp_body_weight_kg -->|body_weight| assess_risk
    inp_device_dose_ug_day -->|device_dose| assess_risk
    assess_risk -->|risk_assessment_summary| write_summary
```
