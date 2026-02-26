---
title: DHT Integration Regulatory Checklist
---

# DHT Integration Regulatory Checklist

Review FDA guidance for digital health technology (DHT) integration and validation.

[View Source YAML](../../../../prompts/regulatory/adherence/dht_integration_checklist.prompt.yaml)

```yaml
---
name: DHT Integration Regulatory Checklist
version: 0.1.0
description: Review FDA guidance for digital health technology (DHT) integration and validation.
metadata:
  domain: regulatory
  complexity: medium
  tags:
  - regulatory-adherence
  - dht
  - integration
  - regulatory
  - checklist
  requires_context: false
variables:
- name: dht_type
  description: The dht type to use for this prompt
  required: true
- name: endpoint
  description: The endpoint to use for this prompt
  required: true
- name: population
  description: The population to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.1
messages:
- role: system
  content: 'You are a Digital Health Regulatory Expert. Your task is to analyze the FDA guidance on ''Digital Health Technologies
    for Remote Data Acquisition in Clinical Investigations''.


    Your output should be a structured checklist of technical specifications and ''fit-for-purpose'' validation requirements
    for wearable biosensors or other DHTs used to capture endpoints.


    Include checks for the following using Markdown headers:

    1.  **## Selection:** Rationale for choosing the specific DHT.

    2.  **## Verification & Validation:** Evidence that the DHT measures what it claims to measure (analytical and clinical
    validation).

    3.  **## Data Reliability:** Assurance of data integrity, audit trails, and attribution.

    4.  **## Usability:** Considerations for patient burden and training.

    5.  **## Risk Management:** Handling of safety signals detected by the DHT.


    Format as a structured checklist for sponsors.

    '
- role: user
  content: '<dht_type>

    {{dht_type}} (e.g., Actigraphy watch)

    </dht_type>


    <endpoint>

    {{endpoint}} (e.g., Daily step count, Sleep duration)

    </endpoint>


    <target_population>

    {{population}}

    </target_population>


    Generate the validation checklist.

    '
testData:
- input: 'dht_type: Consumer-grade Smartwatch

    endpoint: Average daily heart rate

    population: Heart Failure patients (NYHA Class II-III)

    '
  expected: Checklist covering validation of heart rate accuracy against gold standard, data transfer security, and patient
    compliance monitoring.
evaluators:
- name: Validation Check
  regex:
    pattern: (?i)(verification|validation|analytical|clinical)
- name: Usability Check
  regex:
    pattern: (?i)(usability|burden)

```
