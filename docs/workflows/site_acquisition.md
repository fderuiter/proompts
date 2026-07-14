---
title: Site Acquisition Workflow
---

# Site Acquisition Workflow

A workflow for site landscape mapping, feasibility questionnaire building, and investigator outreach.

## Workflow Diagram

```mermaid
graph TD
    INPUT_protocol_summary([Input: protocol_summary])
    INPUT_investigator_name([Input: investigator_name])
    INPUT_site_name([Input: site_name])
    INPUT_city_country([Input: city_country])
    INPUT_recent_relevant_trials([Input: recent_relevant_trials])
    INPUT_unique_site_strength([Input: unique_site_strength])
    INPUT_study_synopsis([Input: study_synopsis])
    INPUT_sponsor_name([Input: sponsor_name])
    site_mapping[site_mapping<br><i>01_site_landscape_mapping.prompt.md</i>]
    INPUT_protocol_summary -. protocol_summary .-> site_mapping
    site_mapping -->|sequential| feasibility_questionnaire
    feasibility_questionnaire[feasibility_questionnaire<br><i>02_tailored_feasibility_questionnaire.prompt.md</i>]
    INPUT_protocol_summary -. protocol_summary .-> feasibility_questionnaire
    feasibility_questionnaire -->|sequential| outreach_email
    outreach_email[outreach_email<br><i>03_investigator_outreach_email_generator.prompt.md</i>]
    INPUT_investigator_name -. investigator_name .-> outreach_email
    INPUT_site_name -. site_name .-> outreach_email
    INPUT_city_country -. city_country .-> outreach_email
    INPUT_recent_relevant_trials -. recent_relevant_trials .-> outreach_email
    INPUT_unique_site_strength -. unique_site_strength .-> outreach_email
    INPUT_study_synopsis -. study_synopsis .-> outreach_email
    INPUT_sponsor_name -. sponsor_name .-> outreach_email
```


