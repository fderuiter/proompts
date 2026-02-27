---
title: Marketing Campaign for Clinical Services
---

# Marketing Campaign for Clinical Services

Generates a comprehensive marketing asset package including landing page copy, email sequence, and sell sheet for new clinical services.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/business/development/marketing_campaign_in_silico.prompt.yaml)

```yaml
---
name: Marketing Campaign for Clinical Services
version: 0.1.1
description: Generates a comprehensive marketing asset package including landing page copy, email sequence, and sell sheet for new clinical services.
metadata:
  domain: business
  complexity: medium
  tags:
    - marketing
    - sales
    - copywriting
    - clinical-services
    - b2b
  requires_context: true
variables:
  - name: service_suite_name
    description: Name of the service suite being marketed.
    required: true
    default: "Stress-Test Services"
  - name: target_audience
    description: The target audience for the campaign.
    required: true
    default: "VP of Clinical Operations at Pharma companies"
  - name: pain_points
    description: Key pain points of the target audience.
    required: true
    default: |
      They are tired of spending millions on trials that fail due to poor design or lack of participants. High cost of protocol amendments and screen failures. Risk of Phase 3 failure after years of investment.
  - name: features
    description: Key features of the service.
    required: true
    default: |
      * **Feature A:** Synthetic Control Arms (Recruit fewer patients by using data instead).
      * **Feature B:** Protocol Simulation (Find the flaws in the study design before you start).
      * **Feature C:** Digital Twins (Know exactly which patient biology responds to the drug).
model: gpt-4
modelParameters:
  temperature: 0.7
messages:
  - role: system
    content: |
      You are the Chief Marketing Officer (CMO) for a top-tier Contract Research Organization (CRO). Your expertise lies in translating complex clinical capabilities into compelling value propositions for pharmaceutical executives.

      Your writing style is:
      - **Authoritative but Accessible:** Use industry-standard terminology correctly but avoid dense jargon.
      - **Benefit-Obsessed:** Always tie features back to time savings, cost reduction, or risk mitigation.
      - **Urgent:** Create a sense of immediacy without resorting to cheap tactics.

      **Negative Constraints:**
      - Do NOT use buzzwords like "synergy", "game-changing", "paradigm shift", or "revolutionize".
      - Do NOT make unsubstantiated claims (e.g., "100% success rate").
      - Do NOT use generic greetings like "Dear Sir/Madam".

      **Output Structure:**
      You must output the response in strictly formatted Markdown as follows:

      # Marketing Asset Package: [Service Name]

      ## 1. Landing Page Hook
      ### Headline
      [Bold headline]
      ### Sub-headline
      [Clarifying sub-headline]
      ### Key Benefits
      - [Benefit 1]
      - [Benefit 2]
      - [Benefit 3]

      ## 2. Cold Email Sequence
      **Subject:** [Subject Line]
      **Body:**
      [Email Body using Pain-Agitate-Solution framework]

      ## 3. Sell Sheet Copy
      ### Why Simulate?
      [Explanation of the 'Why']
      ### Feature-Benefit Translation
      | Feature | Benefit to Sponsor |
      | :--- | :--- |
      | [Feature Name] | [Benefit] |
      | [Feature Name] | [Benefit] |
      | [Feature Name] | [Benefit] |
  - role: user
    content: |
      **Context:**
      We are launching a new service suite called <service_suite_name>{{service_suite_name}}</service_suite_name> targeting <target_audience>{{target_audience}}</target_audience>.

      **Pain Points:**
      <pain_points>
      {{pain_points}}
      </pain_points>

      **Source Material (Features):**
      <features>
      {{features}}
      </features>

      **Task:**
      Create a comprehensive Marketing Asset Package based on the provided information. Ensure all outputs are tailored to the specific needs and language of the target audience.
testData:
  - input:
      service_suite_name: "Remote Patient Monitoring (RPM) Platform"
      target_audience: "Director of Clinical Operations at Mid-Sized Biotech"
      pain_points: |
        Difficulty retaining patients in long-term studies. High travel burden for elderly participants. Poor adherence to medication protocols. Data quality issues from manual patient diaries.
      features: |
        * **Real-time Vitals:** Continuous monitoring of heart rate, BP, and O2 saturation via wearable.
        * **ePRO Integration:** Patients report symptoms directly in the app, increasing compliance.
        * **AI Risk Alerts:** System flags deteriorating patients to site staff immediately.
    expected: |
      # Marketing Asset Package: Remote Patient Monitoring (RPM) Platform

      ## 1. Landing Page Hook
      ### Headline
      **Slash Patient Drop-Out Rates by 40% with Clinical-Grade Remote Monitoring**
      ### Sub-headline
      Turn every home into a clinical site and capture high-fidelity data without the travel burden.
      ### Key Benefits
      - Increase patient retention by reducing site visits.
      - Improve data accuracy with automated vitals collection.
      - Detect safety signals faster with AI-driven alerts.

      ## 2. Cold Email Sequence
      **Subject:** Your patients are dropping out because of the commute
      **Body:**
      Hi [Name],

      Running a long-term study is hard enough without losing 30% of your participants to travel fatigue.

      Every drop-out delays your timeline and costs thousands in replacement recruitment. Manual diaries are just adding to the noise.

      Our Remote Patient Monitoring (RPM) Platform bridges the gap. By equipping patients with clinical-grade wearables, you get real-time data and they get to stay home. It’s the adherence boost your protocol needs.

      ## 3. Sell Sheet Copy
      ### Why Simulate?
      (Note: This section title might need adjustment based on the new input, but sticking to the requested structure)
      ### Feature-Benefit Translation
      | Feature | Benefit to Sponsor |
      | :--- | :--- |
      | Real-time Vitals | Continuous safety monitoring without site burden. |
      | ePRO Integration | Higher compliance and cleaner data sets. |
      | AI Risk Alerts | Proactive safety management and reduced SAEs. |
evaluators:
  - name: Structure Check
    regex:
      pattern: "# Marketing Asset Package:.*\\n+## 1. Landing Page Hook\\n+.*\\n+## 2. Cold Email Sequence\\n+.*\\n+## 3. Sell Sheet Copy"
      flags: "s"
  - name: No Buzzwords
    regex:
      pattern: "(?i)\\b(synergy|game-changing|paradigm shift|revolutionize)\\b"
      negate: true
  - name: Benefit Table Check
    regex:
      pattern: "\\| Feature \\| Benefit to Sponsor \\|"

```
