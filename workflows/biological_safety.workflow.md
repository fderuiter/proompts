# Biological Safety Assessment and Planning

A workflow to perform a risk assessment for a medical device, develop a biological safety plan, and prepare for regulatory submission. This follows the sequence in the biological_safety_prompts directory.

## Visual Flow

```mermaid
flowchart TD
    subgraph Inputs [Global Inputs]
        inp_medical_device_type((medical_device_type))
    end
    perform_risk_assessment["perform_risk_assessment<br/><small>biological_safety_prompts/01_risk_assessment_expert.prompt.yaml</small>"]
    develop_safety_plan["develop_safety_plan<br/><small>biological_safety_prompts/02_biological_safety_plan_developer.prompt.yaml</small>"]
    prepare_submission["prepare_submission<br/><small>biological_safety_prompts/03_regulatory_submission_support.prompt.yaml</small>"]
    inp_medical_device_type -->|medical_device_type| perform_risk_assessment
    perform_risk_assessment -->|risk_assessment| develop_safety_plan
    develop_safety_plan -->|biological_safety_plan| prepare_submission
```
