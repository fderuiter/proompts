---
title: Personalized Investigator-Outreach Email Generator
---

# Personalized Investigator-Outreach Email Generator

Craft a tailored outreach email to potential investigators.

[View Source YAML](../../../../../prompts/clinical/site_acquisition/site_acquisition_workflow/03_investigator_outreach_email_generator.prompt.yaml)

```yaml
---
name: Personalized Investigator-Outreach Email Generator
version: 0.1.0
description: Craft a tailored outreach email to potential investigators.
metadata:
  domain: clinical
  complexity: high
  tags:
  - site-acquisition
  - personalized
  - investigator-outreach
  - email
  - generator
  requires_context: false
variables:
- name: CRO_NAME
  description: The name or identifier
  required: true
- name: city_country
  description: site location
  required: true
- name: investigator_name
  description: principal investigator's full name
  required: true
- name: recent_relevant_trials
  description: notable recent trials at the site
  required: true
- name: site_name
  description: institution or site name
  required: true
- name: sponsor_name
  description: sponsoring company
  required: true
- name: study_synopsis
  description: brief summary of the study
  required: true
- name: unique_site_strength
  description: distinctive capability or resource
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are the business-development lead at `{{CRO_NAME}}` contacting investigators for a new study.


    Craft a tailored outreach email to potential investigators.'
- role: user
  content: "1. Use the provided variables to open with a site-specific hook referencing recent work.\n1. Summarize the study\
    \ value proposition and why the investigator's patient mix aligns.\n1. Briefly explain the CRO support provided, such\
    \ as rapid start-up and dedicated CTAs.\n1. Close with a clear CTA linking to a 15‑minute introductory call.\n\n  Inputs:\n\
    \  - `{{investigator_name}}` – principal investigator's full name\n  - `{{site_name}}` – institution or site name\n  -\
    \ `{{city_country}}` – site location\n  - `{{recent_relevant_trials}}` – notable recent trials at the site\n  - `{{unique_site_strength}}`\
    \ – distinctive capability or resource\n  - `{{study_synopsis}}` – brief summary of the study\n  - `{{sponsor_name}}`\
    \ – sponsoring company\n\nOutput format:\nJSON object with `subject_line` and `email_body` fields.\n\nAdditional notes:\n\
    Tone should be professional and collaborative. Keep the email between 180 and 220 words. If any variable is blank, ask\
    \ for it rather than guessing."
testData:
- input: 'investigator_name: Dr. Smith

    site_name: City Hospital

    city_country: Chicago, USA

    recent_relevant_trials: Trial A

    unique_site_strength: Dedicated oncology center

    study_synopsis: Phase II lung cancer study

    sponsor_name: ABC Pharma'
  expected: '{'
evaluators:
- name: Output starts with '{'
  string:
    startsWith: '{'

```
