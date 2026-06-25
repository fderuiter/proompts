---
title: Tool Registry
---

# Automated Tool Registry

This registry provides a complete view of how prompt files map to MCP tools.

## Live Reloading Feature

The MCP server includes watchdog-based hot-reloading capabilities. When you modify, add, or delete `.prompt.yaml` or `skills.md` files in the `prompts` directory, the server detects these changes and automatically updates the agent. You do not need to restart your Claude Desktop application or the MCP server for the changes to propagate.

## Discovered Tools

| Original Name | Transformed Name | Status |
|---------------|------------------|--------|
| `21 CFR 820 / QMSR Gap-Analysis & Remediation` | `21_CFR_820_QMSR_Gap-Analysis_Remediation` | Sanitized |
| `21 CFR Part 11 Compliance Verification` | `21_CFR_Part_11_Compliance_Verification` | Overridden by `prompts/clinical/data_management/skills.md` |
| `21 CFR Part 14 Auditing` | `21_CFR_Part_14_Auditing` | Overridden by `prompts/regulatory/administrative/skills.md` |
| `360° Operational KPI & Benchmark Review` | `360_Operational_KPI_Benchmark_Review` | Sanitized |
| `3D QSAR Pharmacophore Modeling Architect` | `3D_QSAR_Pharmacophore_Modeling_Architect` | Overridden by `prompts/scientific/chemistry/computational/cheminformatics/skills.md` |
| `510(k) Substantial Equivalence Preparation` | `510_k_Substantial_Equivalence_Preparation` | Sanitized |
| `510(k)/De Novo Pre-Submission Strategy` | `510_k_De_Novo_Pre-Submission_Strategy` | Sanitized |
| `80/20 Crash Course` | `80_20_Crash_Course` | Overridden by `prompts/communication/skills.md` |
| `90-Day Biostatistics Onboarding Plan` | `90-Day_Biostatistics_Onboarding_Plan` | Overridden by `prompts/management/leadership/skills.md` |
| `90-Day Pipeline Health & Next-Best-Action Review` | `90-Day_Pipeline_Health_Next-Best-Action_Review` | Sanitized |
| `ADM 3+1 Decomposition Architect` | `ADM_3_1_Decomposition_Architect` | Overridden by `prompts/scientific/physics/relativity/general_relativity/skills.md` |
| `ADaM ADLB NCI-CTCAE and Hy's Law Toxicity Architect` | `ADaM_ADLB_NCI-CTCAE_and_Hy_s_Law_Toxicity_Architect` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `ADaM ADRS RECIST Derivation Architect` | `ADaM_ADRS_RECIST_Derivation_Architect` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `ADaM ADTTE Oncology Censoring Rules Architect` | `ADaM_ADTTE_Oncology_Censoring_Rules_Architect` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `ADaM ADTTE Time to Event Derivation Architect` | `ADaM_ADTTE_Time_to_Event_Derivation_Architect` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `ADaM Derivation Writer` | `ADaM_Derivation_Writer` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `AGENTS.md Checklist Generator` | `AGENTS_md_Checklist_Generator` | Overridden by `prompts/meta/meta_prompt_chain/skills.md` |
| `AI Coding Agent Plan Generator` | `AI_Coding_Agent_Plan_Generator` | Overridden by `prompts/meta/meta_prompt_chain/skills.md` |
| `AI Email Assistant Go/No-Go Vote` | `AI_Email_Assistant_Go_No-Go_Vote` | Overridden by `prompts/technical/design/skills.md` |
| `AI Model Inference Serving Architect` | `AI_Model_Inference_Serving_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `AI Risk Mapper` | `AI_Risk_Mapper` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `AI-Enhanced RBM Action Plan` | `AI-Enhanced_RBM_Action_Plan` | Overridden by `prompts/management/medical_director/skills.md` |
| `AI-Powered Site and Recruitment Strategy` | `AI-Powered_Site_and_Recruitment_Strategy` | Overridden by `prompts/clinical/trial_execution/skills.md` |
| `AI/ML Predetermined Change Control Plan Architect` | `AI_ML_Predetermined_Change_Control_Plan_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `ALCOA-C Data Integrity Checklist` | `ALCOA-C_Data_Integrity_Checklist` | Overridden by `prompts/regulatory/adherence/skills.md` |
| `API Gateway and BFF Architect` | `API_Gateway_and_BFF_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `API Management and Developer Portal Architect` | `API_Management_and_Developer_Portal_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `API Security & Zero Trust Architect` | `API_Security_Zero_Trust_Architect` | Sanitized |
| `APT Threat Hunting Hypothesis Generation Architect` | `APT_Threat_Hunting_Hypothesis_Generation_Architect` | Overridden by `prompts/technical/security/secops/skills.md` |
| `APT Threat Hunting Query Engineer` | `APT_Threat_Hunting_Query_Engineer` | Overridden by `prompts/technical/security/skills.md` |
| `AWS Lambda Serverless Persistence Forensics Analyst` | `AWS_Lambda_Serverless_Persistence_Forensics_Analyst` | Overridden by `prompts/technical/security/secops/incident_response/skills.md` |
| `Abbreviated New Drug Application (ANDA) Architect` | `Abbreviated_New_Drug_Application_ANDA_Architect` | Sanitized |
| `Accelerate Patient Recruitment & Retention` | `Accelerate_Patient_Recruitment_Retention` | Sanitized |
| `Action-Oriented Meeting Minutes & Tracker` | `Action-Oriented_Meeting_Minutes_Tracker` | Sanitized |
| `Active Directory Domain Dominance Forensics Analyst` | `Active_Directory_Domain_Dominance_Forensics_Analyst` | Overridden by `prompts/technical/security/skills.md` |
| `Activist Investor Defense Strategy Architect` | `Activist_Investor_Defense_Strategy_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Adaptive Control Loop Tuning Architect` | `Adaptive_Control_Loop_Tuning_Architect` | Overridden by `prompts/scientific/mathematics/systems/control_theory/skills.md` |
| `Adaptive Design & Interim Monitoring` | `Adaptive_Design_Interim_Monitoring` | Sanitized |
| `Adaptive Load Shedding and Backpressure Architect` | `Adaptive_Load_Shedding_and_Backpressure_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Adaptive Recruitment and Retention Strategy` | `Adaptive_Recruitment_and_Retention_Strategy` | Overridden by `prompts/clinical/trial_execution/skills.md` |
| `Advanced C2 Beacon PCAP Analysis Engineer` | `Advanced_C2_Beacon_PCAP_Analysis_Engineer` | Overridden by `prompts/technical/security/skills.md` |
| `Advanced Design Patterns: Fluent Interface` | `Advanced_Design_Patterns_Fluent_Interface` | Sanitized |
| `Advanced Python Testing` | `Advanced_Python_Testing` | Overridden by `prompts/technical/languages/python/skills.md` |
| `Advanced Red Team Adversary Emulation Architect` | `Advanced_Red_Team_Adversary_Emulation_Architect` | Overridden by `prompts/technical/security/skills.md` |
| `Advanced SOAR Playbook Engineering Architect` | `Advanced_SOAR_Playbook_Engineering_Architect` | Overridden by `prompts/technical/security/secops/skills.md` |
| `Advanced Sigma Rule Detection Architect` | `Advanced_Sigma_Rule_Detection_Architect` | Overridden by `prompts/technical/security/secops/skills.md` |
| `Advanced Volatile Memory Forensics Analyst` | `Advanced_Volatile_Memory_Forensics_Analyst` | Overridden by `prompts/technical/security/skills.md` |
| `Adversarial Prompt Robustness Tester` | `Adversarial_Prompt_Robustness_Tester` | Overridden by `prompts/technical/prompt_engineering/skills.md` |
| `Agent Persona Generator` | `Agent_Persona_Generator` | Overridden by `prompts/meta/meta_prompt_chain/skills.md` |
| `Air-Gapped Environment Deployment Architect` | `Air-Gapped_Environment_Deployment_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Algorithmic Dynamic Pricing & Yield Management Architect` | `Algorithmic_Dynamic_Pricing_Yield_Management_Architect` | Sanitized |
| `Algorithmic Multi-Touch Attribution Architect` | `Algorithmic_Multi-Touch_Attribution_Architect` | Overridden by `prompts/business/growth_engineering/skills.md` |
| `Analyze Adjudication KPIs` | `Analyze_Adjudication_KPIs` | Overridden by `prompts/clinical/adjudication/adjudication_workflow/skills.md` |
| `Applied Ethical Stress Tester` | `Applied_Ethical_Stress_Tester` | Overridden by `prompts/scientific/philosophy/ethics/normative_ethics/skills.md` |
| `Architect the Integration Blueprint` | `Architect_the_Integration_Blueprint` | Overridden by `prompts/clinical/eclinical_integration/eclinical_integration_workflow/skills.md` |
| `Architecture Design: Page Object Model` | `Architecture_Design_Page_Object_Model` | Sanitized |
| `Architecture Flow & Diagram Architect` | `Architecture_Flow_Diagram_Architect` | Sanitized |
| `Atlas Documentation Specialist` | `Atlas_Documentation_Specialist` | Overridden by `prompts/technical/documentation/skills.md` |
| `Audit Raw Data and Draft a CAPA Summary` | `Audit_Raw_Data_and_Draft_a_CAPA_Summary` | Overridden by `prompts/management/study_director/study_director_workflow/skills.md` |
| `Audit Trail Review` | `Audit_Trail_Review` | Overridden by `prompts/clinical/data_management/skills.md` |
| `Automated E-Discovery Reviewer` | `Automated_E-Discovery_Reviewer` | Overridden by `prompts/business/legal/skills.md` |
| `Automated Financial Variance Analyst` | `Automated_Financial_Variance_Analyst` | Overridden by `prompts/business/finance/skills.md` |
| `Automated Image Assessment System 510(k)` | `Automated_Image_Assessment_System_510_k` | Overridden by `prompts/regulatory/device_specifics/skills.md` |
| `Autonomous Automation Agent` | `Autonomous_Automation_Agent` | Overridden by `prompts/technical/automation/skills.md` |
| `Autonomous Automation Agent Upgrade` | `Autonomous_Automation_Agent_Upgrade` | Overridden by `prompts/technical/automation/skills.md` |
| `Autonomous Vehicle V2X Telemetry Architect` | `Autonomous_Vehicle_V2X_Telemetry_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `BRST Quantization and Faddeev-Popov Ghost Architect` | `BRST_Quantization_and_Faddeev-Popov_Ghost_Architect` | Overridden by `prompts/scientific/physics/quantum_field_theory/skills.md` |
| `Bioburden Testing SOP` | `Bioburden_Testing_SOP` | Overridden by `prompts/scientific/microbiology/microbiology_workflow/skills.md` |
| `Biological Evaluation Plan Builder` | `Biological_Evaluation_Plan_Builder` | Overridden by `prompts/scientific/biosafety/skills.md` |
| `Biological Safety Plan Developer` | `Biological_Safety_Plan_Developer` | Overridden by `prompts/scientific/biosafety/biological_safety_workflow/skills.md` |
| `Biologics License Application (BLA) Architect` | `Biologics_License_Application_BLA_Architect` | Sanitized |
| `Black Hole Perturbation Teukolsky Architect` | `Black_Hole_Perturbation_Teukolsky_Architect` | Overridden by `prompts/scientific/physics/relativity/general_relativity/skills.md` |
| `Board Deck Narrative Generation` | `Board_Deck_Narrative_Generation` | Overridden by `prompts/business/cfo/skills.md` |
| `Breakthrough Device Designation Architect` | `Breakthrough_Device_Designation_Architect` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `Budget Variance Analysis` | `Budget_Variance_Analysis` | Overridden by `prompts/business/cfo/skills.md` |
| `Bug Finder & Fixer (OpenAI Codex)` | `Bug_Finder_Fixer_OpenAI_Codex` | Sanitized |
| `Build an Audit-Ready Site-Payment Schedule` | `Build_an_Audit-Ready_Site-Payment_Schedule` | Overridden by `prompts/business/payment/skills.md` |
| `Build vs. Buy Decision Matrix` | `Build_vs_Buy_Decision_Matrix` | Sanitized |
| `CAPA Investigation Report Writer` | `CAPA_Investigation_Report_Writer` | Overridden by `prompts/regulatory/quality/skills.md` |
| `CAPA Management Process` | `CAPA_Management_Process` | Overridden by `prompts/regulatory/quality/skills.md` |
| `CAPA Plan Builder for Monitoring Findings` | `CAPA_Plan_Builder_for_Monitoring_Findings` | Overridden by `prompts/clinical/monitoring/clinical_monitoring_workflow/skills.md` |
| `CAPA Plan Generator` | `CAPA_Plan_Generator` | Overridden by `prompts/regulatory/quality/skills.md` |
| `CAPA Root Cause Investigator` | `CAPA_Root_Cause_Investigator` | Overridden by `prompts/regulatory/quality/skills.md` |
| `CAPA Root Cause and Resolution Architect` | `CAPA_Root_Cause_and_Resolution_Architect` | Overridden by `prompts/management/operations/skills.md` |
| `CAPA SOP Architect` | `CAPA_SOP_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `CDASH Alignment` | `CDASH_Alignment` | Overridden by `prompts/clinical/forms/skills.md` |
| `CDASH Mapping & Completion-Guide Assistant` | `CDASH_Mapping_Completion-Guide_Assistant` | Sanitized |
| `CDISC CRF Architect` | `CDISC_CRF_Architect` | Overridden by `prompts/clinical/data_management/skills.md` |
| `CDISC Cross-Dataset Relational Architect` | `CDISC_Cross-Dataset_Relational_Architect` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `CDISC SDTM/ADaM Mapping` | `CDISC_SDTM_ADaM_Mapping` | Overridden by `prompts/clinical/data_management/skills.md` |
| `CI/CD Pipeline Poisoning Forensics Architect` | `CI_CD_Pipeline_Poisoning_Forensics_Architect` | Overridden by `prompts/technical/security/skills.md` |
| `CQRS and Event Sourcing Architect` | `CQRS_and_Event_Sourcing_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `CRF Quality Auditor` | `CRF_Quality_Auditor` | Overridden by `prompts/clinical/forms/clinical_prompts_workflow/skills.md` |
| `CRF Shell Generator` | `CRF_Shell_Generator` | Overridden by `prompts/clinical/forms/clinical_prompts_workflow/skills.md` |
| `CRO Trial-Performance KPI Dashboard Blueprint` | `CRO_Trial-Performance_KPI_Dashboard_Blueprint` | Overridden by `prompts/management/operations/skills.md` |
| `CSM Portfolio Balancing` | `CSM_Portfolio_Balancing` | Overridden by `prompts/business/cx/skills.md` |
| `CSR Plain Language Summary Generator` | `CSR_Plain_Language_Summary_Generator` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `CSR Results and Safety Section` | `CSR_Results_and_Safety_Section` | Overridden by `prompts/technical/technical_writing/technical_writer_workflow/skills.md` |
| `CTD Module 2.5 Clinical Overview Architect` | `CTD_Module_2_5_Clinical_Overview_Architect` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `Cache Stampede Mitigation Architect` | `Cache_Stampede_Mitigation_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Callan-Symanzik Beta Function Architect` | `Callan-Symanzik_Beta_Function_Architect` | Overridden by `prompts/scientific/physics/quantum_field_theory/skills.md` |
| `Career Compass Advisor` | `Career_Compass_Advisor` | Overridden by `prompts/management/personal_effectiveness/skills.md` |
| `Carrier Screening System 510(k)` | `Carrier_Screening_System_510_k` | Overridden by `prompts/regulatory/device_specifics/skills.md` |
| `Cascading Failure Resilience Architect` | `Cascading_Failure_Resilience_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Causal Discovery DAG Architect` | `Causal_Discovery_DAG_Architect` | Overridden by `prompts/technical/data_science/skills.md` |
| `Cell-Based Architecture Designer` | `Cell-Based_Architecture_Designer` | Overridden by `prompts/technical/architecture/skills.md` |
| `Central Reading Paradigm Design` | `Central_Reading_Paradigm_Design` | Overridden by `prompts/clinical/imaging/imaging_workflow/skills.md` |
| `Change Control Regulatory Impact Assessor` | `Change_Control_Regulatory_Impact_Assessor` | Overridden by `prompts/regulatory/quality/skills.md` |
| `Change Data Capture Pipeline Architect` | `Change_Data_Capture_Pipeline_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Chaos Engineering Experiment Designer` | `Chaos_Engineering_Experiment_Designer` | Overridden by `prompts/technical/architecture/skills.md` |
| `Chaos Engineering Resilience Architect` | `Chaos_Engineering_Resilience_Architect` | Overridden by `prompts/technical/testing/skills.md` |
| `Chemical Characterization & TRA Work Plan` | `Chemical_Characterization_TRA_Work_Plan` | Sanitized |
| `Chiral Anomaly Fujikawa Path Integral Architect` | `Chiral_Anomaly_Fujikawa_Path_Integral_Architect` | Overridden by `prompts/scientific/physics/quantum_field_theory/skills.md` |
| `Citizen Petition Preparation` | `Citizen_Petition_Preparation` | Overridden by `prompts/regulatory/administrative/skills.md` |
| `Civil Money Penalties Hearing Response` | `Civil_Money_Penalties_Hearing_Response` | Overridden by `prompts/regulatory/administrative/skills.md` |
| `Cleaning Validation Protocol Architect` | `Cleaning_Validation_Protocol_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `ClinRO User Manual Generator` | `ClinRO_User_Manual_Generator` | Overridden by `prompts/scientific/coa/skills.md` |
| `Clinical Chemistry Device Classification` | `Clinical_Chemistry_Device_Classification` | Overridden by `prompts/regulatory/device_specifics/skills.md` |
| `Clinical ETL Mapping Spec` | `Clinical_ETL_Mapping_Spec` | Overridden by `prompts/clinical/data_management/data_management_etl_workflow/skills.md` |
| `Clinical ETL Pipeline Review` | `Clinical_ETL_Pipeline_Review` | Overridden by `prompts/clinical/data_management/data_management_etl_workflow/skills.md` |
| `Clinical ETL Transformation QC` | `Clinical_ETL_Transformation_QC` | Overridden by `prompts/clinical/data_management/data_management_etl_workflow/skills.md` |
| `Clinical Monitoring Plan Development` | `Clinical_Monitoring_Plan_Development` | Overridden by `prompts/clinical/monitoring/skills.md` |
| `Clinical Safety Synopsis for EU MDR CER` | `Clinical_Safety_Synopsis_for_EU_MDR_CER` | Overridden by `prompts/clinical/safety/clinical_safety_workflow/skills.md` |
| `Clinical Study Report (CSR) Narrative Drafter` | `Clinical_Study_Report_CSR_Narrative_Drafter` | Sanitized |
| `Clinical Study Report (CSR) Writing` | `Clinical_Study_Report_CSR_Writing` | Sanitized |
| `Clinical Trial Agreement (CTA) Negotiation` | `Clinical_Trial_Agreement_CTA_Negotiation` | Sanitized |
| `Clinical Trial Document Archiving` | `Clinical_Trial_Document_Archiving` | Overridden by `prompts/clinical/data_management/skills.md` |
| `Clinical Trial Protocol Compliance Review` | `Clinical_Trial_Protocol_Compliance_Review` | Overridden by `prompts/management/medical_director/skills.md` |
| `Clinical Trial Protocol Synopsis Architect` | `Clinical_Trial_Protocol_Synopsis_Architect` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `Clinical-Trial Budget and Burn-Rate Dashboard` | `Clinical-Trial_Budget_and_Burn-Rate_Dashboard` | Overridden by `prompts/business/hr_finance/skills.md` |
| `Clinical-Trial Protocol Creator` | `Clinical-Trial_Protocol_Creator` | Overridden by `prompts/clinical/protocol/protocol_workflow/skills.md` |
| `Clinical-Trial Timeline and Risk Radar` | `Clinical-Trial_Timeline_and_Risk_Radar` | Overridden by `prompts/management/project_management/skills.md` |
| `ClinicalTrials.gov Registration` | `ClinicalTrials_gov_Registration` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `Cloud IAM Least-Privilege Remediation Architect` | `Cloud_IAM_Least-Privilege_Remediation_Architect` | Overridden by `prompts/technical/security/skills.md` |
| `Cloud Identity Fabric Threat Hunting Architect` | `Cloud_Identity_Fabric_Threat_Hunting_Architect` | Overridden by `prompts/technical/security/secops/skills.md` |
| `Cloud Incident Response Forensics Architect` | `Cloud_Incident_Response_Forensics_Architect` | Overridden by `prompts/technical/security/skills.md` |
| `Code Formatting, Linting, and Refactoring Implementation` | `Code_Formatting_Linting_and_Refactoring_Implementation` | Sanitized |
| `Code Review Assistant (Aegis Security)` | `Code_Review_Assistant_Aegis_Security` | Sanitized |
| `Codebase Quality & Maintainability Analysis` | `Codebase_Quality_Maintainability_Analysis` | Sanitized |
| `Codebase Testing Plan` | `Codebase_Testing_Plan` | Overridden by `prompts/technical/software_engineering/tasks/skills.md` |
| `Coding Session Guidelines` | `Coding_Session_Guidelines` | Overridden by `prompts/technical/software_engineering/lifecycle/skills.md` |
| `Coleman-Weinberg Effective Potential Architect` | `Coleman-Weinberg_Effective_Potential_Architect` | Overridden by `prompts/scientific/physics/quantum_field_theory/skills.md` |
| `Combination Product Jurisdiction` | `Combination_Product_Jurisdiction` | Overridden by `prompts/regulatory/submissions/skills.md` |
| `Compassionate Analyst` | `Compassionate_Analyst` | Overridden by `prompts/clinical/therapy/music_therapy_workflow/skills.md` |
| `Compassionate Music Therapist & Composer` | `Compassionate_Music_Therapist_Composer` | Sanitized |
| `Competency-Based Onboarding Blueprint` | `Competency-Based_Onboarding_Blueprint` | Overridden by `prompts/management/training/learning_development_workflow/skills.md` |
| `Competitive-Bid Pricing & Margin Optimizer` | `Competitive-Bid_Pricing_Margin_Optimizer` | Sanitized |
| `Competitor-Positioning Brief` | `Competitor-Positioning_Brief` | Overridden by `prompts/business/development/skills.md` |
| `Compliance Gap & Risk Matrix` | `Compliance_Gap_Risk_Matrix` | Sanitized |
| `Compliance Gap Assessment` | `Compliance_Gap_Assessment` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `Compliance and Data Quality Monitoring Plan` | `Compliance_and_Data_Quality_Monitoring_Plan` | Overridden by `prompts/clinical/trial_execution/skills.md` |
| `Comprehensive Biocompatibility Test Matrix` | `Comprehensive_Biocompatibility_Test_Matrix` | Overridden by `prompts/scientific/biosafety/skills.md` |
| `Comprehensive Risk Register and Mitigation Plan` | `Comprehensive_Risk_Register_and_Mitigation_Plan` | Overridden by `prompts/management/project_management/project_management_workflow/skills.md` |
| `Comprehensive Task Template` | `Comprehensive_Task_Template` | Overridden by `prompts/meta/meta_prompt_chain/skills.md` |
| `Computer System Validation (CSV)` | `Computer_System_Validation_CSV` | Sanitized |
| `Concept Drift Mitigation Architect` | `Concept_Drift_Mitigation_Architect` | Overridden by `prompts/technical/data_science/skills.md` |
| `Confidential Computing Enclave Architect` | `Confidential_Computing_Enclave_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Content Validity & Reliability Analysis` | `Content_Validity_Reliability_Analysis` | Sanitized |
| `Continuous Integration & Delivery (DevOps Architect)` | `Continuous_Integration_Delivery_DevOps_Architect` | Sanitized |
| `Controlled Terminology Harmonizer` | `Controlled_Terminology_Harmonizer` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `Conversation Stochastic Modeler` | `Conversation_Stochastic_Modeler` | Overridden by `prompts/technical/data_science/skills.md` |
| `Corporate Capital Budgeting Investment Appraisal Architect` | `Corporate_Capital_Budgeting_Investment_Appraisal_Architect` | Overridden by `prompts/business/finance/skills.md` |
| `Corporate Capital Structure Optimization Architect` | `Corporate_Capital_Structure_Optimization_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Corporate Digital Transformation ROI Architect` | `Corporate_Digital_Transformation_ROI_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Corporate Diversification Synergy Architect` | `Corporate_Diversification_Synergy_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Corporate ESG Carbon Abatement Strategy Architect` | `Corporate_ESG_Carbon_Abatement_Strategy_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Corporate Financial Distress Predictive Altman Z-Score Architect` | `Corporate_Financial_Distress_Predictive_Altman_Z-Score_Architect` | Overridden by `prompts/business/finance/skills.md` |
| `Corporate Geopolitical Risk Mitigation Architect` | `Corporate_Geopolitical_Risk_Mitigation_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Corporate Merger Arbitrage Deal Risk Architect` | `Corporate_Merger_Arbitrage_Deal_Risk_Architect` | Overridden by `prompts/business/finance/skills.md` |
| `Corporate Spin-Off Carve-Out Architect` | `Corporate_Spin-Off_Carve-Out_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Corporate Transfer Pricing Optimization Architect` | `Corporate_Transfer_Pricing_Optimization_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Corporate Turnaround Restructuring Architect` | `Corporate_Turnaround_Restructuring_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Corporate Venture Capital Strategy Architect` | `Corporate_Venture_Capital_Strategy_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Corporate Vertical Integration Structuring Architect` | `Corporate_Vertical_Integration_Structuring_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Correction and Removal Reporting` | `Correction_and_Removal_Reporting` | Overridden by `prompts/regulatory/compliance/skills.md` |
| `Create a Risk-Based Monitoring & Mitigation SOP for RTSM` | `Create_a_Risk-Based_Monitoring_Mitigation_SOP_for_RTSM` | Sanitized |
| `Crisis-Management Playbook Generator` | `Crisis-Management_Playbook_Generator` | Overridden by `prompts/management/executive/skills.md` |
| `Cross-Border Data Privacy Architect` | `Cross-Border_Data_Privacy_Architect` | Overridden by `prompts/business/legal/skills.md` |
| `Cross-Border Joint Venture Structuring Architect` | `Cross-Border_Joint_Venture_Structuring_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Cross-Browser Infrastructure: Selenium Grid` | `Cross-Browser_Infrastructure_Selenium_Grid` | Sanitized |
| `Cross-Chain Interoperability Bridge Architect` | `Cross-Chain_Interoperability_Bridge_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Cross-Channel Behavioral Trigger Architect` | `Cross-Channel_Behavioral_Trigger_Architect` | Overridden by `prompts/business/growth_engineering/skills.md` |
| `Cross-Functional Advocacy Memo` | `Cross-Functional_Advocacy_Memo` | Overridden by `prompts/business/cx/skills.md` |
| `Cross-Study Operational Risk Heat Map and Mitigation Plan` | `Cross-Study_Operational_Risk_Heat_Map_and_Mitigation_Plan` | Overridden by `prompts/management/project_management/skills.md` |
| `Culinary Amnestic Reconstruction Engine (CARE)` | `Culinary_Amnestic_Reconstruction_Engine_CARE` | Sanitized |
| `Custom Axiomatic System Soundness Evaluator` | `Custom_Axiomatic_System_Soundness_Evaluator` | Overridden by `prompts/scientific/mathematics/formal_logic/skills.md` |
| `Cyber Device Security Plan` | `Cyber_Device_Security_Plan` | Overridden by `prompts/regulatory/compliance/skills.md` |
| `DFT Transition State Architect` | `DFT_Transition_State_Architect` | Overridden by `prompts/scientific/chemistry/computational/quantum_chemistry/skills.md` |
| `DHT Integration Regulatory Checklist` | `DHT_Integration_Regulatory_Checklist` | Overridden by `prompts/regulatory/adherence/skills.md` |
| `DMAIC Process Optimization Architect` | `DMAIC_Process_Optimization_Architect` | Overridden by `prompts/business/operations/lean_six_sigma/skills.md` |
| `DRY Codebase Analysis` | `DRY_Codebase_Analysis` | Overridden by `prompts/technical/architecture/skills.md` |
| `Dantzig-Wolfe Column Generation Architect` | `Dantzig-Wolfe_Column_Generation_Architect` | Overridden by `prompts/scientific/mathematics/optimization/skills.md` |
| `Data Architecture Blueprint` | `Data_Architecture_Blueprint` | Overridden by `prompts/clinical/data_management/skills.md` |
| `Data De-identification` | `Data_De-identification` | Overridden by `prompts/clinical/data_management/skills.md` |
| `Data Integrity ALCOA+ Audit Architect` | `Data_Integrity_ALCOA_Audit_Architect` | Sanitized |
| `Data Management Plan (DMP) Development` | `Data_Management_Plan_DMP_Development` | Sanitized |
| `Data Mapping and Transformation Playbook` | `Data_Mapping_and_Transformation_Playbook` | Overridden by `prompts/clinical/eclinical_integration/eclinical_integration_workflow/skills.md` |
| `Data Mesh Topology Architect` | `Data_Mesh_Topology_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Data Privacy Clean Room Architect` | `Data_Privacy_Clean_Room_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Data Residency & Localization Architect` | `Data_Residency_Localization_Architect` | Sanitized |
| `Data Safety Monitoring Board Report Synthesizer` | `Data_Safety_Monitoring_Board_Report_Synthesizer` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `Data-Quality Risk Heat Map` | `Data-Quality_Risk_Heat_Map` | Overridden by `prompts/management/vp_statistics/vp_statistics_workflow/skills.md` |
| `Data-to-Insight Analyst` | `Data-to-Insight_Analyst` | Overridden by `prompts/communication/skills.md` |
| `Database Lock Procedures` | `Database_Lock_Procedures` | Overridden by `prompts/clinical/data_management/skills.md` |
| `Database Read Replica Lag Mitigation Architect` | `Database_Read_Replica_Lag_Mitigation_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `De Novo Request Preparation` | `De_Novo_Request_Preparation` | Overridden by `prompts/regulatory/submissions/skills.md` |
| `DeFi Protocol Economic Security Architect` | `DeFi_Protocol_Economic_Security_Architect` | Overridden by `prompts/technical/security/skills.md` |
| `Decentralized Identity and Verifiable Credentials Architect` | `Decentralized_Identity_and_Verifiable_Credentials_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Decentralized Trial Risk Matrix` | `Decentralized_Trial_Risk_Matrix` | Overridden by `prompts/clinical/data_management/skills.md` |
| `Deception Technology & Active Defense Architect` | `Deception_Technology_Active_Defense_Architect` | Sanitized |
| `Define-XML Analysis Results Metadata Architect` | `Define-XML_Analysis_Results_Metadata_Architect` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `Density Refiner` | `Density_Refiner` | Overridden by `prompts/communication/skills.md` |
| `Deontic Logic Normative Conflict Resolver` | `Deontic_Logic_Normative_Conflict_Resolver` | Overridden by `prompts/scientific/philosophy/logic/philosophical_logic/skills.md` |
| `Dependencies & Security Posture Analysis` | `Dependencies_Security_Posture_Analysis` | Sanitized |
| `Design Error Prevention` | `Design_Error_Prevention` | Overridden by `prompts/clinical/forms/skills.md` |
| `Design Verification Test Plan` | `Design_Verification_Test_Plan` | Overridden by `prompts/technical/testing/testing_workflow/skills.md` |
| `Design Verification for BCR-ABL Tests` | `Design_Verification_for_BCR-ABL_Tests` | Overridden by `prompts/regulatory/device_specifics/skills.md` |
| `Design a Patient-Centered Randomization Scheme` | `Design_a_Patient-Centered_Randomization_Scheme` | Overridden by `prompts/clinical/rtsm/rtsm_workflow/skills.md` |
| `Design a Robust Preclinical Pathology Study Protocol` | `Design_a_Robust_Preclinical_Pathology_Study_Protocol` | Overridden by `prompts/scientific/pathology/pathology_study_workflow/skills.md` |
| `Design the Study` | `Design_the_Study` | Overridden by `prompts/scientific/chemical_characterization/chemical_characterization_workflow/skills.md` |
| `Detailed Project Blueprint and Timeline` | `Detailed_Project_Blueprint_and_Timeline` | Overridden by `prompts/management/project_management/project_management_workflow/skills.md` |
| `DevEx Documentation Architect` | `DevEx_Documentation_Architect` | Overridden by `prompts/technical/software_engineering/tasks/skills.md` |
| `Development Safety Update Report Architect` | `Development_Safety_Update_Report_Architect` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `Devil’s-Advocate Stress Test` | `Devil_s-Advocate_Stress_Test` | Overridden by `prompts/communication/skills.md` |
| `Digest Regulatory Updates Affecting Protocol` | `Digest_Regulatory_Updates_Affecting_Protocol` | Overridden by `prompts/management/clinical_research_manager/skills.md` |
| `Digital Health Technology (DHT) Validation` | `Digital_Health_Technology_DHT_Validation` | Sanitized |
| `Digital Transformation Roadmap for Clinical Operations` | `Digital_Transformation_Roadmap_for_Clinical_Operations` | Overridden by `prompts/management/executive/skills.md` |
| `Directed Food Laboratory Order Verification` | `Directed_Food_Laboratory_Order_Verification` | Overridden by `prompts/regulatory/food_safety/skills.md` |
| `Discontinuous Galerkin Hyperbolic PDE Architect` | `Discontinuous_Galerkin_Hyperbolic_PDE_Architect` | Overridden by `prompts/scientific/mathematics/numerical_methods/skills.md` |
| `Discrepancy Detection & Query Log Generator` | `Discrepancy_Detection_Query_Log_Generator` | Sanitized |
| `Disruption Radar` | `Disruption_Radar` | Overridden by `prompts/business/vp_tech_innovation/skills.md` |
| `Distressed Debt Restructuring Chapter 11 Architect` | `Distressed_Debt_Restructuring_Chapter_11_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Distributed Actor Model Architect` | `Distributed_Actor_Model_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Actor Model Topology Architect` | `Distributed_Actor_Model_Topology_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Caching Strategy Architect` | `Distributed_Caching_Strategy_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Change Data Capture Pipeline Architect` | `Distributed_Change_Data_Capture_Pipeline_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Circuit Breaker Resiliency Architect` | `Distributed_Circuit_Breaker_Resiliency_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Clock Synchronization Architect` | `Distributed_Clock_Synchronization_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Data Skew Mitigation Architect` | `Distributed_Data_Skew_Mitigation_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Database Clock Synchronization Architect` | `Distributed_Database_Clock_Synchronization_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Database Sharding Architect` | `Distributed_Database_Sharding_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Knowledge Graph Architect` | `Distributed_Knowledge_Graph_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Lock Contention Mitigation Architect` | `Distributed_Lock_Contention_Mitigation_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Lock Manager Architect` | `Distributed_Lock_Manager_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Message Broker Topology Architect` | `Distributed_Message_Broker_Topology_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Observability and Telemetry Architect` | `Distributed_Observability_and_Telemetry_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Rate Limiting Architect` | `Distributed_Rate_Limiting_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Search Engine Topology Architect` | `Distributed_Search_Engine_Topology_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Secrets Management Topology Architect` | `Distributed_Secrets_Management_Topology_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Task Queue and Background Job Processing Architect` | `Distributed_Task_Queue_and_Background_Job_Processing_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Transaction Orchestration Architect` | `Distributed_Transaction_Orchestration_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Vector Database Architect` | `Distributed_Vector_Database_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Distributed Web Crawler Pipeline Architect` | `Distributed_Web_Crawler_Pipeline_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Diversity Action Plan Development` | `Diversity_Action_Plan_Development` | Overridden by `prompts/clinical/trial_execution/skills.md` |
| `Documentation and Repository Structure Implementation` | `Documentation_and_Repository_Structure_Implementation` | Overridden by `prompts/technical/repository_refactoring/skills.md` |
| `Domain-Driven Design Bounded Context Architect` | `Domain-Driven_Design_Bounded_Context_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Draft a Data Management Plan Section` | `Draft_a_Data_Management_Plan_Section` | Overridden by `prompts/clinical/data/clinical_data_workflow/skills.md` |
| `Draft a GLP-Compliant Study Protocol` | `Draft_a_GLP-Compliant_Study_Protocol` | Overridden by `prompts/management/study_director/study_director_workflow/skills.md` |
| `Driver Configuration: WebDriver Initialization` | `Driver_Configuration_WebDriver_Initialization` | Sanitized |
| `Dual MDR / IVDR Conformity-Assessment Roadmap` | `Dual_MDR_IVDR_Conformity-Assessment_Roadmap` | Sanitized |
| `Dual-Language Figure Prompt` | `Dual-Language_Figure_Prompt` | Overridden by `prompts/scientific/biostatistics/skills.md` |
| `Dunnett Adjustment R Code Generator` | `Dunnett_Adjustment_R_Code_Generator` | Overridden by `prompts/scientific/biostatistics/skills.md` |
| `Dynamic Causal Modeling Architect` | `Dynamic_Causal_Modeling_Architect` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `Dynamic Epistemic Drift Mitigator` | `Dynamic_Epistemic_Drift_Mitigator` | Overridden by `prompts/meta/agent_orchestration/skills.md` |
| `E2E Test Discovery Lifecycle Template` | `E2E_Test_Discovery_Lifecycle_Template` | Overridden by `prompts/technical/software_engineering/lifecycle/skills.md` |
| `E2E Test Discovery Template` | `E2E_Test_Discovery_Template` | Overridden by `prompts/technical/testing/testing_workflow/skills.md` |
| `EO Sterilization Validation Protocol` | `EO_Sterilization_Validation_Protocol` | Overridden by `prompts/scientific/microbiology/microbiology_workflow/skills.md` |
| `EU IVDR Performance Evaluation Report Architect` | `EU_IVDR_Performance_Evaluation_Report_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `EU MDR Clinical Evaluation Report Architect` | `EU_MDR_Clinical_Evaluation_Report_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `EU MDR PMCF Plan Architect` | `EU_MDR_PMCF_Plan_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `EU MDR PSUR Architect` | `EU_MDR_PSUR_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `EU MDR Post-Market Surveillance Plan Architect` | `EU_MDR_Post-Market_Surveillance_Plan_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `EU MDR Technical Documentation Architect` | `EU_MDR_Technical_Documentation_Architect` | Overridden by `prompts/regulatory/submissions/skills.md` |
| `EU MDR Technical-Documentation Gap Assessment` | `EU_MDR_Technical-Documentation_Gap_Assessment` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `Earnings Call Script Prep` | `Earnings_Call_Script_Prep` | Overridden by `prompts/business/cfo/skills.md` |
| `Eco-Crypto Haiku Oracle` | `Eco-Crypto_Haiku_Oracle` | Overridden by `prompts/lifestyle/arboreal_crypto_haiku/skills.md` |
| `Edge AI Inference Architect` | `Edge_AI_Inference_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Edge Computing Topology Architect` | `Edge_Computing_Topology_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Edit-Check Specification Builder for New eCRF Fields` | `Edit-Check_Specification_Builder_for_New_eCRF_Fields` | Overridden by `prompts/clinical/data/clinical_data_workflow/skills.md` |
| `Eisenhower Matrix Coach` | `Eisenhower_Matrix_Coach` | Overridden by `prompts/management/personal_effectiveness/skills.md` |
| `Electrocatalytic Mechanism Architect` | `Electrocatalytic_Mechanism_Architect` | Overridden by `prompts/scientific/chemistry/physical/electrochemistry/skills.md` |
| `Electronic Data Capture Implementation` | `Electronic_Data_Capture_Implementation` | Overridden by `prompts/clinical/forms/skills.md` |
| `Elevator Pitch for Expensive Tech` | `Elevator_Pitch_for_Expensive_Tech` | Overridden by `prompts/business/vp_tech_innovation/skills.md` |
| `Emerging-Market Opportunity Scan` | `Emerging-Market_Opportunity_Scan` | Overridden by `prompts/business/development/skills.md` |
| `Emerging-Science Horizon Scan` | `Emerging-Science_Horizon_Scan` | Overridden by `prompts/management/executive/skills.md` |
| `Empathy-Map Facilitator` | `Empathy-Map_Facilitator` | Overridden by `prompts/communication/skills.md` |
| `Enantioselective Catalytic Mechanism Architect` | `Enantioselective_Catalytic_Mechanism_Architect` | Overridden by `prompts/scientific/chemistry/organic/asymmetric_synthesis/skills.md` |
| `Endotoxin Control & 510(k) Risk Plan` | `Endotoxin_Control_510_k_Risk_Plan` | Sanitized |
| `Enterprise Collaboration Portal Architect` | `Enterprise_Collaboration_Portal_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Enterprise RAG Architecture Designer` | `Enterprise_RAG_Architecture_Designer` | Overridden by `prompts/technical/architecture/skills.md` |
| `Ephemeral Sandbox Ecosystem Architect` | `Ephemeral_Sandbox_Ecosystem_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Epistemic Logic Multi-Agent Knowledge Architect` | `Epistemic_Logic_Multi-Agent_Knowledge_Architect` | Overridden by `prompts/scientific/mathematics/formal_logic/skills.md` |
| `Epistemic Regress Topology Architect` | `Epistemic_Regress_Topology_Architect` | Overridden by `prompts/scientific/philosophy/epistemology/formal_epistemology/skills.md` |
| `Establishment of Food Traceability Plan` | `Establishment_of_Food_Traceability_Plan` | Overridden by `prompts/regulatory/food_safety/skills.md` |
| `EtO Sterilization Process FMEA` | `EtO_Sterilization_Process_FMEA` | Overridden by `prompts/scientific/sterility/sterility_workflow/skills.md` |
| `Evaluate Device–Tissue Interface Findings` | `Evaluate_Device_Tissue_Interface_Findings` | Overridden by `prompts/scientific/pathology/pathology_study_workflow/skills.md` |
| `Event-Driven Dead Letter Queue Remediation Architect` | `Event-Driven_Dead_Letter_Queue_Remediation_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Event-Driven Topology Designer` | `Event-Driven_Topology_Designer` | Overridden by `prompts/technical/architecture/skills.md` |
| `Event-Sourced Saga Orchestration Architect` | `Event-Sourced_Saga_Orchestration_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Execution Optimization: Parallel Testing` | `Execution_Optimization_Parallel_Testing` | Sanitized |
| `Executive Briefing Architect (TL;DR)` | `Executive_Briefing_Architect_TL_DR` | Sanitized |
| `Executive Sponsor Briefing Deck Outline` | `Executive_Sponsor_Briefing_Deck_Outline` | Overridden by `prompts/management/project_management/skills.md` |
| `Executive Trial-Health Dashboard` | `Executive_Trial-Health_Dashboard` | Overridden by `prompts/management/executive/skills.md` |
| `Executive-Ready Brief and Talking Points` | `Executive-Ready_Brief_and_Talking_Points` | Overridden by `prompts/management/executive/skills.md` |
| `Explain-Like-I’m-5 (ELI5)` | `Explain-Like-I_m-5_ELI5` | Sanitized |
| `FDA 483 Response Strategist` | `FDA_483_Response_Strategist` | Overridden by `prompts/regulatory/quality/skills.md` |
| `FDA Breakthrough Device Designation Architect` | `FDA_Breakthrough_Device_Designation_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `FDA CSA Risk-Based Testing Strategy Architect` | `FDA_CSA_Risk-Based_Testing_Strategy_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `FDA De Novo Classification Request Architect` | `FDA_De_Novo_Classification_Request_Architect` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `FDA Fast Track Designation Architect` | `FDA_Fast_Track_Designation_Architect` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `FDA MDR/MDV Adverse-Event Narrative` | `FDA_MDR_MDV_Adverse-Event_Narrative` | Overridden by `prompts/clinical/safety/clinical_safety_workflow/skills.md` |
| `FDA Missing-Data Query Response` | `FDA_Missing-Data_Query_Response` | Overridden by `prompts/scientific/biostatistics/skills.md` |
| `FDA OOS Investigation Architect` | `FDA_OOS_Investigation_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `FDA Type II Drug Master File (DMF) Architect` | `FDA_Type_II_Drug_Master_File_DMF_Architect` | Sanitized |
| `FDA-Aligned AI Governance Framework` | `FDA-Aligned_AI_Governance_Framework` | Overridden by `prompts/management/executive/skills.md` |
| `FWER Gatekeeping Procedure Code Generator` | `FWER_Gatekeeping_Procedure_Code_Generator` | Overridden by `prompts/scientific/biostatistics/skills.md` |
| `Fair-Market-Value Budget Negotiation Brief` | `Fair-Market-Value_Budget_Negotiation_Brief` | Overridden by `prompts/management/operations/skills.md` |
| `Feature Flag and Progressive Delivery Architect` | `Feature_Flag_and_Progressive_Delivery_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Federated Learning Differential Privacy Architect` | `Federated_Learning_Differential_Privacy_Architect` | Overridden by `prompts/technical/data_science/skills.md` |
| `Federated Learning Privacy-Preserving Architect` | `Federated_Learning_Privacy-Preserving_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Federated Learning Topology Architect` | `Federated_Learning_Topology_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Feynman Rule Derivation Architect` | `Feynman_Rule_Derivation_Architect` | Overridden by `prompts/scientific/physics/quantum_field_theory/skills.md` |
| `Financial Conflict of Interest (FCOI) Reporting` | `Financial_Conflict_of_Interest_FCOI_Reporting` | Sanitized |
| `Financial Disclosure Certification` | `Financial_Disclosure_Certification` | Overridden by `prompts/regulatory/administrative/skills.md` |
| `Fine-Grained Authorization Architect` | `Fine-Grained_Authorization_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Finite Element Analysis (FEA) Interpreter` | `Finite_Element_Analysis_FEA_Interpreter` | Sanitized |
| `Firmware and UEFI Bootkit Forensics Analyst` | `Firmware_and_UEFI_Bootkit_Forensics_Analyst` | Overridden by `prompts/technical/security/secops/skills.md` |
| `Fishbone Facilitator` | `Fishbone_Facilitator` | Overridden by `prompts/management/operations/skills.md` |
| `Folder and Module Organization` | `Folder_and_Module_Organization` | Overridden by `prompts/technical/software_engineering/lifecycle/skills.md` |
| `Food Safety Audit Reporting (Regulatory)` | `Food_Safety_Audit_Reporting_Regulatory` | Sanitized |
| `Forecast Site-Level Drug Supply & Resupply Strategy` | `Forecast_Site-Level_Drug_Supply_Resupply_Strategy` | Sanitized |
| `Foreign Supplier Verification Program (FSVP) Audit` | `Foreign_Supplier_Verification_Program_FSVP_Audit` | Sanitized |
| `Forensic Super Timeline Analysis Architect` | `Forensic_Super_Timeline_Analysis_Architect` | Overridden by `prompts/technical/security/secops/skills.md` |
| `Forge - Script Reliability Agent` | `Forge_-_Script_Reliability_Agent` | Overridden by `prompts/technical/devops/skills.md` |
| `Forward-Looking Resource & Capacity Forecast` | `Forward-Looking_Resource_Capacity_Forecast` | Sanitized |
| `Fractal Epistemic Consensus Architect` | `Fractal_Epistemic_Consensus_Architect` | Overridden by `prompts/meta/agent_orchestration/skills.md` |
| `Framework Best Practices: Locator Strategy` | `Framework_Best_Practices_Locator_Strategy` | Sanitized |
| `Framework Implementation: Data-Driven Testing` | `Framework_Implementation_Data-Driven_Testing` | Sanitized |
| `Free Energy Perturbation Architect` | `Free_Energy_Perturbation_Architect` | Overridden by `prompts/scientific/chemistry/computational/molecular_dynamics/skills.md` |
| `Free Logic Empty Names Formalizer` | `Free_Logic_Empty_Names_Formalizer` | Overridden by `prompts/scientific/philosophy/logic/philosophical_logic/skills.md` |
| `Freedom of Information Act (FOIA) Request` | `Freedom_of_Information_Act_FOIA_Request` | Sanitized |
| `Friction-Hunting Onboarding Audit` | `Friction-Hunting_Onboarding_Audit` | Overridden by `prompts/business/cx/skills.md` |
| `Functional Data Analysis Architect` | `Functional_Data_Analysis_Architect` | Overridden by `prompts/scientific/statistics/inference/nonparametric_methods/skills.md` |
| `GCP and GDPR Training Compliance Risk Report` | `GCP_and_GDPR_Training_Compliance_Risk_Report` | Overridden by `prompts/business/hr_finance/skills.md` |
| `GLP Quality Assurance` | `GLP_Quality_Assurance` | Overridden by `prompts/regulatory/quality/skills.md` |
| `GPU Cluster Orchestration Architect` | `GPU_Cluster_Orchestration_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `GTM Pricing Elasticity Architect` | `GTM_Pricing_Elasticity_Architect` | Overridden by `prompts/business/growth_engineering/skills.md` |
| `Generate & QC Submission-Ready TLFs` | `Generate_QC_Submission-Ready_TLFs` | Sanitized |
| `Generate an Executive Summary for the Final Report` | `Generate_an_Executive_Summary_for_the_Final_Report` | Overridden by `prompts/management/study_director/study_director_workflow/skills.md` |
| `Generative AI Guardrails Gateway Architect` | `Generative_AI_Guardrails_Gateway_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `GitHub Custom Agent Creator` | `GitHub_Custom_Agent_Creator` | Overridden by `prompts/technical/software_engineering/tasks/skills.md` |
| `Global CDN Topology Architect` | `Global_CDN_Topology_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Global Market Entry Expansion Architect` | `Global_Market_Entry_Expansion_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Global Regulatory and Tax Matrix for Site Payments` | `Global_Regulatory_and_Tax_Matrix_for_Site_Payments` | Overridden by `prompts/business/payment/skills.md` |
| `Global Supply Chain Resilience Architect` | `Global_Supply_Chain_Resilience_Architect` | Overridden by `prompts/business/operations/supply_chain/skills.md` |
| `Graph Database Traversal Architect` | `Graph_Database_Traversal_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `GraphQL Supergraph Federation Architect` | `GraphQL_Supergraph_Federation_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `HFT Low-Latency Architecture Designer` | `HFT_Low-Latency_Architecture_Designer` | Overridden by `prompts/technical/architecture/skills.md` |
| `HTAP Real-Time Analytics Architect` | `HTAP_Real-Time_Analytics_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Hands-On Procedure Coaching` | `Hands-On_Procedure_Coaching` | Overridden by `prompts/scientific/bioskills/bioskills_workflow/skills.md` |
| `Hardware Side-Channel Attack Modeling Architect` | `Hardware_Side-Channel_Attack_Modeling_Architect` | Overridden by `prompts/technical/security/skills.md` |
| `Hero's Journey Storyboarder` | `Hero_s_Journey_Storyboarder` | Overridden by `prompts/communication/skills.md` |
| `Heuristic-Evaluation Coach` | `Heuristic-Evaluation_Coach` | Overridden by `prompts/technical/design/skills.md` |
| `Hexagonal Architecture Implementation` | `Hexagonal_Architecture_Implementation` | Overridden by `prompts/technical/architecture/skills.md` |
| `Hexagonal Architecture Principles` | `Hexagonal_Architecture_Principles` | Overridden by `prompts/technical/architecture/skills.md` |
| `Hexagonal Architecture Review` | `Hexagonal_Architecture_Review` | Overridden by `prompts/technical/architecture/skills.md` |
| `High-Scale OTT Video Streaming Architect` | `High-Scale_OTT_Video_Streaming_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `High-Scale WebSocket Push Architect` | `High-Scale_WebSocket_Push_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `High-Throughput Distributed ID Generator Architect` | `High-Throughput_Distributed_ID_Generator_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `High-Throughput Geospatial Indexing Architect` | `High-Throughput_Geospatial_Indexing_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `High-Throughput LLM Inference Serving Architect` | `High-Throughput_LLM_Inference_Serving_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `High-Throughput Order Matching Engine Architect` | `High-Throughput_Order_Matching_Engine_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Hodge Theory Harmonic Form Architect` | `Hodge_Theory_Harmonic_Form_Architect` | Overridden by `prompts/scientific/mathematics/geometry/differential/skills.md` |
| `Hostile Takeover Defense Matrix Architect` | `Hostile_Takeover_Defense_Matrix_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Hosting Cost Reduction ToT Plan` | `Hosting_Cost_Reduction_ToT_Plan` | Overridden by `prompts/management/executive/skills.md` |
| `Human Factors Validation Study Protocol` | `Human_Factors_Validation_Study_Protocol` | Overridden by `prompts/technical/testing/testing_workflow/skills.md` |
| `Human Factors/Usability Summary` | `Human_Factors_Usability_Summary` | Overridden by `prompts/regulatory/adherence/skills.md` |
| `Humanitarian Device Exemption (HDE)` | `Humanitarian_Device_Exemption_HDE` | Sanitized |
| `Hype vs. Reality Analysis` | `Hype_vs_Reality_Analysis` | Sanitized |
| `ICH E9(R1) Estimand Builder` | `ICH_E9_R1_Estimand_Builder` | Sanitized |
| `IDE Application Preparation` | `IDE_Application_Preparation` | Overridden by `prompts/regulatory/submissions/skills.md` |
| `IDE Determination and Device Classification` | `IDE_Determination_and_Device_Classification` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `IEC 62366-1 Summative Usability Evaluation Protocol Architect` | `IEC_62366-1_Summative_Usability_Evaluation_Protocol_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `IND Determination and Application` | `IND_Determination_and_Application` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `IND Readiness Gap Analysis & Filing Road-Map` | `IND_Readiness_Gap_Analysis_Filing_Road-Map` | Sanitized |
| `IQ/OQ/PQ Validation` | `IQ_OQ_PQ_Validation` | Overridden by `prompts/clinical/eclinical_integration/skills.md` |
| `IRB Protocol Review` | `IRB_Protocol_Review` | Overridden by `prompts/regulatory/compliance/skills.md` |
| `ISO 10993 Biological Evaluation Plan Architect` | `ISO_10993_Biological_Evaluation_Plan_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `ISO Strategist` | `ISO_Strategist` | Overridden by `prompts/clinical/therapy/music_therapy_workflow/skills.md` |
| `IVD Performance Study Compliance Review` | `IVD_Performance_Study_Compliance_Review` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `IVDR Performance-Evaluation Plan Blueprint` | `IVDR_Performance-Evaluation_Plan_Blueprint` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `Idempotency and API Retry Strategy Architect` | `Idempotency_and_API_Retry_Strategy_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Identity Threat Detection and Response Architect` | `Identity_Threat_Detection_and_Response_Architect` | Overridden by `prompts/technical/security/iam_security/skills.md` |
| `Image Acquisition QC Workflow Blueprint` | `Image_Acquisition_QC_Workflow_Blueprint` | Overridden by `prompts/clinical/imaging/imaging_workflow/skills.md` |
| `Imaging Charter Draft` | `Imaging_Charter_Draft` | Overridden by `prompts/clinical/imaging/imaging_workflow/skills.md` |
| `Imaging Endpoint Process Standards Checklist` | `Imaging_Endpoint_Process_Standards_Checklist` | Overridden by `prompts/regulatory/adherence/skills.md` |
| `Immutable Financial Ledger Architect` | `Immutable_Financial_Ledger_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Import Entry Data Element Compilation` | `Import_Entry_Data_Element_Compilation` | Overridden by `prompts/regulatory/administrative/skills.md` |
| `Inclusion/Exclusion, Endpoints & Sample-Size Deep Dive` | `Inclusion_Exclusion_Endpoints_Sample-Size_Deep_Dive` | Sanitized |
| `Inflationary Tensor Perturbation Architect` | `Inflationary_Tensor_Perturbation_Architect` | Overridden by `prompts/scientific/physics/cosmology/early_universe/skills.md` |
| `Informed Consent Exception (Emergency)` | `Informed_Consent_Exception_Emergency` | Sanitized |
| `Informed Consent Form Plain Language Translator` | `Informed_Consent_Form_Plain_Language_Translator` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `Informed Consent Process Optimization` | `Informed_Consent_Process_Optimization` | Overridden by `prompts/clinical/trial_execution/skills.md` |
| `Infrastructure Configuration Drift Remediation Architect` | `Infrastructure_Configuration_Drift_Remediation_Architect` | Overridden by `prompts/technical/devops/skills.md` |
| `Infrastructure as Code (IaC) Security Architect` | `Infrastructure_as_Code_IaC_Security_Architect` | Sanitized |
| `Insider Threat Behavioral Analytics Engineer` | `Insider_Threat_Behavioral_Analytics_Engineer` | Overridden by `prompts/technical/security/skills.md` |
| `Inspection-Readiness Drill (CAPA Builder)` | `Inspection-Readiness_Drill_CAPA_Builder` | Sanitized |
| `Integrated Submission Strategy Coach` | `Integrated_Submission_Strategy_Coach` | Overridden by `prompts/regulatory/quality/skills.md` |
| `Intellectual Property Claim Drafter` | `Intellectual_Property_Claim_Drafter` | Overridden by `prompts/business/legal/skills.md` |
| `Intended Use and Indications for Use Alignment` | `Intended_Use_and_Indications_for_Use_Alignment` | Overridden by `prompts/regulatory/adherence/skills.md` |
| `Interim Results Executive Brief` | `Interim_Results_Executive_Brief` | Overridden by `prompts/management/vp_statistics/vp_statistics_workflow/skills.md` |
| `Interpret the Chemistry & Assess Risk` | `Interpret_the_Chemistry_Assess_Risk` | Sanitized |
| `Intuitionistic Logic Natural Deduction Prover` | `Intuitionistic_Logic_Natural_Deduction_Prover` | Overridden by `prompts/scientific/philosophy/logic/foundations/proof_theory/skills.md` |
| `Inventory & Demand-Planning Simulation` | `Inventory_Demand-Planning_Simulation` | Sanitized |
| `Investigational New Drug (IND) Architect` | `Investigational_New_Drug_IND_Architect` | Sanitized |
| `Investigator Follow-up Email & Action-Item Tracker` | `Investigator_Follow-up_Email_Action-Item_Tracker` | Sanitized |
| `Investigator's Brochure Safety Update Architect` | `Investigator_s_Brochure_Safety_Update_Architect` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `Investigator's Brochure Summary of Changes` | `Investigator_s_Brochure_Summary_of_Changes` | Overridden by `prompts/technical/technical_writing/technical_writer_workflow/skills.md` |
| `Investigator-Site Payment Forecast` | `Investigator-Site_Payment_Forecast` | Overridden by `prompts/business/payment/skills.md` |
| `Investor FAQ Generation` | `Investor_FAQ_Generation` | Overridden by `prompts/business/cfo/skills.md` |
| `Investor and Board Narrative Builder` | `Investor_and_Board_Narrative_Builder` | Overridden by `prompts/management/executive/skills.md` |
| `IoT Digital Twin Architect` | `IoT_Digital_Twin_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Jules API Scout` | `Jules_API_Scout` | Overridden by `prompts/google_jules/skills.md` |
| `Jules Agile Orchestrator` | `Jules_Agile_Orchestrator` | Overridden by `prompts/google_jules/skills.md` |
| `Jules Compliance Officer` | `Jules_Compliance_Officer` | Overridden by `prompts/google_jules/skills.md` |
| `Jules Concurrency Architect` | `Jules_Concurrency_Architect` | Overridden by `prompts/google_jules/skills.md` |
| `Jules Data Architect` | `Jules_Data_Architect` | Overridden by `prompts/google_jules/skills.md` |
| `Jules DevOps Engineer` | `Jules_DevOps_Engineer` | Overridden by `prompts/google_jules/skills.md` |
| `Jules Developer Agent` | `Jules_Developer_Agent` | Overridden by `prompts/google_jules/skills.md` |
| `Jules E2E Test Engineer` | `Jules_E2E_Test_Engineer` | Overridden by `prompts/google_jules/skills.md` |
| `Jules FinOps Profiler` | `Jules_FinOps_Profiler` | Overridden by `prompts/google_jules/skills.md` |
| `Jules Maintainer` | `Jules_Maintainer` | Overridden by `prompts/google_jules/skills.md` |
| `Jules Orchestrator` | `Jules_Orchestrator` | Overridden by `prompts/google_jules/skills.md` |
| `Jules Product Architect` | `Jules_Product_Architect` | Overridden by `prompts/google_jules/skills.md` |
| `Jules QA Gatekeeper` | `Jules_QA_Gatekeeper` | Overridden by `prompts/google_jules/skills.md` |
| `Jules Security Auditor` | `Jules_Security_Auditor` | Overridden by `prompts/google_jules/skills.md` |
| `Jules System Designer` | `Jules_System_Designer` | Overridden by `prompts/google_jules/skills.md` |
| `Jules Test Generator` | `Jules_Test_Generator` | Overridden by `prompts/google_jules/skills.md` |
| `Jules UX Writer` | `Jules_UX_Writer` | Overridden by `prompts/google_jules/skills.md` |
| `KPI Dashboard & Monthly Ops-Review Pack` | `KPI_Dashboard_Monthly_Ops-Review_Pack` | Sanitized |
| `Kubernetes Cluster Security Posture Architect` | `Kubernetes_Cluster_Security_Posture_Architect` | Overridden by `prompts/technical/security/skills.md` |
| `Kubernetes Container Escape Forensics Analyst` | `Kubernetes_Container_Escape_Forensics_Analyst` | Overridden by `prompts/technical/security/secops/incident_response/skills.md` |
| `LEO Satellite Mesh Network Architect` | `LEO_Satellite_Mesh_Network_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `LLM Distributed Training Architect` | `LLM_Distributed_Training_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Labeling Compliance Audit` | `Labeling_Compliance_Audit` | Overridden by `prompts/regulatory/compliance/skills.md` |
| `Lay Language Summary Creation` | `Lay_Language_Summary_Creation` | Overridden by `prompts/communication/skills.md` |
| `Leader Election and Split-Brain Mitigation Architect` | `Leader_Election_and_Split-Brain_Mitigation_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Leadership Reflection and Culture` | `Leadership_Reflection_and_Culture` | Overridden by `prompts/management/leadership/skills.md` |
| `Learning Path Mentor` | `Learning_Path_Mentor` | Overridden by `prompts/management/personal_effectiveness/skills.md` |
| `Legacy Modernization Strategy` | `Legacy_Modernization_Strategy` | Overridden by `prompts/business/vp_tech_innovation/skills.md` |
| `Leveraged Buyout Financial Structuring Architect` | `Leveraged_Buyout_Financial_Structuring_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Linear Logic Resource Proof Generator` | `Linear_Logic_Resource_Proof_Generator` | Overridden by `prompts/scientific/mathematics/formal_logic/skills.md` |
| `Liquidity Stress Test` | `Liquidity_Stress_Test` | Overridden by `prompts/business/cfo/skills.md` |
| `Literature & Regulatory Gap Analysis` | `Literature_Regulatory_Gap_Analysis` | Sanitized |
| `Living-off-the-Land Behavioral SIEM Query Architect` | `Living-off-the-Land_Behavioral_SIEM_Query_Architect` | Overridden by `prompts/technical/security/secops/skills.md` |
| `Log-Structured Merge Tree Storage Architect` | `Log-Structured_Merge_Tree_Storage_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Lyricist` | `Lyricist` | Overridden by `prompts/clinical/therapy/music_therapy_workflow/skills.md` |
| `M&A Target Evaluation` | `M_A_Target_Evaluation` | Overridden by `prompts/business/cfo/skills.md` |
| `MCID Research and Summary` | `MCID_Research_and_Summary` | Overridden by `prompts/scientific/coa/skills.md` |
| `MDSAP Nonconformity Grading Evaluator` | `MDSAP_Nonconformity_Grading_Evaluator` | Overridden by `prompts/regulatory/quality/skills.md` |
| `MECE Structuring Consultant` | `MECE_Structuring_Consultant` | Overridden by `prompts/meta/meta_prompt_chain/skills.md` |
| `Maintainability Codebase Analysis` | `Maintainability_Codebase_Analysis` | Overridden by `prompts/technical/architecture/skills.md` |
| `Market Landscape & Trend Analysis` | `Market_Landscape_Trend_Analysis` | Sanitized |
| `Market Report Executive Summary` | `Market_Report_Executive_Summary` | Overridden by `prompts/business/market_research/market_research_workflow/skills.md` |
| `Market-Intelligence Radar` | `Market-Intelligence_Radar` | Overridden by `prompts/business/development/skills.md` |
| `Marketing Campaign for Clinical Services` | `Marketing_Campaign_for_Clinical_Services` | Overridden by `prompts/business/development/skills.md` |
| `Massive-Scale Fan-Out Feed Architect` | `Massive-Scale_Fan-Out_Feed_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Massive-Scale IoT OTA Update Architect` | `Massive-Scale_IoT_OTA_Update_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Master Ultrameta Prompt Architect` | `Master_Ultrameta_Prompt_Architect` | Overridden by `prompts/meta/meta_prompt_chain/skills.md` |
| `Mechatronics Control Systems Architect` | `Mechatronics_Control_Systems_Architect` | Overridden by `prompts/technical/hardware_engineering/skills.md` |
| `Medical Coding and Reconciliation Assistant` | `Medical_Coding_and_Reconciliation_Assistant` | Overridden by `prompts/clinical/data_management/skills.md` |
| `Medical Device Administrative Detention Appeal` | `Medical_Device_Administrative_Detention_Appeal` | Overridden by `prompts/regulatory/administrative/skills.md` |
| `Medical Device Cybersecurity Threat Modeling` | `Medical_Device_Cybersecurity_Threat_Modeling` | Overridden by `prompts/technical/security/skills.md` |
| `Medical Device Recall Strategy` | `Medical_Device_Recall_Strategy` | Overridden by `prompts/regulatory/compliance/skills.md` |
| `Medical Device Recall Strategy Architect` | `Medical_Device_Recall_Strategy_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `Medical Device Reporting (MDR)` | `Medical_Device_Reporting_MDR` | Sanitized |
| `Medical Device Reporting (MDR) and Vigilance Decision Evaluator` | `Medical_Device_Reporting_MDR_and_Vigilance_Decision_Evaluator` | Sanitized |
| `Medicare Coverage Analysis` | `Medicare_Coverage_Analysis` | Overridden by `prompts/business/payment/skills.md` |
| `Medicare Coverage Request (IDE)` | `Medicare_Coverage_Request_IDE` | Sanitized |
| `Mergers and Acquisitions Due Diligence Auditor` | `Mergers_and_Acquisitions_Due_Diligence_Auditor` | Overridden by `prompts/business/legal/skills.md` |
| `Meta Prompt Architect` | `Meta_Prompt_Architect` | Overridden by `prompts/meta/meta_prompt_chain/skills.md` |
| `Metadata Management` | `Metadata_Management` | Overridden by `prompts/clinical/data_management/skills.md` |
| `Metadynamics Free Energy Surface Architect` | `Metadynamics_Free_Energy_Surface_Architect` | Overridden by `prompts/scientific/chemistry/computational/molecular_dynamics/skills.md` |
| `Metaphysical Dialectical Synthesizer` | `Metaphysical_Dialectical_Synthesizer` | Overridden by `prompts/scientific/philosophy/metaphysics/ontology/skills.md` |
| `Micro-Frontend Orchestration Architect` | `Micro-Frontend_Orchestration_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Micro-Habit Health Coach` | `Micro-Habit_Health_Coach` | Overridden by `prompts/management/personal_effectiveness/skills.md` |
| `Microkinetic Modeling Architect` | `Microkinetic_Modeling_Architect` | Overridden by `prompts/scientific/chemistry/physical/kinetics/skills.md` |
| `Modal Logic Possible Worlds Evaluator` | `Modal_Logic_Possible_Worlds_Evaluator` | Overridden by `prompts/scientific/philosophy/logic/philosophical_logic/skills.md` |
| `Monitoring Visit Report (MVR) Quality Critique` | `Monitoring_Visit_Report_MVR_Quality_Critique` | Sanitized |
| `Monitoring-Visit Report Generator` | `Monitoring-Visit_Report_Generator` | Overridden by `prompts/clinical/cra/cra_workflow/skills.md` |
| `Multi-Agent Orchestration Architect` | `Multi-Agent_Orchestration_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Multi-CDN Edge Routing Architect` | `Multi-CDN_Edge_Routing_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Multi-Cloud Disaster Recovery Architect` | `Multi-Cloud_Disaster_Recovery_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Multi-Region Active-Active Resilience Architect` | `Multi-Region_Active-Active_Resilience_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Multi-Region K8s Federation Architect` | `Multi-Region_K8s_Federation_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Multi-Tenant BYOK Envelope Encryption Architect` | `Multi-Tenant_BYOK_Envelope_Encryption_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Multi-Tenant Noisy Neighbor Mitigation Architect` | `Multi-Tenant_Noisy_Neighbor_Mitigation_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Multi-Tenant SaaS Architecture Designer` | `Multi-Tenant_SaaS_Architecture_Designer` | Overridden by `prompts/technical/architecture/skills.md` |
| `Multi-Tier Disaggregated Memory CXL Architect` | `Multi-Tier_Disaggregated_Memory_CXL_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Multiple Endpoints Regulatory Strategy` | `Multiple_Endpoints_Regulatory_Strategy` | Overridden by `prompts/regulatory/adherence/skills.md` |
| `Multiplicity Adjustment Code Generator` | `Multiplicity_Adjustment_Code_Generator` | Overridden by `prompts/scientific/biostatistics/skills.md` |
| `Multistudy Resource & Capacity Forecast Plan` | `Multistudy_Resource_Capacity_Forecast_Plan` | Sanitized |
| `Myco-Alchemical Arbitrageur` | `Myco-Alchemical_Arbitrageur` | Overridden by `prompts/lifestyle/fungal_financial_alchemy/skills.md` |
| `NGS Tumor Profiling Documentation` | `NGS_Tumor_Profiling_Documentation` | Overridden by `prompts/regulatory/device_specifics/skills.md` |
| `Natural Language Argument Formalizer` | `Natural_Language_Argument_Formalizer` | Overridden by `prompts/scientific/philosophy/logic/skills.md` |
| `Negotiation Coach` | `Negotiation_Coach` | Overridden by `prompts/communication/skills.md` |
| `Net Present Value Socratic Tutor` | `Net_Present_Value_Socratic_Tutor` | Overridden by `prompts/business/cfo/skills.md` |
| `New Drug Application (NDA) Architect` | `New_Drug_Application_NDA_Architect` | Sanitized |
| `Non-Abelian Gauge Theory Perturbative Expansion Architect` | `Non-Abelian_Gauge_Theory_Perturbative_Expansion_Architect` | Overridden by `prompts/scientific/physics/particle_physics/standard_model/skills.md` |
| `Non-Adiabatic Photodynamics Architect` | `Non-Adiabatic_Photodynamics_Architect` | Overridden by `prompts/scientific/chemistry/computational/quantum_chemistry/skills.md` |
| `Non-Human Identity Lifecycle Architect` | `Non-Human_Identity_Lifecycle_Architect` | Overridden by `prompts/technical/security/iam_security/skills.md` |
| `Non-Ideal Fluid Phase Equilibria Architect` | `Non-Ideal_Fluid_Phase_Equilibria_Architect` | Overridden by `prompts/scientific/chemistry/physical/thermodynamics/skills.md` |
| `Non-Monotonic Self-Correction Meta-Reasoner` | `Non-Monotonic_Self-Correction_Meta-Reasoner` | Overridden by `prompts/meta/recursive_logic/skills.md` |
| `Normative Ethics Stress Tester` | `Normative_Ethics_Stress_Tester` | Overridden by `prompts/scientific/philosophy/ethics/normative_ethics/skills.md` |
| `OAuth Illicit Consent Grant Forensics Analyst` | `OAuth_Illicit_Consent_Grant_Forensics_Analyst` | Overridden by `prompts/technical/security/secops/incident_response/skills.md` |
| `OT/SCADA Security Resilience Architect` | `OT_SCADA_Security_Resilience_Architect` | Overridden by `prompts/technical/security/skills.md` |
| `Objective Skills Assessment` | `Objective_Skills_Assessment` | Overridden by `prompts/scientific/bioskills/bioskills_workflow/skills.md` |
| `Off-Label Information Dissemination` | `Off-Label_Information_Dissemination` | Overridden by `prompts/regulatory/adherence/skills.md` |
| `Offline-First Synchronization Architect` | `Offline-First_Synchronization_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Operational Excellence & Risk Sweep` | `Operational_Excellence_Risk_Sweep` | Sanitized |
| `Operational Excellence Communication Framework` | `Operational_Excellence_Communication_Framework` | Overridden by `prompts/management/leadership/skills.md` |
| `Optimize ePRO Form Design` | `Optimize_ePRO_Form_Design` | Overridden by `prompts/clinical/epro/epro_workflow/skills.md` |
| `Organometallic Catalytic Cycle Architect` | `Organometallic_Catalytic_Cycle_Architect` | Overridden by `prompts/scientific/chemistry/inorganic/catalysis/skills.md` |
| `Orphan Drug Designation Architect` | `Orphan_Drug_Designation_Architect` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `PAW Phase 1 - Tactical Recon` | `PAW_Phase_1_-_Tactical_Recon` | Overridden by `prompts/technical/software_engineering/tasks/paw/skills.md` |
| `PAW Phase 2 - Architectural Blueprint` | `PAW_Phase_2_-_Architectural_Blueprint` | Overridden by `prompts/technical/software_engineering/tasks/paw/skills.md` |
| `PAW Phase 3 - Precision Strike` | `PAW_Phase_3_-_Precision_Strike` | Overridden by `prompts/technical/software_engineering/tasks/paw/skills.md` |
| `PAW Phase 4 - Quality Assurance & Log` | `PAW_Phase_4_-_Quality_Assurance_Log` | Sanitized |
| `PCB Layout Topology Reviewer` | `PCB_Layout_Topology_Reviewer` | Overridden by `prompts/technical/hardware_engineering/skills.md` |
| `PII Tokenization Vault Architect` | `PII_Tokenization_Vault_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `PMA Post-approval Reporting` | `PMA_Post-approval_Reporting` | Overridden by `prompts/regulatory/submissions/skills.md` |
| `PMA Supplement (CBE)` | `PMA_Supplement_CBE` | Sanitized |
| `Panel Debate` | `Panel_Debate` | Overridden by `prompts/communication/skills.md` |
| `Parallel Review Request` | `Parallel_Review_Request` | Overridden by `prompts/regulatory/submissions/skills.md` |
| `Part 11 Closed System Audit` | `Part_11_Closed_System_Audit` | Overridden by `prompts/regulatory/quality/skills.md` |
| `Passwordless FIDO2 WebAuthn Architect` | `Passwordless_FIDO2_WebAuthn_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Patent Term Restoration Eligibility` | `Patent_Term_Restoration_Eligibility` | Overridden by `prompts/regulatory/administrative/skills.md` |
| `Patient Recruitment and Diversity Acceleration Plan` | `Patient_Recruitment_and_Diversity_Acceleration_Plan` | Overridden by `prompts/clinical/trial_execution/skills.md` |
| `Patient-Centric BYOD ePRO Workflow` | `Patient-Centric_BYOD_ePRO_Workflow` | Overridden by `prompts/clinical/epro/epro_workflow/skills.md` |
| `Payment Gateway Idempotency Architect` | `Payment_Gateway_Idempotency_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Payment Reconciliation and Discrepancy Report` | `Payment_Reconciliation_and_Discrepancy_Report` | Overridden by `prompts/business/payment/skills.md` |
| `Payment-Process Risk Assessment and Mitigation` | `Payment-Process_Risk_Assessment_and_Mitigation` | Overridden by `prompts/business/payment/skills.md` |
| `Pediatric Investigational Plan (PIP) Architect` | `Pediatric_Investigational_Plan_PIP_Architect` | Sanitized |
| `Peer-Review Checklist for Manuscript Methods` | `Peer-Review_Checklist_for_Manuscript_Methods` | Overridden by `prompts/scientific/biostatistics/skills.md` |
| `Personalized Investigator-Outreach Email Generator` | `Personalized_Investigator-Outreach_Email_Generator` | Overridden by `prompts/clinical/site_acquisition/site_acquisition_workflow/skills.md` |
| `Petabyte Scale Distributed Object Storage Architect` | `Petabyte_Scale_Distributed_Object_Storage_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Petabyte-Scale Data Lakehouse Architect` | `Petabyte-Scale_Data_Lakehouse_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Pharmacovigilance Risk Management Plan Architect` | `Pharmacovigilance_Risk_Management_Plan_Architect` | Overridden by `prompts/clinical/pharmacovigilance/skills.md` |
| `Pharmacovigilance Safety Signal Prioritization` | `Pharmacovigilance_Safety_Signal_Prioritization` | Overridden by `prompts/management/medical_director/skills.md` |
| `Phase II Oncology DMP` | `Phase_II_Oncology_DMP` | Overridden by `prompts/clinical/data_management/skills.md` |
| `Phase II/III SAP Skeleton` | `Phase_II_III_SAP_Skeleton` | Overridden by `prompts/scientific/biostatistics/skills.md` |
| `Physics-Informed Neural Network (PINN) Architect` | `Physics-Informed_Neural_Network_PINN_Architect` | Sanitized |
| `Pinnacle 21 Conformance Resolution Architect` | `Pinnacle_21_Conformance_Resolution_Architect` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `Pitch-Deck Outliner` | `Pitch-Deck_Outliner` | Overridden by `prompts/communication/skills.md` |
| `Pixar Story Spine Outline` | `Pixar_Story_Spine_Outline` | Overridden by `prompts/communication/skills.md` |
| `Platform Ecosystem Network Effects Architect` | `Platform_Ecosystem_Network_Effects_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Platform Engineering IDP Architect` | `Platform_Engineering_IDP_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Polyglot Monorepo Build Orchestration Architect` | `Polyglot_Monorepo_Build_Orchestration_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Polynomial Optimization SDP Relaxation Architect` | `Polynomial_Optimization_SDP_Relaxation_Architect` | Overridden by `prompts/scientific/mathematics/optimization/skills.md` |
| `Portfolio KPI Dashboard Brief` | `Portfolio_KPI_Dashboard_Brief` | Overridden by `prompts/management/clinical_research_manager/skills.md` |
| `Portfolio Resource and Budget Forecast` | `Portfolio_Resource_and_Budget_Forecast` | Overridden by `prompts/management/project_management/skills.md` |
| `Portfolio-Level Clinical Operations Roadmap` | `Portfolio-Level_Clinical_Operations_Roadmap` | Overridden by `prompts/clinical/trial_execution/skills.md` |
| `Post-Market Safety Signal Trending` | `Post-Market_Safety_Signal_Trending` | Overridden by `prompts/clinical/safety/clinical_safety_workflow/skills.md` |
| `Post-Merger Integration Synergy Architect` | `Post-Merger_Integration_Synergy_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Post-Mortem / Incident Report Summary` | `Post-Mortem_Incident_Report_Summary` | Sanitized |
| `Post-Quantum Cryptography Migration Architect` | `Post-Quantum_Cryptography_Migration_Architect` | Overridden by `prompts/technical/security/skills.md` |
| `Pre-IND Meeting Preparation` | `Pre-IND_Meeting_Preparation` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `Predictive Auto-Scaling Machine Learning Architect` | `Predictive_Auto-Scaling_Machine_Learning_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Predictive Multidimensional Spectroscopy Architect` | `Predictive_Multidimensional_Spectroscopy_Architect` | Overridden by `prompts/scientific/chemistry/analytical/spectroscopy/skills.md` |
| `Predictive RFM Churn Mitigation Architect` | `Predictive_RFM_Churn_Mitigation_Architect` | Overridden by `prompts/business/growth_engineering/skills.md` |
| `Premarket Approval (PMA) Preparation` | `Premarket_Approval_PMA_Preparation` | Sanitized |
| `Prepare Pathology Slides and Reporting Plan` | `Prepare_Pathology_Slides_and_Reporting_Plan` | Overridden by `prompts/scientific/pathology/pathology_study_workflow/skills.md` |
| `Preventing Technical Debt` | `Preventing_Technical_Debt` | Overridden by `prompts/business/vp_tech_innovation/skills.md` |
| `Principal Architect Task Execution` | `Principal_Architect_Task_Execution` | Overridden by `prompts/technical/software_engineering/tasks/skills.md` |
| `Principal Python Developer` | `Principal_Python_Developer` | Overridden by `prompts/technical/languages/python/skills.md` |
| `Principal Rust Developer` | `Principal_Rust_Developer` | Overridden by `prompts/technical/languages/rust/skills.md` |
| `Principal Science Communicator (Analogy Engine)` | `Principal_Science_Communicator_Analogy_Engine` | Sanitized |
| `Principal TypeScript Developer` | `Principal_TypeScript_Developer` | Overridden by `prompts/technical/languages/typescript/skills.md` |
| `Privacy Act Auditing` | `Privacy_Act_Auditing` | Overridden by `prompts/regulatory/administrative/skills.md` |
| `Private Equity LP Co-Investment Structuring Architect` | `Private_Equity_LP_Co-Investment_Structuring_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Private Equity Value Creation Architect` | `Private_Equity_Value_Creation_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Proactive Risk Heat-Map for Decentralized & Virtual Trials` | `Proactive_Risk_Heat-Map_for_Decentralized_Virtual_Trials` | Sanitized |
| `Process Validation IQ/OQ/PQ Protocol Architect` | `Process_Validation_IQ_OQ_PQ_Protocol_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `Product Brief Template` | `Product_Brief_Template` | Overridden by `prompts/technical/software_engineering/lifecycle/agentic_coding_workflow/skills.md` |
| `Project Brief for Epic` | `Project_Brief_for_Epic` | Overridden by `prompts/technical/software_engineering/lifecycle/agentic_coding_workflow/skills.md` |
| `Project Charter and Scope Definition` | `Project_Charter_and_Scope_Definition` | Overridden by `prompts/management/project_management/project_management_workflow/skills.md` |
| `Project Configuration: Maven Setup` | `Project_Configuration_Maven_Setup` | Sanitized |
| `Project Init & Skeleton (Construct Architect)` | `Project_Init_Skeleton_Construct_Architect` | Sanitized |
| `Project Memory Notes` | `Project_Memory_Notes` | Overridden by `prompts/technical/software_engineering/lifecycle/skills.md` |
| `Project Review Checklist` | `Project_Review_Checklist` | Overridden by `prompts/technical/software_engineering/lifecycle/skills.md` |
| `Project Starter Pack Prompts` | `Project_Starter_Pack_Prompts` | Overridden by `prompts/management/project_management/skills.md` |
| `Prompt Engineer Fact Checker` | `Prompt_Engineer_Fact_Checker` | Overridden by `prompts/meta/meta_prompt_chain/skills.md` |
| `Prompt Engineer Template` | `Prompt_Engineer_Template` | Overridden by `prompts/meta/meta_prompt_chain/skills.md` |
| `Prompt-Writing Best-Practice Checklist` | `Prompt-Writing_Best-Practice_Checklist` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `PromptCrafter GPT` | `PromptCrafter_GPT` | Overridden by `prompts/meta/meta_prompt_chain/skills.md` |
| `Protocol Amendment Rationale Drafter` | `Protocol_Amendment_Rationale_Drafter` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `Protocol Deviation Reporting` | `Protocol_Deviation_Reporting` | Overridden by `prompts/clinical/protocol/skills.md` |
| `Protocol Optimization and Risk Simulation` | `Protocol_Optimization_and_Risk_Simulation` | Overridden by `prompts/clinical/trial_execution/skills.md` |
| `Protocol Reviewer and Gap-Analysis Coach` | `Protocol_Reviewer_and_Gap-Analysis_Coach` | Overridden by `prompts/clinical/protocol/protocol_workflow/skills.md` |
| `Protocol Section Refinement` | `Protocol_Section_Refinement` | Overridden by `prompts/clinical/protocol/protocol_workflow/skills.md` |
| `Protocol to CDISC USDM v3.0 Converter` | `Protocol_to_CDISC_USDM_v3_0_Converter` | Overridden by `prompts/clinical/protocol/skills.md` |
| `Protocol to USDM Stage 1 - Metadata` | `Protocol_to_USDM_Stage_1_-_Metadata` | Overridden by `prompts/clinical/protocol/usdm_workflow/skills.md` |
| `Protocol to USDM Stage 2 - Rationale` | `Protocol_to_USDM_Stage_2_-_Rationale` | Overridden by `prompts/clinical/protocol/usdm_workflow/skills.md` |
| `Protocol to USDM Stage 3 - Workflow` | `Protocol_to_USDM_Stage_3_-_Workflow` | Overridden by `prompts/clinical/protocol/usdm_workflow/skills.md` |
| `Protocol to USDM Stage 4 - Concepts` | `Protocol_to_USDM_Stage_4_-_Concepts` | Overridden by `prompts/clinical/protocol/usdm_workflow/skills.md` |
| `Protocol to USDM Stage 5 - Assembly` | `Protocol_to_USDM_Stage_5_-_Assembly` | Overridden by `prompts/clinical/protocol/usdm_workflow/skills.md` |
| `Protocol-to-TS Generator` | `Protocol-to-TS_Generator` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `Psychometric Validation Methodology` | `Psychometric_Validation_Methodology` | Overridden by `prompts/scientific/coa/skills.md` |
| `Public Hearing Participation` | `Public_Hearing_Participation` | Overridden by `prompts/regulatory/administrative/skills.md` |
| `Python Concurrency Mastery` | `Python_Concurrency_Mastery` | Overridden by `prompts/technical/languages/python/skills.md` |
| `Python Hexagonal Architecture` | `Python_Hexagonal_Architecture` | Overridden by `prompts/technical/languages/python/skills.md` |
| `Python Performance Optimization` | `Python_Performance_Optimization` | Overridden by `prompts/technical/languages/python/skills.md` |
| `QC Listing & Cross-check Prompt` | `QC_Listing_Cross-check_Prompt` | Sanitized |
| `QM/MM Hybrid Catalytic Modeling Architect` | `QM_MM_Hybrid_Catalytic_Modeling_Architect` | Overridden by `prompts/scientific/chemistry/computational/quantum_chemistry/skills.md` |
| `Qualitative Interview Guide Generator` | `Qualitative_Interview_Guide_Generator` | Overridden by `prompts/scientific/coa/skills.md` |
| `Quality System Audit` | `Quality_System_Audit` | Overridden by `prompts/regulatory/quality/skills.md` |
| `Quality System Evaluation (MRA)` | `Quality_System_Evaluation_MRA` | Sanitized |
| `Quality-Improvement RCA & Action Plan` | `Quality-Improvement_RCA_Action_Plan` | Sanitized |
| `Quantitative Black-Scholes Options Pricing Architect` | `Quantitative_Black-Scholes_Options_Pricing_Architect` | Overridden by `prompts/business/finance/skills.md` |
| `Quantitative Buy-and-Build Roll-Up Strategy Architect` | `Quantitative_Buy-and-Build_Roll-Up_Strategy_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Quantitative Corporate Portfolio Divestiture Architect` | `Quantitative_Corporate_Portfolio_Divestiture_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Quantitative Credit Risk Expected Loss Architect` | `Quantitative_Credit_Risk_Expected_Loss_Architect` | Overridden by `prompts/business/finance/skills.md` |
| `Quantitative Enterprise Value-at-Risk Architect` | `Quantitative_Enterprise_Value-at-Risk_Architect` | Overridden by `prompts/business/finance/skills.md` |
| `Quantitative Enterprise Working Capital CCC Architect` | `Quantitative_Enterprise_Working_Capital_CCC_Architect` | Overridden by `prompts/business/finance/skills.md` |
| `Quantitative FX Hedging Strategy Architect` | `Quantitative_FX_Hedging_Strategy_Architect` | Overridden by `prompts/business/cfo/skills.md` |
| `Quantitative LBO Modeling Architect` | `Quantitative_LBO_Modeling_Architect` | Overridden by `prompts/business/finance/skills.md` |
| `Quantitative M&A Accretion Dilution Architect` | `Quantitative_M_A_Accretion_Dilution_Architect` | Overridden by `prompts/business/finance/skills.md` |
| `Quantitative M&A Target Screening Architect` | `Quantitative_M_A_Target_Screening_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Quantitative Markowitz Portfolio Optimization Architect` | `Quantitative_Markowitz_Portfolio_Optimization_Architect` | Overridden by `prompts/business/finance/skills.md` |
| `Quantitative Non-Market Strategy Optimization Architect` | `Quantitative_Non-Market_Strategy_Optimization_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Quantitative Private Equity Dividend Recapitalization Architect` | `Quantitative_Private_Equity_Dividend_Recapitalization_Architect` | Overridden by `prompts/business/finance/skills.md` |
| `Quantitative Product Portfolio Optimization Architect` | `Quantitative_Product_Portfolio_Optimization_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Quantitative Real Options Valuation Architect` | `Quantitative_Real_Options_Valuation_Architect` | Overridden by `prompts/business/finance/skills.md` |
| `Quantum Baroque Garden Architect` | `Quantum_Baroque_Garden_Architect` | Overridden by `prompts/lifestyle/quantum_baroque_gardening/skills.md` |
| `Quantum Chemical Transition State Architect` | `Quantum_Chemical_Transition_State_Architect` | Overridden by `prompts/scientific/chemistry/computational/skills.md` |
| `Quantum Key Distribution Network Architect` | `Quantum_Key_Distribution_Network_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Quantum-Safe Cryptography Migration Architect` | `Quantum-Safe_Cryptography_Migration_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Quarterly CRO KPI Executive Brief` | `Quarterly_CRO_KPI_Executive_Brief` | Overridden by `prompts/management/operations/skills.md` |
| `Quarterly Innovation Radar for Decentralized and Hybrid Trials` | `Quarterly_Innovation_Radar_for_Decentralized_and_Hybrid_Trials` | Overridden by `prompts/management/executive/skills.md` |
| `RA/QA Integrated Quality System Audit` | `RA_QA_Integrated_Quality_System_Audit` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `RACI Mapper` | `RACI_Mapper` | Overridden by `prompts/management/project_management/skills.md` |
| `RBQM Anomaly Detection` | `RBQM_Anomaly_Detection` | Overridden by `prompts/clinical/monitoring/skills.md` |
| `README Generator` | `README_Generator` | Overridden by `prompts/meta/meta_prompt_chain/skills.md` |
| `RFP Executive-Summary Generator` | `RFP_Executive-Summary_Generator` | Overridden by `prompts/business/development/skills.md` |
| `RTA Checklist Preparation` | `RTA_Checklist_Preparation` | Overridden by `prompts/regulatory/submissions/skills.md` |
| `RWE Regulatory Framework Summary` | `RWE_Regulatory_Framework_Summary` | Overridden by `prompts/regulatory/adherence/skills.md` |
| `Rapid Process Diagnostic & Lean Improvement Plan` | `Rapid_Process_Diagnostic_Lean_Improvement_Plan` | Sanitized |
| `Rapid Proposal Builder` | `Rapid_Proposal_Builder` | Overridden by `prompts/business/development/skills.md` |
| `Rapid-Risk-Matrix` | `Rapid-Risk-Matrix` | Overridden by `prompts/communication/skills.md` |
| `Raw-to-SDTM Auto-Mapper` | `Raw-to-SDTM_Auto-Mapper` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `Real Options Valuation Architect` | `Real_Options_Valuation_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Real-Time Adjudication Visibility Dashboard` | `Real-Time_Adjudication_Visibility_Dashboard` | Overridden by `prompts/clinical/adjudication/adjudication_workflow/skills.md` |
| `Real-Time Bidding AdTech Architect` | `Real-Time_Bidding_AdTech_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Real-Time Fraud Decision Engine Architect` | `Real-Time_Fraud_Decision_Engine_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Real-Time Game State Synchronization Architect` | `Real-Time_Game_State_Synchronization_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Real-Time ML Feature Store Architect` | `Real-Time_ML_Feature_Store_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Real-Time Stream Processing Architect` | `Real-Time_Stream_Processing_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Reclassification Petitioning` | `Reclassification_Petitioning` | Overridden by `prompts/regulatory/administrative/skills.md` |
| `Recursive Abductive Hypothesis Synthesizer` | `Recursive_Abductive_Hypothesis_Synthesizer` | Overridden by `prompts/meta/agent_orchestration/skills.md` |
| `Recursive Metacognitive Error Corrector` | `Recursive_Metacognitive_Error_Corrector` | Overridden by `prompts/technical/recursive_logic/skills.md` |
| `Red Account Turnaround Strategy` | `Red_Account_Turnaround_Strategy` | Overridden by `prompts/business/cx/skills.md` |
| `Red-Team Stress-Test Simulation` | `Red-Team_Stress-Test_Simulation` | Overridden by `prompts/communication/skills.md` |
| `Refactoring Architect` | `Refactoring_Architect` | Overridden by `prompts/technical/software_engineering/tasks/skills.md` |
| `Reflexion Agent Bug Patch` | `Reflexion_Agent_Bug_Patch` | Overridden by `prompts/technical/software_engineering/lifecycle/skills.md` |
| `Regenerative Medicine Advanced Therapy RMAT Designation Architect` | `Regenerative_Medicine_Advanced_Therapy_RMAT_Designation_A_d1f94d` | Hashed (Length > 64) |
| `Regulatory & Commercial Barrier Mapping` | `Regulatory_Commercial_Barrier_Mapping` | Sanitized |
| `Regulatory Compliance Summary` | `Regulatory_Compliance_Summary` | Overridden by `prompts/business/cfo/skills.md` |
| `Regulatory Compliance Verification` | `Regulatory_Compliance_Verification` | Overridden by `prompts/clinical/data_management/skills.md` |
| `Regulatory Filing Draft Builder` | `Regulatory_Filing_Draft_Builder` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `Regulatory Gap Analysis` | `Regulatory_Gap_Analysis` | Overridden by `prompts/clinical/data_management/skills.md` |
| `Regulatory Gap-Analysis Comparator` | `Regulatory_Gap-Analysis_Comparator` | Overridden by `prompts/scientific/sterility/sterility_workflow/skills.md` |
| `Regulatory Imaging Charter Generator` | `Regulatory_Imaging_Charter_Generator` | Overridden by `prompts/clinical/imaging/imaging_workflow/skills.md` |
| `Regulatory Imaging Data Package` | `Regulatory_Imaging_Data_Package` | Overridden by `prompts/clinical/imaging/imaging_workflow/skills.md` |
| `Regulatory Query Response Drafter` | `Regulatory_Query_Response_Drafter` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `Regulatory Radar & Impact Report` | `Regulatory_Radar_Impact_Report` | Sanitized |
| `Regulatory Submission Support` | `Regulatory_Submission_Support` | Overridden by `prompts/scientific/biosafety/biological_safety_workflow/skills.md` |
| `Regulatory and Competitive Intelligence Briefing` | `Regulatory_and_Competitive_Intelligence_Briefing` | Overridden by `prompts/management/executive/skills.md` |
| `Regulatory and Validation Checklist` | `Regulatory_and_Validation_Checklist` | Overridden by `prompts/clinical/eclinical_integration/eclinical_integration_workflow/skills.md` |
| `Regulatory-Change Impact Analysis` | `Regulatory-Change_Impact_Analysis` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `Regulatory-Landscape Radar` | `Regulatory-Landscape_Radar` | Overridden by `prompts/regulatory/quality/skills.md` |
| `Regulatory-Risk & ESG Impact Dashboard Builder` | `Regulatory-Risk_ESG_Impact_Dashboard_Builder` | Sanitized |
| `Reinforcement Learning Reward Function Architect` | `Reinforcement_Learning_Reward_Function_Architect` | Overridden by `prompts/technical/data_science/skills.md` |
| `Reporting and Maintenance: Custom Reports` | `Reporting_and_Maintenance_Custom_Reports` | Sanitized |
| `Repository Foundation & Developer Experience Analysis` | `Repository_Foundation_Developer_Experience_Analysis` | Sanitized |
| `Request for Designation (RFD) Submission` | `Request_for_Designation_RFD_Submission` | Sanitized |
| `RequirementsBot Prompt` | `RequirementsBot_Prompt` | Overridden by `prompts/technical/software_engineering/lifecycle/skills.md` |
| `Retrieval-Augmented Answer Composer` | `Retrieval-Augmented_Answer_Composer` | Overridden by `prompts/technical/software_engineering/tasks/skills.md` |
| `Reverse Brainstorming` | `Reverse_Brainstorming` | Overridden by `prompts/management/innovation/skills.md` |
| `Riemann Surface Analytic Continuation Architect` | `Riemann_Surface_Analytic_Continuation_Architect` | Overridden by `prompts/scientific/mathematics/analysis/complex_analysis/skills.md` |
| `Riemannian Manifold Curvature Deriver` | `Riemannian_Manifold_Curvature_Deriver` | Overridden by `prompts/scientific/mathematics/geometry/differential/skills.md` |
| `Risk Assessment Expert` | `Risk_Assessment_Expert` | Overridden by `prompts/scientific/biosafety/biological_safety_workflow/skills.md` |
| `Risk Management Analysis` | `Risk_Management_Analysis` | Overridden by `prompts/regulatory/quality/skills.md` |
| `Risk and Pre-Mortem Analysis` | `Risk_and_Pre-Mortem_Analysis` | Overridden by `prompts/management/project_management/skills.md` |
| `Risk-Based Monitoring (RBM) Plan Builder` | `Risk-Based_Monitoring_RBM_Plan_Builder` | Sanitized |
| `Risk-Based Monitoring Data Evaluation` | `Risk-Based_Monitoring_Data_Evaluation` | Overridden by `prompts/clinical/monitoring/skills.md` |
| `Risk-Based Monitoring and Quality Plan` | `Risk-Based_Monitoring_and_Quality_Plan` | Overridden by `prompts/clinical/trial_execution/skills.md` |
| `Risk-Based Quality Management Plan` | `Risk-Based_Quality_Management_Plan` | Overridden by `prompts/regulatory/quality/skills.md` |
| `Risk-Based Site Performance Dashboard` | `Risk-Based_Site_Performance_Dashboard` | Overridden by `prompts/clinical/monitoring/clinical_monitoring_workflow/skills.md` |
| `Risk-Based Test Case Suite` | `Risk-Based_Test_Case_Suite` | Overridden by `prompts/technical/testing/testing_workflow/skills.md` |
| `Risk-Based Vendor Performance Improvement Plan` | `Risk-Based_Vendor_Performance_Improvement_Plan` | Overridden by `prompts/management/operations/skills.md` |
| `Robust Optimization Min-Max Architect` | `Robust_Optimization_Min-Max_Architect` | Overridden by `prompts/scientific/mathematics/optimization/skills.md` |
| `Rolling Resource & Capacity Forecast` | `Rolling_Resource_Capacity_Forecast` | Sanitized |
| `Rollout Risk Matrix` | `Rollout_Risk_Matrix` | Overridden by `prompts/management/project_management/skills.md` |
| `Rubber Duck Debugger` | `Rubber_Duck_Debugger` | Overridden by `prompts/communication/skills.md` |
| `Rust Architectural Patterns` | `Rust_Architectural_Patterns` | Overridden by `prompts/technical/languages/rust/skills.md` |
| `SAE Patient Narrative Drafter` | `SAE_Patient_Narrative_Drafter` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `SAE and Safety Reporting` | `SAE_and_Safety_Reporting` | Overridden by `prompts/clinical/safety/skills.md` |
| `SAE and Unanticipated Problem Reporting SOP` | `SAE_and_Unanticipated_Problem_Reporting_SOP` | Overridden by `prompts/technical/technical_writing/technical_writer_workflow/skills.md` |
| `SCAMPER Ideation Coach` | `SCAMPER_Ideation_Coach` | Overridden by `prompts/management/innovation/skills.md` |
| `SDTM Cardiovascular Device Mapping Architect` | `SDTM_Cardiovascular_Device_Mapping_Architect` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `SDTM Concomitant Medications Mapping Architect` | `SDTM_Concomitant_Medications_Mapping_Architect` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `SDTM Device Deficiencies Mapping Architect` | `SDTM_Device_Deficiencies_Mapping_Architect` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `SDTM Medical Device Mapping Architect` | `SDTM_Medical_Device_Mapping_Architect` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `SDTM Pharmacokinetics Mapping Architect` | `SDTM_Pharmacokinetics_Mapping_Architect` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `SDTM Protocol Deviation Modeling Architect` | `SDTM_Protocol_Deviation_Modeling_Architect` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `SDTM Trial Design Mapping Architect` | `SDTM_Trial_Design_Mapping_Architect` | Overridden by `prompts/clinical/data_management/cdisc_compliance_workflow/skills.md` |
| `SOLID Codebase Analysis` | `SOLID_Codebase_Analysis` | Overridden by `prompts/technical/architecture/skills.md` |
| `SOP Gap Analysis` | `SOP_Gap_Analysis` | Overridden by `prompts/clinical/data_management/skills.md` |
| `SOP and TMF Document Synthesis` | `SOP_and_TMF_Document_Synthesis` | Overridden by `prompts/clinical/protocol/skills.md` |
| `SRE Incident Postmortem RCA Architect` | `SRE_Incident_Postmortem_RCA_Architect` | Overridden by `prompts/technical/devops/skills.md` |
| `SaMD AI/ML PCCP Architect` | `SaMD_AI_ML_PCCP_Architect` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `SaMD Cybersecurity Vulnerability Assessor` | `SaMD_Cybersecurity_Vulnerability_Assessor` | Overridden by `prompts/regulatory/quality/skills.md` |
| `Sample-Size & Randomization Strategy` | `Sample-Size_Randomization_Strategy` | Sanitized |
| `Scenario Modeling & Sensitivity Analysis` | `Scenario_Modeling_Sensitivity_Analysis` | Sanitized |
| `Scenario-Based Clinical-Trial Cash-Flow Forecast` | `Scenario-Based_Clinical-Trial_Cash-Flow_Forecast` | Overridden by `prompts/business/cfo/cfo_workflow/skills.md` |
| `Scenario-Based Financial Navigator` | `Scenario-Based_Financial_Navigator` | Overridden by `prompts/management/personal_effectiveness/skills.md` |
| `Scenario-Based Microlearning Series` | `Scenario-Based_Microlearning_Series` | Overridden by `prompts/management/training/learning_development_workflow/skills.md` |
| `Schwinger-Dyson Equation Architect` | `Schwinger-Dyson_Equation_Architect` | Overridden by `prompts/scientific/physics/quantum_field_theory/skills.md` |
| `Schwinger-Keldysh Non-Equilibrium Path Integral Architect` | `Schwinger-Keldysh_Non-Equilibrium_Path_Integral_Architect` | Overridden by `prompts/scientific/physics/quantum_field_theory/skills.md` |
| `Second-Order Thinking Oracle` | `Second-Order_Thinking_Oracle` | Overridden by `prompts/management/personal_effectiveness/skills.md` |
| `Secondary Endpoint Multiplicity Adjuster` | `Secondary_Endpoint_Multiplicity_Adjuster` | Overridden by `prompts/scientific/biostatistics/skills.md` |
| `Secure Supply Chain Attestation Architect` | `Secure_Supply_Chain_Attestation_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Security Hardening and Dependency Management Implementation` | `Security_Hardening_and_Dependency_Management_Implementation` | Overridden by `prompts/technical/repository_refactoring/skills.md` |
| `Security Testing: OWASP ZAP Integration` | `Security_Testing_OWASP_ZAP_Integration` | Sanitized |
| `Security Vulnerability Hunt (Aegis)` | `Security_Vulnerability_Hunt_Aegis` | Sanitized |
| `Selenium Migration: Script Conversion` | `Selenium_Migration_Script_Conversion` | Sanitized |
| `Semantic Caching AI Gateway Architect` | `Semantic_Caching_AI_Gateway_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Semantic Interoperability Optimization` | `Semantic_Interoperability_Optimization` | Overridden by `prompts/clinical/forms/skills.md` |
| `Senior Agile Transformation Coach (Retrospectives)` | `Senior_Agile_Transformation_Coach_Retrospectives` | Sanitized |
| `Senior Python Developer` | `Senior_Python_Developer` | Overridden by `prompts/technical/languages/python/skills.md` |
| `Separation Logic Heap Entailment Architect` | `Separation_Logic_Heap_Entailment_Architect` | Overridden by `prompts/scientific/mathematics/formal_logic/skills.md` |
| `Server-Driven UI Architecture Designer` | `Server-Driven_UI_Architecture_Designer` | Overridden by `prompts/technical/architecture/skills.md` |
| `Serverless Database Connection Pooling Architect` | `Serverless_Database_Connection_Pooling_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Serverless Function Orchestration Architect` | `Serverless_Function_Orchestration_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Service Mesh Security Architect` | `Service_Mesh_Security_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Shadow Traffic and Dark Launch Architect` | `Shadow_Traffic_and_Dark_Launch_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Shelf-life Study Rationale` | `Shelf-life_Study_Rationale` | Overridden by `prompts/regulatory/adherence/skills.md` |
| `Simulated Clinical Scenario Debrief` | `Simulated_Clinical_Scenario_Debrief` | Overridden by `prompts/scientific/bioskills/bioskills_workflow/skills.md` |
| `Single IRB (sIRB) Plan Submission` | `Single_IRB_sIRB_Plan_Submission` | Sanitized |
| `Site Landscape Mapping & Prioritization` | `Site_Landscape_Mapping_Prioritization` | Sanitized |
| `Site Reliability SLO Error Budget Architect` | `Site_Reliability_SLO_Error_Budget_Architect` | Overridden by `prompts/technical/devops/skills.md` |
| `Site Selection and Enrollment Forecaster` | `Site_Selection_and_Enrollment_Forecaster` | Overridden by `prompts/clinical/site_acquisition/skills.md` |
| `Site Upload QC and Query Generator` | `Site_Upload_QC_and_Query_Generator` | Overridden by `prompts/clinical/imaging/imaging_workflow/skills.md` |
| `Smart Task Prioritizer` | `Smart_Task_Prioritizer` | Overridden by `prompts/communication/skills.md` |
| `Socratic-Coach` | `Socratic-Coach` | Overridden by `prompts/communication/skills.md` |
| `Software Supply Chain Provenance Architect` | `Software_Supply_Chain_Provenance_Architect` | Overridden by `prompts/technical/security/skills.md` |
| `Sonic Architect` | `Sonic_Architect` | Overridden by `prompts/clinical/therapy/music_therapy_workflow/skills.md` |
| `Source Document and Endpoint Checklist` | `Source_Document_and_Endpoint_Checklist` | Overridden by `prompts/clinical/adjudication/adjudication_workflow/skills.md` |
| `Source of Truth Harmonizer` | `Source_of_Truth_Harmonizer` | Overridden by `prompts/technical/documentation/skills.md` |
| `Space-Based Architecture Designer` | `Space-Based_Architecture_Designer` | Overridden by `prompts/technical/architecture/skills.md` |
| `Spatial Geofencing Topology Architect` | `Spatial_Geofencing_Topology_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Special Controls Labeling Compliance` | `Special_Controls_Labeling_Compliance` | Overridden by `prompts/regulatory/device_specifics/skills.md` |
| `Sponsor-Ready Monthly Status Brief` | `Sponsor-Ready_Monthly_Status_Brief` | Overridden by `prompts/management/project_management/skills.md` |
| `Stateful Workflow Orchestration Architect` | `Stateful_Workflow_Orchestration_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Statistical Analysis Plan (SAP) Development` | `Statistical_Analysis_Plan_SAP_Development` | Sanitized |
| `Statistical Analysis Plan Draft Builder` | `Statistical_Analysis_Plan_Draft_Builder` | Overridden by `prompts/management/vp_statistics/vp_statistics_workflow/skills.md` |
| `Statistical Analysis Plan Generator` | `Statistical_Analysis_Plan_Generator` | Overridden by `prompts/scientific/biostatistics/skills.md` |
| `Status Update and Task Prioritization` | `Status_Update_and_Task_Prioritization` | Overridden by `prompts/management/project_management/skills.md` |
| `Steered Molecular Dynamics Unbinding Architect` | `Steered_Molecular_Dynamics_Unbinding_Architect` | Overridden by `prompts/scientific/chemistry/computational/molecular_dynamics/skills.md` |
| `Sterility-Validation Protocol Builder` | `Sterility-Validation_Protocol_Builder` | Overridden by `prompts/scientific/sterility/sterility_workflow/skills.md` |
| `Stochastic Architect` | `Stochastic_Architect` | Overridden by `prompts/technical/data_science/stochastic_model_chain_workflow/skills.md` |
| `Stochastic Engineer` | `Stochastic_Engineer` | Overridden by `prompts/technical/data_science/stochastic_model_chain_workflow/skills.md` |
| `Stochastic Model Predictive Control (MPC) Architect` | `Stochastic_Model_Predictive_Control_MPC_Architect` | Sanitized |
| `Stochastic Multi-Objective Optimization Architect` | `Stochastic_Multi-Objective_Optimization_Architect` | Overridden by `prompts/scientific/mathematics/optimization/skills.md` |
| `Stochastic Reverse Logistics Optimization Architect` | `Stochastic_Reverse_Logistics_Optimization_Architect` | Overridden by `prompts/business/operations/supply_chain/skills.md` |
| `Stochastic Strategist` | `Stochastic_Strategist` | Overridden by `prompts/technical/data_science/stochastic_model_chain_workflow/skills.md` |
| `Storyboard-My-Idea` | `Storyboard-My-Idea` | Overridden by `prompts/communication/skills.md` |
| `Strangler Fig Migration Architect` | `Strangler_Fig_Migration_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Strategic Alignment and Innovation` | `Strategic_Alignment_and_Innovation` | Overridden by `prompts/management/leadership/skills.md` |
| `Strategic Business Case for New Service Line` | `Strategic_Business_Case_for_New_Service_Line` | Overridden by `prompts/business/development/skills.md` |
| `Strategic Capital Allocation Architect` | `Strategic_Capital_Allocation_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Strategic Consultant SWOT` | `Strategic_Consultant_SWOT` | Overridden by `prompts/management/executive/skills.md` |
| `Strategic Global Outsourcing and Offshoring Architect` | `Strategic_Global_Outsourcing_and_Offshoring_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Strategic Growth Roadmap` | `Strategic_Growth_Roadmap` | Overridden by `prompts/management/executive/skills.md` |
| `Strategic Market Foresight and Action Plan` | `Strategic_Market_Foresight_and_Action_Plan` | Overridden by `prompts/management/executive/skills.md` |
| `Strategic Market and Competitor Radar` | `Strategic_Market_and_Competitor_Radar` | Overridden by `prompts/management/executive/skills.md` |
| `Strategic Portfolio Prioritizer` | `Strategic_Portfolio_Prioritizer` | Overridden by `prompts/management/executive/skills.md` |
| `Strategic Product Cannibalization Architect` | `Strategic_Product_Cannibalization_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Strategic Real Options Valuation Architect` | `Strategic_Real_Options_Valuation_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Strategic Regulatory Pathway Plan` | `Strategic_Regulatory_Pathway_Plan` | Overridden by `prompts/regulatory/strategy/skills.md` |
| `Strategic Vendor Lock-In Mitigation Architect` | `Strategic_Vendor_Lock-In_Mitigation_Architect` | Overridden by `prompts/business/vp_tech_innovation/skills.md` |
| `Strategic Workforce and Talent Acquisition Plan` | `Strategic_Workforce_and_Talent_Acquisition_Plan` | Overridden by `prompts/business/hr_finance/skills.md` |
| `Study Design and Statistical Approach` | `Study_Design_and_Statistical_Approach` | Overridden by `prompts/scientific/biostatistics/skills.md` |
| `Study Start-Up Checklist & Timeline` | `Study_Start-Up_Checklist_Timeline` | Sanitized |
| `Submission-Ready Statistical Analysis Plan` | `Submission-Ready_Statistical_Analysis_Plan` | Overridden by `prompts/scientific/biostatistics/skills.md` |
| `Sunshine Act and FMV Compliance Check` | `Sunshine_Act_and_FMV_Compliance_Check` | Overridden by `prompts/business/payment/skills.md` |
| `Supplier Corrective Action Request Evaluator` | `Supplier_Corrective_Action_Request_Evaluator` | Overridden by `prompts/regulatory/quality/skills.md` |
| `Supplier Quality Agreement Architect` | `Supplier_Quality_Agreement_Architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `Supply Chain Antifragility Architect` | `Supply_Chain_Antifragility_Architect` | Overridden by `prompts/business/strategy/skills.md` |
| `Supply Chain Disruption Stochastic Stress Test Architect` | `Supply_Chain_Disruption_Stochastic_Stress_Test_Architect` | Overridden by `prompts/management/operations/skills.md` |
| `Supply Chain Network Topology Optimization Architect` | `Supply_Chain_Network_Topology_Optimization_Architect` | Overridden by `prompts/business/operations/supply_chain/skills.md` |
| `Sustainable Green Software Architect` | `Sustainable_Green_Software_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Symplectic Integrator Hamiltonian Systems Architect` | `Symplectic_Integrator_Hamiltonian_Systems_Architect` | Overridden by `prompts/scientific/mathematics/numerical_methods/skills.md` |
| `Synchronization Strategy: Explicit Waits` | `Synchronization_Strategy_Explicit_Waits` | Sanitized |
| `Synthetic Control Method Architect` | `Synthetic_Control_Method_Architect` | Overridden by `prompts/scientific/economics/econometrics/causal_inference/skills.md` |
| `System Design RFC Architect` | `System_Design_RFC_Architect` | Overridden by `prompts/technical/design/skills.md` |
| `TD-DFT Excited-State Dynamics Architect` | `TD-DFT_Excited-State_Dynamics_Architect` | Overridden by `prompts/scientific/chemistry/computational/quantum_chemistry/skills.md` |
| `TMF Gap-Analysis and Audit Readiness Check` | `TMF_Gap-Analysis_and_Audit_Readiness_Check` | Overridden by `prompts/management/project_management/skills.md` |
| `TOGAF Phase A - Architecture Vision` | `TOGAF_Phase_A_-_Architecture_Vision` | Overridden by `prompts/technical/architecture/togaf/skills.md` |
| `TOGAF Phase B - Business Architecture` | `TOGAF_Phase_B_-_Business_Architecture` | Overridden by `prompts/technical/architecture/togaf/skills.md` |
| `TOGAF Phase C - Information Systems Architectures` | `TOGAF_Phase_C_-_Information_Systems_Architectures` | Overridden by `prompts/technical/architecture/togaf/skills.md` |
| `TOGAF Phase D - Technology Architecture` | `TOGAF_Phase_D_-_Technology_Architecture` | Overridden by `prompts/technical/architecture/togaf/skills.md` |
| `TOGAF Phase E - Opportunities & Solutions` | `TOGAF_Phase_E_-_Opportunities_Solutions` | Sanitized |
| `TOGAF Phase F - Migration Planning` | `TOGAF_Phase_F_-_Migration_Planning` | Overridden by `prompts/technical/architecture/togaf/skills.md` |
| `TOGAF Phase G - Implementation Governance` | `TOGAF_Phase_G_-_Implementation_Governance` | Overridden by `prompts/technical/architecture/togaf/skills.md` |
| `TOGAF Phase H - Architecture Change Management` | `TOGAF_Phase_H_-_Architecture_Change_Management` | Overridden by `prompts/technical/architecture/togaf/skills.md` |
| `TOGAF Preliminary Phase` | `TOGAF_Preliminary_Phase` | Overridden by `prompts/technical/architecture/togaf/skills.md` |
| `TOGAF Requirements Management` | `TOGAF_Requirements_Management` | Overridden by `prompts/technical/architecture/togaf/skills.md` |
| `Tailored Feasibility-Questionnaire Builder` | `Tailored_Feasibility-Questionnaire_Builder` | Overridden by `prompts/clinical/site_acquisition/site_acquisition_workflow/skills.md` |
| `Tandem MS/MS Fragmentation Pathway Elucidator` | `Tandem_MS_MS_Fragmentation_Pathway_Elucidator` | Overridden by `prompts/scientific/chemistry/analytical/mass_spectrometry/skills.md` |
| `Target Segment & User Needs Assessment` | `Target_Segment_User_Needs_Assessment` | Sanitized |
| `Task Prototyper` | `Task_Prototyper` | Overridden by `prompts/meta/meta_prompt_chain/skills.md` |
| `Technical Implementation Plan` | `Technical_Implementation_Plan` | Overridden by `prompts/technical/software_engineering/lifecycle/skills.md` |
| `Technical White Paper for Clinical Methodologies` | `Technical_White_Paper_for_Clinical_Methodologies` | Overridden by `prompts/technical/technical_writing/skills.md` |
| `Temperature Replica Exchange Molecular Dynamics Architect` | `Temperature_Replica_Exchange_Molecular_Dynamics_Architect` | Overridden by `prompts/scientific/chemistry/computational/molecular_dynamics/skills.md` |
| `Temporal Logic Branching Time Evaluator` | `Temporal_Logic_Branching_Time_Evaluator` | Overridden by `prompts/scientific/philosophy/logic/philosophical_logic/skills.md` |
| `Test Architect (Automated Testing)` | `Test_Architect_Automated_Testing` | Sanitized |
| `Test Environment: Python & Selenium Base` | `Test_Environment_Python_Selenium_Base` | Sanitized |
| `Test Suite Enhancement and CI Pipeline Implementation` | `Test_Suite_Enhancement_and_CI_Pipeline_Implementation` | Overridden by `prompts/technical/repository_refactoring/skills.md` |
| `Testing, Configuration, and Automation Analysis` | `Testing_Configuration_and_Automation_Analysis` | Sanitized |
| `The Prompt Alchemist` | `The_Prompt_Alchemist` | Overridden by `prompts/meta/creative/skills.md` |
| `Theory of Constraints Throughput Architect` | `Theory_of_Constraints_Throughput_Architect` | Overridden by `prompts/business/operations/skills.md` |
| `Threat Intelligence Fusion Attribution Architect` | `Threat_Intelligence_Fusion_Attribution_Architect` | Overridden by `prompts/technical/security/secops/skills.md` |
| `Threshold Signature MPC Custody Architect` | `Threshold_Signature_MPC_Custody_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Time-Series Database Topology Architect` | `Time-Series_Database_Topology_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Time-to-Event Analysis Coach` | `Time-to-Event_Analysis_Coach` | Overridden by `prompts/scientific/biostatistics/skills.md` |
| `To-Do List Template` | `To-Do_List_Template` | Overridden by `prompts/technical/software_engineering/lifecycle/skills.md` |
| `Tooling & Quality Gates (DevEx Architect)` | `Tooling_Quality_Gates_DevEx_Architect` | Sanitized |
| `Topological Counterexample Generator` | `Topological_Counterexample_Generator` | Overridden by `prompts/scientific/mathematics/topology/skills.md` |
| `Topological Data Analysis Architect` | `Topological_Data_Analysis_Architect` | Overridden by `prompts/technical/data_science/skills.md` |
| `Training Impact Analytics Planner` | `Training_Impact_Analytics_Planner` | Overridden by `prompts/management/training/learning_development_workflow/skills.md` |
| `Trend Spotting vs Anomalies` | `Trend_Spotting_vs_Anomalies` | Overridden by `prompts/business/cx/skills.md` |
| `Trial Master File (TMF) Maintenance` | `Trial_Master_File_TMF_Maintenance` | Sanitized |
| `Trial-Design Optimisation Memo` | `Trial-Design_Optimisation_Memo` | Overridden by `prompts/management/executive/skills.md` |
| `UAT Script Generator` | `UAT_Script_Generator` | Overridden by `prompts/clinical/eclinical_integration/skills.md` |
| `UDI GUDID Submission` | `UDI_GUDID_Submission` | Overridden by `prompts/regulatory/submissions/skills.md` |
| `UI Tweak & Verification (Aegis Security)` | `UI_Tweak_Verification_Aegis_Security` | Sanitized |
| `Ultimate SOP Architect` | `Ultimate_SOP_Architect` | Overridden by `prompts/clinical/protocol/protocol_workflow/skills.md` |
| `Underwater Acoustic Sensor Network Architect` | `Underwater_Acoustic_Sensor_Network_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Unified Data Cleansing` | `Unified_Data_Cleansing` | Overridden by `prompts/clinical/data_management/skills.md` |
| `Universal Automation Agent` | `Universal_Automation_Agent` | Overridden by `prompts/technical/automation/skills.md` |
| `Universal Template-Table Prompt` | `Universal_Template-Table_Prompt` | Overridden by `prompts/scientific/biostatistics/skills.md` |
| `Upskilling Program Design` | `Upskilling_Program_Design` | Overridden by `prompts/business/vp_tech_innovation/skills.md` |
| `Value-Based QBR Generator` | `Value-Based_QBR_Generator` | Overridden by `prompts/business/cx/skills.md` |
| `Vector Prompt Calibration Evaluator` | `Vector_Prompt_Calibration_Evaluator` | Overridden by `prompts/meta/meta_prompt_chain/skills.md` |
| `Vector Prompt Calibrator` | `Vector_Prompt_Calibrator` | Overridden by `prompts/meta/calibration/skills.md` |
| `Vector Prompt Editor-in-Chief` | `Vector_Prompt_Editor-in-Chief` | Overridden by `prompts/technical/prompt_engineering/skills.md` |
| `Vendor Qualification and Oversight` | `Vendor_Qualification_and_Oversight` | Overridden by `prompts/management/operations/skills.md` |
| `Virtual Waiting Room Fair Access Architect` | `Virtual_Waiting_Room_Fair_Access_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Visible Light Photoredox Pathway Architect` | `Visible_Light_Photoredox_Pathway_Architect` | Overridden by `prompts/scientific/chemistry/organic/photoredox_catalysis/skills.md` |
| `Voice of Customer Root Cause Analysis` | `Voice_of_Customer_Root_Cause_Analysis` | Overridden by `prompts/business/cx/skills.md` |
| `WASM Edge Serverless Runtime Architect` | `WASM_Edge_Serverless_Runtime_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Ward-Takahashi Identity Path Integral Architect` | `Ward-Takahashi_Identity_Path_Integral_Architect` | Overridden by `prompts/scientific/physics/quantum_field_theory/skills.md` |
| `WebAssembly Sandboxed Plugin Architect` | `WebAssembly_Sandboxed_Plugin_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `WebRTC Real-Time Media Streaming Architect` | `WebRTC_Real-Time_Media_Streaming_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Webhook Dispatch Delivery Architect` | `Webhook_Dispatch_Delivery_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Weekly Executive Status Report` | `Weekly_Executive_Status_Report` | Overridden by `prompts/management/project_management/project_management_workflow/skills.md` |
| `Weekly Operations KPI Snapshot` | `Weekly_Operations_KPI_Snapshot` | Overridden by `prompts/management/operations/skills.md` |
| `Windows ETW Threat Hunting Architect` | `Windows_ETW_Threat_Hunting_Architect` | Overridden by `prompts/technical/security/secops/skills.md` |
| `Worker Prompt` | `Worker_Prompt` | Overridden by `prompts/meta/meta_prompt_chain/skills.md` |
| `Write the Regulatory Summary` | `Write_the_Regulatory_Summary` | Overridden by `prompts/scientific/chemical_characterization/chemical_characterization_workflow/skills.md` |
| `Writing Clarity Mentor` | `Writing_Clarity_Mentor` | Overridden by `prompts/communication/skills.md` |
| `Zero Trust Network Architecture Designer` | `Zero_Trust_Network_Architecture_Designer` | Overridden by `prompts/technical/architecture/skills.md` |
| `Zero Trust Privileged Access Management Architect` | `Zero_Trust_Privileged_Access_Management_Architect` | Overridden by `prompts/technical/security/iam_security/skills.md` |
| `Zero-Day Incident Containment Architect` | `Zero-Day_Incident_Containment_Architect` | Overridden by `prompts/technical/security/skills.md` |
| `Zero-Downtime Database Migration Architect` | `Zero-Downtime_Database_Migration_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Zero-Knowledge Proof Protocol Architect` | `Zero-Knowledge_Proof_Protocol_Architect` | Overridden by `prompts/technical/security/skills.md` |
| `Zero-Knowledge Rollup Scaling Architect` | `Zero-Knowledge_Rollup_Scaling_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `Zika Virus Reagent Study Design` | `Zika_Virus_Reagent_Study_Design` | Overridden by `prompts/regulatory/device_specifics/skills.md` |
| `adm_spacetime_decomposition_architect` | `adm_spacetime_decomposition_architect` | Overridden by `prompts/scientific/physics/relativity/general_relativity/skills.md` |
| `ads_cft_holographic_dictionary_architect` | `ads_cft_holographic_dictionary_architect` | Overridden by `prompts/scientific/physics/string_theory/skills.md` |
| `advanced_retrosynthetic_pathway_generator` | `advanced_retrosynthetic_pathway_generator` | Overridden by `prompts/scientific/chemistry/organic/retrosynthesis/skills.md` |
| `adverse_event_signal_detection_architect` | `adverse_event_signal_detection_architect` | Overridden by `prompts/clinical/pharmacovigilance/skills.md` |
| `affective_polarization_contagion_mapper` | `affective_polarization_contagion_mapper` | Overridden by `prompts/scientific/psychology/epidemiology/affective_polarization/skills.md` |
| `agm_belief_revision_formal_engine` | `agm_belief_revision_formal_engine` | Overridden by `prompts/scientific/philosophy/logic/philosophical_logic/skills.md` |
| `ai_threat_modeling_architect` | `ai_threat_modeling_architect` | Overridden by `prompts/technical/security/skills.md` |
| `algorithmic_behavior_echo_chamber_modeler` | `algorithmic_behavior_echo_chamber_modeler` | Overridden by `prompts/scientific/psychology/computational/network_contagion/skills.md` |
| `algorithmic_cognitive_overload_epidemiological_mapper` | `algorithmic_cognitive_overload_epidemiological_mapper` | Overridden by `prompts/scientific/psychology/epidemiology/global_mental_health/skills.md` |
| `algorithmic_misinformation_contagion_modeler` | `algorithmic_misinformation_contagion_modeler` | Overridden by `prompts/scientific/psychology/computational/network_contagion/skills.md` |
| `algorithmic_multi_touch_attribution_modeler` | `algorithmic_multi_touch_attribution_modeler` | Overridden by `prompts/growth/analytics/skills.md` |
| `algorithmic_social_contagion_modeler` | `algorithmic_social_contagion_modeler` | Overridden by `prompts/computational/network_contagion/skills.md` |
| `ambiguous_natural_language_fol_formalizer` | `ambiguous_natural_language_fol_formalizer` | Overridden by `prompts/scientific/formal_logic/systems/first_order_logic/skills.md` |
| `approximate_bayesian_computation_architect` | `approximate_bayesian_computation_architect` | Overridden by `prompts/scientific/statistics/inference/bayesian_methods/skills.md` |
| `astrocytic_tripartite_synapse_architect` | `astrocytic_tripartite_synapse_architect` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `astrocytic_tripartite_synapse_calcium_dynamics_architect` | `astrocytic_tripartite_synapse_calcium_dynamics_architect` | Overridden by `prompts/scientific/cellular/neurophysiology/skills.md` |
| `asymptotic_distribution_mle_architect` | `asymptotic_distribution_mle_architect` | Overridden by `prompts/scientific/statistics/theory/asymptotics/skills.md` |
| `atiyah_singer_index_theorem_architect` | `atiyah_singer_index_theorem_architect` | Overridden by `prompts/scientific/mathematics/geometry/differential/skills.md` |
| `automated_malware_reverse_engineering_analyst` | `automated_malware_reverse_engineering_analyst` | Overridden by `prompts/technical/security/skills.md` |
| `b2b_abm_pipeline_velocity_architect` | `b2b_abm_pipeline_velocity_architect` | Overridden by `prompts/growth/predictive_modeling/skills.md` |
| `banach_space_operator_architect` | `banach_space_operator_architect` | Overridden by `prompts/scientific/mathematics/analysis/functional_analysis/skills.md` |
| `basal_ganglia_td_learning_architect` | `basal_ganglia_td_learning_architect` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `bayesian_epistemological_update_formalizer` | `bayesian_epistemological_update_formalizer` | Overridden by `prompts/scientific/philosophy/epistemology/formal_epistemology/skills.md` |
| `bayesian_hierarchical_model_architect` | `bayesian_hierarchical_model_architect` | Overridden by `prompts/scientific/statistics/inference/bayesian_methods/skills.md` |
| `bayesian_media_mix_modeling_architect` | `bayesian_media_mix_modeling_architect` | Overridden by `prompts/growth/performance_marketing/skills.md` |
| `bayesian_optimization_hyperparameter_architect` | `bayesian_optimization_hyperparameter_architect` | Overridden by `prompts/technical/data_science/skills.md` |
| `bayesian_phylogenetic_inference_mcmc_architect` | `bayesian_phylogenetic_inference_mcmc_architect` | Overridden by `prompts/scientific/computational_biology/skills.md` |
| `bayesian_vector_autoregression_architect` | `bayesian_vector_autoregression_architect` | Overridden by `prompts/scientific/economics/econometrics/time_series/skills.md` |
| `behavioral_epidemiology_social_contagion_modeler` | `behavioral_epidemiology_social_contagion_modeler` | Overridden by `prompts/scientific/psychology/computational/network_contagion/skills.md` |
| `biophysical_hodgkin_huxley_modeler` | `biophysical_hodgkin_huxley_modeler` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `blinder_oaxaca_decomposition_architect` | `blinder_oaxaca_decomposition_architect` | Overridden by `prompts/scientific/sociology/methods/quantitative/skills.md` |
| `blue_ocean_value_innovation_architect` | `blue_ocean_value_innovation_architect` | Overridden by `prompts/business/strategy/skills.md` |
| `breakthrough_therapy_designation_rationale_architect` | `breakthrough_therapy_designation_rationale_architect` | Overridden by `prompts/clinical/regulatory_affairs/skills.md` |
| `byzantine_fault_tolerant_consensus_architect` | `byzantine_fault_tolerant_consensus_architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `calculus_of_constructions_proof_architect` | `calculus_of_constructions_proof_architect` | Overridden by `prompts/scientific/mathematics/foundations/proof_theory/skills.md` |
| `capa_root_cause_analysis_architect` | `capa_root_cause_analysis_architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `capa_root_cause_resolution_architect` | `capa_root_cause_resolution_architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `carceral_state_expansion_modeler` | `carceral_state_expansion_modeler` | Overridden by `prompts/scientific/sociology/institutions/macro_structures/skills.md` |
| `categorical_theorem_translator` | `categorical_theorem_translator` | Overridden by `prompts/scientific/mathematics/category_theory/skills.md` |
| `category_theory_adjunction_architect` | `category_theory_adjunction_architect` | Overridden by `prompts/scientific/mathematics/category_theory/skills.md` |
| `causal_inference_dag_architect` | `causal_inference_dag_architect` | Overridden by `prompts/scientific/statistics/design/causal_inference/skills.md` |
| `central_pattern_generator_circuit_modeler` | `central_pattern_generator_circuit_modeler` | Overridden by `prompts/scientific/systems/neural_circuits/skills.md` |
| `cer_literature_review_architect` | `cer_literature_review_architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `chaos_mesh_fault_injection_architect` | `chaos_mesh_fault_injection_architect` | Overridden by `prompts/technical/devops/skills.md` |
| `characteristic_class_cobordism_architect` | `characteristic_class_cobordism_architect` | Overridden by `prompts/scientific/mathematics/topology/algebraic_topology/skills.md` |
| `chromatin_conformation_hic_contact_map_architect` | `chromatin_conformation_hic_contact_map_architect` | Overridden by `prompts/scientific/genetics/genomics/skills.md` |
| `clinical_study_report_patient_narrative_architect` | `clinical_study_report_patient_narrative_architect` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `cognitive_bias_epistemological_deconstructor` | `cognitive_bias_epistemological_deconstructor` | Overridden by `prompts/scientific/philosophy/epistemology/formal_epistemology/skills.md` |
| `cognitive_bias_mitigation_architect` | `cognitive_bias_mitigation_architect` | Overridden by `prompts/scientific/psychology/cognitive/information_processing/skills.md` |
| `cognitive_diagnostic_modeling_architect` | `cognitive_diagnostic_modeling_architect` | Overridden by `prompts/scientific/psychology/quantitative/psychometrics/skills.md` |
| `cognitive_inoculation_campaign_architect` | `cognitive_inoculation_campaign_architect` | Overridden by `prompts/scientific/psychology/computational/network_contagion/skills.md` |
| `cohort_retention_survival_analysis_architect` | `cohort_retention_survival_analysis_architect` | Overridden by `prompts/growth/lifecycle/skills.md` |
| `collective_panic_cascade_architect` | `collective_panic_cascade_architect` | Overridden by `prompts/scientific/sociology/mass_behavior/skills.md` |
| `companion_diagnostic_analytical_validation_architect` | `companion_diagnostic_analytical_validation_architect` | Overridden by `prompts/regulatory/device_specifics/skills.md` |
| `complex_ppi_network_mapper` | `complex_ppi_network_mapper` | Overridden by `prompts/scientific/molecular/proteomics/skills.md` |
| `confidential_computing_enclave_architect` | `confidential_computing_enclave_architect` | Overridden by `prompts/technical/security/skills.md` |
| `constructive_intuitionistic_natural_deduction_prover` | `constructive_intuitionistic_natural_deduction_prover` | Overridden by `prompts/scientific/formal_logic/systems/intuitionistic_logic/skills.md` |
| `continuous_attractor_neural_network_architect` | `continuous_attractor_neural_network_architect` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `continuous_time_asset_pricing_architect` | `continuous_time_asset_pricing_architect` | Overridden by `prompts/scientific/economics/finance/asset_pricing/skills.md` |
| `corporate_b2b_saas_pricing_tier_architect` | `corporate_b2b_saas_pricing_tier_architect` | Overridden by `prompts/business/strategy/skills.md` |
| `corporate_fx_hedging_currency_risk_architect` | `corporate_fx_hedging_currency_risk_architect` | Overridden by `prompts/business/strategy/skills.md` |
| `corporate_ip_portfolio_monetization_architect` | `corporate_ip_portfolio_monetization_architect` | Overridden by `prompts/business/strategy/skills.md` |
| `corporate_wargaming_scenario_planning_architect` | `corporate_wargaming_scenario_planning_architect` | Overridden by `prompts/business/strategy/skills.md` |
| `counterfactual_semantics_stalnaker_lewis_evaluator` | `counterfactual_semantics_stalnaker_lewis_evaluator` | Overridden by `prompts/scientific/philosophy/logic/philosophical_logic/skills.md` |
| `crdt_conflict_resolution_architect` | `crdt_conflict_resolution_architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `crispr_cas9_off_target_predictive_modeler` | `crispr_cas9_off_target_predictive_modeler` | Overridden by `prompts/scientific/genetics/genomics/skills.md` |
| `crispr_cas9_off_target_probabilistic_modeler` | `crispr_cas9_off_target_probabilistic_modeler` | Overridden by `prompts/scientific/computational_biology/skills.md` |
| `crispr_cas9_off_target_thermodynamic_architect` | `crispr_cas9_off_target_thermodynamic_architect` | Overridden by `prompts/scientific/biology/genetics/genomics/skills.md` |
| `cross_channel_behavioral_trigger_architect` | `cross_channel_behavioral_trigger_architect` | Overridden by `prompts/growth/lifecycle/skills.md` |
| `csr_efficacy_narrative_architect` | `csr_efficacy_narrative_architect` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `csr_patient_narrative_architect` | `csr_patient_narrative_architect` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `csr_patient_safety_narrative_architect` | `csr_patient_safety_narrative_architect` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `ctd_module_2_7_clinical_summary_architect` | `ctd_module_2_7_clinical_summary_architect` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `custom_axiomatic_system_soundness_evaluator` | `custom_axiomatic_system_soundness_evaluator` | Overridden by `prompts/scientific/formal_logic/foundations/proof_theory/skills.md` |
| `d_brane_worldvolume_effective_action_architect` | `d_brane_worldvolume_effective_action_architect` | Overridden by `prompts/scientific/physics/string_theory/brane_dynamics/skills.md` |
| `deep_brain_stimulation_biophysical_architect` | `deep_brain_stimulation_biophysical_architect` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `dendritic_cable_theory_computation_architect` | `dendritic_cable_theory_computation_architect` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `dependent_type_theory_judgment_derivation` | `dependent_type_theory_judgment_derivation` | Overridden by `prompts/scientific/mathematics/formal_logic/skills.md` |
| `dialectical_materialism_structural_crisis_modeler` | `dialectical_materialism_structural_crisis_modeler` | Overridden by `prompts/scientific/sociology/theory/critical_frameworks/skills.md` |
| `dialectical_metaphysical_synthesizer` | `dialectical_metaphysical_synthesizer` | Overridden by `prompts/scientific/philosophy/metaphysics/skills.md` |
| `diamond_mortensen_pissarides_architect` | `diamond_mortensen_pissarides_architect` | Overridden by `prompts/scientific/economics/macroeconomics/search_and_matching/skills.md` |
| `differential_alternative_splicing_isoform_architect` | `differential_alternative_splicing_isoform_architect` | Overridden by `prompts/scientific/genetics/transcriptomics/skills.md` |
| `differential_diagnosis_mapping_architect` | `differential_diagnosis_mapping_architect` | Overridden by `prompts/scientific/psychology/clinical/psychopathology/skills.md` |
| `digital_phenotyping_epidemiological_surveillance_architect` | `digital_phenotyping_epidemiological_surveillance_architect` | Overridden by `prompts/scientific/psychology/epidemiology/global_mental_health/skills.md` |
| `dimensional_psychopathology_hierarchical_modeler` | `dimensional_psychopathology_hierarchical_modeler` | Overridden by `prompts/scientific/psychology/clinical/psychopathology/skills.md` |
| `dirichlet_process_mixture_architect` | `dirichlet_process_mixture_architect` | Overridden by `prompts/scientific/statistics/inference/bayesian_methods/skills.md` |
| `double_machine_learning_architect` | `double_machine_learning_architect` | Overridden by `prompts/scientific/statistics/inference/causal_inference/skills.md` |
| `dynamic_fleet_routing_optimization_architect` | `dynamic_fleet_routing_optimization_architect` | Overridden by `prompts/management/operations/skills.md` |
| `dynamic_panel_gmm_architect` | `dynamic_panel_gmm_architect` | Overridden by `prompts/scientific/economics/econometrics/panel_data/skills.md` |
| `eBPF Network Observability Architect` | `eBPF_Network_Observability_Architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `eBPF Runtime Security Architect` | `eBPF_Runtime_Security_Architect` | Overridden by `prompts/technical/security/skills.md` |
| `eConsent Implementation Strategy` | `eConsent_Implementation_Strategy` | Overridden by `prompts/clinical/eclinical_integration/skills.md` |
| `ePRO Adoption Plan for Sponsors` | `ePRO_Adoption_Plan_for_Sponsors` | Overridden by `prompts/clinical/epro/epro_workflow/skills.md` |
| `ePRO Migration Equivalence Checker` | `ePRO_Migration_Equivalence_Checker` | Overridden by `prompts/scientific/coa/skills.md` |
| `eTMF Artifact Classifier` | `eTMF_Artifact_Classifier` | Overridden by `prompts/clinical/data_management/skills.md` |
| `eTMF Compliance Gap Analysis` | `eTMF_Compliance_Gap_Analysis` | Overridden by `prompts/regulatory/quality/skills.md` |
| `ecological_momentary_assessment_multilevel_modeler` | `ecological_momentary_assessment_multilevel_modeler` | Overridden by `prompts/scientific/psychology/developmental/longitudinal_modeling/skills.md` |
| `effective_field_theory_matching_rg_running_architect` | `effective_field_theory_matching_rg_running_architect` | Overridden by `prompts/scientific/physics/quantum_field_theory/skills.md` |
| `empirical_process_theory_architect` | `empirical_process_theory_architect` | Overridden by `prompts/scientific/statistics/theory/asymptotics/skills.md` |
| `epigenetic_methylation_hmm_architect` | `epigenetic_methylation_hmm_architect` | Overridden by `prompts/scientific/genetics/genomics/skills.md` |
| `epistemic_defeater_formal_analyzer` | `epistemic_defeater_formal_analyzer` | Overridden by `prompts/scientific/philosophy/epistemology/formal_epistemology/skills.md` |
| `epistemic_logic_omniscience_paradox_resolver` | `epistemic_logic_omniscience_paradox_resolver` | Overridden by `prompts/scientific/philosophy/logic/philosophical_logic/skills.md` |
| `epistemic_modal_logic_kripke_evaluator` | `epistemic_modal_logic_kripke_evaluator` | Overridden by `prompts/scientific/formal_logic/non_classical/modal_logic/skills.md` |
| `epistemic_peer_disagreement_formalizer` | `epistemic_peer_disagreement_formalizer` | Overridden by `prompts/scientific/philosophy/epistemology/formal_epistemology/skills.md` |
| `eu_mdr_clinical_evaluation_report_architect` | `eu_mdr_clinical_evaluation_report_architect` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `eu_mdr_sscp_architect` | `eu_mdr_sscp_architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `evidence_based_intervention_architect` | `evidence_based_intervention_architect` | Overridden by `prompts/scientific/psychology/clinical/treatment_planning/skills.md` |
| `exponential_random_graph_model_architect` | `exponential_random_graph_model_architect` | Overridden by `prompts/scientific/sociology/methods/social_network_analysis/skills.md` |
| `fast_track_designation_request_architect` | `fast_track_designation_request_architect` | Overridden by `prompts/clinical/regulatory_affairs/skills.md` |
| `fda_483_warning_letter_remediation_architect` | `fda_483_warning_letter_remediation_architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `fda_510k_substantial_equivalence_architect` | `fda_510k_substantial_equivalence_architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `fda_de_novo_classification_request_architect` | `fda_de_novo_classification_request_architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `fda_q_submission_pre_sub_meeting_package_architect` | `fda_q_submission_pre_sub_meeting_package_architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `fda_type_b_meeting_briefing_package_architect` | `fda_type_b_meeting_briefing_package_architect` | Overridden by `prompts/clinical/regulatory_affairs/skills.md` |
| `financial_frictions_dsge_architect` | `financial_frictions_dsge_architect` | Overridden by `prompts/scientific/economics/macroeconomics/dsge_modeling/skills.md` |
| `finops_cloud_cost_optimization_architect` | `finops_cloud_cost_optimization_architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `first_order_logic_natural_language_translator` | `first_order_logic_natural_language_translator` | Overridden by `prompts/scientific/mathematics/formal_logic/skills.md` |
| `first_order_logic_semantic_tableau_generator` | `first_order_logic_semantic_tableau_generator` | Overridden by `prompts/scientific/mathematics/formal_logic/skills.md` |
| `first_order_logic_sequent_calculus_prover` | `first_order_logic_sequent_calculus_prover` | Overridden by `prompts/scientific/mathematics/formal_logic/skills.md` |
| `fokker_planck_population_dynamics_architect` | `fokker_planck_population_dynamics_architect` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `forcing_poset_generic_extension_architect` | `forcing_poset_generic_extension_architect` | Overridden by `prompts/scientific/mathematics/foundations/set_theory/skills.md` |
| `fractional_calculus_pde_modeler` | `fractional_calculus_pde_modeler` | Overridden by `prompts/scientific/mathematics/numerical_methods/skills.md` |
| `free_energy_principle_active_inference_architect` | `free_energy_principle_active_inference_architect` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `freemium_conversion_velocity_architect` | `freemium_conversion_velocity_architect` | Overridden by `prompts/growth/product_marketing/skills.md` |
| `fully_homomorphic_encryption_circuit_architect` | `fully_homomorphic_encryption_circuit_architect` | Overridden by `prompts/technical/cryptography/skills.md` |
| `galois_group_resolvent_architect` | `galois_group_resolvent_architect` | Overridden by `prompts/scientific/mathematics/algebra/galois_theory/skills.md` |
| `game_theoretic_competitive_dynamics_architect` | `game_theoretic_competitive_dynamics_architect` | Overridden by `prompts/business/strategy/skills.md` |
| `gamified_behavioral_addiction_contagion_modeler` | `gamified_behavioral_addiction_contagion_modeler` | Overridden by `prompts/scientific/psychology/computational/network_contagion/skills.md` |
| `gaussian_process_regression_architect` | `gaussian_process_regression_architect` | Overridden by `prompts/scientific/statistics/inference/bayesian_methods/skills.md` |
| `generalizability_theory_architect` | `generalizability_theory_architect` | Overridden by `prompts/scientific/psychology/quantitative/psychometrics/skills.md` |
| `genome_scale_metabolic_flux_modeler` | `genome_scale_metabolic_flux_modeler` | Overridden by `prompts/scientific/cellular/metabolism/skills.md` |
| `gentrification_displacement_spatial_inequality_architect` | `gentrification_displacement_spatial_inequality_architect` | Overridden by `prompts/scientific/sociology/stratification/systemic_inequality/skills.md` |
| `gini_coefficient_income_stratification_architect` | `gini_coefficient_income_stratification_architect` | Overridden by `prompts/scientific/sociology/stratification/systemic_inequality/skills.md` |
| `gitops_continuous_delivery_architect` | `gitops_continuous_delivery_architect` | Overridden by `prompts/technical/devops/skills.md` |
| `global_supply_chain_geopolitical_duress_architect` | `global_supply_chain_geopolitical_duress_architect` | Overridden by `prompts/business/operations/supply_chain/skills.md` |
| `godel_incompleteness_arithmetization_engineer` | `godel_incompleteness_arithmetization_engineer` | Overridden by `prompts/scientific/mathematics/formal_logic/skills.md` |
| `graph_theoretical_connectome_analyzer` | `graph_theoretical_connectome_analyzer` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `gtm_pricing_elasticity_architect` | `gtm_pricing_elasticity_architect` | Overridden by `prompts/growth/strategy/skills.md` |
| `gwas_polygenic_risk_score_architect` | `gwas_polygenic_risk_score_architect` | Overridden by `prompts/scientific/genetics/genomics/skills.md` |
| `hamiltonian_monte_carlo_architect` | `hamiltonian_monte_carlo_architect` | Overridden by `prompts/scientific/statistics/inference/bayesian_methods/skills.md` |
| `hank_macroeconomic_architect` | `hank_macroeconomic_architect` | Overridden by `prompts/scientific/economics/macroeconomics/heterogeneous_agents/skills.md` |
| `health_inequality_concentration_index_architect` | `health_inequality_concentration_index_architect` | Overridden by `prompts/scientific/sociology/stratification/systemic_inequality/skills.md` |
| `hidden_markov_model_architect` | `hidden_markov_model_architect` | Overridden by `prompts/scientific/statistics/stochastic/markov_processes/skills.md` |
| `high_dimensional_sparse_regression_architect` | `high_dimensional_sparse_regression_architect` | Overridden by `prompts/scientific/statistics/modeling/high_dimensional_analysis/skills.md` |
| `higher_homotopy_postnikov_tower_architect` | `higher_homotopy_postnikov_tower_architect` | Overridden by `prompts/scientific/mathematics/topology/algebraic_topology/skills.md` |
| `higher_order_unification_resolution_architect` | `higher_order_unification_resolution_architect` | Overridden by `prompts/scientific/formal_logic/systems/higher_order_logic/skills.md` |
| `highly_available_distributed_block_storage_architect` | `highly_available_distributed_block_storage_architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `hodgkin_huxley_biophysical_modeler` | `hodgkin_huxley_biophysical_modeler` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `homotopy_type_theory_univalence_architect` | `homotopy_type_theory_univalence_architect` | Overridden by `prompts/scientific/mathematics/foundations/proof_theory/skills.md` |
| `iCGM Clinical Testing Strategy` | `iCGM_Clinical_Testing_Strategy` | Overridden by `prompts/regulatory/device_specifics/skills.md` |
| `icf_readability_compliance_architect` | `icf_readability_compliance_architect` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `ich_e2c_pbrer_benefit_risk_architect` | `ich_e2c_pbrer_benefit_risk_architect` | Overridden by `prompts/clinical/pharmacovigilance/skills.md` |
| `ich_e3_clinical_study_report_architect` | `ich_e3_clinical_study_report_architect` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `ich_m4e_ctd_clinical_overview_architect` | `ich_m4e_ctd_clinical_overview_architect` | Overridden by `prompts/regulatory/submissions/skills.md` |
| `iec_62304_soup_anomaly_evaluator` | `iec_62304_soup_anomaly_evaluator` | Overridden by `prompts/regulatory/quality/skills.md` |
| `incrementality_causal_inference_modeler` | `incrementality_causal_inference_modeler` | Overridden by `prompts/growth/analytics/skills.md` |
| `ind_clinical_hold_response_architect` | `ind_clinical_hold_response_architect` | Overridden by `prompts/clinical/regulatory_affairs/skills.md` |
| `institutional_isomorphism_lifecycle_modeler` | `institutional_isomorphism_lifecycle_modeler` | Overridden by `prompts/scientific/sociology/institutions/skills.md` |
| `institutional_trust_hemorrhage_modeler` | `institutional_trust_hemorrhage_modeler` | Overridden by `prompts/scientific/sociology/mass_behavior/skills.md` |
| `intergenerational_mobility_modeler` | `intergenerational_mobility_modeler` | Overridden by `prompts/scientific/sociology/stratification/skills.md` |
| `intergenerational_social_mobility_markov_chain_architect` | `intergenerational_social_mobility_markov_chain_architect` | Overridden by `prompts/scientific/sociology/stratification/systemic_inequality/skills.md` |
| `intergenerational_social_mobility_markov_modeler` | `intergenerational_social_mobility_markov_modeler` | Overridden by `prompts/scientific/sociology/demography/skills.md` |
| `intersectional_stratification_mechanism_modeler` | `intersectional_stratification_mechanism_modeler` | Overridden by `prompts/scientific/sociology/stratification/skills.md` |
| `intuitionistic_logic_natural_deduction_generator` | `intuitionistic_logic_natural_deduction_generator` | Overridden by `prompts/scientific/mathematics/foundations/proof_theory/skills.md` |
| `intuitionistic_natural_deduction_prover` | `intuitionistic_natural_deduction_prover` | Overridden by `prompts/scientific/mathematics/formal_logic/skills.md` |
| `investigators_brochure_safety_synthesizer` | `investigators_brochure_safety_synthesizer` | Overridden by `prompts/clinical/regulatory_affairs/skills.md` |
| `investigators_brochure_synthesis_architect` | `investigators_brochure_synthesis_architect` | Overridden by `prompts/scientific/medical_writing/skills.md` |
| `item_response_theory_dif_analyzer` | `item_response_theory_dif_analyzer` | Overridden by `prompts/scientific/psychology/quantitative/psychometrics/skills.md` |
| `joint_longitudinal_survival_architect` | `joint_longitudinal_survival_architect` | Overridden by `prompts/scientific/statistics/modeling/survival_analysis/skills.md` |
| `jump_diffusion_modeler` | `jump_diffusion_modeler` | Overridden by `prompts/scientific/statistics/stochastic/stochastic_differential_equations/skills.md` |
| `large_cardinal_elementary_embedding_architect` | `large_cardinal_elementary_embedding_architect` | Overridden by `prompts/scientific/mathematics/foundations/set_theory/skills.md` |
| `large_scale_axial_coding_framework_generator` | `large_scale_axial_coding_framework_generator` | Overridden by `prompts/scientific/sociology/methods/ethnographic_coding/skills.md` |
| `latent_growth_curve_modeling_architect` | `latent_growth_curve_modeling_architect` | Overridden by `prompts/scientific/psychology/developmental/longitudinal_modeling/skills.md` |
| `latent_profile_mixture_modeling_architect` | `latent_profile_mixture_modeling_architect` | Overridden by `prompts/scientific/psychology/quantitative/psychometrics/skills.md` |
| `lattice_boltzmann_multiphase_architect` | `lattice_boltzmann_multiphase_architect` | Overridden by `prompts/scientific/applied_mathematics/physics/fluid_dynamics/skills.md` |
| `lean_six_sigma_vsm_architect` | `lean_six_sigma_vsm_architect` | Overridden by `prompts/management/operations/skills.md` |
| `linear_temporal_logic_model_checker` | `linear_temporal_logic_model_checker` | Overridden by `prompts/scientific/mathematics/formal_logic/skills.md` |
| `local_polynomial_regression_discontinuity_architect` | `local_polynomial_regression_discontinuity_architect` | Overridden by `prompts/scientific/economics/econometrics/causal_inference/skills.md` |
| `log_gaussian_cox_process_architect` | `log_gaussian_cox_process_architect` | Overridden by `prompts/scientific/statistics/modeling/spatial_point_processes/skills.md` |
| `longitudinal_measurement_invariance_evaluator` | `longitudinal_measurement_invariance_evaluator` | Overridden by `prompts/scientific/psychology/quantitative/psychometrics/skills.md` |
| `longitudinal_trauma_propagation_modeler` | `longitudinal_trauma_propagation_modeler` | Overridden by `prompts/scientific/epidemiology/global_mental_health/skills.md` |
| `macOS ESF Unified Logging Threat Hunter` | `macOS_ESF_Unified_Logging_Threat_Hunter` | Overridden by `prompts/technical/security/secops/skills.md` |
| `mass_psychogenic_illness_diffusion_modeler` | `mass_psychogenic_illness_diffusion_modeler` | Overridden by `prompts/scientific/psychology/computational/network_contagion/skills.md` |
| `mereological_composition_analyzer` | `mereological_composition_analyzer` | Overridden by `prompts/scientific/philosophy/metaphysics/ontology/skills.md` |
| `metabolic_control_analysis_architect` | `metabolic_control_analysis_architect` | Overridden by `prompts/scientific/cellular/metabolism/skills.md` |
| `metagenomic_assembly_taxonomic_binning_architect` | `metagenomic_assembly_taxonomic_binning_architect` | Overridden by `prompts/scientific/genetics/genomics/skills.md` |
| `metaphysical_grounding_fundamentality_formalizer` | `metaphysical_grounding_fundamentality_formalizer` | Overridden by `prompts/scientific/philosophy/metaphysics/ontology/skills.md` |
| `mirrleesian_optimal_income_tax_architect` | `mirrleesian_optimal_income_tax_architect` | Overridden by `prompts/scientific/economics/public_economics/optimal_tax_theory/skills.md` |
| `mixed_frequency_dynamic_factor_nowcasting_architect` | `mixed_frequency_dynamic_factor_nowcasting_architect` | Overridden by `prompts/scientific/economics/econometrics/time_series/skills.md` |
| `model_theoretic_type_space_architect` | `model_theoretic_type_space_architect` | Overridden by `prompts/scientific/mathematics/foundations/model_theory/skills.md` |
| `molecular_dynamics_simulation_architect` | `molecular_dynamics_simulation_architect` | Overridden by `prompts/scientific/computational_biology/skills.md` |
| `mu_recursive_function_derivation_architect` | `mu_recursive_function_derivation_architect` | Overridden by `prompts/scientific/mathematics/formal_logic/skills.md` |
| `multi_echelon_inventory_optimization_architect` | `multi_echelon_inventory_optimization_architect` | Overridden by `prompts/management/operations/skills.md` |
| `multi_modal_fmri_eeg_integration_architect` | `multi_modal_fmri_eeg_integration_architect` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `multi_national_behavioral_intervention_architect` | `multi_national_behavioral_intervention_architect` | Overridden by `prompts/scientific/psychology/cross_cultural/population_psychometrics/skills.md` |
| `multi_objective_stochastic_optimization_architect` | `multi_objective_stochastic_optimization_architect` | Overridden by `prompts/computational/operations_research/skills.md` |
| `multi_omics_data_integration_architect` | `multi_omics_data_integration_architect` | Overridden by `prompts/scientific/computational_biology/skills.md` |
| `multi_scale_pde_asymptotic_homogenization_architect` | `multi_scale_pde_asymptotic_homogenization_architect` | Overridden by `prompts/computational/numerical_methods/skills.md` |
| `multi_step_retrosynthetic_pathway_architect` | `multi_step_retrosynthetic_pathway_architect` | Overridden by `prompts/scientific/chemistry/organic/retrosynthesis/skills.md` |
| `multidimensional_item_response_theory_architect` | `multidimensional_item_response_theory_architect` | Overridden by `prompts/scientific/psychology/quantitative/psychometrics/skills.md` |
| `multidimensional_nmr_hrms_structure_elucidator` | `multidimensional_nmr_hrms_structure_elucidator` | Overridden by `prompts/scientific/chemistry/analytical/skills.md` |
| `multidimensional_poverty_alkire_foster_architect` | `multidimensional_poverty_alkire_foster_architect` | Overridden by `prompts/scientific/sociology/stratification/systemic_inequality/skills.md` |
| `multifactorial_behavioral_intervention_architect` | `multifactorial_behavioral_intervention_architect` | Overridden by `prompts/scientific/psychology/quantitative/experimental_design/skills.md` |
| `multinational_longitudinal_intervention_architect` | `multinational_longitudinal_intervention_architect` | Overridden by `prompts/scientific/psychology/epidemiology/global_mental_health/skills.md` |
| `multivariate_extreme_value_architect` | `multivariate_extreme_value_architect` | Overridden by `prompts/scientific/statistics/modeling/extreme_value_theory/skills.md` |
| `n_player_bayesian_nash_equilibrium_auction_architect` | `n_player_bayesian_nash_equilibrium_auction_architect` | Overridden by `prompts/scientific/economics/microeconomics/game_theory/skills.md` |
| `network_psychometrics_architect` | `network_psychometrics_architect` | Overridden by `prompts/scientific/psychology/quantitative/psychometrics/skills.md` |
| `neural_field_theory_spatiotemporal_dynamics_architect` | `neural_field_theory_spatiotemporal_dynamics_architect` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `neural_manifold_state_space_analyzer` | `neural_manifold_state_space_analyzer` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `neuromorphic_spiking_network_biophysical_architect` | `neuromorphic_spiking_network_biophysical_architect` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `neurovascular_coupling_hemodynamic_response_architect` | `neurovascular_coupling_hemodynamic_response_architect` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `new_keynesian_dsge_architect` | `new_keynesian_dsge_architect` | Overridden by `prompts/scientific/economics/macroeconomics/dsge_modeling/skills.md` |
| `non_standard_analysis_hyperreal_architect` | `non_standard_analysis_hyperreal_architect` | Overridden by `prompts/scientific/mathematics/foundations/proof_theory/skills.md` |
| `non_stationary_13c_metabolic_flux_analysis_architect` | `non_stationary_13c_metabolic_flux_analysis_architect` | Overridden by `prompts/scientific/cellular/metabolism/skills.md` |
| `nrr_expansion_propensity_architect` | `nrr_expansion_propensity_architect` | Overridden by `prompts/growth/lifecycle/skills.md` |
| `occupational_segregation_opportunity_hoarding_architect` | `occupational_segregation_opportunity_hoarding_architect` | Overridden by `prompts/scientific/sociology/stratification/systemic_inequality/skills.md` |
| `open_economy_dsge_architect` | `open_economy_dsge_architect` | Overridden by `prompts/scientific/economics/macroeconomics/dsge_modeling/skills.md` |
| `operational_resilience_tabletop_simulation_architect` | `operational_resilience_tabletop_simulation_architect` | Overridden by `prompts/management/operations/skills.md` |
| `operational_turnaround_restructuring_architect` | `operational_turnaround_restructuring_architect` | Overridden by `prompts/management/operations/skills.md` |
| `optimal_mechanism_design_architect` | `optimal_mechanism_design_architect` | Overridden by `prompts/scientific/economics/microeconomics/mechanism_design/skills.md` |
| `optogenetic_photocurrent_biophysical_modeler` | `optogenetic_photocurrent_biophysical_modeler` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `orphan_drug_designation_application_architect` | `orphan_drug_designation_application_architect` | Overridden by `prompts/clinical/regulatory_affairs/skills.md` |
| `pangenome_graph_structural_variant_architect` | `pangenome_graph_structural_variant_architect` | Overridden by `prompts/scientific/genetics/genomics/skills.md` |
| `paraconsistent_logic_dialetheism_evaluator` | `paraconsistent_logic_dialetheism_evaluator` | Overridden by `prompts/scientific/philosophy/logic/philosophical_logic/skills.md` |
| `peer_to_peer_gossip_protocol_architect` | `peer_to_peer_gossip_protocol_architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `phenomenological_reduction_engine` | `phenomenological_reduction_engine` | Overridden by `prompts/scientific/philosophy/phenomenology/skills.md` |
| `physics_informed_neural_network_architect` | `physics_informed_neural_network_architect` | Overridden by `prompts/computational/numerical_methods/skills.md` |
| `pinn_stiff_pde_architect` | `pinn_stiff_pde_architect` | Overridden by `prompts/scientific/applied_mathematics/computational/physics_informed_neural_networks/skills.md` |
| `population_macro_nudging_architect` | `population_macro_nudging_architect` | Overridden by `prompts/scientific/psychology/behavioral_economics/macro_nudging/skills.md` |
| `post_merger_integration_synergy_architect` | `post_merger_integration_synergy_architect` | Overridden by `prompts/management/operations/skills.md` |
| `post_quantum_cryptography_migration_architect` | `post_quantum_cryptography_migration_architect` | Overridden by `prompts/technical/cryptography/skills.md` |
| `predictive_cac_payback_modeler` | `predictive_cac_payback_modeler` | Overridden by `prompts/growth/performance_marketing/skills.md` |
| `predictive_churn_ltv_optimization_architect` | `predictive_churn_ltv_optimization_architect` | Overridden by `prompts/growth/predictive_modeling/skills.md` |
| `predictive_rfm_churn_mitigation_architect` | `predictive_rfm_churn_mitigation_architect` | Overridden by `prompts/growth/lifecycle/skills.md` |
| `product_led_growth_k_factor_architect` | `product_led_growth_k_factor_architect` | Overridden by `prompts/growth/product_marketing/skills.md` |
| `projective_scheme_sheaf_cohomology_architect` | `projective_scheme_sheaf_cohomology_architect` | Overridden by `prompts/scientific/mathematics/geometry/algebraic_geometry/skills.md` |
| `propositional_dynamic_logic_pdl_evaluator` | `propositional_dynamic_logic_pdl_evaluator` | Overridden by `prompts/scientific/mathematics/formal_logic/skills.md` |
| `protein_ligand_free_energy_perturbation_architect` | `protein_ligand_free_energy_perturbation_architect` | Overridden by `prompts/scientific/molecular/proteomics/skills.md` |
| `protocol_deviation_assessment_architect` | `protocol_deviation_assessment_architect` | Overridden by `prompts/clinical/medical_writing/skills.md` |
| `pseudo_riemannian_tensor_calculus_prover` | `pseudo_riemannian_tensor_calculus_prover` | Overridden by `prompts/scientific/mathematics/geometry/differential/skills.md` |
| `psychological_trauma_epidemiology_mapper` | `psychological_trauma_epidemiology_mapper` | Overridden by `prompts/scientific/psychology/epidemiology/global_mental_health/skills.md` |
| `qms_management_review_architect` | `qms_management_review_architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `quantitative_commercial_due_diligence_architect` | `quantitative_commercial_due_diligence_architect` | Overridden by `prompts/business/strategy/skills.md` |
| `quantitative_fixed_income_duration_convexity_architect` | `quantitative_fixed_income_duration_convexity_architect` | Overridden by `prompts/business/finance/skills.md` |
| `quantitative_shareholder_distribution_optimization_architect` | `quantitative_shareholder_distribution_optimization_architect` | Overridden by `prompts/business/strategy/skills.md` |
| `rare_pediatric_disease_designation_architect` | `rare_pediatric_disease_designation_architect` | Overridden by `prompts/clinical/regulatory_affairs/skills.md` |
| `red_team_exploit_chain_architect` | `red_team_exploit_chain_architect` | Overridden by `prompts/technical/security/skills.md` |
| `regulatory_compliance_automation_architect` | `regulatory_compliance_automation_architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `relevance_logic_entailment_evaluator` | `relevance_logic_entailment_evaluator` | Overridden by `prompts/scientific/philosophy/logic/philosophical_logic/skills.md` |
| `residential_segregation_spatial_inequality_modeler` | `residential_segregation_spatial_inequality_modeler` | Overridden by `prompts/scientific/sociology/demography/skills.md` |
| `reversible_jump_mcmc_architect` | `reversible_jump_mcmc_architect` | Overridden by `prompts/scientific/statistics/inference/bayesian_methods/skills.md` |
| `risk_based_monitoring_strategist` | `risk_based_monitoring_strategist` | Overridden by `prompts/clinical/clinical_operations/skills.md` |
| `samd_hazard_traceability_matrix_generator` | `samd_hazard_traceability_matrix_generator` | Overridden by `prompts/regulatory/quality/skills.md` |
| `samd_iec62304_software_architecture_architect` | `samd_iec62304_software_architecture_architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `samd_iec_62304_software_safety_classification_architect` | `samd_iec_62304_software_safety_classification_architect` | Overridden by `prompts/regulatory/quality/skills.md` |
| `semantic_mutation_censorship_evasion_modeler` | `semantic_mutation_censorship_evasion_modeler` | Overridden by `prompts/scientific/psychology/computational/network_contagion/skills.md` |
| `serre_spectral_sequence_calculator` | `serre_spectral_sequence_calculator` | Overridden by `prompts/scientific/mathematics/topology/algebraic_topology/skills.md` |
| `set_theoretic_forcing_architect` | `set_theoretic_forcing_architect` | Overridden by `prompts/scientific/mathematics/foundations/proof_theory/skills.md` |
| `shotgun_metagenomic_assembly_binning_architect` | `shotgun_metagenomic_assembly_binning_architect` | Overridden by `prompts/scientific/microbiology/metagenomics/skills.md` |
| `signal_detection_evaluator` | `signal_detection_evaluator` | Overridden by `prompts/clinical/pharmacovigilance/skills.md` |
| `signal_detection_theory_architect` | `signal_detection_theory_architect` | Overridden by `prompts/scientific/psychology/cognitive/information_processing/skills.md` |
| `single_cell_rna_seq_trajectory_inference_architect` | `single_cell_rna_seq_trajectory_inference_architect` | Overridden by `prompts/scientific/genetics/transcriptomics/skills.md` |
| `social_isolation_epidemiological_contagion_modeler` | `social_isolation_epidemiological_contagion_modeler` | Overridden by `prompts/scientific/psychology/epidemiology/global_mental_health/skills.md` |
| `spatial_metapopulation_seir_epidemiology_architect` | `spatial_metapopulation_seir_epidemiology_architect` | Overridden by `prompts/scientific/ecology/population_dynamics/skills.md` |
| `spatial_mismatch_employment_accessibility_modeler` | `spatial_mismatch_employment_accessibility_modeler` | Overridden by `prompts/scientific/sociology/stratification/systemic_inequality/skills.md` |
| `spatial_transcriptomics_cellular_communication_architect` | `spatial_transcriptomics_cellular_communication_architect` | Overridden by `prompts/scientific/genetics/transcriptomics/skills.md` |
| `spatio_temporal_geostatistical_spde_inla_architect` | `spatio_temporal_geostatistical_spde_inla_architect` | Overridden by `prompts/scientific/statistics/modeling/spatio_temporal_analysis/skills.md` |
| `staggered_difference_in_differences_architect` | `staggered_difference_in_differences_architect` | Overridden by `prompts/scientific/economics/econometrics/causal_inference/skills.md` |
| `stiff_pde_numerical_stability_architect` | `stiff_pde_numerical_stability_architect` | Overridden by `prompts/scientific/mathematics/numerical_methods/skills.md` |
| `stochastic_gene_regulatory_network_cme_architect` | `stochastic_gene_regulatory_network_cme_architect` | Overridden by `prompts/scientific/computational_biology/skills.md` |
| `stochastic_lotka_volterra_population_modeler` | `stochastic_lotka_volterra_population_modeler` | Overridden by `prompts/scientific/ecology/population_dynamics/skills.md` |
| `stochastic_market_entry_greenfield_architect` | `stochastic_market_entry_greenfield_architect` | Overridden by `prompts/business/strategy/skills.md` |
| `stochastic_multi_objective_optimization_architect` | `stochastic_multi_objective_optimization_architect` | Overridden by `prompts/scientific/applied_mathematics/optimization/operations_research/skills.md` |
| `stochastic_radicalization_cascade_modeler` | `stochastic_radicalization_cascade_modeler` | Overridden by `prompts/scientific/psychology/computational/network_contagion/skills.md` |
| `string_worldsheet_scattering_amplitude_architect` | `string_worldsheet_scattering_amplitude_architect` | Overridden by `prompts/scientific/physics/string_theory/skills.md` |
| `structural_equation_modeling_architect` | `structural_equation_modeling_architect` | Overridden by `prompts/scientific/psychology/quantitative/skills.md` |
| `structural_proof_theory_cut_elimination_architect` | `structural_proof_theory_cut_elimination_architect` | Overridden by `prompts/scientific/formal_logic/foundations/proof_theory/skills.md` |
| `structural_vector_autoregression_architect` | `structural_vector_autoregression_architect` | Overridden by `prompts/scientific/economics/econometrics/time_series/skills.md` |
| `symplectic_manifold_moment_map_architect` | `symplectic_manifold_moment_map_architect` | Overridden by `prompts/scientific/mathematics/geometry/differential/skills.md` |
| `synaptic_plasticity_weight_update_architect` | `synaptic_plasticity_weight_update_architect` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `synthetic_media_epistemic_collapse_modeler` | `synthetic_media_epistemic_collapse_modeler` | Overridden by `prompts/scientific/psychology/computational/network_contagion/skills.md` |
| `target_trial_emulation_architect` | `target_trial_emulation_architect` | Overridden by `prompts/scientific/statistics/inference/causal_inference/skills.md` |
| `theil_t_index_inequality_decomposer` | `theil_t_index_inequality_decomposer` | Overridden by `prompts/scientific/sociology/stratification/systemic_inequality/skills.md` |
| `top_down_proteomics_ptm_mapping_architect` | `top_down_proteomics_ptm_mapping_architect` | Overridden by `prompts/scientific/molecular/proteomics/skills.md` |
| `topos_theoretic_sheaf_semantics_evaluator` | `topos_theoretic_sheaf_semantics_evaluator` | Overridden by `prompts/scientific/mathematics/category_theory/skills.md` |
| `transactional_outbox_event_publishing_architect` | `transactional_outbox_event_publishing_architect` | Overridden by `prompts/technical/architecture/skills.md` |
| `transfinite_induction_well_ordering_architect` | `transfinite_induction_well_ordering_architect` | Overridden by `prompts/scientific/mathematics/foundations/set_theory/skills.md` |
| `turing_degree_reduction_evaluator` | `turing_degree_reduction_evaluator` | Overridden by `prompts/scientific/formal_logic/computability/recursion_theory/skills.md` |
| `ultraproduct_los_theorem_architect` | `ultraproduct_los_theorem_architect` | Overridden by `prompts/scientific/mathematics/foundations/model_theory/skills.md` |
| `variational_inference_architect` | `variational_inference_architect` | Overridden by `prompts/scientific/statistics/inference/bayesian_methods/skills.md` |
| `vine_copula_dependency_architect` | `vine_copula_dependency_architect` | Overridden by `prompts/scientific/statistics/modeling/multivariate_analysis/skills.md` |
| `wealth_concentration_decomposition_architect` | `wealth_concentration_decomposition_architect` | Overridden by `prompts/scientific/sociology/stratification/systemic_inequality/skills.md` |
| `whole_brain_biophysical_network_simulator` | `whole_brain_biophysical_network_simulator` | Overridden by `prompts/scientific/computational_theoretical_neuroscience/skills.md` |
| `zero_based_budgeting_turnaround_architect` | `zero_based_budgeting_turnaround_architect` | Overridden by `prompts/business/strategy/skills.md` |
