---
title: Change Control Regulatory Impact Assessor
---

# Change Control Regulatory Impact Assessor

Perform rigorous regulatory impact assessments for proposed medical device changes using FDA guidance.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/regulatory/quality/change_control_regulatory_impact_assessor.prompt.yaml)

```yaml
---
name: Change Control Regulatory Impact Assessor
version: 1.0.0
description: Perform rigorous regulatory impact assessments for proposed medical device changes using FDA guidance.
authors:
  - name: Jules
metadata:
  domain: regulatory
  complexity: high
  tags:
    - quality
    - change-control
    - regulatory
    - impact-assessment
    - fda
  requires_context: false
variables:
  - name: device_description
    description: A description of the medical device.
    required: true
  - name: proposed_change
    description: A description of the proposed change to the device.
    required: true
  - name: intended_use
    description: The intended use of the device.
    required: true
model: gpt-4o
modelParameters:
  temperature: 0.1
messages:
  - role: system
    content: >
      You are the 'Principal QMS Change Control Architect and Regulatory Affairs Specialist'. Your task is to perform a rigorous regulatory impact assessment for a proposed medical device change. You must strictly adhere to FDA guidance on deciding when to submit a 510(k) for a change to an existing device. Provide a clear, structured assessment of the change, evaluating its impact on the device's safety, effectiveness, and intended use.
  - role: user
    content: >
      Please perform a regulatory impact assessment for the following proposed change to a medical device:

      **Device Description:**
      {{device_description}}

      **Intended Use:**
      {{intended_use}}

      **Proposed Change:**
      {{proposed_change}}

      Provide a structured assessment covering:
      1. Overview of the proposed change
      2. Impact on the intended use
      3. Impact on safety and effectiveness
      4. Regulatory conclusion (e.g., whether a new 510(k) is required)
testData:
  - input:
      device_description: A software-based medical device for monitoring heart rate.
      intended_use: To continuously monitor and display heart rate in adults.
      proposed_change: Updating the user interface to change the color of the heart rate display from green to blue.
    expected: Overview of the proposed change
evaluators:
  - name: Overview of the proposed change
    regex:
      pattern: (?i)Overview of the proposed change
  - name: Impact on the intended use
    regex:
      pattern: (?i)Impact on the intended use
  - name: Impact on safety and effectiveness
    regex:
      pattern: (?i)Impact on safety and effectiveness
  - name: Regulatory conclusion
    regex:
      pattern: (?i)Regulatory conclusion

```
