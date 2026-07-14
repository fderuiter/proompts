---
title: Clinical Safety Workflow
---

# Clinical Safety Workflow

A workflow for creating a clinical safety synopsis, an adverse event narrative, and trending safety signals.

## Workflow Diagram

```mermaid
graph TD
    INPUT_surveillance_data([Input: surveillance_data])
    INPUT_adverse_event_data([Input: adverse_event_data])
    INPUT_post_market_data([Input: post_market_data])
    safety_synopsis[safety_synopsis<br><i>01_eu_cer_clinical_safety_synopsis.prompt.md</i>]
    INPUT_surveillance_data -. input .-> safety_synopsis
    safety_synopsis -->|sequential| adverse_event_narrative
    adverse_event_narrative[adverse_event_narrative<br><i>02_fda_mdr_adverse_event_narrative.prompt.md</i>]
    INPUT_adverse_event_data -. input .-> adverse_event_narrative
    adverse_event_narrative -->|sequential| safety_signal_trending
    safety_signal_trending[safety_signal_trending<br><i>03_post_market_safety_signal_trending.prompt.md</i>]
    INPUT_post_market_data -. input .-> safety_signal_trending
```


