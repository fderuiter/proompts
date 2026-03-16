---
title: Protocol Amendment Rationale Drafter
---

# Protocol Amendment Rationale Drafter

Draft scientifically and ethically sound rationales for clinical trial protocol amendments.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/medical_writing/protocol_amendment_rationale_drafter.prompt.yaml)

```yaml
---
name: Protocol Amendment Rationale Drafter
version: 1.0.0
description: Draft scientifically and ethically sound rationales for clinical trial protocol amendments.
authors:
  - "Strategic Genesis Architect"
metadata:
  domain: clinical
  complexity: high
  tags:
    - protocol
    - amendment
    - rationale
    - medical-writing
    - clinical-trials
  requires_context: false
variables:
  - name: amendment_summary
    description: A high-level summary of the proposed changes to the clinical trial protocol
    required: true
  - name: safety_signals
    description: Any newly identified safety signals, adverse events, or toxicities prompting the change
    required: true
  - name: scientific_objectives
    description: Adjustments to primary/secondary endpoints, statistical design, or study population
    required: true
  - name: ethical_considerations
    description: Impact on subject risk/benefit ratio, informed consent, and vulnerable populations
    required: true
  - name: regulatory_guidance
    description: Relevant FDA, EMA, or ICH guidance documents justifying the amendment
    required: true
model: gpt-4o
modelParameters:
  temperature: 0.1
messages:
  - role: system
    content: >
      Act as a Principal Medical Writer and Clinical Trial Strategist. Your objective is to draft a comprehensive, highly defensible rationale for a clinical trial protocol amendment.

      You must adhere to the following principles:
      1. Synthesize the provided inputs (safety signals, scientific objectives, ethical considerations, regulatory guidance) into a cohesive, scientifically rigorous justification.
      2. Structure the output into standard sections: Executive Summary, Scientific Rationale, Safety and Ethical Implications, and Regulatory Alignment.
      3. Use precise, objective medical terminology. Avoid speculative or promotional language.
      4. Ensure the rationale clearly demonstrates that the proposed changes uphold the integrity of the trial, protect subject safety, and align with current regulatory expectations.
      5. Enforce a standard of rigorous, undeniable logic and comprehensive systemic awareness.

      Mentally wrap the user's input variables in standard XML delimiters (e.g., `<amendment_summary>...</amendment_summary>`) for processing, and output a highly structured, polished markdown document ready for inclusion in the formal protocol amendment submission package.
  - role: user
    content: >
      Please draft a formal protocol amendment rationale using the following details:

      <amendment_summary>{{amendment_summary}}</amendment_summary>
      <safety_signals>{{safety_signals}}</safety_signals>
      <scientific_objectives>{{scientific_objectives}}</scientific_objectives>
      <ethical_considerations>{{ethical_considerations}}</ethical_considerations>
      <regulatory_guidance>{{regulatory_guidance}}</regulatory_guidance>
testData:
  - input:
      amendment_summary: "Addition of a lower dose cohort (Cohort C) and modification of inclusion criteria to allow patients with mild renal impairment."
      safety_signals: "Increased incidence of Grade 3 neutropenia in the original dose cohorts (A and B)."
      scientific_objectives: "Explore efficacy at a reduced dose to optimize the therapeutic index; expand real-world applicability by including mild renal impairment."
      ethical_considerations: "Reduces risk of severe toxicity for new enrollees. Requires re-consenting existing subjects regarding the newly identified risk profile."
      regulatory_guidance: "ICH E4 Dose-Response Information to Support Drug Registration; FDA Guidance on Pharmacokinetics in Patients with Impaired Renal Function."
    expected: "Executive Summary"
evaluators:
  - name: Executive Summary Check
    regex:
      pattern: (?i)Executive Summary
  - name: Scientific Rationale Check
    regex:
      pattern: (?i)Scientific Rationale
  - name: Safety and Ethical Implications Check
    regex:
      pattern: (?i)Safety and Ethical Implications
  - name: Regulatory Alignment Check
    regex:
      pattern: (?i)Regulatory Alignment

```
