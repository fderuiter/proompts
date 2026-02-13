---
layout: default
title: Chemical Characterization and Biocompatibility Assessment
parent: Workflows
nav_order: 99
---

# Chemical Characterization and Biocompatibility Assessment

A workflow to design a chemical characterization study, assess the risks from the results, and write a regulatory summary. This follows the sequence in the chemical_characterization_prompts directory.

## Workflow Diagram\n\n<div class="mermaid">\ngraph TD
    Input_device_description[Input: device_description] --> Steps
    Input_body_weight_kg[Input: body_weight_kg] --> Steps
    Input_device_dose_ug_day[Input: device_dose_ug_day] --> Steps
    design_study[Step: design_study]
    Input_device_description --> design_study
    assess_risk[Step: assess_risk]
    design_study --> assess_risk
    Input_body_weight_kg --> assess_risk
    Input_device_dose_ug_day --> assess_risk
    write_summary[Step: write_summary]
    assess_risk --> write_summary\n</div>\n
[View Source YAML](../../workflows/scientific/chemical_characterization.workflow.yaml)
