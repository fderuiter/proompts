---
layout: default
title: Testing Workflow
parent: Workflows
nav_order: 99
---

# Testing Workflow

A workflow for end-to-end test discovery, design verification, human factors validation, and risk-based test case suite generation.

## Workflow Diagram

```mermaid
graph TD
    Input_project_name[Input: project_name] --> Steps
    Input_languages_frameworks[Input: languages_frameworks] --> Steps
    Input_business_goal[Input: business_goal] --> Steps
    Input_device_name[Input: device_name] --> Steps
    Input_device_class[Input: device_class] --> Steps
    Input_hazard_analysis_table[Input: hazard_analysis_table] --> Steps
    e2e_test_discovery[Step: e2e_test_discovery]
    Input_project_name --> e2e_test_discovery
    Input_languages_frameworks --> e2e_test_discovery
    Input_business_goal --> e2e_test_discovery
    design_verification[Step: design_verification]
    Input_device_name --> design_verification
    human_factors_validation[Step: human_factors_validation]
    Input_device_name --> human_factors_validation
    Input_device_class --> human_factors_validation
    risk_based_test_suite[Step: risk_based_test_suite]
    Input_device_name --> risk_based_test_suite
    Input_hazard_analysis_table --> risk_based_test_suite
```

[View Source YAML](../workflows_src/technical/testing.workflow.yaml)
