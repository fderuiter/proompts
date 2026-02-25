---
title: Learning and Development Workflow
---

# Learning and Development Workflow

A workflow for creating a competency-based onboarding blueprint, a scenario-based microlearning series, and a training impact analytics plan.

## Workflow Diagram

```mermaid
graph TD
    Input_existing_modules[Input: existing_modules] --> Steps
    Input_audience_role[Input: audience_role] --> Steps
    Input_analysis_goal[Input: analysis_goal] --> Steps
    onboarding_blueprint[Step: onboarding_blueprint]
    Input_existing_modules --> onboarding_blueprint
    microlearning_series[Step: microlearning_series]
    Input_audience_role --> microlearning_series
    analytics_plan[Step: analytics_plan]
    Input_analysis_goal --> analytics_plan
```

[View Source YAML](../../workflows/management/learning_development.workflow.yaml)
