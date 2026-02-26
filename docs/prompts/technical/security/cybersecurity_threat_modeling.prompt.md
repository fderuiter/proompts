---
title: Medical Device Cybersecurity Threat Modeling
---

# Medical Device Cybersecurity Threat Modeling

Analyze system architecture using STRIDE.

[View Source YAML](../../../../prompts/technical/security/cybersecurity_threat_modeling.prompt.yaml)

```yaml
---
name: Medical Device Cybersecurity Threat Modeling
version: 1.0.0
description: Analyze system architecture using STRIDE.
metadata:
  domain: technical
  complexity: high
  tags:
  - security
  - medical
  - device
  - cybersecurity
  - threat
  requires_context: false
variables:
- name: system_architecture
  description: The detailed system architecture to analyze.
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.1
messages:
- role: system
  content: "You are a Senior Medical Device Cybersecurity Architect. Your task is to perform a rigorous STRIDE threat modeling analysis for a medical device system, strictly adhering to FDA Premarket Cybersecurity Guidance (FDA-2018-D-3443).\n\nAnalyze the provided system architecture description for potential vulnerabilities across all STRIDE categories:\n- **S**poofing\n- **T**ampering\n- **R**epudiation\n- **I**nformation Disclosure\n- **D**enial of Service\n- **E**levation of Privilege\n\nProvide a structured report including an Executive Summary, a detailed STRIDE Analysis table, and prioritized Mitigation Strategies."
- role: user
  content: "Analyze the following medical device system architecture:\n\n<system_architecture>\n{{system_architecture}}\n</system_architecture>\n\nGenerate a comprehensive Threat Modeling Report.\n\nOutput format:\n\n# Executive Summary\n[Brief overview of the system's risk profile]\n\n## STRIDE Threat Analysis\n| Threat Category | Potential Vulnerability | Impact | Likelihood |\n| :--- | :--- | :--- | :--- |\n| Spoofing | ... | ... | ... |\n| ... | ... | ... | ... |\n\n## Mitigation Strategies\n1. **[Threat ID]**: [Specific technical control]\n2. ...\n\n## Compliance Note\nConfirm alignment with FDA Premarket Cybersecurity Guidance."
testData:
- input:
    system_architecture: "NeuroLink BCI System: A brain-computer interface implant communicating via BLE 5.0 to a patient mobile app (iOS/Android). The app syncs data to a cloud backend (AWS HIPAA-compliant) via HTTPS/TLS 1.3. OTA updates are pushed from the cloud to the implant via the mobile app. The implant has no physical ports."
  expected: "Detailed STRIDE analysis covering BLE spoofing, Man-in-the-Middle attacks on OTA updates, and cloud data breaches."
- input:
    system_architecture: "Legacy Mechanical Ventilator (Model V-200): A standalone life-support device with no network connectivity (WiFi/Bluetooth disabled/removed). It features a USB port for firmware updates and maintenance logs, accessible only by authorized service technicians using a physical key to open the port cover."
  expected: "Analysis focusing on physical access threats, USB-based malware introduction (Tampering), and insider threats (Service Technicians)."
- input:
    system_architecture: "Secure Box: A generic medical device that claims to be 'unhackable' because it uses 'proprietary encryption'."
  expected: "Critical analysis highlighting the risks of 'security by obscurity', lack of standard protocols, and potential implementation flaws in proprietary encryption."
evaluators:
- name: Executive Summary Header
  regex:
    pattern: "(?m)^# Executive Summary"
- name: STRIDE Analysis Header
  regex:
    pattern: "(?m)^## STRIDE Threat Analysis"
- name: Mitigation Strategies Header
  regex:
    pattern: "(?m)^## Mitigation Strategies"
- name: STRIDE Categories
  regex:
    pattern: "(?s)Spoofing.*Tampering.*Repudiation.*Information Disclosure.*Denial of Service.*Elevation of Privilege"
- name: FDA Compliance Reference
  regex:
    pattern: "(?i)FDA Premarket Cybersecurity Guidance"

```
