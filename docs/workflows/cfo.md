---
title: CFO Workflow
---

# CFO Workflow

A workflow for financial forecasting, competitive bid pricing, and regulatory risk assessment.

## Workflow Diagram

```mermaid
graph TD
    INPUT_base_revenue([Input: base_revenue])
    INPUT_base_costs([Input: base_costs])
    INPUT_starting_cash([Input: starting_cash])
    INPUT_notes([Input: notes])
    INPUT_competitor_bids([Input: competitor_bids])
    INPUT_internal_cost([Input: internal_cost])
    INPUT_target_margin([Input: target_margin])
    INPUT_volume_adjustments([Input: volume_adjustments])
    INPUT_study_portfolio([Input: study_portfolio])
    INPUT_reg_updates([Input: reg_updates])
    INPUT_esg_baseline([Input: esg_baseline])
    INPUT_risk_tolerance([Input: risk_tolerance])
    forecast[forecast<br><i>01_scenario_cash_flow_forecast.prompt.md</i>]
    INPUT_base_revenue -. base_revenue .-> forecast
    INPUT_base_costs -. base_costs .-> forecast
    INPUT_starting_cash -. starting_cash .-> forecast
    INPUT_notes -. notes .-> forecast
    forecast -->|sequential| pricing
    pricing[pricing<br><i>02_competitive_bid_pricing.prompt.md</i>]
    INPUT_competitor_bids -. competitor_bids .-> pricing
    INPUT_internal_cost -. internal_cost .-> pricing
    INPUT_target_margin -. target_margin .-> pricing
    INPUT_volume_adjustments -. volume_adjustments .-> pricing
    pricing -->|sequential| risk_dashboard
    risk_dashboard[risk_dashboard<br><i>03_regulatory_risk_dashboard.prompt.md</i>]
    INPUT_study_portfolio -. study_portfolio .-> risk_dashboard
    INPUT_reg_updates -. reg_updates .-> risk_dashboard
    INPUT_esg_baseline -. esg_baseline .-> risk_dashboard
    INPUT_risk_tolerance -. risk_tolerance .-> risk_dashboard
```


