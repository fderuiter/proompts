---
title: Clinical-Trial Budget and Burn-Rate Dashboard
---

# Clinical-Trial Budget and Burn-Rate Dashboard

Produce a month-end dashboard comparing planned versus actual spend and forecasting when budgets will run out for each active study.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/business/hr_finance/clinical_trial_budget_burn_rate_dashboard.prompt.yaml)

```yaml
---
name: Clinical-Trial Budget and Burn-Rate Dashboard
version: 0.1.0
description: Produce a month-end dashboard comparing planned versus actual spend and forecasting when budgets will run out
  for each active study.
metadata:
  domain: business
  complexity: high
  tags:
  - hr-finance
  - clinical-trial
  - budget
  - burn-rate
  - dashboard
  requires_context: false
variables:
- name: invoices
  description: pass-through invoice amounts
  required: true
- name: milestones
  description: milestone payment schedule
  required: true
- name: planned_budget
  description: approved budget per study
  required: true
- name: staffing_hours
  description: hours logged per study
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are an **AI Clinical-Trial Budget Analyst**. Source data arrives as Google Sheets with staffed hours, pass-through
    invoices, milestone payments, and planned budgets.


    1. Clean and join the data sets.

    2. Calculate cumulative spend and burn rate in USD per week for each study.

    3. Forecast the dates when actual spend will hit 90% and 100% of budget.

    4. Highlight variances of 10% or greater and suggest corrective levers, such as renegotiating vendor rates or reducing
    CRA travel.

    5. Present only the final answers.


    Keep the entire response under 300 words.'
- role: user
  content: '- `<staffing_hours>{{staffing_hours}}</staffing_hours>` – hours logged per study.

    - `<invoices>{{invoices}}</invoices>` – pass-through invoice amounts.

    - `<milestones>{{milestones}}</milestones>` – milestone payment schedule.

    - `<planned_budget>{{planned_budget}}</planned_budget>` – approved budget per study.


    Output format: - Markdown table (study ID, burn rate, percent of budget consumed, projected run-out date).

    - Up to five bullet-point recommendations.'
testData:
  - inputs:
      staffing_hours: |
        Study_ID,Month,Role,Hours_Logged
        ONC-2024-001,Oct-2024,CRA,120.5
        ONC-2024-001,Oct-2024,Project Manager,45.0
        CARDIO-2024-B,Oct-2024,Data Manager,60.0
      invoices: |
        Study_ID,Vendor,Invoice_Amount,Date
        ONC-2024-001,Central Lab,$45,000,2024-10-15
        CARDIO-2024-B,Travel Agency,$12,500,2024-10-20
      milestones: |
        Study_ID,Milestone_Name,Amount,Scheduled_Date
        ONC-2024-001,First Patient In,$150,000,2024-11-01
        CARDIO-2024-B,Site Initiation,$75,000,2024-10-01
      planned_budget: |
        Study_ID,Total_Budget,Start_Date,End_Date
        ONC-2024-001,$2,500,000,2024-01-01,2025-12-31
        CARDIO-2024-B,$1,200,000,2024-06-01,2025-06-01
    expected: "Markdown table with recommendations"
  - inputs:
      staffing_hours: ""
      invoices: |
        Study_ID,Vendor,Invoice_Amount,Date
        NEURO-2024-X,Imaging Center,$85,000,2024-10-10
      milestones: |
        Study_ID,Milestone_Name,Amount,Scheduled_Date
        NEURO-2024-X,Database Lock,$250,000,2024-12-15
      planned_budget: |
        Study_ID,Total_Budget,Start_Date,End_Date
        NEURO-2024-X,$3,000,000,2023-01-01,2024-12-31
    expected: "Markdown table reflecting missing staffing hours"
evaluators:
  - name: "Output includes markdown table"
    regex:
      pattern: "\\|.*\\|.*\\|.*\\|.*\\|"
      flags: "gm"
  - name: "Output includes bullet points"
    regex:
      pattern: "^\\s*[-*]\\s+.*$"
      flags: "gm"

```
