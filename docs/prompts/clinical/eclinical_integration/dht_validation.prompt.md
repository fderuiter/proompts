---
title: Digital Health Technology (DHT) Validation
---

# Digital Health Technology (DHT) Validation

Create validation strategy for DHTs.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/eclinical_integration/dht_validation.prompt.yaml)

```yaml
---
name: Digital Health Technology (DHT) Validation
version: 0.1.0
description: Create validation strategy for DHTs.
metadata:
  domain: clinical
  complexity: low
  tags:
  - eclinical-integration
  - digital
  - health
  - technology
  - dht
  requires_context: false
variables:
- name: dht_specs
  description: The dht specs to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Digital Health Scientist. Create a validation strategy for using an accelerometer-derived stride velocity
    endpoint in a trial, including requirements for algorithm freezing and software update plans. Reference FDA PDUFA VII
    and EMA Guidance.
- role: user
  content: 'Create a validation strategy for using an accelerometer-derived stride velocity endpoint in a trial, including
    requirements for algorithm freezing and software update plans.


    Inputs:

    - `{{dht_specs}}`


    Output format:

    Markdown Validation Strategy.'
testData:
- input: 'dht_specs: Accelerometer for gait analysis.

    '
  expected: 'Validation Strategy

    '
evaluators:
- name: Algorithm Freezing
  string:
    contains: Algorithm Freezing
- name: Software Update
  string:
    contains: Software Update

```
