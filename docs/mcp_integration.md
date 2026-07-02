# Agent Integration via Model Context Protocol (MCP)

This guide explains how to connect the Proompts repository to your local AI agents (such as Claude Desktop) using the Model Context Protocol (MCP). By configuring the internal MCP server, you can dynamically expose the prompt library as actionable tools for your agent.

## Prerequisites

Before configuring the MCP server, ensure your local environment meets the following technical requirements:

- **Python Version:** Python 3.10 or higher
- **Required Libraries:**
  - `mcp` (>= 1.27.2)
  - `watchdog` (>= 6.0.0)
  - `jsonschema` (>= 4.26.0)
  - `promptops` (internal toolkit)

*Note: All dependencies are installed automatically when you run `pip install -r requirements.txt` in an active virtual environment.*

## Configuring Claude Desktop

The repository includes a dedicated CLI utility to generate the necessary configuration for Claude Desktop. This utility handles platform-specific pathing and sets up the server command automatically.

### Step-by-Step Walkthrough

1. **Initialize Your Environment:**
   Ensure your virtual environment is active and dependencies are installed.
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Generate the Configuration JSON:**
   Run the `promptops` agent config command to generate the required JSON structure for Claude Desktop. 
   ```bash
   promptops agent config --dir prompts
   ```

3. **Update Claude Desktop Config:**
   Copy the output JSON and paste it into your Claude Desktop configuration file.
   - **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

4. **Restart Claude Desktop:**
   Restart the Claude Desktop application to establish the connection with the newly configured MCP server.

## Auditing Tools with Discovery CLI

The prompt library uses naming conventions and `skills.md` manifests to dynamically map prompt files to tool names. Because these mappings can truncate long names or override them via manifests, you can audit the current state of your tools using the discovery command.

### Running the Discovery Report

To see exactly which prompts are exposed and how their tool names are generated, run:

```bash
promptops agent discovery --dir prompts
```

This will output a comprehensive report showing:
- **Tool Name Transformations:** Details on how original prompt names were reformatted or truncated to comply with tool naming rules.
- **Overridden Tools:** Identifies which prompts are being overridden by custom instructions defined in `skills.md` files.

## Server Implementation Details

For developers looking to understand or modify the underlying server, the MCP server is implemented in [`mcp_server.py`](../mcp_server.py) at the root of the repository. It uses `watchdog` to monitor the `prompts/` directory for live changes and automatically notifies the client when tools are updated.


<!-- TOOL_REGISTRY_START -->
## Available Tools

### Workflows

| Tool Name | Description | Inputs |
|-----------|-------------|--------|
| `Adjudication_Workflow` | A workflow to design an adjudication dashboard, create a source document checklist, and analyze adju | `charter_excerpt, adjudication_log_csv` |
| `Agentic_Coding_From_Idea_to_Epics` | A workflow that takes a product concept, generates a product brief, and then creates project epics f | `product_concept` |
| `BioSkills_Workflow` | A workflow for coaching, feedback, and assessment of bioskills. | `procedure_name, procedure_notes` |
| `Biological_Safety_Assessment_and_Planning` | A workflow to perform a risk assessment for a medical device, develop a biological safety plan, and  | `medical_device_type` |
| `CFO_Workflow` | A workflow for financial forecasting, competitive bid pricing, and regulatory risk assessment. | `base_revenue, base_costs, starting_cash, notes, competitor_bids, internal_cost, target_margin, volume_adjustments, study_portfolio, reg_updates, esg_baseline, risk_tolerance` |
| `CRA_Workflow` | A workflow for generating a monitoring visit report, tracking investigator follow-up emails, and bui | `visit_info, pending_actions, study_info` |
| `Chemical_Characterization_and_Biocompatibility_Assessment` | A workflow to design a chemical characterization study, assess the risks from the results, and write | `device_description, body_weight_kg, device_dose_ug_day` |
| `Clinical_Data_Workflow` | A workflow for detecting discrepancies, drafting a DMP section, and building edit check specificatio | `edc_export_csv, dmp_section_requirements, edit_check_rules` |
| `Clinical_ETL_Pipeline_Design_and_Review` | A workflow to create an ETL mapping spec, define QC transformations, and review the final pipeline.  | `etl_requirements` |
| `Clinical_Monitoring_Workflow` | A workflow for creating a site performance dashboard, building a CAPA plan, and critiquing a monitor | `site_performance_data, monitoring_findings, mvr_report` |
| `Clinical_Prompts_Workflow` | A workflow to generate a CRF shell, audit it, and create a CDASH mapping guide. | `protocol_summary, variable_list` |
| `Clinical_Safety_Workflow` | A workflow for creating a clinical safety synopsis, an adverse event narrative, and trending safety  | `surveillance_data, adverse_event_data, post_market_data` |
| `Compassionate_Music_Therapy_Workflow` | A 4-step workflow to deconstruct venting, plan a therapeutic arc, compose a musical blueprint, and w | `venting_text` |
| `Imaging_Workflow` | A workflow for various imaging-related tasks, including charter drafting, QC, central reading design | `charter_draft_protocol_synopsis, charter_draft_modalities, charter_draft_endpoints, charter_draft_sites, charter_draft_regulations, upload_log_csv, central_reading_disease, central_reading_timepoints, central_reading_endpoints, central_reading_reader_pool_size, central_reading_budget, reg_charter_study_overview, reg_charter_modalities, reg_charter_regions, reg_charter_endpoint_description, qc_workflow_study_description, qc_workflow_modalities, data_package_study_summary, data_package_metrics_data, data_package_reader_agreement` |
| `Learning_and_Development_Workflow` | A workflow for creating a competency-based onboarding blueprint, a scenario-based microlearning seri | `existing_modules, audience_role, analysis_goal` |
| `Market_Research_Workflow` | A workflow for market landscape analysis, user needs assessment, barrier mapping, and executive summ | `device_or_assay, application, device, markets, market_report` |
| `Meta-Prompt_Chain_L1_-_L2_-_L3_-_L4` | A workflow that implements the full meta-prompt generative chain. | `end_task, policy_block, token_budget_l3, token_limit_l4, task_description, input_block, output_schema` |
| `Microbiology_Workflow` | A workflow for creating a bioburden testing SOP, an EO sterilization validation protocol, and an end | `device_description, device_name` |
| `Preclinical_Pathology_Study_Workflow` | A workflow to design a pathology study protocol, evaluate the device-tissue interface, and plan the  | `study_details` |
| `Principal_Architect_Workflow_PAW` | A state-machine workflow for disciplined software engineering tasks, enforcing Design, Refactor, Imp | `todo_content, file_structure, relevant_source_code` |
| `Project_Management_Workflow` | A workflow to create a project charter, risk register, status report, and timeline. | `project_name, project_description, budget, deadline, stakeholders, business_outcome, update_notes, project_type, objectives, milestone_data` |
| `Protocol_Workflow` | A workflow to create, review, and refine a clinical trial protocol. | `summary_sheet, process_information, condition, draft_section` |
| `Protocol_to_USDM_Workflow` | A 5-stage chain to convert unstructured Clinical Protocol text into CDISC USDM v3.0 JSON. | `protocol_text, protocol_objectives_text, protocol_soa_text` |
| `RTSM_Workflow` | A workflow for designing a randomization scheme, a supply strategy, and a risk-based monitoring SOP. | `study_parameters, trial_enrollment, existing_sop` |
| `Site_Acquisition_Workflow` | A workflow for site landscape mapping, feasibility questionnaire building, and investigator outreach | `protocol_summary, investigator_name, site_name, city_country, recent_relevant_trials, unique_site_strength, study_synopsis, sponsor_name` |
| `Sterility_Workflow` | A workflow for building a sterility validation protocol, comparing regulatory gaps, and performing a | `device_description, process_description` |
| `Stochastic_Model_Chain_Architect_-_Engineer_-_Strategist` | A three-stage workflow to model, simulate, and analyze conversation risks using Game Theory and Mont | `conversation_scenario` |
| `Study_Director_Workflow` | A workflow for drafting a GLP-compliant study protocol, auditing raw data, and generating an executi | `protocol_basics, data_csv, report_sections` |
| `Technical_Writer_Workflow` | A workflow for drafting a CSR results and safety section, an Investigator's Brochure summary of chan | `study_context, sponsor_requirements` |
| `Testing_Workflow` | A workflow for end-to-end test discovery, design verification, human factors validation, and risk-ba | `project_name, languages_frameworks, business_goal, device_name, device_class, hazard_analysis_table` |
| `VP_Statistics_Workflow` | A workflow for creating an interim results executive brief, a statistical analysis plan, and a data  | `analysis_results, statistical_plan, safety_listings, protocol_synopsis, raw_eds_dump, query_log` |
| `eClinical_Integration_Workflow` | A workflow for architecting an integration blueprint, creating a data mapping playbook, and compilin | `integration_description, mapping_requirements, validation_info` |
| `ePRO_Workflow` | A workflow for designing a patient-centric BYOD workflow, optimizing ePRO form design, and creating  | `byod_requirements, form_details, rollout_details` |

### Prompts

| Tool Name | Description | Inputs |
|-----------|-------------|--------|

### Skills

| Tool Name | Description | Inputs |
|-----------|-------------|--------|
| `21_CFR_820_QMSR_Gap-Analysis_Remediation` | Evaluate the quality-management system against current 21 CFR 820 and the proposed QMSR. | `device_class, employee_count, qms_documents` |
| `21_CFR_Part_11_Compliance_Verification` | Confirm system compliance with electronic signatures. | `system_features` |
| `21_CFR_Part_14_Auditing` | Audit advisory committee meeting minutes for compliance with record-keeping elements. | `input` |
| `360_Operational_KPI_Benchmark_Review` | Compare internal KPIs to industry benchmarks and propose improvements. | `kpi_csv` |
| `3D_QSAR_Pharmacophore_Modeling_Architect` | Generates expert-level 3D Quantitative Structure-Activity Relationship (QSAR) models and pharmacopho | `input_compounds, target_macromolecule, target_property` |
| `510_k_De_Novo_Pre-Submission_Strategy` | Determine the best U.S. regulatory pathway and craft a 12‑month pre‑submission plan. | `device_description, predicate_devices` |
| `510_k_Substantial_Equivalence_Preparation` | Draft a substantial equivalence comparison and summary between a subject device and predicate(s) to  | `input` |
| `80_20_Crash_Course` | Teach me the essentials of [SUBJECT] using the Pareto Principle: | `input, macros, subject` |
| `90-Day_Biostatistics_Onboarding_Plan` | Design a structured program to move new statisticians from orientation to productive project work in | `cohort_size, therapeutic_focus` |
| `90-Day_Pipeline_Health_Next-Best-Action_Review` | Assess the health of the sales pipeline and recommend next-best actions. | `crm_csv, crm_data, macros` |
| `ADM_3_1_Decomposition_Architect` | Systematically derives and formulates the Arnowitt-Deser-Misner (ADM) 3+1 decomposition of spacetime | `metric_ansatz, matter_energy_momentum_tensor, lapse_and_shift_conditions` |
| `ADaM_ADLB_NCI-CTCAE_and_Hy_s_Law_Toxicity_Architect` | Automates the rigorous algorithmic derivation of NCI-CTCAE toxicity grades, complex baseline flaggin | `sdtm_lb_data, adsl_data, protocol_toxicity_criteria, constraints, instructions, persona` |
| `ADaM_ADRS_RECIST_Derivation_Architect` | Automates the complex derivation of oncology RECIST 1.1 criteria for the ADaM ADRS (Tumor Response)  | `sdtm_tu_data, sdtm_tr_data, recist_version` |
| `ADaM_ADTTE_Oncology_Censoring_Rules_Architect` | Automates the complex derivation of oncology Time-to-Event (TTE) endpoints (e.g., Progression-Free S | `adsl_data, adrs_data, endpoint_type, protocol_censoring_rules, constraints, instructions, persona` |
| `ADaM_ADTTE_Time_to_Event_Derivation_Architect` | Automates the complex algorithmic derivation of Time-to-Event (ADTTE) analysis datasets for oncology | `source_sdtm_data, survival_endpoint_definition, target_adam_version, constraints, instructions, persona` |
| `ADaM_Derivation_Writer` | Translates SAS/R programming logic into plain-English derivation descriptions for CDISC define.xml d | `programming_logic` |
| `AGENTS_md_Checklist_Generator` | Create a best-practice checklist for writing an AGENTS.md file and provide a meta‑prompt to generate | `repo_url` |
| `AI-Enhanced_RBM_Action_Plan` | Generate next-week monitoring actions that optimize patient safety and data quality. | `site_metrics` |
| `AI-Powered_Site_and_Recruitment_Strategy` | Select optimal sites and anticipate dropout risks using simulated EHR insights. | `criteria, target_enrollment` |
| `AI_Coding_Agent_Plan_Generator` | Provide a structured plan for completing a coding task in an existing repository. | `repo_access, task_description` |
| `AI_Email_Assistant_Go_No-Go_Vote` | Personas: UX designer, data scientist, CFO. Objective: decide whether to move forward with the proto | `input, macros, user_input` |
| `AI_ML_Predetermined_Change_Control_Plan_Architect` | Formulates a rigorous AI/ML Predetermined Change Control Plan (PCCP) for continuous learning algorit | `algorithm_description, proposed_changes, performance_metrics` |
| `AI_Model_Inference_Serving_Architect` | Designs highly scalable, low-latency, and cost-efficient architecture topologies for serving large-s | `model_characteristics, workload_profile, infrastructure_constraints, user_query` |
| `AI_Risk_Mapper` | Create a quick-look risk register for a specified AI system. | `AI_SYSTEM` |
| `ALCOA-C_Data_Integrity_Checklist` | Ensure data integrity following ALCOA-C principles. | `site_role, system_type` |
| `API_Gateway_and_BFF_Architect` | Designs highly scalable, secure, and performant API Gateway and Backend-for-Frontend (BFF) architect | `client_ecosystem, backend_services, non_functional_requirements` |
| `API_Management_and_Developer_Portal_Architect` | Designs highly secure, multi-tenant API Management lifecycles and scalable Developer Portal architec | `api_topology, security_governance, developer_experience` |
| `API_Security_Zero_Trust_Architect` | Formulates mathematically rigorous and cryptographically sound API Security and Zero Trust network a | `api_architecture_description, security_compliance_requirements, architecture_description, compliance_requirements` |
| `APT_Threat_Hunting_Hypothesis_Generation_Architect` | Acts as a Cybersecurity Genesis Architect to engineer rigorous, intelligence-driven threat hunting h | `threat_actor, target_environment, intelligence_feed_summary` |
| `APT_Threat_Hunting_Query_Engineer` | Translates high-level Advanced Persistent Threat (APT) TTPs into precise, actionable SIEM queries fo | `apt_ttp_description, target_siem_platform, log_sources, macros, user_query` |
| `AWS_Lambda_Serverless_Persistence_Forensics_Analyst` | Generates expert-level forensic analysis and response strategies for detecting, reconstructing, and  | `cloudtrail_logs, lambda_telemetry, function_configuration, macros` |
| `Abbreviated_New_Drug_Application_ANDA_Architect` | Formulates rigorous, compliant FDA Abbreviated New Drug Application (ANDA) eCTD submissions for gene | `generic_drug_name, reference_listed_drug, bioequivalence_summary, q1_q2_formulation_details` |
| `Accelerate_Patient_Recruitment_Retention` | Develop a high-impact recruitment and retention strategy for a stalling clinical trial. | `study_phase, therapeutic_area, target_enrollment, num_sites, timeline_months, budget, pain_points, study_details` |
| `Action-Oriented_Meeting_Minutes_Tracker` | Capture decisions and action items from cross-functional meetings. | `meeting_transcript` |
| `Active_Directory_Domain_Dominance_Forensics_Analyst` | Generates expert-level forensic analysis and threat hunting strategies for identifying advanced Acti | `network_telemetry, endpoint_artifacts, identity_posture` |
| `Activist_Investor_Defense_Strategy_Architect` | Architects rigorous, actionable activist investor defense strategies, conducting vulnerability asses | `current_vulnerabilities, financial_baseline, activist_profile` |
| `Adaptive_Control_Loop_Tuning_Architect` | Formulates mathematically rigorous adaptive control loop tuning algorithms for highly noisy, non-sta | `PLANT_DYNAMICS, DISTURBANCE_PROFILE, PERFORMANCE_OBJECTIVES, disturbance_profile, performance_objectives, plant_dynamics` |
| `Adaptive_Design_Interim_Monitoring` | Provide guidance on adaptive trial design and interim monitoring strategies. | `trial_details` |
| `Adaptive_Load_Shedding_and_Backpressure_Architect` | Designs highly resilient, adaptive load shedding and backpressure mechanisms for distributed systems | `traffic_profile, downstream_dependencies, business_criticality_tiers, user_query` |
| `Adaptive_Recruitment_and_Retention_Strategy` | Design an optimized recruitment and retention plan for a multi-site pivotal study. | `device_or_ivd, patient_population` |
| `Advanced_C2_Beacon_PCAP_Analysis_Engineer` | Systematically reverse-engineers and analyzes network packet captures (PCAP) to identify, decode, an | `pcap_summary, beaconing_characteristics` |
| `Advanced_Design_Patterns_Fluent_Interface` | Extend Page Objects with method chaining to create a more readable test API. | `java_class` |
| `Advanced_Python_Testing` | A comprehensive guide to Python testing, covering Pytest fixtures, Property-Based Testing (Hypothesi | `input` |
| `Advanced_Red_Team_Adversary_Emulation_Architect` | Generates highly rigorous, tactically sound, and evasive adversary emulation campaigns based on spec | `threat_actor_profile, target_environment_architecture, emulation_objectives, macros, unsafe_input` |
| `Advanced_SOAR_Playbook_Engineering_Architect` | Formulates precise, highly complex, and automated Security Orchestration, Automation, and Response ( | `incident_type, environment_stack, operational_constraints` |
| `Advanced_Sigma_Rule_Detection_Architect` | Architects robust, highly-optimized, cross-platform Sigma detection rules tailored for uncovering co | `threat_behavior, targeted_log_sources, environmental_tuning` |
| `Advanced_Volatile_Memory_Forensics_Analyst` | Generates highly technical, precise volatile memory forensic analysis workflows and advanced rootkit | `os_architecture, suspected_malware_family, intrusion_context` |
| `Adversarial_Prompt_Robustness_Tester` | Acts as a Principal AI Red Teamer to systematically stress-test draft prompts against adversarial in | `draft_prompt, threat_model` |
| `Agent_Persona_Generator` | Generate detailed, high-integrity agent personas based on a provided role and goal, using a strict s | `context, goal, role, TEST_COMMAND` |
| `Air-Gapped_Environment_Deployment_Architect` | Designs secure, resilient, and fully autonomous software deployment architectures for highly restric | `deployment_artifacts, security_constraints, operational_scale, user_query` |
| `Algorithmic_Dynamic_Pricing_Yield_Management_Architect` | Designs rigorous algorithmic dynamic pricing and yield management strategies to optimize revenue max | `capacity_constraints, demand_stochasticity, pricing_objective` |
| `Algorithmic_Multi-Touch_Attribution_Architect` | Constructs highly rigorous, algorithmic multi-touch attribution (MTA) models using Markov chains and | `user_journey_data, channel_costs, business_constraints` |
| `Analyze_Adjudication_KPIs` | Calculate adjudication performance metrics and recommend improvements. | `adjudication_log` |
| `Applied_Ethical_Stress_Tester` | Systematically stress-tests complex ethical dilemmas and applied scenarios using Kantian and Utilita | `ethical_dilemma` |
| `Architect_the_Integration_Blueprint` | Provide a structured plan for integrating site EHR systems with the sponsor's EDC and CTMS. | `input` |
| `Architecture_Design_Page_Object_Model` | Implement the Page Object Model pattern to separate UI locators from test logic. | `html_source` |
| `Architecture_Flow_Diagram_Architect` | A Principal System Architect's guide to tracing request lifecycles, identifying bottlenecks, and gen | `input, context, entry_point` |
| `Atlas_Documentation_Specialist` | A comprehensive system prompt tailored for a documentation and visualization specialist named "Atlas | `input` |
| `Audit_Raw_Data_and_Draft_a_CAPA_Summary` | Review study data for deviations and produce a corrective-action plan. | `data_csv` |
| `Audit_Trail_Review` | Review subject audit logs for compliance and data integrity. | `audit_logs, system_specs` |
| `Automated_E-Discovery_Reviewer` | Automates the first-pass review of legal documents for relevance, privilege, and key entity extracti | `document_text, matter_description, responsive_issues` |
| `Automated_Financial_Variance_Analyst` | Automates the cognitive labor of a corporate financial analyst by systematically processing variance | `financial_data, float, integer, macros, string` |
| `Automated_Image_Assessment_System_510_k` | Draft a detailed device description for an automated image assessment system for microbial colonies. | `input` |
| `Autonomous_Automation_Agent` | A Principal DevOps Automation Engineer persona that executes a fully autonomous repository commit an | `workspace_state` |
| `Autonomous_Automation_Agent_Upgrade` | Executes a fully autonomous repository commit and generates a pull request based on the current work | `None` |
| `Autonomous_Vehicle_V2X_Telemetry_Architect` | Designs highly resilient, low-latency edge-to-cloud telemetry and V2X (Vehicle-to-Everything) commun | `fleet_sensor_profile, network_intermittency_model, latency_critical_thresholds, user_query` |
| `BRST_Quantization_and_Faddeev-Popov_Ghost_Architect` | Formulates the rigorous BRST quantization of gauge theories, extracting the complete effective Lagra | `classical_action, gauge_transformation, gauge_fixing_condition, user_query` |
| `Bioburden_Testing_SOP` | Draft a standard operating procedure for bioburden enumeration compliant with ISO 11737‑1:2018. | `device_description, macros` |
| `Biological_Evaluation_Plan_Builder` | Draft a complete Biological Evaluation Plan (BEP) for a specified medical device. | `device_details` |
| `Biological_Safety_Plan_Developer` | Create a biological safety plan for the preclinical phase of a new medical device. | `device_description` |
| `Biologics_License_Application_BLA_Architect` | Formulates rigorous, compliant FDA Biologics License Application (BLA) eCTD submissions for biologic | `product_type, intended_indication, clinical_phase, manufacturing_summary` |
| `Black_Hole_Perturbation_Teukolsky_Architect` | Systematically derives the Teukolsky master equation for gravitational, electromagnetic, and scalar  | `background_metric, perturbation_spin_weight, coordinate_system, user_input` |
| `Board_Deck_Narrative_Generation` | Draft the 'CFO Commentary' slide for a Board meeting. | `context, macros` |
| `Breakthrough_Device_Designation_Architect` | Formulates compelling FDA Breakthrough Device Designation (BDD) requests based on statutory criteria | `device_description, proposed_indications_for_use, target_disease_condition, standard_of_care_shortcomings, clinical_evidence_summary` |
| `Budget_Variance_Analysis` | Identify top variances in a budget-to-actuals report and draft explanations for the Board. | `report` |
| `Bug_Finder_Fixer_OpenAI_Codex` | Reproduce and resolve a bug within the specified package or module. | `input, package_path, bug_report, context, module` |
| `Build_an_Audit-Ready_Site-Payment_Schedule` | Generate a transparent investigator payment schedule that withstands audit review. | `cta_budget, fmv_benchmarks, fx_table, visit_grid` |
| `Build_vs_Buy_Decision_Matrix` | Create a weighted decision matrix for evaluating build vs. buy options. | `function, team_capacity, vendor` |
| `CAPA_Investigation_Report_Writer` | Draft a formal CAPA investigation report for regulatory review. | `actions_taken, effectiveness_check, incident_summary, root_cause` |
| `CAPA_Management_Process` | Identify non-compliance, conduct RCA, and track CAPA. | `deviation_log` |
| `CAPA_Plan_Builder_for_Monitoring_Findings` | You are a **Regulatory Quality Advisor** specializing in ICH-GCP compliance. | `input` |
| `CAPA_Plan_Generator` | Generate a Corrective and Preventive Action (CAPA) plan based on audit findings. | `audit_findings` |
| `CAPA_Root_Cause_Investigator` | Deep-dive Root Cause Analysis (RCA) using Fishbone and 5 Whys methods. | `problem_description` |
| `CAPA_Root_Cause_and_Resolution_Architect` | A highly analytical operational architect designed to perform rigorous Corrective and Preventive Act | `incident_report, quality_standard` |
| `CAPA_SOP_Architect` | Establish a comprehensive CAPA SOP compliant with ISO 9001 and ISO 13485. | `company_context` |
| `CDASH_Alignment` | Standardize clinical data collection fields using CDASH models. | `cdash_guide, crf_draft` |
| `CDASH_Mapping_Completion-Guide_Assistant` | - For every variable in the list, supply: | `input` |
| `CDISC_CRF_Architect` | Design CDASH/SDTM compliant CRFs from a Clinical Protocol. | `protocol_text` |
| `CDISC_Cross-Dataset_Relational_Architect` | Automates the complex algorithmic mapping and harmonization of relational data across CDISC SDTM dom | `primary_domain_data, secondary_domain_data, target_sdtm_version, constraints, instructions, persona` |
| `CDISC_SDTM_ADaM_Mapping` | Map raw clinical data to standardized CDISC SDTM and ADaM domains. | `curation_guidelines, metadata_defs, metadata_rules, raw_data` |
| `CI_CD_Pipeline_Poisoning_Forensics_Architect` | Conducts rigorous forensic analysis of compromised CI/CD pipelines to detect advanced pipeline poiso | `pipeline_configuration, execution_logs, incident_indicators` |
| `CQRS_and_Event_Sourcing_Architect` | Designs highly scalable Command Query Responsibility Segregation (CQRS) and Event Sourcing architect | `system_requirements, input` |
| `CRF_Quality_Auditor` | - Evaluate against CDISC CDASH IG v2.1 and SDTM traceability. | `input` |
| `CRF_Shell_Generator` | - Read the protocol summary. | `input, macros, protocol_summary` |
| `CRO_Trial-Performance_KPI_Dashboard_Blueprint` | Outline metrics and visuals for a CRO trial-performance dashboard. | `portfolio_summary` |
| `CSM_Portfolio_Balancing` | Propose a weighted scoring model to balance account loads among CSMs. | `csm_data` |
| `CSR_Plain_Language_Summary_Generator` | Generates a Plain Language Summary (PLS) from a Clinical Study Report (CSR) following EU CTR 536/201 | `csr_data` |
| `CSR_Results_and_Safety_Section` | Draft Sections 11 and 12 of an ICH E3 clinical study report. | `None` |
| `CTD_Module_2_5_Clinical_Overview_Architect` | Acts as a Principal Regulatory Medical Writer to synthesize complex clinical data (biopharmaceutics, | `clinical_data_summary, target_indication, product_information` |
| `Cache_Stampede_Mitigation_Architect` | Designs highly resilient distributed caching architectures specifically to mitigate and recover from | `system_scale, caching_infrastructure, data_characteristics, user_query` |
| `Callan-Symanzik_Beta_Function_Architect` | Derives Callan-Symanzik equations, calculates beta functions at one-loop order, and analyzes renorma | `lagrangian_density, regularization_scheme, coupling_constant, user_input` |
| `Career_Compass_Advisor` | Map the user's next career move and provide a concise action plan. | `background` |
| `Carrier_Screening_System_510_k` | Compile technical information for an autosomal recessive carrier screening gene mutation detection s | `input` |
| `Cascading_Failure_Resilience_Architect` | Architects system-wide resilience patterns to mitigate cascading failures, including circuit breakin | `system_topology, failure_scenarios, configuration, macros, safety_instruction, scenarios, topology` |
| `Causal_Discovery_DAG_Architect` | Designs highly robust causal discovery workflows and Structural Causal Models (SCMs) for high-dimens | `data_characteristics, domain_knowledge, modeling_goals` |
| `Cell-Based_Architecture_Designer` | Architects robust, hyper-scalable, and blast-radius-contained distributed systems using advanced Cel | `system_scale_requirements, availability_targets, traffic_patterns, user_query` |
| `Central_Reading_Paradigm_Design` | Recommend an efficient central reading model for an oncology trial. | `budget, disease, endpoints, reader_pool_size, timepoints` |
| `Change_Control_Regulatory_Impact_Assessor` | Perform rigorous regulatory impact assessments for proposed medical device changes using FDA guidanc | `device_description, proposed_change, intended_use` |
| `Change_Data_Capture_Pipeline_Architect` | Designs highly reliable, low-latency Change Data Capture (CDC) pipelines for log-based database repl | `source_system, target_scale` |
| `Chaos_Engineering_Experiment_Designer` | Designs targeted chaos engineering experiments to uncover systemic weaknesses in distributed archite | `target_architecture, macros` |
| `Chaos_Engineering_Resilience_Architect` | Designs rigorous chaos engineering experiments and fault injection protocols to empirically validate | `system_architecture, steady_state_metrics, failure_hypotheses` |
| `Chemical_Characterization_TRA_Work_Plan` | Create a work plan for chemical characterization and toxicological risk assessment (TRA) for a medic | `device_information` |
| `Chiral_Anomaly_Fujikawa_Path_Integral_Architect` | Formulates the rigorous derivation of chiral anomalies using Fujikawa's path integral measure evalua | `gauge_group, fermion_representation, spacetime_dimension, user_query` |
| `Citizen_Petition_Preparation` | Draft a Citizen Petition requesting administrative action by the Commissioner. | `input` |
| `Civil_Money_Penalties_Hearing_Response` | Draft a formal 'Answer' to an FDA complaint seeking civil money penalties. | `input` |
| `Cleaning_Validation_Protocol_Architect` | Formulates highly rigorous, FDA and EMA compliant Cleaning Validation Protocols for pharmaceutical a | `equipment_description, previous_product, next_product, cleaning_procedure, sampling_methodology, input_variable, macros` |
| `ClinRO_User_Manual_Generator` | Draft a standardized user manual for ClinRO administration and training. | `clinro_name, measurement_type, requirements, clinro_instrument, specific_requirements` |
| `Clinical-Trial_Budget_and_Burn-Rate_Dashboard` | Produce a month-end dashboard comparing planned versus actual spend and forecasting when budgets wil | `invoices, milestones, planned_budget, staffing_hours` |
| `Clinical-Trial_Protocol_Creator` | Generate a full clinical-trial protocol from a one-page summary sheet. | `summary_sheet` |
| `Clinical-Trial_Timeline_and_Risk_Radar` | Evaluate study schedule variance and prioritize mitigation actions. | `csv_data` |
| `ClinicalTrials_gov_Registration` | Draft registration summary and outcome measures. | `protocol_final` |
| `Clinical_Chemistry_Device_Classification` | Identify classification and regulatory requirements (general/special controls) for a clinical chemis | `input` |
| `Clinical_ETL_Mapping_Spec` | Create an ETL mapping specification for clinical data. | `etl_requirements` |
| `Clinical_ETL_Pipeline_Review` | Review the clinical ETL pipeline for accuracy and efficiency. | `etl_qc_plan` |
| `Clinical_ETL_Transformation_QC` | Define quality checks for clinical ETL transformations. | `etl_mapping_spec` |
| `Clinical_Monitoring_Plan_Development` | Draft a risk-based Clinical Monitoring Plan. | `trial_details` |
| `Clinical_Safety_Synopsis_for_EU_MDR_CER` | Provide a concise clinical safety synopsis for the EU MDR Clinical Evaluation Report. | `input, macros, user_input` |
| `Clinical_Study_Report_CSR_Narrative_Drafter` | Automate the drafting of patient narratives for Clinical Study Reports (CSRs) by transforming clinic | `patient_data` |
| `Clinical_Study_Report_CSR_Writing` | Draft Clinical Study Report sections. | `statistical_outputs` |
| `Clinical_Trial_Agreement_CTA_Negotiation` | Review CTA for missing clauses. | `cta_draft` |
| `Clinical_Trial_Document_Archiving` | Develop archival strategy for TMF. | `tmf_details` |
| `Clinical_Trial_Protocol_Compliance_Review` | Evaluate a draft protocol for quality and regulatory compliance. | `protocol_text` |
| `Clinical_Trial_Protocol_Synopsis_Architect` | Synthesizes a comprehensive, regulatory-compliant Clinical Trial Protocol Synopsis from raw study de | `study_parameters, macros` |
| `Cloud_IAM_Least-Privilege_Remediation_Architect` | Analyzes overly permissive cloud Identity and Access Management (IAM) configurations and generates p | `current_iam_policy, architecture_context` |
| `Cloud_Identity_Fabric_Threat_Hunting_Architect` | Architects advanced, high-fidelity threat hunting strategies targeting multi-cloud identity fabrics, | `identity_provider_telemetry, target_threat_actor_profile, multi_cloud_fabric_constraints, user_query` |
| `Cloud_Incident_Response_Forensics_Architect` | Generates highly technical, cloud-native (AWS/Azure/GCP) incident response playbooks and forensic ev | `cloud_environment, incident_indicators, critical_assets, macros` |
| `Code_Formatting_Linting_and_Refactoring_Implementation` | Improve the codebase's internal quality and consistency by introducing and configuring a standard co | `None` |
| `Code_Review_Assistant_Aegis_Security` | Conduct a comprehensive security-focused code review, identifying vulnerabilities, logic flaws, and  | `input, context, diff, thinking` |
| `Codebase_Quality_Maintainability_Analysis` | Conduct a deep analysis of the codebase's quality and maintainability to identify key areas for refa | `target_codebase_context, codebase_context` |
| `Codebase_Testing_Plan` | As a Distinguished Quality Engineer, generate a comprehensive testing strategy and implementation ro | `input, macros, project_context` |
| `Coding_Session_Guidelines` | Provide step-by-step guidance for running productive coding sessions. | `None` |
| `Coleman-Weinberg_Effective_Potential_Architect` | Formulates the rigorous derivation of the one-loop Coleman-Weinberg effective potential, demonstrati | `classical_potential, field_content, renormalization_condition, user_query` |
| `Combination_Product_Jurisdiction` | Prepare a Request for Designation (RFD) to identify primary FDA jurisdiction. | `input` |
| `Compassionate_Analyst` | Deconstructs user venting into actionable psychological data. | `venting_text` |
| `Compassionate_Music_Therapist_Composer` | AI Music Therapist using ISO Principle to transmute emotions into song. | `input, macros, user_input` |
| `Competency-Based_Onboarding_Blueprint` | Create an onboarding program that reduces time to independent monitoring to six weeks or less. | `existing_modules` |
| `Competitive-Bid_Pricing_Margin_Optimizer` | Compare competitor bids and internal costs to recommend a winning price with target margin. | `competitor_bids, internal_cost, target_margin, volume_adjustments` |
| `Competitor-Positioning_Brief` | Provide a competitor comparison to highlight differentiators for an upcoming board review. | `public_sources, macros` |
| `Compliance_Gap_Assessment` | Evaluate organizational controls against a specified compliance framework and prioritize remediation | `EMPLOYEES, FRAMEWORK, RISK_APPETITE, controls, evidence_logs` |
| `Compliance_Gap_Risk_Matrix` | Quantify compliance gaps and associated risks against a selected standard or law. | `known_nonconformities, sops` |
| `Compliance_and_Data_Quality_Monitoring_Plan` | Design an AI-assisted monitoring plan to ensure compliance and data integrity. | `None` |
| `Comprehensive_Biocompatibility_Test_Matrix` | Generate a detailed biocompatibility test matrix for a medical device. | `device_materials` |
| `Comprehensive_Risk_Register_and_Mitigation_Plan` | Produce a risk register with mitigation actions and overall strategies. | `project_overview` |
| `Comprehensive_Task_Template` | Provide a reusable prompt that guides an AI through planning, execution and self-checking for any co | `expert_role, task` |
| `Computer_System_Validation_CSV` | Generate validation documents for EDC systems. | `system_requirements` |
| `Concept_Drift_Mitigation_Architect` | Designs robust automated concept drift detection and mitigation pipelines for continuous machine lea | `model_characteristics, data_characteristics, business_constraints` |
| `Confidential_Computing_Enclave_Architect` | Architects highly secure Trusted Execution Environments (TEEs) and confidential computing solutions  | `requirements, Aegis, macros` |
| `Content_Validity_Reliability_Analysis` | Analyze clinician interview transcripts for content validity and plan inter-rater reliability. | `clinro_description, disease, interview_data, clinro_instrument_description, target_disease` |
| `Continuous_Integration_Delivery_DevOps_Architect` | Design and implement secure, efficient, and scalable CI/CD pipelines for AI-integrated applications. | `input, macros, project_requirements` |
| `Controlled_Terminology_Harmonizer` | Standardizes a list of values (e.g., Units) to CDISC Controlled Terminology (NCI Preferred Terms). | `value_list, macros` |
| `Conversation_Stochastic_Modeler` | Maps human-to-human or human-to-AI interactions into a mathematical framework to predict outcomes an | `input, conversation_transcript, macros` |
| `Corporate_Capital_Budgeting_Investment_Appraisal_Architect` | Architects robust, quantitative capital budgeting frameworks using NPV, IRR, and WACC to rigorously  | `investment_opportunity, cash_flow_projections, capital_structure` |
| `Corporate_Capital_Structure_Optimization_Architect` | Architects rigorous corporate capital structure optimization strategies, conducting zero-based budge | `financial_distress_indicators, capital_allocation_inefficiencies, target_leverage_ratios` |
| `Corporate_Digital_Transformation_ROI_Architect` | Architects rigorous enterprise digital transformation roadmaps, modeling technology ROI, capability  | `legacy_technology_debt, target_digital_capabilities, transformation_constraints` |
| `Corporate_Diversification_Synergy_Architect` | Evaluates concentric, horizontal, and conglomerate diversification models and mathematically models  | `current_portfolio, proposed_diversification_target, resource_constraints` |
| `Corporate_ESG_Carbon_Abatement_Strategy_Architect` | Architects rigorous, financially quantified enterprise ESG transition and carbon abatement strategie | `current_emissions_profile, capital_constraints, regulatory_landscape` |
| `Corporate_Financial_Distress_Predictive_Altman_Z-Score_Architect` | Architects robust predictive financial distress models using the Altman Z-Score to evaluate bankrupt | `balance_sheet_data, income_statement_data, market_capitalization` |
| `Corporate_Geopolitical_Risk_Mitigation_Architect` | Architects robust corporate geopolitical risk mitigation strategies, evaluating supply chain vulnera | `supply_chain_exposure, regulatory_sanctions_environment, financial_vulnerability` |
| `Corporate_Merger_Arbitrage_Deal_Risk_Architect` | Evaluate deal completion probabilities, antitrust risk, and expected annualized returns using advanc | `target_company, acquiring_company, deal_terms, regulatory_landscape, macros` |
| `Corporate_Spin-Off_Carve-Out_Architect` | Architects highly rigorous corporate spin-off and carve-out strategies, formulating parentco/spinco  | `conglomerate_portfolio_composition, sum_of_the_parts_valuation_gap, stranded_cost_and_tsa_constraints` |
| `Corporate_Transfer_Pricing_Optimization_Architect` | Architects rigorous corporate transfer pricing strategies, conducting Functions, Assets, and Risks ( | `intercompany_transactions, far_analysis_inputs, tax_jurisdiction_constraints` |
| `Corporate_Turnaround_Restructuring_Architect` | Designs rigorous financial and operational restructuring plans for distressed corporate entities. | `distressed_financials, operational_inefficiencies, market_and_creditor_dynamics` |
| `Corporate_Venture_Capital_Strategy_Architect` | Designs highly rigorous, quantitatively backed Corporate Venture Capital (CVC) investment theses and | `parent_company_strategy, technology_threat_landscape, target_startup_profile` |
| `Corporate_Vertical_Integration_Structuring_Architect` | Formulates rigorous vertical integration and make-or-buy strategies, utilizing Transaction Cost Econ | `supply_chain_context, asset_specificity, strategic_objectives` |
| `Correction_and_Removal_Reporting` | Draft a written report to FDA for a device correction or removal. | `input` |
| `Create_a_Risk-Based_Monitoring_Mitigation_SOP_for_RTSM` | Draft a standard operating procedure for risk‑based monitoring and mitigation in RTSM operations. | `existing_sop` |
| `Crisis-Management_Playbook_Generator` | Provide a concise playbook for handling critical incidents affecting customer data. | `input` |
| `Cross-Border_Data_Privacy_Architect` | A workflow dedicated to mapping data flows against overlapping jurisdictional frameworks (GDPR, CCPA | `data_flow_diagram, jurisdictions, data_types` |
| `Cross-Border_Joint_Venture_Structuring_Architect` | Formulates rigorous, strategic cross-border joint venture (JV) structuring architectures. | `partner_profiles, regulatory_jurisdictions, contribution_matrix` |
| `Cross-Browser_Infrastructure_Selenium_Grid` | Configure a Selenium Grid Hub and Nodes to distribute test execution. | `browser_count, grid_version` |
| `Cross-Chain_Interoperability_Bridge_Architect` | Expert-level prompt to architect secure, decentralized cross-chain interoperability bridges, address | `source_and_target_chains, asset_type_and_volume, security_assumptions` |
| `Cross-Channel_Behavioral_Trigger_Architect` | Constructs complex, predictive cross-channel behavioral trigger sequences for enterprise SaaS, optim | `user_telemetry_data, channel_architecture, financial_targets` |
| `Cross-Functional_Advocacy_Memo` | Draft a memo to Product/Sales focusing on revenue risk to prioritize features. | `feature_request, pipeline_stalled, renewal_risk, macros` |
| `Cross-Study_Operational_Risk_Heat_Map_and_Mitigation_Plan` | Identify and prioritize the top portfolio-level operational risks and propose mitigations. | `risk_register` |
| `Culinary_Amnestic_Reconstruction_Engine_CARE` | A cybernetic gastronomy system that reconstructs forgotten food memories into precise molecular reci | `memory_fragment, sensory_triggers, emotional_resonance` |
| `Custom_Axiomatic_System_Soundness_Evaluator` | Evaluates the logical soundness of custom axiomatic systems by rigorously proving that all axioms ar | `axioms, inference_rules, formal_semantics, system_directive` |
| `Cyber_Device_Security_Plan` | Draft a postmarket cybersecurity plan and Software Bill of Materials (SBOM). | `input` |
| `DFT_Transition_State_Architect` | A highly rigorous prompt for orchestrating Density Functional Theory (DFT) transition state optimiza | `reactants, products, functional_basis_set, solvent_model` |
| `DHT_Integration_Regulatory_Checklist` | Review FDA guidance for digital health technology (DHT) integration and validation. | `dht_type, endpoint, population, target_population` |
| `DMAIC_Process_Optimization_Architect` | Formulates rigorous Lean Six Sigma DMAIC optimization frameworks to eliminate process defects and mi | `process_baseline_metrics, critical_to_quality_ctq_parameters, suspected_root_causes` |
| `DRY_Codebase_Analysis` | Identify opportunities to remove code duplication and enforce the DRY principle. | `codebase` |
| `Dantzig-Wolfe_Column_Generation_Architect` | Formulates highly rigorous Dantzig-Wolfe decomposition and Column Generation models for large-scale, | `COMPACT_FORMULATION, BLOCK_STRUCTURE, PRICING_LOGIC, block_structure, compact_formulation, pricing_logic` |
| `Data-Quality_Risk_Heat_Map` | Assess site-level data quality and recommend mitigation actions. | `query_log, raw_eds_dump` |
| `Data-to-Insight_Analyst` | Here is a CSV (pasted or uploaded): [DATA]. | `input` |
| `Data_Architecture_Blueprint` | Draft a blueprint for clinical data architecture. | `input` |
| `Data_De-identification` | De-identify patient-level data according to HIPAA Privacy Rule. | `code_key_logic, identifiers_list, raw_data, macros` |
| `Data_Integrity_ALCOA_Audit_Architect` | Acts as a Principal Data Integrity & Compliance Architect to systematically audit complex digital he | `system_architecture, data_flow_description, identified_vulnerabilities` |
| `Data_Management_Plan_DMP_Development` | Create a DMP outlining data lifecycle and quality control. | `study_details` |
| `Data_Mapping_and_Transformation_Playbook` | Provide a repeatable workflow for mapping JSON FHIR bundles to SDTM-compliant tables. | `input` |
| `Data_Mesh_Topology_Architect` | Designs decentralized data mesh topologies with federated computational governance. | `domain_requirements, macros` |
| `Data_Privacy_Clean_Room_Architect` | Designs highly secure, multi-party Data Clean Room architectures leveraging privacy-enhancing techno | `participating_entities, analytical_workloads, privacy_constraints, user_query` |
| `Data_Residency_Localization_Architect` | Designs robust, globally distributed architectures enforcing strict data sovereignty and privacy com | `compliance_frameworks, global_distribution, data_classification` |
| `Data_Safety_Monitoring_Board_Report_Synthesizer` | Synthesizes unblinded clinical trial safety and efficacy data into a comprehensive, confidential rep | `trial_protocol_summary, unblinded_safety_data, unblinded_efficacy_data, formatting_constraints, inputs, instructions, macros, persona` |
| `Database_Lock_Procedures` | Review CRFs and prepare for database lock. | `crf_status` |
| `Database_Read_Replica_Lag_Mitigation_Architect` | Architects robust mitigation strategies for read replica lag and eventual consistency challenges in  | `topology_details, write_workload, consistency_requirements` |
| `DeFi_Protocol_Economic_Security_Architect` | Expert-level prompt to architect and evaluate the economic security of Decentralized Finance (DeFi)  | `protocol_type, oracle_dependency, tokenomics_model` |
| `De_Novo_Request_Preparation` | Generate a summary of risks and mitigations for a De Novo classification request. | `input` |
| `Decentralized_Identity_and_Verifiable_Credentials_Architect` | Expert-level prompt to architect scalable, privacy-preserving Decentralized Identity (DID) and Verif | `ecosystem_scale, regulatory_compliance, credential_lifecycle` |
| `Decentralized_Trial_Risk_Matrix` | Build a risk matrix for decentralized trials. | `input` |
| `Deception_Technology_Active_Defense_Architect` | Designs highly specialized deception environments and active defense architectures to entangle, anal | `target_environment, adversary_profile` |
| `Define-XML_Analysis_Results_Metadata_Architect` | Automates the complex structural generation and mapping of Analysis Results Metadata (ARM) for Defin | `statistical_display_spec, adam_dataset_metadata, target_define_xml_version, constraints, instructions, persona` |
| `Density_Refiner` | Craft a concise yet information-rich summary of provided text. | `input` |
| `Deontic_Logic_Normative_Conflict_Resolver` | Systematically formalizes and resolves normative conflicts (e.g., moral dilemmas) using Standard Deo | `normative_conflict, conflict` |
| `Dependencies_Security_Posture_Analysis` | Perform a thorough audit of the repository's dependencies and overall security posture to identify a | `None` |
| `Design_Error_Prevention` | Review and optimize CRF layout to avoid duplication and non-essential fields. | `crf_draft, endpoints, hypothesis, protocol` |
| `Design_Verification_Test_Plan` | Create a complete test plan for verifying that a medical device meets its design requirements. | `device_name` |
| `Design_Verification_for_BCR-ABL_Tests` | Outline design verification and validation requirements for a BCR-ABL quantitation test. | `input` |
| `Design_a_Patient-Centered_Randomization_Scheme` | Create a randomization scheme that balances patient needs with logistical simplicity. | `study_parameters` |
| `Design_a_Robust_Preclinical_Pathology_Study_Protocol` | Outline a GLP-compliant pathology study plan for a medical device evaluation. | `study_details` |
| `Design_the_Study` | You are a senior analytical chemist specializing in medical-device Extractables & Leachables (E&L).  | `device_description` |
| `Detailed_Project_Blueprint_and_Timeline` | Provide a comprehensive roadmap with phases, milestones, success metrics, and stakeholders. | `milestone_data, objectives, project_type` |
| `DevEx_Documentation_Architect` | A Senior Developer Experience Engineer's guide to creating world-class documentation, onboarding pat | `input, context` |
| `Development_Safety_Update_Report_Architect` | Synthesizes cumulative safety data into a comprehensive, regulatory-compliant Development Safety Upd | `safety_data, macros` |
| `Devil_s-Advocate_Stress_Test` | Act as a seasoned critic. | `input` |
| `Digest_Regulatory_Updates_Affecting_Protocol` | Analyze new regulatory guidance documents for impact on specific clinical protocols, differentiating | `guidance_document, therapeutic_area, protocol_phase, current_protocol_excerpt, protocol_excerpt, regulatory_context` |
| `Digital_Health_Technology_DHT_Validation` | Create validation strategy for DHTs. | `dht_specs` |
| `Digital_Transformation_Roadmap_for_Clinical_Operations` | Develop a high-level strategic roadmap for digital transformation in clinical operations, focusing o | `current_state, macros` |
| `Directed_Food_Laboratory_Order_Verification` | Review a Directed Food Laboratory Order to identify mandatory testing parameters. | `input` |
| `Discontinuous_Galerkin_Hyperbolic_PDE_Architect` | Engineers robust Discontinuous Galerkin (DG) schemes for solving non-linear hyperbolic partial diffe | `PDE_SYSTEM, DOMAIN_GEOMETRY, NUMERICAL_REQUIREMENTS, domain_geometry, numerical_requirements, pde_system` |
| `Discrepancy_Detection_Query_Log_Generator` | Examine a CSV dataset to detect discrepancies and generate a query log. | `input, csv` |
| `Disruption_Radar` | Identify emerging threats and startups that could disrupt core products. | `core_product` |
| `Distressed_Debt_Restructuring_Chapter_11_Architect` | Formulates rigorous Chapter 11 distressed debt restructuring models, Cram-Down matrices, and Absolut | `capital_structure_hierarchy, enterprise_valuation_scenario, proposed_cram_down_mechanics` |
| `Distributed_Actor_Model_Architect` | Designs highly concurrent, fault-tolerant distributed actor systems, optimizing for message-passing  | `actor_framework, state_management, scale_and_throughput, user_query` |
| `Distributed_Actor_Model_Topology_Architect` | Designs extreme-scale, stateful distributed actor model topologies optimized for highly concurrent p | `application_domain, concurrency_scale, state_durability_requirements` |
| `Distributed_Caching_Strategy_Architect` | Designs highly resilient, multi-level distributed caching architectures, handling cache topologies,  | `system_workload, data_characteristics, non_functional_requirements` |
| `Distributed_Change_Data_Capture_Pipeline_Architect` | Designs highly resilient, high-throughput distributed Change Data Capture (CDC) pipelines for real-t | `source_database, target_system, macros` |
| `Distributed_Circuit_Breaker_Resiliency_Architect` | Architects robust distributed circuit breaker topologies for preventing cascading failures in high-t | `topology_scale, failure_modes, resilience_constraints` |
| `Distributed_Clock_Synchronization_Architect` | Architects mathematically rigorous distributed clock synchronization and logical time topologies to  | `system_scale, consistency_requirements, infrastructure_constraints` |
| `Distributed_Data_Skew_Mitigation_Architect` | Architects advanced resolution strategies for distributed data skew, hot partitions, and uneven shar | `system_topology, skew_symptoms, workload_characteristics` |
| `Distributed_Database_Clock_Synchronization_Architect` | Designs robust, highly accurate clock synchronization and logical time topologies for globally distr | `physical_infrastructure, consistency_requirements, global_scale, user_query` |
| `Distributed_Database_Sharding_Architect` | Designs highly scalable distributed database sharding and partitioning strategies. | `system_requirements, input` |
| `Distributed_Knowledge_Graph_Architect` | Designs highly scalable, performant distributed graph database architectures for Semantic Knowledge  | `graph_topology, query_patterns, non_functional_requirements` |
| `Distributed_Lock_Contention_Mitigation_Architect` | Architects advanced resolution strategies for severe distributed lock contention, resolving deadlock | `contention_context, input` |
| `Distributed_Lock_Manager_Architect` | Designs highly robust, fault-tolerant distributed lock management architectures to guarantee mutual  | `scale_requirements, consistency_tolerance, infrastructure_environment, user_query, xml` |
| `Distributed_Message_Broker_Topology_Architect` | Architects highly scalable, fault-tolerant distributed message broker topologies (e.g., Kafka, Pulsa | `streaming_requirements, durability_constraints` |
| `Distributed_Observability_and_Telemetry_Architect` | A Principal Distributed Observability and Telemetry Architect to design highly scalable, robust dist | `system_architecture, scale_requirements, macros` |
| `Distributed_Rate_Limiting_Architect` | Architect a highly scalable, distributed rate limiting strategy for high-throughput API gateways and | `traffic_profile, target_scale` |
| `Distributed_Search_Engine_Topology_Architect` | Architects massively scalable, high-throughput distributed search engine topologies focusing on inve | `search_requirements, ingestion_constraints` |
| `Distributed_Secrets_Management_Topology_Architect` | Designs highly secure, highly available distributed secrets management topologies with dynamic rotat | `scale_and_distribution, authentication_and_identity, secret_characteristics, user_query` |
| `Distributed_Task_Queue_and_Background_Job_Processing_Architect` | Designs highly reliable, distributed task queue and background job processing architectures for hand | `workload_characteristics, scale_and_throughput, fault_tolerance_requirements` |
| `Distributed_Transaction_Orchestration_Architect` | Designs highly resilient, distributed transaction orchestration architectures using Saga, 2PC, or TC | `microservices_topology, transaction_requirements, failure_modes, user_query` |
| `Distributed_Vector_Database_Architect` | Designs highly scalable distributed vector database architectures for trillion-scale embedding searc | `vector_dimensionality_and_volume, search_requirements, infrastructure_constraints, macros, user_query` |
| `Distributed_Web_Crawler_Pipeline_Architect` | Designs highly scalable, fault-tolerant distributed web crawling pipelines featuring advanced crawl  | `target_scale, compliance_constraints, payload_processing, user_query` |
| `Diversity_Action_Plan_Development` | Generate a Diversity Action Plan per FDA guidance. | `epidemiology_data` |
| `Documentation_and_Repository_Structure_Implementation` | Implement foundational improvements for the repository's structure and documentation. | `None` |
| `Domain-Driven_Design_Bounded_Context_Architect` | Designs mathematically rigorous and logically coherent Domain-Driven Design (DDD) bounded contexts,  | `domain_complexity_context, input` |
| `Draft_a_Data_Management_Plan_Section` | Act as a Clinical Data Management subject-matter expert. | `input` |
| `Draft_a_GLP-Compliant_Study_Protocol` | Produce a detailed study plan that satisfies OECD and FDA GLP regulations. | `protocol_basics` |
| `Driver_Configuration_WebDriver_Initialization` | Initialize and configure WebDriver instances with specific browser options. | `browser, proxy_url` |
| `Dual-Language_Figure_Prompt` | Generate a Kaplan–Meier figure in both R and SAS from ADaM ADTTE data. | `dataset_path, dual` |
| `Dual_MDR_IVDR_Conformity-Assessment_Roadmap` | Develop a coordinated roadmap for simultaneous MDR and IVDR submissions. | `startup_info` |
| `Dunnett_Adjustment_R_Code_Generator` | Generate R code for Dunnett multiplicity adjustments using the 'multcomp' package. | `control_label, dataframe, dose_var, response_var, control_group_label, dataframe_name, dose_variable, response_variable` |
| `Dynamic_Causal_Modeling_Architect` | A Principal Computational Neuroscientist agent designed to formulate advanced Dynamic Causal Modelin | `imaging_modality, neural_mass_model, experimental_design` |
| `Dynamic_Epistemic_Drift_Mitigator` | An advanced meta-reasoning architecture that acts as a Genesis Architect for mitigating semantic dri | `initial_hypothesis, iterative_trajectory` |
| `E2E_Test_Discovery_Lifecycle_Template` | Provide a system prompt template that guides an LLM to analyse a codebase and generate a comprehensi | `BUSINESS_GOAL, LANGUAGES_FRAMEWORKS, PROJECT_NAME` |
| `E2E_Test_Discovery_Template` | Guide a model to analyze a codebase and produce a comprehensive end‑to‑end test plan. | `business_goal, languages_frameworks, project_name` |
| `EO_Sterilization_Validation_Protocol` | Outline a protocol to achieve SAL 10^-6 using an ethylene‑oxide half‑cycle approach. | `device_name` |
| `EU_IVDR_Performance_Evaluation_Report_Architect` | Designs comprehensive, regulatory-compliant Performance Evaluation Reports (PER) under EU IVDR 2017/ | `ivd_device_description, scientific_validity_summary, analytical_performance_data, clinical_performance_data` |
| `EU_MDR_Clinical_Evaluation_Report_Architect` | Designs comprehensive, regulatory-compliant Clinical Evaluation Reports (CER) under EU MDR 2017/745  | `device_description, state_of_the_art, clinical_data_summary, user_query` |
| `EU_MDR_PMCF_Plan_Architect` | Designs comprehensive, regulatory-compliant Post-Market Clinical Follow-up (PMCF) Plans under EU MDR | `device_description, clinical_data_gaps, pmcf_activities` |
| `EU_MDR_PSUR_Architect` | Designs comprehensive, regulatory-compliant Periodic Safety Update Reports (PSUR) under EU MDR 2017/ | `device_name, device_class, reporting_period, pms_data_summary, sales_volume, macros` |
| `EU_MDR_Post-Market_Surveillance_Plan_Architect` | Design comprehensive, regulatory-compliant Post-Market Surveillance (PMS) Plans under EU MDR 2017/74 | `device_class, intended_purpose, market_history, input, pms_plan` |
| `EU_MDR_Technical-Documentation_Gap_Assessment` | Identify deficiencies in technical documentation against EU MDR Annex II and III. | `device_info, technical_docs` |
| `EU_MDR_Technical_Documentation_Architect` | Formulates rigorous, compliant EU MDR Annex II and III technical documentation for medical devices,  | `device_classification, intended_purpose, basic_udi_di, clinical_data_summary` |
| `Earnings_Call_Script_Prep` | Prepare for tough analyst questions on an earnings call. | `challenge, macros` |
| `Eco-Crypto_Haiku_Oracle` | Transforms arboreal environmental data into cryptographically seeded haikus for the forest blockchai | `tree_species, growth_ring_width_mm, carbon_isotope_ratio, block_hash, arboreal_packet, growth, isotope, prev_hash, species` |
| `Edge_AI_Inference_Architect` | Designs low-latency, bandwidth-constrained AI inference architectures directly at the edge, featurin | `edge_device_constraints, inference_sla, security_compliance, user_query` |
| `Edge_Computing_Topology_Architect` | Designs highly optimized edge computing topologies to minimize latency, ensure offline capability, a | `domain_requirements` |
| `Edit-Check_Specification_Builder_for_New_eCRF_Fields` | Create edit-check specifications for the new Concomitant Medication module in Medidata Rave. | `input` |
| `Eisenhower_Matrix_Coach` | Triage a to-do list using the Eisenhower Matrix. | `tasks` |
| `Electrocatalytic_Mechanism_Architect` | Formulates rigorous electrocatalytic reaction mechanisms, computing activation barriers, overpotenti | `reaction, catalyst_surface, electrolyte_conditions` |
| `Electronic_Data_Capture_Implementation` | Design eCRFs with built-in edit checks and automation. | `dcp, dmp, protocol` |
| `Elevator_Pitch_for_Expensive_Tech` | Create a persuasive elevator pitch for expensive technology investments focusing on business outcome | `budget, current_problem, specific_tools, technology` |
| `Emerging-Market_Opportunity_Scan` | Identify high-growth therapeutic areas or sponsor segments for CRO services. | `market_data_sources, macros, market_data` |
| `Emerging-Science_Horizon_Scan` | Highlight emerging therapeutic areas or technologies likely to disrupt CRO services in the next thre | `input` |
| `Empathy-Map_Facilitator` | Quickly capture a user persona’s voice and pain points. | `input` |
| `Enantioselective_Catalytic_Mechanism_Architect` | Generates rigorous transition state models and kinetic pathways for enantioselective catalytic mecha | `catalyst_structure, substrates, conditions` |
| `Endotoxin_Control_510_k_Risk_Plan` | Draft a risk-based endotoxin-testing plan for a 510(k) submission. | `device_name, 85` |
| `Enterprise_Collaboration_Portal_Architect` | Designs the system architecture for a web-based Enterprise Collaboration Portal that abstracts Git a | `functional_requirements, constraints` |
| `Enterprise_RAG_Architecture_Designer` | Designs highly secure, hallucination-resistant, and high-throughput Retrieval-Augmented Generation ( | `data_sources, security_compliance, scale_latency_sla` |
| `Ephemeral_Sandbox_Ecosystem_Architect` | Acts as a Staff Platform Engineer to design highly secure, isolated, and automated ephemeral sandbox | `target_workloads, cloud_infrastructure, isolation_constraints` |
| `Epistemic_Logic_Multi-Agent_Knowledge_Architect` | Formulates rigorous multi-agent epistemic logic frameworks to model knowledge, belief, and informati | `multi_agent_scenario, input` |
| `Epistemic_Regress_Topology_Architect` | A rigorous prompt designed to systematically map, formalize, and resolve epistemic justificatory cha | `EPISTEMIC_CLAIM, JUSTIFICATION_FRAMEWORK, DEFEATER_CONDITION, defeater_condition, epistemic_claim, justification_framework` |
| `Establishment_of_Food_Traceability_Plan` | Create a structured traceability plan for a facility handling foods on the Food Traceability List. | `input` |
| `EtO_Sterilization_Process_FMEA` | Facilitate a Failure Mode and Effects Analysis for an ethylene oxide sterilization process. | `process_description` |
| `Evaluate_Device_Tissue_Interface_Findings` | Interpret histopathology results from implant studies and recommend next steps. | `study_protocol` |
| `Event-Driven_Dead_Letter_Queue_Remediation_Architect` | Strategic Genesis Architect persona for designing advanced, automated remediation frameworks for Dea | `broker_ecosystem, remediation_pattern, architecture_constraints` |
| `Event-Driven_Topology_Designer` | Architects robust event-driven topologies and asynchronous workflows from domain requirements. | `domain_requirements` |
| `Event-Sourced_Saga_Orchestration_Architect` | Designs robust, stateful saga orchestration architectures for long-running, distributed business tra | `business_transaction_workflow` |
| `Execution_Optimization_Parallel_Testing` | Configure the automation suite to execute multiple tests simultaneously. | `language, WebDriver` |
| `Executive-Ready_Brief_and_Talking_Points` | Turn disparate reports into a concise executive brief and talking points. | `input` |
| `Executive_Briefing_Architect_TL_DR` | Synthesize complex inputs into high-signal executive briefs. | `input` |
| `Executive_Sponsor_Briefing_Deck_Outline` | Provide a slide-by-slide outline for a quarterly sponsor briefing. | `challenges, kpi_snapshot, strategic_wins` |
| `Executive_Trial-Health_Dashboard` | Summarize the health of active studies in a weekly dashboard. | `input` |
| `Explain-Like-I_m-5_ELI5` | Explain ‘[TOPIC]’ as if I’m five: | `input, macros, topic` |
| `FDA-Aligned_AI_Governance_Framework` | Draft an AI governance framework that satisfies regulators and sponsors. | `input` |
| `FDA_483_Response_Strategist` | Design comprehensive, regulatory-compliant responses to FDA Form 483 observations, employing an auth | `observation_text, background_context, immediate_corrections, root_cause_investigation, corrective_action_plan` |
| `FDA_Breakthrough_Device_Designation_Architect` | Formulates rigorous, compelling applications for the FDA Breakthrough Devices Program, accelerating  | `device_description, target_disease_condition, comparative_standard_of_care` |
| `FDA_CSA_Risk-Based_Testing_Strategy_Architect` | Formulates rigorous, risk-based Computer Software Assurance (CSA) testing strategies to optimize sof | `software_system_description, patient_safety_risk_assessment, product_quality_risk_assessment` |
| `FDA_De_Novo_Classification_Request_Architect` | Architect rigorous, compliant FDA De Novo Classification Requests for novel medical devices, ensurin | `device_description, risk_mitigation_strategy` |
| `FDA_Fast_Track_Designation_Architect` | Designs a rigorous, strategically aligned FDA Fast Track Designation application focusing on demonst | `product_description, target_condition, supporting_data` |
| `FDA_MDR_MDV_Adverse-Event_Narrative` | 1. Extract: event date, patient age/sex, device identifiers, reporter type. | `input, macros` |
| `FDA_Missing-Data_Query_Response` | Draft a response letter to an FDA information request about missing data. | `fda_questions, sap_references` |
| `FDA_OOS_Investigation_Architect` | Acts as a Strategic Genesis Architect to formulate rigorous, compliant Out of Specification (OOS) in | `product_name, batch_lot_number, analytical_method, expected_specification, reported_result, initial_analyst_observations` |
| `FDA_Type_II_Drug_Master_File_DMF_Architect` | Formulates rigorous, compliant FDA Type II Drug Master File (DMF) submissions for Drug Substances (A | `active_pharmaceutical_ingredient, manufacturing_process, impurity_profile, stability_data` |
| `FWER_Gatekeeping_Procedure_Code_Generator` | Generate code for sequential and gatekeeping procedures to control Family-Wise Error Rate (FWER). | `alpha, endpoints, language, alpha_level` |
| `Fair-Market-Value_Budget_Negotiation_Brief` | Prepare a concise briefing to support FMV negotiations with a pharma sponsor. | `site_cost_data` |
| `Feature_Flag_and_Progressive_Delivery_Architect` | Designs highly reliable, scalable, and risk-mitigated feature flag and progressive delivery architec | `deployment_environment, application_architecture, risk_tolerance` |
| `Federated_Learning_Differential_Privacy_Architect` | Designs highly secure, privacy-preserving Federated Learning architectures using rigorous Differenti | `network_topology, privacy_budget, threat_model` |
| `Federated_Learning_Privacy-Preserving_Architect` | Designs highly secure, privacy-preserving federated learning architectures utilizing advanced crypto | `data_heterogeneity_context, privacy_constraints, aggregation_topology, user_query` |
| `Federated_Learning_Topology_Architect` | Architects secure, robust, and highly scalable federated learning distributed topologies, emphasizin | `client_distribution, model_complexity, privacy_security_constraints, user_query` |
| `Feynman_Rule_Derivation_Architect` | Derives Feynman rules and vertex factors from novel Lagrangians in Quantum Field Theory, applying ex | `lagrangian_density, field_content, symmetry_group, user_query` |
| `Financial_Conflict_of_Interest_FCOI_Reporting` | Review disclosures and draft management plan. | `sfi_disclosure` |
| `Financial_Disclosure_Certification` | Identify required financial disclosure forms and draft attestations for clinical investigators. | `input` |
| `Fine-Grained_Authorization_Architect` | Designs highly scalable, low-latency, and distributed Fine-Grained Authorization (FGA) architectures | `authorization_model, traffic_profile, integration_ecosystem` |
| `Finite_Element_Analysis_FEA_Interpreter` | An agent that analyzes stress, thermal, and vibration simulation outputs to recommend geometric opti | `simulation_type, material_properties, simulation_results` |
| `Firmware_and_UEFI_Bootkit_Forensics_Analyst` | Conducts expert-level digital forensics on low-level firmware, UEFI interfaces, and persistent bootk | `suspicious_artifact, environment_context, objective, user_query` |
| `Fishbone_Facilitator` | Identify possible root causes of a problem using a fishbone diagram. | `problem` |
| `Folder_and_Module_Organization` | Provide a detailed plan for restructuring a Python codebase into clearer, feature-based modules. | `repo_path` |
| `Food_Safety_Audit_Reporting_Regulatory` | Draft a regulatory audit report for an eligible entity after a food safety audit. | `input, macros` |
| `Forecast_Site-Level_Drug_Supply_Resupply_Strategy` | Plan site-level drug supply and resupply for an adaptive trial. | `trial_enrollment` |
| `Foreign_Supplier_Verification_Program_FSVP_Audit` | Draft a summary report of an onsite audit for a foreign food supplier including conclusions and corr | `input` |
| `Forensic_Super_Timeline_Analysis_Architect` | Generates expert-level digital forensics and incident response (DFIR) super timeline analysis strate | `intrusion_context, artifacts_collected, specific_threat_indicators` |
| `Forge_-_Script_Reliability_Agent` | A reliability-obsessed agent who builds unbreakable development environments. | `script_content` |
| `Forward-Looking_Resource_Capacity_Forecast` | Project FTE demand and recommend actions to balance capacity for the next 90 days. | `current_staffing, pipeline_forecast` |
| `Fractal_Epistemic_Consensus_Architect` | An advanced meta-reasoning architecture designed to orchestrate non-monotonic, mathematically rigoro | `problem_space, agent_hypotheses` |
| `Framework_Best_Practices_Locator_Strategy` | Transition from brittle XPaths to robust locators like ID or CSS selectors. | `locators` |
| `Framework_Implementation_Data-Driven_Testing` | Utilize data providers to execute the same test logic with multiple sets of data. | `None` |
| `Free_Energy_Perturbation_Architect` | Generates rigorous molecular dynamics simulation protocols for alchemical Free Energy Perturbation ( | `receptor, reference_ligand, target_ligand, conditions` |
| `Free_Logic_Empty_Names_Formalizer` | A highly rigorous prompt designed to systematically formalize and evaluate propositions containing n | `PROPOSITION, FREE_LOGIC_SYSTEM, ONTOLOGICAL_DOMAIN, free_logic_system, ontological_domain, proposition` |
| `Freedom_of_Information_Act_FOIA_Request` | Draft a request for records regarding a specific 510(k) clearance. | `input` |
| `Friction-Hunting_Onboarding_Audit` | Critique onboarding steps to identify friction and propose low-touch alternatives. | `onboarding_steps, macros` |
| `Functional_Data_Analysis_Architect` | Acts as a Principal Statistician to design robust nonparametric methodologies for infinite-dimension | `data_characteristics, analytical_objective, computational_constraints` |
| `GCP_and_GDPR_Training_Compliance_Risk_Report` | Generate a monthly assessment of staff training compliance for GCP and GDPR regulations. | `training_records, macros` |
| `GLP_Quality_Assurance` | Prepare a statement for a nonclinical study report certifying inspection dates. | `input` |
| `GPU_Cluster_Orchestration_Architect` | Designs highly performant, distributed GPU cluster architectures optimized for massively parallel AI | `cluster_workload_parameters, input` |
| `GTM_Pricing_Elasticity_Architect` | Constructs deeply rigorous Go-To-Market (GTM) pricing elasticity matrices, modeling price sensitivit | `product_value_proposition, target_market_segments, financial_constraints` |
| `Generate_QC_Submission-Ready_TLFs` | Produce validated tables, listings, and figures (TLFs) ready for regulatory submission. | `adae_path, adlb_path, adsl_path` |
| `Generate_an_Executive_Summary_for_the_Final_Report` | Write a concise executive summary of a non-clinical study report. | `report_sections` |
| `Generative_AI_Guardrails_Gateway_Architect` | Architect high-performance, robust gateway strategies for Large Language Models (LLMs) focusing on p | `threat_landscape, latency_constraints, regulatory_compliance, user_query` |
| `GitHub_Custom_Agent_Creator` | Expertly craft configuration files for GitHub Custom Agents with strict YAML frontmatter and structu | `input, agent_requirements` |
| `Global_CDN_Topology_Architect` | Designs highly resilient, hyper-scalable Global Content Delivery Network (CDN) topologies for low-la | `asset_profiles, traffic_patterns, caching_requirements, user_query` |
| `Global_Market_Entry_Expansion_Architect` | Architects highly rigorous, data-driven global market entry strategies and international expansion b | `target_market, product_portfolio, internal_capabilities` |
| `Global_Regulatory_and_Tax_Matrix_for_Site_Payments` | Summarize key payment compliance requirements across major regions. | `regional_guidelines` |
| `Global_Supply_Chain_Resilience_Architect` | Designs highly rigorous, quantitative supply chain network optimization models to mitigate geopoliti | `network_topology, disruption_scenario, financial_constraints` |
| `GraphQL_Supergraph_Federation_Architect` | Designs robust GraphQL supergraph federated architectures, establishing subgraph boundaries and reso | `domain_boundaries, client_access_patterns` |
| `Graph_Database_Traversal_Architect` | Designs highly optimized, massively scalable graph database architectures and complex traversal algo | `dataset_characteristics, traversal_requirements` |
| `HFT_Low-Latency_Architecture_Designer` | Designs strictly optimized, sub-microsecond latency network and hardware architectures for High-Freq | `exchange_protocols, hardware_constraints, deployment_topology` |
| `HTAP_Real-Time_Analytics_Architect` | Designs Hybrid Transactional/Analytical Processing (HTAP) architectures bridging OLTP and OLAP workl | `workload_profile, latency_requirements, macros, request` |
| `Hands-On_Procedure_Coaching` | Coach a trainee through a vascular access technique using a training model. | `procedure_name` |
| `Hardware_Side-Channel_Attack_Modeling_Architect` | Designs highly rigorous, physics-based side-channel attack models and advanced countermeasures for e | `target_hardware_architecture, attack_vector_focus` |
| `Hero_s_Journey_Storyboarder` | Craft a brief marketing narrative following the Hero's Journey structure. | `product` |
| `Heuristic-Evaluation_Coach` | Guide a junior designer through heuristic evaluation of a mobile app. | `APP_NAME, app_name` |
| `Hexagonal_Architecture_Implementation` | Expert guidance on implementing Hexagonal Architecture, focusing on data flow, dependency inversion, | `implementation_query, scenario` |
| `Hexagonal_Architecture_Principles` | Explain the core philosophy, skeleton, and benefits of Hexagonal Architecture (Ports and Adapters). | `input, request` |
| `Hexagonal_Architecture_Review` | Analyze code for adherence to Hexagonal Architecture principles, identifying layer violations and de | `input, code, macros` |
| `High-Scale_OTT_Video_Streaming_Architect` | Designs highly resilient, massively scalable Over-The-Top (OTT) video streaming pipelines with dynam | `ingestion_specs, playback_requirements, scale_and_latency` |
| `High-Scale_WebSocket_Push_Architect` | Designs highly scalable, stateful, and performant persistent WebSocket architectures capable of hand | `connection_scale, broadcast_requirements, infrastructure_constraints, user_input` |
| `High-Throughput_Distributed_ID_Generator_Architect` | Designs highly scalable, strictly monotonic, globally unique identifier (UUID/Snowflake/ULID) genera | `scale_requirements, ordering_semantics, deployment_topology, user_query` |
| `High-Throughput_Geospatial_Indexing_Architect` | Architects highly scalable, low-latency spatial index and geofencing systems for real-time location  | `requirements, Aegis, macros` |
| `High-Throughput_LLM_Inference_Serving_Architect` | Designs highly optimized, ultra-low-latency Large Language Model (LLM) inference serving topologies, | `model_specifications, workload_characteristics, hardware_constraints` |
| `High-Throughput_Order_Matching_Engine_Architect` | Designs ultra-low latency, highly deterministic order matching engine architectures for high-frequen | `throughput_requirements, matching_algorithm, deployment_topology, user_query` |
| `Hodge_Theory_Harmonic_Form_Architect` | Generates mathematically rigorous derivations of harmonic forms and solutions to the Hodge decomposi | `manifold_definition, differential_form` |
| `Hostile_Takeover_Defense_Matrix_Architect` | Constructs a rigorous quantitative defense matrix and poison pill trigger model for hostile takeover | `company_financials, acquirer_profile, market_conditions` |
| `Hosting_Cost_Reduction_ToT_Plan` | Develop a tree-of-thought plan to reduce hosting costs. | `input` |
| `Human_Factors_Usability_Summary` | Summarize usability testing results to demonstrate minimized use-related risks. | `input` |
| `Human_Factors_Validation_Study_Protocol` | Draft a user validation study protocol for a medical device. | `class, device_name` |
| `Humanitarian_Device_Exemption_HDE` | Explain why the health benefit of a HUD outweighs the risk of injury. | `input` |
| `Hype_vs_Reality_Analysis` | Evaluate a specific technology for pragmatic application, cutting through the hype. | `industry, technology` |
| `ICH_E9_R1_Estimand_Builder` | Construct a primary estimand description following the ICH E9 (R1) framework. | `clinical_setting, ice_list, scientific_question, key_intercurrent_events` |
| `IDE_Application_Preparation` | Draft an Investigational Device Exemption (IDE) application, including risk analysis and investigati | `input` |
| `IDE_Determination_and_Device_Classification` | Assess risk classification and draft rationale. | `device_study_desc` |
| `IEC_62366-1_Summative_Usability_Evaluation_Protocol_Architect` | Design comprehensive, regulatory-compliant Summative Usability Evaluation Protocols under IEC 62366- | `device_description, user_profiles, critical_tasks, input, usability_protocol` |
| `IND_Determination_and_Application` | Determine IND exemption and prepare dossier. | `protocol_and_status` |
| `IND_Readiness_Gap_Analysis_Filing_Road-Map` | Assess IND readiness and create a filing road‑map for a therapeutic program. | `data_snapshots, first_in_human_date, program_summary` |
| `IQ_OQ_PQ_Validation` | Design and execute a series of IQ, OQ, and PQ validation tests for clinical systems. | `cdms_specs, crf_draft, dmp, protocol, validation_tests` |
| `IRB_Protocol_Review` | Evaluate a clinical investigation protocol to ensure it meets IRB approval criteria. | `input` |
| `ISO_10993_Biological_Evaluation_Plan_Architect` | Generates a comprehensive, ISO 10993-1 compliant Biological Evaluation Plan (BEP) based on device ma | `device_description, patient_contact, materials_list, manufacturing_processes` |
| `ISO_Strategist` | Plans the therapeutic journey using the ISO Principle. | `psychological_profile` |
| `IVDR_Performance-Evaluation_Plan_Blueprint` | Draft a comprehensive Performance‑Evaluation Plan (PEP) that satisfies Article 56 and Annex XIII of  | `device_details` |
| `IVD_Performance_Study_Compliance_Review` | Review an IVD performance study for compliance with MDCG 2024‑4 and related guidance. | `study_overview` |
| `Idempotency_and_API_Retry_Strategy_Architect` | Designs highly robust, distributed idempotency and retry architectures for APIs and message-driven s | `system_context, failure_scenarios, macros` |
| `Identity_Threat_Detection_and_Response_Architect` | Acts as a Principal Security Architect to design highly rigorous Identity Threat Detection and Respo | `identity_infrastructure, attack_surface_concerns, macros` |
| `Image_Acquisition_QC_Workflow_Blueprint` | Design a site-facing SOP for image acquisition and quality control. | `modalities, study_description` |
| `Imaging_Charter_Draft` | Create a study-specific imaging charter compliant with global regulations. | `endpoints, list, modalities, protocol_synopsis, regulations, sites` |
| `Imaging_Endpoint_Process_Standards_Checklist` | Review FDA guidance on imaging endpoints and create process checklists. | `endpoint, modality, imaging_modality, primary_endpoint` |
| `Immutable_Financial_Ledger_Architect` | Designs strictly immutable, highly auditable financial ledger architectures enforcing dual-entry acc | `financial_context, input` |
| `Import_Entry_Data_Element_Compilation` | Compile required identifying information (510(k), UFI, NDC, NDA) for electronic import entry of drug | `input` |
| `Inclusion_Exclusion_Endpoints_Sample-Size_Deep_Dive` | Clarify criteria, endpoints, and sample-size considerations for a medical device trial. | `device_description, population_details` |
| `Inflationary_Tensor_Perturbation_Architect` | Acts as a Theoretical Physics Genesis Architect to mathematically derive the primordial tensor power | `inflationary_potential, gauge_choice` |
| `Informed_Consent_Exception_Emergency` | Draft IRB documentation for an exception from informed consent in emergency research. | `input` |
| `Informed_Consent_Form_Plain_Language_Translator` | Translates complex clinical trial protocols into plain-language Informed Consent Forms (ICFs) ensuri | `protocol_section, target_reading_level` |
| `Informed_Consent_Process_Optimization` | Review and rewrite ICF for readability. | `icf_text` |
| `Infrastructure_Configuration_Drift_Remediation_Architect` | Designs and enforces rigorous automated workflows to detect, analyze, and remediate Infrastructure a | `iac_tooling, cloud_environment, drift_tolerance_policy` |
| `Infrastructure_as_Code_IaC_Security_Architect` | Designs and enforces rigorous security policies, threat models, and compliance checks for Infrastruc | `iac_framework, deployment_architecture, compliance_standards` |
| `Insider_Threat_Behavioral_Analytics_Engineer` | Formulates highly rigorous User and Entity Behavior Analytics (UEBA) models and insider threat detec | `baseline_behavior, observed_anomaly, target_platform, macros, scenario` |
| `Inspection-Readiness_Drill_CAPA_Builder` | Prepare for regulatory inspections by rehearsing high‑risk questions and drafting CAPAs. | `audit_notes` |
| `Integrated_Submission_Strategy_Coach` | Create a phased submission roadmap for Project Phoenix. | `project_details` |
| `Intellectual_Property_Claim_Drafter` | A prompt that enforces USPTO or EPO formatting constraints to translate engineering specifications i | `engineering_spec, patent_office, claim_type` |
| `Intended_Use_and_Indications_for_Use_Alignment` | Review 510(k) drafts to ensure 'Intended Use' and 'Indications for Use' are verbatim and consistent. | `input` |
| `Interim_Results_Executive_Brief` | Summarize interim analysis findings for cross-functional leadership. | `analysis_results, safety_listings, statistical_plan` |
| `Interpret_the_Chemistry_Assess_Risk` | Act as a board-certified toxicologist. | `body_weight, device_dose, study_results` |
| `Intuitionistic_Logic_Natural_Deduction_Prover` | Systematically generates formal natural deduction proofs in intuitionistic logic, explicitly avoidin | `premises, conclusion` |
| `Inventory_Demand-Planning_Simulation` | Create a forecast and inventory plan from historical demand data. | `inventory_csv` |
| `Investigational_New_Drug_IND_Architect` | Formulates rigorous, compliant Investigational New Drug (IND) applications (21 CFR Part 312), explic | `drug_substance_overview, nonclinical_safety_summary, clinical_protocol_design, cmc_status` |
| `Investigator-Site_Payment_Forecast` | Produce a month-by-month cash-flow forecast for site payments. | `enrollment_curve, fx_rates, site_data, macros` |
| `Investigator_Follow-up_Email_Action-Item_Tracker` | Compose a follow-up email to the PI summarizing visit findings and action items, plus a tracking tab | `input` |
| `Investigator_s_Brochure_Safety_Update_Architect` | Synthesizes cumulative clinical and nonclinical safety data into an updated Investigator's Brochure  | `current_rsi, cumulative_safety_data, nonclinical_findings, formatting_constraints, inputs, instructions, macros, persona` |
| `Investigator_s_Brochure_Summary_of_Changes` | Produce a detailed summary of changes for the annual Investigator’s Brochure update. | `None` |
| `Investor_FAQ_Generation` | Generate an FAQ for a bearish investor based on press release and 10-K. | `documents, macros` |
| `Investor_and_Board_Narrative_Builder` | Craft a concise two-slide narrative for investors and board members. | `input` |
| `IoT_Digital_Twin_Architect` | Designs highly accurate, scalable, and synchronized digital twin architectures for complex IoT ecosy | `physical_system_spec, user_query` |
| `Jules_API_Scout` | AI Integration Specialist for researching live API contracts to prevent hallucinations. | `target_service, context` |
| `Jules_Agile_Orchestrator` | AI Product Engineering Lead for Agile project management, backlog refinement, and atomic task decomp | `project_goals, context, macros` |
| `Jules_Compliance_Officer` | AI Risk Mitigator for ensuring accessibility, privacy, and legal compliance. | `target_code, context, button, macros` |
| `Jules_Concurrency_Architect` | AI State Management Architect for defining async flows and race condition handling. | `target_epic` |
| `Jules_Data_Architect` | AI Database Architect for designing schemas, migrations, and indexing strategies. | `target_epic, current_schema, macros` |
| `Jules_DevOps_Engineer` | AI Site Reliability Engineer for CI/CD, containerization, and deployment. | `application_code, environment, macros` |
| `Jules_Developer_Agent` | AI Software Engineer for executing specific tasks with strict adherence to technical specs and scope | `assigned_task, tech_spec, target_files, macros` |
| `Jules_E2E_Test_Engineer` | AI Test Automation Engineer for writing end-to-end integration tests. | `completed_tasks, spec` |
| `Jules_FinOps_Profiler` | AI Performance Watchdog for detecting resource inefficiencies and cost risks. | `source_code, context` |
| `Jules_Maintainer` | AI Documentation Maintainer for syncing codebase reality with documentation. | `completed_tasks, codebase_diff, current_docs` |
| `Jules_Orchestrator` | Lead AI Technical Project Manager & Architect for state analysis, documentation enhancement, and ato | `project_goals, context, macros` |
| `Jules_Product_Architect` | AI Product Architect for translating seed visions into high-level execution roadmaps. | `seed_idea, current_state, macros` |
| `Jules_QA_Gatekeeper` | AI Quality Control Agent for validating developer code against specs and constraints. | `assigned_task, tech_spec, source_code, macros` |
| `Jules_Security_Auditor` | AI DevSecOps agent for auditing specs and code for security vulnerabilities. | `target_document, context` |
| `Jules_System_Designer` | AI Lead System Designer for creating rigid technical specifications from high-level Epics. | `target_epic, seed_idea, current_architecture, macros` |
| `Jules_Test_Generator` | A specialized prompt for Google Jules to autonomously generate comprehensive test suites for existin | `target_files` |
| `Jules_UX_Writer` | AI Localization Expert for generating professional copy and error messages. | `ui_components, macros` |
| `KPI_Dashboard_Monthly_Ops-Review_Pack` | Summarize operational performance and highlight required actions for the monthly review. | `kpi_data, strategic_priorities` |
| `Kubernetes_Cluster_Security_Posture_Architect` | Analyzes Kubernetes (K8s) cluster configurations, RBAC policies, and manifest files to identify secu | `cluster_manifests, rbac_policies, compliance_framework` |
| `Kubernetes_Container_Escape_Forensics_Analyst` | Generates expert-level forensic analysis and response strategies for detecting, reconstructing, and  | `kubernetes_audit_logs, node_telemetry, container_manifests` |
| `LEO_Satellite_Mesh_Network_Architect` | Designs highly dynamic, resilient Low Earth Orbit (LEO) satellite mesh network architectures, optimi | `orbital_mechanics_context, traffic_qos_constraints, hardware_constraints, user_query` |
| `LLM_Distributed_Training_Architect` | Architects massive-scale distributed training infrastructure for Large Language Models using 3D para | `model_architecture, cluster_topology, constraints, user_query` |
| `Labeling_Compliance_Audit` | Audit device labeling for compliance with mandatory elements (Manufacturer, UDI, date formats). | `input` |
| `Lay_Language_Summary_Creation` | Summarize trial results for lay audience with rigorous formatting and safety checks. | `technical_results, macros` |
| `Leader_Election_and_Split-Brain_Mitigation_Architect` | Designs highly available, consensus-driven architectures for leader election and robust split-brain  | `cluster_topology, workload_requirements, infrastructure_constraints, user_query` |
| `Leadership_Reflection_and_Culture` | Assess leadership values and identify actions to strengthen team cohesion. | `current_values, team_context` |
| `Learning_Path_Mentor` | Design a phased roadmap that guides users toward skill mastery. | `skill_level, weekly_hours` |
| `Legacy_Modernization_Strategy` | Create a phased roadmap for migrating legacy systems to modern architectures. | `budget, downtime_limit, legacy_system` |
| `Leveraged_Buyout_Financial_Structuring_Architect` | Architects robust Leveraged Buyout (LBO) financial structures, evaluating debt capacity, capital str | `target_financials, debt_markets, sponsor_returns` |
| `Linear_Logic_Resource_Proof_Generator` | Automatically generates rigorous natural deduction or sequent calculus proofs in Girard's Linear Log | `premises, conclusion, proof_system` |
| `Liquidity_Stress_Test` | Run a stress test on cash flow forecast assuming a drop in collections. | `drop_percentage, forecast, macros` |
| `Literature_Regulatory_Gap_Analysis` | Identify evidence and regulatory gaps for a planned pivotal clinical study. | `device_or_ivd, target_indication` |
| `Living-off-the-Land_Behavioral_SIEM_Query_Architect` | Architects advanced, high-fidelity SIEM behavioral queries targeting Living-off-the-Land (LotL) tech | `target_lotl_binary, siem_platform_syntax, baseline_noise_profile, user_query` |
| `Log-Structured_Merge_Tree_Storage_Architect` | Designs high-performance, write-optimized storage engines based on Log-Structured Merge (LSM) trees, | `workload_profile, hardware_constraints, durability_requirements, user_query` |
| `Lyricist` | Writes the actual lyrics using the themes and structure. | `psychological_profile, therapeutic_arc, musical_blueprint` |
| `MCID_Research_and_Summary` | Research and summarize Minimal Clinically Important Differences (MCIDs) for measurement tools. | `disease_area, tools, measurement_tools` |
| `MDSAP_Nonconformity_Grading_Evaluator` | Evaluate audit findings based on the GHTF/SG3/N19:2012 5-step grading matrix, enforcing the 'Vector' | `audit_finding, direct_qms_impact, repeat_finding, input, mdsap_evaluation` |
| `MECE_Structuring_Consultant` | Reorganize brainstorm ideas into three mutually exclusive, collectively exhaustive buckets. | `LIST` |
| `M_A_Target_Evaluation` | Evaluate a potential acquisition target based on financial statements. | `financial_statements, target_description` |
| `Maintainability_Codebase_Analysis` | Improve code maintainability by addressing readability, organization, and test quality. | `codebase` |
| `Market-Intelligence_Radar` | Prioritize high-potential biotech or pharma companies for partnership opportunities. | `company_size, geography_focus, preferred_areas, macros` |
| `Market_Landscape_Trend_Analysis` | Summarize the global market for `{{ device_or_assay }}` and highlight key trends. | `device_or_assay, macros` |
| `Market_Report_Executive_Summary` | Draft and refine an executive summary for the uploaded market report. | `market_report` |
| `Marketing_Campaign_for_Clinical_Services` | Generates a comprehensive marketing asset package including landing page copy, email sequence, and s | `service_suite_name, target_audience, pain_points, features` |
| `Massive-Scale_Fan-Out_Feed_Architect` | Designs highly scalable, low-latency news feed and timeline architectures to handle extreme fan-out  | `user_base_scale, connection_graph_density, feed_ranking_requirements, user_query` |
| `Massive-Scale_IoT_OTA_Update_Architect` | Designs highly resilient, fault-tolerant Over-The-Air (OTA) update architectures for massive-scale I | `device_fleet_characteristics, network_constraints, rollout_and_scale, user_query` |
| `Master_Ultrameta_Prompt_Architect` | Construct a five-layer prompt stack (L0–L4) that reliably executes `{{ end_task }}`. | `end_task, policy_block` |
| `Mechatronics_Control_Systems_Architect` | A workflow bridging mechanical systems with software logic (PID controller tuning, actuator timing a | `mechanical_plant, actuators_and_sensors, control_objective` |
| `Medical_Coding_and_Reconciliation_Assistant` | Automatically predict and apply medical terms to clinical data, and perform automated data reconcili | `input, clinical_data` |
| `Medical_Device_Administrative_Detention_Appeal` | Draft a written appeal for an administrative detention order issued on a food item or medical device | `input` |
| `Medical_Device_Cybersecurity_Threat_Modeling` | Analyze system architecture using STRIDE. | `system_architecture` |
| `Medical_Device_Recall_Strategy` | Develop a mandatory recall strategy for a device posing health risks. | `input` |
| `Medical_Device_Recall_Strategy_Architect` | Designs comprehensive Health Hazard Evaluation (HHE) and recall execution strategies, adhering stric | `issue_description, clinical_impact, distribution_scope` |
| `Medical_Device_Reporting_MDR` | Summarize an adverse event for mandatory electronic submission or develop an MDR SOP. | `input` |
| `Medical_Device_Reporting_MDR_and_Vigilance_Decision_Evaluator` | Evaluate post-market complaints and adverse events for regulatory reportability under FDA 21 CFR 803 | `complaint_description, device_information, patient_impact` |
| `Medicare_Coverage_Analysis` | Determine qualifying status and billing justification. | `schedule_of_events` |
| `Medicare_Coverage_Request_IDE` | Prepare a request packet for CMS reimbursement of an IDE study. | `input` |
| `Mergers_and_Acquisitions_Due_Diligence_Auditor` | An agent designed to process data room artifacts, flag indemnity risks, and generate risk matrices f | `contract_text, transaction_type, jurisdiction` |
| `Meta_Prompt_Architect` | Design an L2 prompt that instructs a Prompt Engineer to create a domain-specific template achieving  | `end_task, policy_block` |
| `Metadata_Management` | Extract and store standardized metadata for reuse. | `crf_templates, mdr_schema` |
| `Metadynamics_Free_Energy_Surface_Architect` | Generates rigorous metadynamics simulation protocols for exploring complex free energy surfaces and  | `molecular_system, collective_variables, conditions` |
| `Metaphysical_Dialectical_Synthesizer` | Systematically executes a rigorous dialectical synthesis of mutually exclusive metaphysical framewor | `thesis_framework, antithesis_framework, antithesis, thesis` |
| `Micro-Frontend_Orchestration_Architect` | Designs robust, scalable micro-frontend architectures, addressing orchestration, state management, a | `application_requirements, input` |
| `Micro-Habit_Health_Coach` | Deliver a concise 7-day wellness plan combining meals, movement, and mindset. | `user_info` |
| `Microkinetic_Modeling_Architect` | Generates rigorous microkinetic models for complex catalytic cycles, calculating kinetic rate equati | `catalytic_system, reaction_network, operating_conditions` |
| `Modal_Logic_Possible_Worlds_Evaluator` | A highly rigorous prompt designed to systematically evaluate modal propositions and counterfactual s | `MODAL_PROPOSITION, ACCESSIBILITY_RELATION, ONTOLOGICAL_DOMAIN, accessibility_relation, modal_proposition, ontological_domain` |
| `Monitoring-Visit_Report_Generator` | Draft a monitoring visit report summarizing on-site activities, findings, follow-ups, and attachment | `input` |
| `Monitoring_Visit_Report_MVR_Quality_Critique` | You are a **Senior Monitoring Oversight Lead** conducting quality review of a draft **Monitoring Vis | `input` |
| `Multi-Agent_Orchestration_Architect` | Designs highly robust, scalable, and resilient multi-agent system (MAS) orchestration architectures, | `agent_ecosystem, interaction_dynamics, constraints_and_slas` |
| `Multi-CDN_Edge_Routing_Architect` | Strategic Genesis Architect persona for designing advanced, intelligent Multi-CDN routing and traffi | `primary_workload_type, routing_strategy, global_constraints` |
| `Multi-Cloud_Disaster_Recovery_Architect` | Designs active-active and active-passive multi-cloud disaster recovery architectures with rigorous R | `workload_criticality, current_topology, compliance_constraints, user_query` |
| `Multi-Region_Active-Active_Resilience_Architect` | Designs true active-active multi-region topologies, resolving global state conflict and replication  | `system_workload, cloud_provider` |
| `Multi-Region_K8s_Federation_Architect` | Acts as an Expert-level Genesis Architect to systematically engineer robust, fault-tolerant Multi-Re | `application_workloads, network_topology, synchronization_constraints` |
| `Multi-Tenant_BYOK_Envelope_Encryption_Architect` | Architects robust, multi-tenant "Bring Your Own Key" (BYOK) envelope encryption topologies for isola | `tenant_isolation_level, key_hierarchy_requirements, throughput_latency_sla, user_query` |
| `Multi-Tenant_Noisy_Neighbor_Mitigation_Architect` | Designs highly resilient architecture frameworks to detect, throttle, and mitigate noisy neighbor sc | `scale_context, input` |
| `Multi-Tenant_SaaS_Architecture_Designer` | Designs highly scalable, secure, and cost-efficient multi-tenant SaaS architectures, focusing on ten | `saas_requirements, input` |
| `Multi-Tier_Disaggregated_Memory_CXL_Architect` | Designs highly scalable, low-latency multi-tier disaggregated memory architectures leveraging Comput | `scale_requirements, compute_topology, user_query` |
| `Multiple_Endpoints_Regulatory_Strategy` | Review and summarize FDA guidance on multiple endpoints and multiplicity strategies. | `issues, therapeutic_area, multiplicity_issues` |
| `Multiplicity_Adjustment_Code_Generator` | Generate SAS code for multiplicity adjustments (Bonferroni, Holm, Hochberg). | `dataset, p_value_var, treatment_var, dataset_name, p_value_variable, treatment_variable` |
| `Multistudy_Resource_Capacity_Forecast_Plan` | Outline a data-driven approach for forecasting resources across multiple upcoming trials. | `historical_utilization` |
| `Myco-Alchemical_Arbitrageur` | An experimental High-Frequency Trading (HFT) entity that perceives market data as organic decay and  | `market_feed, decomposition_rate, transmutation_goal` |
| `NGS_Tumor_Profiling_Documentation` | Develop documentation supporting the clinical significance of mutations in an NGS-based tumor profil | `input` |
| `Natural_Language_Argument_Formalizer` | Systematically formalizes complex natural language philosophical arguments into rigorous symbolic lo | `natural_language_argument, target_logic_system` |
| `Negotiation_Coach` | Prepare the user for salary negotiations by roleplaying as a manager and offering feedback. | `input, macros, user_scenario` |
| `Net_Present_Value_Socratic_Tutor` | Guide the learner to derive and apply the NPV formula through short Socratic questioning. | `None` |
| `New_Drug_Application_NDA_Architect` | Formulates rigorous, compliant FDA New Drug Application (NDA) eCTD submissions for small molecule dr | `active_pharmaceutical_ingredient, intended_indication, clinical_evidence_summary, cmc_overview` |
| `Non-Abelian_Gauge_Theory_Perturbative_Expansion_Architect` | A highly specialized theoretical physics prompt for generating rigorous mathematical derivations of  | `gauge_group, loop_order, gauge_fixing_condition` |
| `Non-Adiabatic_Photodynamics_Architect` | Generates highly specialized non-adiabatic molecular dynamics protocols, computing excited-state dec | `molecule, excitation_energy, solvent_environment` |
| `Non-Human_Identity_Lifecycle_Architect` | Engineers robust zero-trust security architectures for managing the complete lifecycle of non-human  | `environment_topology, operational_scale` |
| `Non-Ideal_Fluid_Phase_Equilibria_Architect` | Generates rigorous thermodynamic models of multi-component, non-ideal fluid phase equilibria using a | `mixture_components, state_variables, equation_of_state` |
| `Non-Monotonic_Self-Correction_Meta-Reasoner` | An advanced meta-reasoning prompt that mandates a non-monotonic epistemic graph (Graph of Operations | `complex_problem_statement, epistemic_update, final_synthesis, reasoning_graph` |
| `Normative_Ethics_Stress_Tester` | Systematically stress-tests complex, applied ethical dilemmas through mutually exclusive normative m | `ethical_dilemma, primary_normative_framework, secondary_normative_framework` |
| `OAuth_Illicit_Consent_Grant_Forensics_Analyst` | Generates expert-level forensic analysis and response strategies for identifying and eradicating OAu | `audit_logs, application_manifests, post_compromise_telemetry` |
| `OT_SCADA_Security_Resilience_Architect` | Engineers robust zero-trust security architectures tailored for Operational Technology (OT) and Supe | `industrial_control_environment, operational_constraints` |
| `Objective_Skills_Assessment` | Design an objective skills checklist for a surgical stapler deployment lab. | `procedure_name` |
| `Off-Label_Information_Dissemination` | Prepare a mandatory disclosure statement for disseminating peer-reviewed articles on unapproved uses | `input` |
| `Offline-First_Synchronization_Architect` | Designs highly resilient, offline-first data synchronization and conflict resolution architectures f | `data_model, client_topology, conflict_resolution_requirements` |
| `Operational_Excellence_Communication_Framework` | improved collaboration strategy between Business Development, Clinical Operations, and Data Manageme | `current_processes` |
| `Operational_Excellence_Risk_Sweep` | Deliver a 90-day action plan to cut cycle time and reduce recruitment failure. | `trial_metrics` |
| `Optimize_ePRO_Form_Design` | Improve ePRO form usability and data quality. | `input` |
| `Organometallic_Catalytic_Cycle_Architect` | Generates rigorous organometallic catalytic cycles, deriving complex kinetic rate equations and anal | `precatalyst, reactants, conditions, reaction_type` |
| `Orphan_Drug_Designation_Architect` | Formulates a compelling FDA Orphan Drug Designation (ODD) request incorporating rigorous epidemiolog | `drug_mechanism, disease_target, epidemiological_data` |
| `PAW_Phase_1_-_Tactical_Recon` | Phase 1 of the Principal Architect Workflow (PAW). Analyzes TODO.md and file structure to generate a | `todo_content, file_structure` |
| `PAW_Phase_2_-_Architectural_Blueprint` | Phase 2 of the Principal Architect Workflow (PAW). Designs the solution based on the Tactical Brief. | `tactical_brief, relevant_source_code` |
| `PAW_Phase_3_-_Precision_Strike` | Phase 3 of the Principal Architect Workflow (PAW). Implements the design spec with surgical accuracy | `design_spec, relevant_source_code, answer` |
| `PAW_Phase_4_-_Quality_Assurance_Log` | Phase 4 of the Principal Architect Workflow (PAW). Verifies the implementation and updates the TODO  | `implementation_code, todo_content` |
| `PCB_Layout_Topology_Reviewer` | A prompt designed to evaluate printed circuit board schematics for signal integrity, electromagnetic | `pcb_specifications, signal_types, layout_description` |
| `PII_Tokenization_Vault_Architect` | Architect highly secure, isolated, and scalable PII (Personally Identifiable Information) tokenizati | `compliance_frameworks, throughput_latency_sla, encryption_key_management, user_query` |
| `PMA_Post-approval_Reporting` | Compile a summary of post-approval requirements, including clinical study data, manufacturing change | `input` |
| `PMA_Supplement_CBE` | Draft a 'Special PMA Supplement - Changes Being Effected' for safety warnings. | `input` |
| `Panel_Debate` | Host a simulated debate among three experts on a chosen topic. | `input` |
| `Parallel_Review_Request` | Draft an email requesting enrollment in the Parallel Review program. | `input` |
| `Part_11_Closed_System_Audit` | Audit a software supplier's closed system for electronic record integrity. | `input` |
| `Passwordless_FIDO2_WebAuthn_Architect` | Designs highly secure, phishing-resistant passwordless authentication architectures utilizing FIDO2  | `application_context, identity_provider, macros, var` |
| `Patent_Term_Restoration_Eligibility` | Determine if a medical product's review period qualifies for patent term restoration. | `input` |
| `Patient-Centric_BYOD_ePRO_Workflow` | Design a streamlined ePRO workflow that supports a BYOD model and maximizes patient compliance. | `input` |
| `Patient_Recruitment_and_Diversity_Acceleration_Plan` | Boost enrollment and improve demographic diversity in a stalled Phase III study. | `None` |
| `Payment-Process_Risk_Assessment_and_Mitigation` | Identify weak points in the site-payment workflow and propose mitigations. | `kpi_metrics, technology_stack, workflow_description` |
| `Payment_Gateway_Idempotency_Architect` | Designs highly resilient, strictly idempotent payment processing architectures capable of handling d | `payment_rails, throughput_requirements, consistency_constraints` |
| `Payment_Reconciliation_and_Discrepancy_Report` | Identify and categorize payment discrepancies before study close-out. | `cta_budget, payment_ledger, site_queries` |
| `Pediatric_Investigational_Plan_PIP_Architect` | Synthesizes scientific rationale and clinical development strategy into a comprehensive, EMA-complia | `adult_clinical_data, mechanism_of_action, target_pediatric_condition, proposed_pediatric_studies, formatting_constraints, inputs, instructions, persona` |
| `Peer-Review_Checklist_for_Manuscript_Methods` | Provide a structured checklist for reviewing the statistical methods section of a manuscript. | `manuscript_excerpt` |
| `Personalized_Investigator-Outreach_Email_Generator` | Craft a tailored outreach email to potential investigators. | `CRO_NAME, city_country, investigator_name, recent_relevant_trials, site_name, sponsor_name, study_synopsis, unique_site_strength` |
| `Petabyte-Scale_Data_Lakehouse_Architect` | Designs highly scalable, governed, and performant Data Lakehouse architectures for petabyte-scale an | `data_requirements, input` |
| `Petabyte_Scale_Distributed_Object_Storage_Architect` | Designs massively scalable, highly available distributed object storage architectures (similar to S3 | `storage_requirements, consistency_model, deployment_topology, user_query` |
| `Pharmacovigilance_Risk_Management_Plan_Architect` | Acts as a Principal Pharmacovigilance Risk Management Scientist to synthesize complex post-market sa | `product_profile, safety_specification, regulatory_framework` |
| `Pharmacovigilance_Safety_Signal_Prioritization` | Detect emerging safety signals and recommend follow-up actions. | `ae_listing, benchmark_rates` |
| `Phase_II_III_SAP_Skeleton` | Provide a high-level statistical analysis plan skeleton for an adaptive Phase II/III trial. | `trial_overview` |
| `Phase_II_Oncology_DMP` | Create a Data Management Plan for a Phase II oncology study. | `input` |
| `Physics-Informed_Neural_Network_PINN_Architect` | Formulates rigorous, structurally sound physics-informed neural network architectures for solving st | `GOVERNING_EQUATIONS, DOMAIN_AND_BOUNDARIES, ARCHITECTURE_CONSTRAINTS, architecture_constraints, domain_and_boundaries, governing_equations` |
| `Pinnacle_21_Conformance_Resolution_Architect` | Automates the resolution of complex Pinnacle 21 (P21) conformance rule rejections by analyzing valid | `p21_rule_id, issue_description, dataset_context, target_standard, constraints, instructions, persona` |
| `Pitch-Deck_Outliner` | Draft a high-impact, 10-slide VC pitch deck outline. | `business_idea, macros` |
| `Pixar_Story_Spine_Outline` | Guide the model in creating a short Pixar-style story outline for middle-grade readers. | `topic` |
| `Platform_Ecosystem_Network_Effects_Architect` | Formulates highly rigorous platform ecosystem strategies maximizing direct, indirect, and cross-side | `platform_value_proposition, market_friction_and_homing, monetization_and_subsidies` |
| `Platform_Engineering_IDP_Architect` | Designs scalable, developer-centric Internal Developer Platforms (IDPs) utilizing platform engineeri | `organization_context, target_capabilities, operational_constraints` |
| `Polyglot_Monorepo_Build_Orchestration_Architect` | Designs highly scalable, hermetic build and deployment orchestrations for massive-scale enterprise p | `monorepo_scale, ci_cd_constraints, security_boundaries, Aegis` |
| `Polynomial_Optimization_SDP_Relaxation_Architect` | Formulates highly rigorous, computationally tractable exact global optimization models using Lasserr | `POLYNOMIAL_OBJECTIVE, POLYNOMIAL_CONSTRAINTS, RELAXATION_ORDER, polynomial_constraints, polynomial_objective, relaxation_order` |
| `Portfolio-Level_Clinical_Operations_Roadmap` | Provide a 12‑month roadmap for a portfolio of clinical trials. | `None` |
| `Portfolio_KPI_Dashboard_Brief` | Produce a one-page executive dashboard of enrollment, deviation, SDV, and budget KPIs for live studi | `input, macros, portfolio_data` |
| `Portfolio_Resource_and_Budget_Forecast` | Generate a rolling 12‑month FTE and budget forecast for active trials. | `enrollment_deltas, historic_burn_rates` |
| `Post-Market_Safety_Signal_Trending` | Analyze post-market data to identify emerging safety signals. | `input` |
| `Post-Merger_Integration_Synergy_Architect` | Architects rigorous, actionable Post-Merger Integration (PMI) synergy realization plans, quantifying | `target_operating_model, financial_synergies, cultural_integration` |
| `Post-Mortem_Incident_Report_Summary` | Summarize technical post-mortems for a general company audience. | `cause, post_mortem_details` |
| `Post-Quantum_Cryptography_Migration_Architect` | Formulates rigorous architectural strategies and roadmaps for migrating enterprise cryptographic sys | `current_cryptographic_inventory, critical_assets_and_data_flows, regulatory_and_compliance_constraints` |
| `Pre-IND_Meeting_Preparation` | Draft Pre-IND briefing package and questions. | `preclinical_data` |
| `Predictive_Auto-Scaling_Machine_Learning_Architect` | Designs highly resilient, ML-driven predictive auto-scaling topologies to eliminate cold starts and  | `workload_patterns, infrastructure_constraints, predictive_model_specifications, user_query` |
| `Predictive_Multidimensional_Spectroscopy_Architect` | Generates predictive structural modeling and analytical spectral profiles for novel compounds, synth | `molecular_structure, spectroscopic_techniques, solvent_system` |
| `Predictive_RFM_Churn_Mitigation_Architect` | Constructs deeply rigorous, predictive churn mitigation workflows using advanced Recency-Frequency-M | `customer_dataset, financial_metrics, growth_objectives` |
| `Premarket_Approval_PMA_Preparation` | Draft a detailed summary of a PMA application, including clinical investigation results and manufact | `input` |
| `Prepare_Pathology_Slides_and_Reporting_Plan` | Plan slide preparation and review activities for a GLP cardiovascular stent study. | `interface_evaluation` |
| `Preventing_Technical_Debt` | Justify technical debt reduction to non-technical stakeholders using financial analogies. | `refactoring_percentage, timeframe` |
| `Principal_Architect_Task_Execution` | A Principal Architect persona for executing tasks from TODO.md with strict adherence to SOLID, DRY,  | `todo_content, project_context` |
| `Principal_Python_Developer` | A Principal Engineer's guide to Python development, focusing on architecture, decoupling, robustness | `input` |
| `Principal_Rust_Developer` | A Principal Engineer's guide to Rust development, focusing on type-driven architecture, error handli | `input, Connected` |
| `Principal_Science_Communicator_Analogy_Engine` | Deconstruct complex concepts and map them to intuitive physical realities using rigorous cognitive s | `concept, target_audience, macros` |
| `Principal_TypeScript_Developer` | A Principal Engineer's guide to TypeScript development, focusing on type-driven architecture, runtim | `input` |
| `Privacy_Act_Auditing` | Draft a notice for a new FDA Privacy Act Record System. | `input` |
| `Private_Equity_LP_Co-Investment_Structuring_Architect` | Architects highly rigorous, quantitative Limited Partner (LP) co-investment structures, enforcing op | `deal_parameters, lp_commitments, return_hurdles` |
| `Private_Equity_Value_Creation_Architect` | Designs highly rigorous, quantitative value creation plans and LBO optimization models for private e | `target_financials, capital_structure, operational_levers` |
| `Proactive_Risk_Heat-Map_for_Decentralized_Virtual_Trials` | Visualize portfolio risks and propose mitigation actions. | `portfolio_snapshot` |
| `Process_Validation_IQ_OQ_PQ_Protocol_Architect` | Formulates highly rigorous, FDA 21 CFR 820.75 and ISO 13485 compliant IQ/OQ/PQ process validation pr | `equipment_description, process_parameters, quality_attributes, sampling_plan, anticipated_worst_case, macros` |
| `Product_Brief_Template` | Outline the high-level vision, features, and architecture for a new software project. | `architecture, context_notes, features, vision` |
| `Project_Brief_for_Epic` | Summarize a project epic with key features, rules, and success metrics. | `business_rules, data_models, key_features, project_description, success_metrics` |
| `Project_Charter_and_Scope_Definition` | Create a complete project charter summarizing background, objectives, scope, deliverables, and key r | `budget, business_outcome, deadline, project_description, project_name, stakeholders, macros` |
| `Project_Configuration_Maven_Setup` | Set up a Maven project structure and pom.xml file with necessary Selenium client libraries. | `java_version, test_framework, artifactId` |
| `Project_Init_Skeleton_Construct_Architect` | A Principal Cloud-Native Architect's blueprint for initializing secure, scalable, and 12-Factor comp | `input, project_requirements` |
| `Project_Memory_Notes` | Maintain a running log of architectural decisions and contextual notes for the project. | `None` |
| `Project_Review_Checklist` | Verify completion of a coding project before finalizing. | `None` |
| `Project_Starter_Pack_Prompts` | Provide ready-to-copy prompt templates for common project documentation. | `alternatives, budget, business_outcome, deadline, decision, decision_date, feature_area, project_description, project_name, stakeholders` |
| `Prompt-Writing_Best-Practice_Checklist` | Summarize key elements of effective prompt design. | `None` |
| `PromptCrafter_GPT` | Generate three distinct, best-practice prompts for a given topic. | `optional_flags, target_audience, topic` |
| `Prompt_Engineer_Fact_Checker` | Rewrite an original prompt so it is clear, fully sourced and produces accurate answers with inline c | `original_prompt` |
| `Prompt_Engineer_Template` | Produce an L3 task template that enables a Task Prototyper to fulfil `{{ end_task }}`. | `end_task, generated_prompt, token_budget_l3, answer, thinking` |
| `Protocol-to-TS_Generator` | Automates the extraction of trial design parameters from a clinical protocol for the CDISC SDTM Tria | `protocol_synopsis` |
| `Protocol_Amendment_Rationale_Drafter` | Drafts scientifically and ethically sound rationales for clinical trial protocol amendments. | `proposed_changes, scientific_justification, safety_impact, formatting_constraints, inputs, instructions, persona` |
| `Protocol_Deviation_Reporting` | Identify and report protocol deviations from clinical trial logs. | `trial_logs, macros` |
| `Protocol_Optimization_and_Risk_Simulation` | Evaluate a draft clinical protocol and simulate the effects of simplifying key elements. | `draft_protocol` |
| `Protocol_Reviewer_and_Gap-Analysis_Coach` | Evaluate a clinical-trial protocol for patient experience, site feasibility, and regulatory complete | `protocol_text_or_nct` |
| `Protocol_Section_Refinement` | Improve the eligibility criteria section of an IVD performance trial protocol. | `condition, draft_section` |
| `Protocol_to_CDISC_USDM_v3_0_Converter` | Convert unstructured Clinical Research Protocol text into a structured CDISC USDM v3.0 JSON object. | `protocol_text` |
| `Protocol_to_USDM_Stage_1_-_Metadata` | Extract Study Level Metadata and Design from Protocol. | `protocol_text` |
| `Protocol_to_USDM_Stage_2_-_Rationale` | Extract Objectives, Endpoints, and Eligibility Criteria. | `protocol_objectives_text` |
| `Protocol_to_USDM_Stage_3_-_Workflow` | Extract Encounters and Activities from Schedule of Activities. | `protocol_soa_text` |
| `Protocol_to_USDM_Stage_4_-_Concepts` | Map Activities to Biomedical Concepts. | `activities_json` |
| `Protocol_to_USDM_Stage_5_-_Assembly` | Assemble the final USDM JSON from previous stages. | `metadata_json, rationale_json, workflow_json, concepts_json` |
| `Psychometric_Validation_Methodology` | Apply Rasch and IRT models for COA validation and psychometric evidence generation. | `dataset_description, instrument_name, target_population, coa_instrument, dataset_characteristics` |
| `Public_Hearing_Participation` | Complete a Notice of Participation for a formal evidentiary public hearing. | `input` |
| `Python_Concurrency_Mastery` | A Principal-level guide to mastering Python concurrency, focusing on AsyncIO, Structured Concurrency | `input` |
| `Python_Hexagonal_Architecture` | A Principal-level guide to decoupling Python systems using Hexagonal Architecture, Protocols, and De | `input` |
| `Python_Performance_Optimization` | A Senior-level guide to optimizing Python code, focusing on profiling, memory management, and GIL wo | `input` |
| `QC_Listing_Cross-check_Prompt` | Automate a listing and QC cross-check between independent R and SAS runs. | `dataset_paths` |
| `QM_MM_Hybrid_Catalytic_Modeling_Architect` | Generates automated hybrid Quantum Mechanics/Molecular Mechanics (QM/MM) catalytic models, rigorousl | `active_site_system, mm_environment, theoretical_level, input, macros` |
| `Qualitative_Interview_Guide_Generator` | Draft a qualitative patient interview guide for concept elicitation and cognitive debriefing. | `areas_of_interest, disease, pro_instrument, target_disease` |
| `Quality-Improvement_RCA_Action_Plan` | Identify root causes of a recurring defect and propose a 90‑day corrective‑action roadmap. | `defect_data_csv, prior_mitigation` |
| `Quality_System_Audit` | Generate an internal audit checklist or report focusing on design controls, production processes, an | `input` |
| `Quality_System_Evaluation_MRA` | Generate a quality system evaluation report for a manufacturer under the US-EC MRA. | `input` |
| `Quantitative_Black-Scholes_Options_Pricing_Architect` | Architects mathematically rigorous Black-Scholes option pricing models, calculating theoretical valu | `underlying_asset_parameters, contract_specifications, risk_free_rate_environment, input` |
| `Quantitative_Buy-and-Build_Roll-Up_Strategy_Architect` | Architects rigorous, highly quantitative Buy-and-Build and industry Roll-Up strategies, modeling syn | `platform_acquisition_details, add_on_target_criteria, synergy_integration_targets, macros` |
| `Quantitative_Corporate_Portfolio_Divestiture_Architect` | Optimizes corporate portfolios and divestitures using rigorous financial modeling. | `portfolio_assets, financial_constraints, market_multiples` |
| `Quantitative_Credit_Risk_Expected_Loss_Architect` | Architects robust, quantitative credit risk modeling frameworks to calculate Expected Loss (EL) and  | `credit_portfolio, default_probability_metrics, recovery_assumptions` |
| `Quantitative_Enterprise_Value-at-Risk_Architect` | Architects rigorous enterprise risk management frameworks using Monte Carlo simulation to calculate  | `portfolio_exposure, market_volatility, tail_risk_assumptions` |
| `Quantitative_Enterprise_Working_Capital_CCC_Architect` | Formulates rigorous quantitative frameworks for optimizing the Cash Conversion Cycle (CCC) and worki | `company_financials, supply_chain_dynamics, market_conditions` |
| `Quantitative_FX_Hedging_Strategy_Architect` | Formulates rigorous corporate Foreign Exchange (FX) risk mitigation strategies, optimizing hedging p | `currency_exposures, macroeconomic_volatility_forecast, hedging_constraints_and_objectives` |
| `Quantitative_LBO_Modeling_Architect` | Architects mathematically rigorous Leveraged Buyout (LBO) financial models, optimizing debt schedule | `transaction_assumptions, operating_model, exit_assumptions` |
| `Quantitative_M_A_Accretion_Dilution_Architect` | Architects rigorous M&A financial models, executing advanced accretion/dilution analyses, target val | `target_financials, acquirer_capital_structure, synergy_and_integration_assumptions` |
| `Quantitative_M_A_Target_Screening_Architect` | Architects rigorous quantitative screening models for Mergers & Acquisitions (M&A) target identifica | `investment_mandate, quantitative_screening_criteria, valuation_multiples` |
| `Quantitative_Markowitz_Portfolio_Optimization_Architect` | Architects rigorous quantitative Markowitz Mean-Variance Optimization models, evaluating optimal ass | `asset_universe, covariance_matrix_estimates, investor_preferences` |
| `Quantitative_Non-Market_Strategy_Optimization_Architect` | Architects mathematically rigorous non-market strategies, optimizing corporate lobbying expenditures | `regulatory_environment, corporate_objectives, stakeholder_matrix` |
| `Quantitative_Private_Equity_Dividend_Recapitalization_Architect` | Architects rigorous quantitative Private Equity Dividend Recapitalization models, evaluating optimal | `portfolio_company_financials, existing_capital_structure, recapitalization_objectives` |
| `Quantitative_Product_Portfolio_Optimization_Architect` | Architects highly rigorous, quantitative product portfolio optimization strategies, integrating mult | `product_portfolio_data, resource_constraints, strategic_objectives` |
| `Quantitative_Real_Options_Valuation_Architect` | Models complex managerial flexibility in capital budgeting by designing mathematically rigorous Real | `underlying_project_cash_flows, volatility_estimates, options_parameters` |
| `Quantum-Safe_Cryptography_Migration_Architect` | Designs highly secure, crypto-agile migration architectures to transition enterprise systems from cl | `current_cryptographic_inventory, performance_latency_constraints, system_components, user_query` |
| `Quantum_Baroque_Garden_Architect` | Designs hyper-complex vertical garden structures that merge Baroque aesthetics with quantum probabil | `space_dimensions, light_conditions, aesthetic_preference` |
| `Quantum_Chemical_Transition_State_Architect` | Generates automated quantum mechanical transition state analyses and complex kinetic rate equations  | `reactants, conditions, reaction_type` |
| `Quantum_Key_Distribution_Network_Architect` | Designs highly secure, scalable Quantum Key Distribution (QKD) network topologies to safeguard sensi | `network_topology, cryptographic_constraints, threat_model, user_query` |
| `Quarterly_CRO_KPI_Executive_Brief` | Present key operational KPIs and recommended actions for the quarterly review. | `functional_comments, kpi_definitions, operational_dataset` |
| `Quarterly_Innovation_Radar_for_Decentralized_and_Hybrid_Trials` | Identify and prioritize technologies for decentralized or hybrid trials. | `input` |
| `RACI_Mapper` | Clarify team responsibilities using a RACI matrix. | `project_phase, tasks` |
| `RA_QA_Integrated_Quality_System_Audit` | Prepare for a combined FDA QSR and EU MDR/IVDR audit by identifying quality-management gaps and reco | `qms_documents, macros` |
| `RBQM_Anomaly_Detection` | Identify data outliers, anomalies, and atypical patient patterns in real-time across clinical trial  | `input, site_data` |
| `README_Generator` | Scan an entire repository and produce a polished README.md covering everything a new developer needs | `repo_access` |
| `RFP_Executive-Summary_Generator` | Produce a persuasive executive summary for an RFP response. | `rfp_synopsis` |
| `RTA_Checklist_Preparation` | Annotate the RTA checklist with page numbers and sections where requirements are addressed in a 510( | `input` |
| `RWE_Regulatory_Framework_Summary` | Review the FDA Real-World Evidence (RWE) Framework and fitness-for-use criteria. | `data_source, use_case, intended_use, rwd_source` |
| `Rapid-Risk-Matrix` | Act as a risk-manager. Objective: assess “[PROJECT/PROCESS]”. | `input` |
| `Rapid_Process_Diagnostic_Lean_Improvement_Plan` | Create a concise process review and improvement roadmap. | `avg_cycle_time, current_volume, pain_points, process_name, target_outcome` |
| `Rapid_Proposal_Builder` | Draft a concise capabilities and budget proposal for a prospective client. | `client_name, input, client_details, macros, project_requirements` |
| `Raw-to-SDTM_Auto-Mapper` | Intelligently maps raw EDC variables to standard SDTM variables based on fuzzy logic and context. | `target_domain, raw_variables` |
| `Real-Time_Adjudication_Visibility_Dashboard` | Design a dashboard that provides real-time visibility into clinical endpoint adjudication workflows. | `input, user_query` |
| `Real-Time_Bidding_AdTech_Architect` | Designs ultra-low-latency, highly concurrent Real-Time Bidding (RTB) architectures for AdTech platfo | `qps_target, latency_sla, data_gravity, user_query` |
| `Real-Time_Fraud_Decision_Engine_Architect` | Designs highly scalable, ultra-low-latency real-time fraud decision engines integrating stream proce | `traffic_profile, data_sources, model_characteristics, user_query` |
| `Real-Time_Game_State_Synchronization_Architect` | Designs highly responsive, authoritative, and partition-tolerant state synchronization architectures | `game_genre_and_pacing, network_topology, latency_and_consistency_targets` |
| `Real-Time_ML_Feature_Store_Architect` | Designs highly scalable, low-latency Feature Stores unifying online inference and offline training,  | `feature_requirements, serving_scale, data_sources` |
| `Real-Time_Stream_Processing_Architect` | Designs highly scalable, fault-tolerant real-time data streaming and processing architectures. | `streaming_requirements, input` |
| `Real_Options_Valuation_Architect` | Designs rigorous Real Options Valuation (ROV) frameworks to value strategic flexibility under extrem | `investment_scenario, uncertainty_factors, strategic_flexibilities` |
| `Reclassification_Petitioning` | Prepare a statement of the basis for disagreement with a current device classification. | `input` |
| `Recursive_Abductive_Hypothesis_Synthesizer` | An advanced meta-reasoning architecture that executes a Counterfactual Abductive Synthesis Topology  | `anomalous_phenomenon, axiomatic_framework` |
| `Recursive_Metacognitive_Error_Corrector` | An advanced meta-reasoning architecture that executes a Step-Back Abstraction Graph to identify logi | `initial_output, objective_constraints` |
| `Red-Team_Stress-Test_Simulation` | Assemble a ruthless panel of adversaries (Hacker, Competitor, Regulator) to dismantle a strategy. | `input, concept` |
| `Red_Account_Turnaround_Strategy` | Draft a re-engagement playbook for at-risk high-value accounts. | `account_details` |
| `Refactoring_Architect` | A Principal Software Architect's guide to surgical refactoring, focusing on decoupling, testability, | `input, code_snippet, macros` |
| `Reflexion_Agent_Bug_Patch` | Locate and fix a bug using a structured reflexion workflow. | `code, code_snippet, macros` |
| `Regenerative_Medicine_Advanced_Therapy_RMAT_Designation_daf043a1` | Architects compelling RMAT designation requests to the FDA for cell therapies and tissue engineering | `therapy_description, target_disease, preliminary_clinical_evidence, standard_of_care_comparison` |
| `Regulatory-Change_Impact_Analysis` | Assess how a new regulation affects company operations and outline a phased response plan. | `COMPANY, EFFECTIVE_DATE, INDUSTRY_AND_REGION, REGULATION_NAME, company_profile, regulation_text` |
| `Regulatory-Landscape_Radar` | Provide a weekly snapshot of regulatory developments relevant to early‑phase oncology and rare‑disea | `portfolio_snapshot` |
| `Regulatory-Risk_ESG_Impact_Dashboard_Builder` | Aggregate regulatory changes and ESG metrics into a compliance risk dashboard. | `esg_baseline, reg_updates, risk_tolerance, study_portfolio` |
| `Regulatory_Commercial_Barrier_Mapping` | Assess hurdles for launching `<device>{{ device }}</device>` in major markets. | `device, markets` |
| `Regulatory_Compliance_Summary` | Summarize key financial disclosure changes for a specific regulation. | `annual_report, industry, regulation` |
| `Regulatory_Compliance_Verification` | Verify electronic records and signatures against 21 CFR Part 11. | `audit_logs, system_specs` |
| `Regulatory_Filing_Draft_Builder` | Produce a regulator‑ready draft document using provided financials and risk data. | `DATE, DOCUMENT_TYPE, REGULATOR, SPECIFIC_GUIDELINE, financial_data, prior_filing, risk_memo` |
| `Regulatory_Gap-Analysis_Comparator` | Compare sterility-assurance requirements across key standards and guidance. | `device_description, text` |
| `Regulatory_Gap_Analysis` | Assess regulatory compliance gaps in trial data processes. | `input` |
| `Regulatory_Imaging_Charter_Generator` | Generate an imaging charter that satisfies FDA and ISO requirements. | `endpoint_description, modalities, regions, study_overview` |
| `Regulatory_Imaging_Data_Package` | Assemble the imaging section of a PMA or 510(k) submission. | `study_summary, metrics_data, reader_agreement` |
| `Regulatory_Query_Response_Drafter` | Drafts precise, evidence-backed, and regulatory-compliant responses to Health Authority (e.g., FDA/E | `health_authority_query, clinical_source_data, previous_submission_context, formatting_constraints, inputs, instructions, persona` |
| `Regulatory_Radar_Impact_Report` | Track and assess recent regulatory changes that may impact the company. | `company_profile, compliance_posture` |
| `Regulatory_Submission_Support` | Draft regulatory-ready documentation for a medical device submission. | `device_description` |
| `Regulatory_and_Competitive_Intelligence_Briefing` | Provide a Monday-morning briefing on regulatory changes and competitor moves that may affect decentr | `company_name, input` |
| `Regulatory_and_Validation_Checklist` | Compile a compliance checklist for digital trial data integrations. | `input` |
| `Reinforcement_Learning_Reward_Function_Architect` | Designs mathematically rigorous, sparse/dense reward structures for multi-agent RL environments, exp | `environment_dynamics, agent_objectives, known_exploits` |
| `Reporting_and_Maintenance_Custom_Reports` | Integrate reporting libraries and screenshot utilities to capture execution evidence. | `framework, report_format` |
| `Repository_Foundation_Developer_Experience_Analysis` | Analyze the repository's foundation and developer experience to prepare it for future growth and eas | `repo_structure, file_contents, macros` |
| `Request_for_Designation_RFD_Submission` | Draft RFD for combination products. | `product_desc` |
| `RequirementsBot_Prompt` | Guide an AI assistant to inspect a repository and generate a complete `REQUIREMENTS.md` file. | `repository_url` |
| `Retrieval-Augmented_Answer_Composer` | Provide concise, grounded answers using only supplied knowledge-base files, with strict security bou | `FILES, QUESTION, knowledge_base, macros, user_query` |
| `Reverse_Brainstorming` | Flip negative ideas into constructive solutions. | `problem` |
| `Riemann_Surface_Analytic_Continuation_Architect` | Systematically engineers rigorous analytic continuations and rigorously models Riemann surfaces for  | `function_definition, topological_constraints` |
| `Riemannian_Manifold_Curvature_Deriver` | Systematically computes intrinsic curvature properties (Christoffel symbols, Riemann curvature tenso | `manifold_definition, metric_tensor, derivations_requested, computation_request, manifold_context` |
| `Risk-Based_Monitoring_Data_Evaluation` | Remote evaluation of accumulating trial data to identify outliers and data integrity problems. | `clinical_data, monitoring_plan, risk_assessment` |
| `Risk-Based_Monitoring_RBM_Plan_Builder` | Develop a site-level risk-based monitoring plan with risk matrix, KRIs, and adaptive strategy. | `input` |
| `Risk-Based_Monitoring_and_Quality_Plan` | Develop a risk-based monitoring plan for a Phase II oncology trial. | `None` |
| `Risk-Based_Quality_Management_Plan` | Create a concise RBQM plan for a first‑in‑human Phase I healthy‑volunteer study. | `study_overview` |
| `Risk-Based_Site_Performance_Dashboard` | You are an experienced **Clinical Monitoring Manager** at a global CRO overseeing several Phase II o | `input, site_data` |
| `Risk-Based_Test_Case_Suite` | Generate a test-case suite prioritizing controls for high and medium residual risks. | `device_name, hazard_analysis_table` |
| `Risk-Based_Vendor_Performance_Improvement_Plan` | Raise overall vendor performance and reduce operational risk. | `audit_reports, contract_terms, vendor_scorecards` |
| `Risk_Assessment_Expert` | Provide a comprehensive biocompatibility risk assessment for a specified device. | `medical_device_type` |
| `Risk_Management_Analysis` | Perform a risk analysis (e.g., PHA) to identify potential hazards, hazardous situations, and mitigat | `input` |
| `Risk_and_Pre-Mortem_Analysis` | Identify early failure points and mitigation strategies for a project or study. | `project_name, project_summary` |
| `Robust_Optimization_Min-Max_Architect` | Formulates highly rigorous exact robust counterparts for optimization problems subject to bounded pa | `NOMINAL_PROBLEM, UNCERTAIN_PARAMETERS, UNCERTAINTY_SET_GEOMETRY, nominal_problem, uncertain_parameters, uncertainty_set_geometry` |
| `Rolling_Resource_Capacity_Forecast` | Generate a 12-month forecast of FTE demand and utilization by function and region. | `headcount, project_list, time_tracking_csv` |
| `Rollout_Risk_Matrix` | Assess rollout risks and propose key mitigation actions. | `risk_list` |
| `Rubber_Duck_Debugger` | Guide developers through self-explanation to uncover bugs before providing fixes. | `input` |
| `Rust_Architectural_Patterns` | Deep dive into Typestate and Zero-Cost FFI abstractions for Principal-level Rust. | `input, Armed, Flying, Idle, State, T, Wrapper, native_ctx_t` |
| `SAE_Patient_Narrative_Drafter` | Synthesizes complex clinical trial data into regulatory-compliant Serious Adverse Event (SAE) patien | `trial_protocol_summary, patient_data, macros` |
| `SAE_and_Safety_Reporting` | Analyze SAEs for expedited reporting criteria. | `sae_report, macros` |
| `SAE_and_Unanticipated_Problem_Reporting_SOP` | Develop a standard operating procedure for reporting serious adverse events and unanticipated proble | `study_context, sponsor_requirements` |
| `SCAMPER_Ideation_Coach` | Break creative blocks using SCAMPER techniques. | `input, macros, user_input` |
| `SDTM_Cardiovascular_Device_Mapping_Architect` | Automates the complex algorithmic mapping of raw Electronic Data Capture (EDC) data and external dev | `device_type, raw_edc_data, external_telemetry_data, target_standard, constraints, instructions, persona` |
| `SDTM_Concomitant_Medications_Mapping_Architect` | Automates the complex algorithmic mapping of raw EDC Concomitant Medication data and WHODrug coding  | `raw_edc_data, whodrug_coding_data, target_sdtm_version, constraints, instructions, persona` |
| `SDTM_Device_Deficiencies_Mapping_Architect` | Automates the algorithmic mapping and evaluation of raw Medical Device deficiency reports from EDC s | `edc_deficiency_data, device_dictionary_data, target_sdtm_version, constraints, instructions, persona` |
| `SDTM_Medical_Device_Mapping_Architect` | Automates the complex algorithmic mapping of raw EDC and external medical device data into CDISC SDT | `source_data_schema, target_domains, cdisc_ig_version, constraints, instructions, persona` |
| `SDTM_Pharmacokinetics_Mapping_Architect` | Automates the complex algorithmic mapping of raw EDC and external vendor pharmacokinetic data into C | `vendor_data_extract, edc_dosing_data, target_sdtm_version, constraints, instructions, persona` |
| `SDTM_Protocol_Deviation_Modeling_Architect` | Automates the complex algorithmic mapping of raw EDC and CTMS protocol deviation data into the CDISC | `raw_deviation_data, protocol_schedule, target_sdtm_version, constraints, instructions, persona` |
| `SDTM_Trial_Design_Mapping_Architect` | Automates the complex algorithmic mapping and generation of CDISC SDTM Trial Design domains (TA, TE, | `protocol_schedule, edc_metadata, sdtm_ig_version, constraints, instructions, persona` |
| `SOLID_Codebase_Analysis` | Evaluate code against SOLID principles and suggest refactoring tasks. | `codebase` |
| `SOP_Gap_Analysis` | Identify gaps in data management standard operating procedures. | `input` |
| `SOP_and_TMF_Document_Synthesis` | Provide a quick retrieval and synthesis of information from specific internal SOPs and TMF documents | `documents, query, context_documents` |
| `SRE_Incident_Postmortem_RCA_Architect` | Formulates rigorous, blameless Site Reliability Engineering (SRE) incident postmortems and Root Caus | `incident_timeline, system_architecture, root_cause_hypotheses` |
| `SaMD_AI_ML_PCCP_Architect` | Design rigorous Predetermined Change Control Plans (PCCP) for AI/ML-enabled Software as a Medical De | `device_description, proposed_modifications, algorithm_architecture` |
| `SaMD_Cybersecurity_Vulnerability_Assessor` | Evaluates Common Vulnerabilities and Exposures (CVEs) in Software as a Medical Device (SaMD) against | `cve_data, system_architecture, intended_use` |
| `Sample-Size_Randomization_Strategy` | Determine sample size and recommend a randomization strategy for a clinical trial. | `dropout_rate, response_rate_active, response_rate_control` |
| `Scenario-Based_Clinical-Trial_Cash-Flow_Forecast` | Model 12-quarter cash flows under baseline, inflation, and recruitment slowdown scenarios. | `base_costs, base_revenue, notes, starting_cash` |
| `Scenario-Based_Financial_Navigator` | Generate long-term wealth scenarios and actionable tactics. | `user_data` |
| `Scenario-Based_Microlearning_Series` | Design short interactive modules that help CRO staff apply GCP principles correctly during site visi | `audience_role` |
| `Scenario_Modeling_Sensitivity_Analysis` | Create three financial scenarios (Conservative, Base, and Aggressive) based on historical data and m | `cac, churn, decision` |
| `Schwinger-Dyson_Equation_Architect` | A highly specialized theoretical physics prompt for the rigorous mathematical derivation of non-pert | `target_lagrangian, field_variable, n_point_function` |
| `Schwinger-Keldysh_Non-Equilibrium_Path_Integral_Architect` | Formulates the rigorous Schwinger-Keldysh (in-in) closed-time path integral formalism to compute rea | `lagrangian_density, initial_density_matrix, observable, user_query` |
| `Second-Order_Thinking_Oracle` | Assess first- and second-order effects of a decision. | `decision` |
| `Secondary_Endpoint_Multiplicity_Adjuster` | Apply Bonferroni-Holm (step-down) procedure to secondary efficacy endpoints. | `endpoints, p_values, raw_p_values, secondary_endpoints` |
| `Secure_Supply_Chain_Attestation_Architect` | Designs highly rigorous, cryptographically verifiable software supply chain architectures to ensure  | `build_environment, compliance_requirements, ecosystem_dependencies, user_query` |
| `Security_Hardening_and_Dependency_Management_Implementation` | Secure the repository and manage its dependencies by externalizing secrets, addressing vulnerabiliti | `None` |
| `Security_Testing_OWASP_ZAP_Integration` | Configure Selenium to route traffic through the OWASP ZAP proxy for security scanning. | `None` |
| `Security_Vulnerability_Hunt_Aegis` | Locate and fix memory-safety vulnerabilities in C/C++ code with a structured analysis. | `input, package_path, code_context, macros, metadata` |
| `Selenium_Migration_Script_Conversion` | Translate recorded browser actions (Selenese) from Selenium IDE into structured Java test scripts. | `package_name, selenese_code` |
| `Semantic_Caching_AI_Gateway_Architect` | Designs highly scalable AI Gateway architectures featuring advanced semantic caching, context-aware  | `traffic_scale, embedding_models, cache_hit_heuristics, user_query` |
| `Semantic_Interoperability_Optimization` | Bind clinical concepts in CRF questions to LOINC, SNOMED CT, or UCUM. | `crf_metadata, terminology_catalogs` |
| `Senior_Agile_Transformation_Coach_Retrospectives` | Design a high-impact retrospective agenda tailored to team sentiment and sprint outcomes, focusing o | `sprint_context, team_sentiment` |
| `Senior_Python_Developer` | A Senior Developer's guide to Python execution, focusing on idiomatic code, maintainability, and cod | `input` |
| `Separation_Logic_Heap_Entailment_Architect` | Formulates rigorous separation logic frameworks to verify program correctness and manage heap memory | `heap_verification_scenario, input` |
| `Server-Driven_UI_Architecture_Designer` | Designs flexible, responsive Server-Driven UI (SDUI) architectures to control layouts dynamically fr | `application_context, input` |
| `Serverless_Database_Connection_Pooling_Architect` | Designs highly resilient, scalable serverless database connection pooling architectures to prevent c | `cloud_provider, database_engine, expected_concurrency, current_bottleneck` |
| `Serverless_Function_Orchestration_Architect` | Designs highly scalable, resilient, and cost-efficient serverless function orchestration architectur | `business_workflow, event_sources, constraints_and_slas` |
| `Service_Mesh_Security_Architect` | Designs zero-trust mTLS communication policies and robust service mesh architectures within Kubernet | `target_cluster, mesh_provider` |
| `Shadow_Traffic_and_Dark_Launch_Architect` | Architects highly secure and robust shadow traffic and dark launching topologies for safe validation | `current_architecture, target_deployment, critical_constraints, Aegis, macros` |
| `Shelf-life_Study_Rationale` | Draft a rationale for correlating accelerated aging data with real-time requirements. | `input` |
| `Simulated_Clinical_Scenario_Debrief` | Provide constructive feedback after a simulated clinical scenario. | `procedure_notes` |
| `Single_IRB_sIRB_Plan_Submission` | Generate sIRB Plan and communication strategy. | `grant_details` |
| `Site_Landscape_Mapping_Prioritization` | Rank investigative sites for an upcoming study. | `protocol_summary` |
| `Site_Reliability_SLO_Error_Budget_Architect` | Formulates rigorous Site Reliability Engineering (SRE) Service Level Objectives (SLOs) and Error Bud | `service_architecture, historical_reliability_data, business_requirements` |
| `Site_Selection_and_Enrollment_Forecaster` | Analyze historical site performance and patient demographics to rank investigative sites and predict | `input, feasibility_data` |
| `Site_Upload_QC_and_Query_Generator` | Automate QC of imaging uploads and craft site queries. | `upload_log_csv, Site_ID` |
| `Smart_Task_Prioritizer` | Transform a raw to-do list into a structured Prioritization Matrix (Impact/Urgency/Effort) and an ac | `input, task_list` |
| `Socratic-Coach` | You are a Master Socratic Coach guiding the user through deep reflection and critical thinking. | `input, macros` |
| `Software_Supply_Chain_Provenance_Architect` | Architects robust, mathematically sound, and SLSA-compliant software supply chain security framework | `build_environment, compliance_target` |
| `Sonic_Architect` | Translates the emotional arc into concrete music theory and production choices. | `psychological_profile, therapeutic_arc` |
| `Source_Document_and_Endpoint_Checklist` | Create a clear checklist of required documents and endpoint criteria for clinical adjudication. | `charter_excerpt` |
| `Source_of_Truth_Harmonizer` | Harmonizes codebase documentation with a provided 'New Source of Truth'. | `input` |
| `Space-Based_Architecture_Designer` | Acts as a Strategic Genesis Architect to design extreme-scale, highly concurrent Space-Based Archite | `scale_requirements, transactional_domain, xml` |
| `Spatial_Geofencing_Topology_Architect` | Acts as a Strategic Genesis Architect to design hyper-scale, low-latency real-time spatial geofencin | `spatial_scale, throughput_requirements, latency_constraints` |
| `Special_Controls_Labeling_Compliance` | Generate mandatory labeling content, including warnings and limitations, for HCV antibody tests. | `input` |
| `Sponsor-Ready_Monthly_Status_Brief` | Draft a concise, escalation-ready monthly status report for study sponsors. | `monthly_notes` |
| `Stateful_Workflow_Orchestration_Architect` | Designs highly resilient, durable execution and stateful workflow orchestration architectures for co | `workflow_requirements, scale_and_throughput, durability_and_latency_sla, user_query` |
| `Statistical_Analysis_Plan_Draft_Builder` | Create the initial draft of a Statistical Analysis Plan (SAP) for a Phase II oncology trial. | `protocol_synopsis` |
| `Statistical_Analysis_Plan_Generator` | Generate a comprehensive, regulatory-compliant (ICH E9) Statistical Analysis Plan (SAP) for clinical | `study_details, population, intervention, control, endpoints, statistical_methods, indication, macros, objective, phase, study_phase` |
| `Statistical_Analysis_Plan_SAP_Development` | Draft a comprehensive SAP. | `protocol_summary` |
| `Status_Update_and_Task_Prioritization` | Summarize recent progress and recommend prioritized next actions. | `status_notes` |
| `Steered_Molecular_Dynamics_Unbinding_Architect` | Generates rigorous steered molecular dynamics (SMD) simulation protocols for calculating protein-lig | `macromolecular_target, ligand, conditions` |
| `Sterility-Validation_Protocol_Builder` | Draft a complete validation protocol for a single-use Class II instrument sterilized by gamma irradi | `device_description, macros` |
| `Stochastic_Architect` | Analyzes a conversation or scenario to map it into a formal Stochastic State Model, defining states, | `conversation_scenario, conversation_context, stochastic_model` |
| `Stochastic_Engineer` | Generates a Python Monte Carlo simulation script based on provided state definitions and transition  | `architect_output, architect_model, simulation_code, stochastic_model` |
| `Stochastic_Model_Predictive_Control_MPC_Architect` | Formulates mathematically rigorous, robust, and stochastic Model Predictive Control (MPC) frameworks | `SYSTEM_DYNAMICS, CONTROL_OBJECTIVES, SYSTEM_CONSTRAINTS, control_objectives, system_constraints, system_dynamics` |
| `Stochastic_Multi-Objective_Optimization_Architect` | Formulates robust, multi-objective stochastic optimization models for complex operations research sc | `SCENARIO_DESCRIPTION, UNCERTAINTY_SOURCES, DECISION_VARIABLES, decision_variables, scenario_description, uncertainty_sources` |
| `Stochastic_Reverse_Logistics_Optimization_Architect` | Architects mathematically rigorous, stochastic reverse logistics network models to optimize product  | `return_volume_distributions, processing_center_capabilities, secondary_market_demand` |
| `Stochastic_Strategist` | Analyzes the stochastic model and simulation logic to provide strategic advice, identifying "Black S | `architect_output, engineer_output, architect_model, simulation_logic, strategic_analysis` |
| `Storyboard-My-Idea` | Storyboard “[PROJECT OR MESSAGE]” for a 60-second explainer video: | `input` |
| `Strangler_Fig_Migration_Architect` | Architect a Strangler Fig pattern migration from a legacy monolith to microservices. | `legacy_system, target_state` |
| `Strategic_Alignment_and_Innovation` | Develop a roadmap that aligns global trial operations with emerging industry trends. | `current_operations` |
| `Strategic_Business_Case_for_New_Service_Line` | Drafts a comprehensive New Venture Strategic Plan for a new service line, focusing on market shift,  | `organization_context, source_material` |
| `Strategic_Capital_Allocation_Architect` | Formulates mathematically rigorous capital allocation strategies optimizing for Risk-Adjusted Return | `capital_constraints, investment_opportunities, risk_parameters` |
| `Strategic_Consultant_SWOT` | Generates a high-impact, board-ready SWOT analysis for Life Sciences organizations, delivered by a S | `business, input` |
| `Strategic_Global_Outsourcing_and_Offshoring_Architect` | Architects rigorous global delivery models, executing complex business process outsourcing (BPO) and | `operational_scope, vendor_risk_profile, financial_arbitrage_targets` |
| `Strategic_Growth_Roadmap` | Rank therapeutic areas for expansion over the next three years. | `input` |
| `Strategic_Market_Foresight_and_Action_Plan` | Detect market inflections and craft a response plan. | `input` |
| `Strategic_Market_and_Competitor_Radar` | Provide an executive briefing on growth areas, competitor moves, and regulatory shifts. | `input` |
| `Strategic_Portfolio_Prioritizer` | Rank proposed clinical projects by scientific merit, ROI, risk, and strategic fit. | `project_data, input` |
| `Strategic_Product_Cannibalization_Architect` | Formulates rigorous corporate strategy to manage controlled product cannibalization, utilizing quant | `legacy_product, new_product, market_dynamics` |
| `Strategic_Real_Options_Valuation_Architect` | Formulates rigorous real options valuation models for strategic investment decisions under extreme u | `underlying_asset_parameters, volatility_and_risk, strategic_flexibility` |
| `Strategic_Regulatory_Pathway_Plan` | Outline a holistic global regulatory pathway for a medical device or IVD. | `device_name, intended_use` |
| `Strategic_Vendor_Lock-In_Mitigation_Architect` | Analyzes proposed enterprise technology stacks and architects highly rigorous, multi-vendor interope | `PROPOSED_TECH_STACK, BUSINESS_OBJECTIVES` |
| `Strategic_Workforce_and_Talent_Acquisition_Plan` | Create a 12‑month hiring and retention roadmap that fills projected staffing gaps while keeping turn | `cro_name, headcount_data, salary_benchmarks, macros` |
| `Study_Design_and_Statistical_Approach` | Propose a clinical trial design with corresponding statistical approach. | `device_type, endpoints, regulatory_target, trial_phase` |
| `Study_Start-Up_Checklist_Timeline` | Provide an actionable checklist and timeline for Phase IIb study start-up. | `fpi_date, regions, regulations, therapeutic_area` |
| `Submission-Ready_Statistical_Analysis_Plan` | Generate sections of a submission-ready statistical analysis plan. | `study_overview` |
| `Sunshine_Act_and_FMV_Compliance_Check` | Audit site-payment data for Sunshine Act reporting and FMV adherence. | `fmv_table, fx_rates, payment_ledger_csv` |
| `Supplier_Corrective_Action_Request_Evaluator` | Evaluates a Supplier Corrective Action Request (SCAR) response for adequacy, regulatory compliance,  | `scar_details, supplier_response, objective_evidence` |
| `Supplier_Quality_Agreement_Architect` | Acts as a Principal Supplier Quality Architect to draft, review, and negotiate rigorous Supplier Qua | `manufacturer_type, supplier_type, risk_classification, critical_requirements` |
| `Supply_Chain_Antifragility_Architect` | Formulates mathematically rigorous supply chain antifragility and nearshoring strategy architectures | `current_network_topology, shock_scenarios, financial_constraints` |
| `Supply_Chain_Disruption_Stochastic_Stress_Test_Architect` | Conducts rigorous stochastic stress testing and resilience optimization for global supply chain netw | `supply_chain_network_data, disruption_scenario, macros` |
| `Supply_Chain_Network_Topology_Optimization_Architect` | Architects mathematically rigorous supply chain network topologies, optimizing facility location, ca | `demand_nodes_and_volumes, candidate_facility_locations, transportation_and_flow_constraints` |
| `Sustainable_Green_Software_Architect` | Acts as a Principal Green Software Architect to formulate comprehensive, data-driven technical archi | `system_requirements, deployment_environment, xml` |
| `Symplectic_Integrator_Hamiltonian_Systems_Architect` | Formulates structure-preserving numerical methods for long-term integration of complex Hamiltonian s | `HAMILTONIAN_FUNCTION, TIME_DOMAIN_CONSTRAINTS, CONSERVATION_TOLERANCES, conservation_tolerances, hamiltonian_function, time_domain_constraints` |
| `Synchronization_Strategy_Explicit_Waits` | Replace brittle Thread.sleep() calls with dynamic Explicit or Fluent waits. | `code_snippet, code` |
| `Synthetic_Control_Method_Architect` | A highly rigorous prompt for designing and estimating Synthetic Control Method models in econometric | `treatment_unit, donor_pool, outcome_variable, predictors, intervention_time` |
| `System_Design_RFC_Architect` | Draft a high-level Request for Comments (RFC) for a system design, focusing on trade-offs, security, | `input, macros, requirements` |
| `TD-DFT_Excited-State_Dynamics_Architect` | Generates rigorous Time-Dependent Density Functional Theory (TD-DFT) computational protocols to calc | `molecular_system, solvent_environment, photophysical_properties` |
| `TMF_Gap-Analysis_and_Audit_Readiness_Check` | Identify missing or outdated Trial Master File documents and propose corrective actions. | `tmf_index` |
| `TOGAF_Phase_A_-_Architecture_Vision` | Guide for defining the Architecture Vision, stakeholders, and the Statement of Architecture Work (Th | `input, request` |
| `TOGAF_Phase_B_-_Business_Architecture` | Guide for defining the Business Architecture, baseline/target states, and gap analysis (The Core Eng | `input, request` |
| `TOGAF_Phase_C_-_Information_Systems_Architectures` | Guide for defining the Information Systems Architectures (Data and Application Architectures). | `input, request` |
| `TOGAF_Phase_D_-_Technology_Architecture` | Guide for defining the Technology Architecture (infrastructure, hardware, networks). | `input, request` |
| `TOGAF_Phase_E_-_Opportunities_Solutions` | Guide for identifying delivery vehicles (projects), grouping gaps into work packages, and creating t | `input, request` |
| `TOGAF_Phase_F_-_Migration_Planning` | Guide for creating the detailed Implementation and Migration Plan and prioritizing work packages (Re | `input, request` |
| `TOGAF_Phase_G_-_Implementation_Governance` | Guide for overseeing the implementation to ensure conformance with the architecture (Sustaining Inte | `input, request` |
| `TOGAF_Phase_H_-_Architecture_Change_Management` | Guide for managing the architecture lifecycle after deployment and handling change requests (The Liv | `input, request` |
| `TOGAF_Preliminary_Phase` | Guide for establishing the Architecture Capability and defining the organizational footprint (The Ge | `input, macros, request` |
| `TOGAF_Requirements_Management` | Guide for the continuous process of managing architecture requirements throughout the ADM cycle (The | `input, request` |
| `Tailored_Feasibility-Questionnaire_Builder` | Draft a site-feasibility questionnaire to confirm patient availability and operational readiness. | `protocol_summary` |
| `Tandem_MS_MS_Fragmentation_Pathway_Elucidator` | Formulates rigorous, step-by-step gas-phase fragmentation mechanisms and predictive mass spectra for | `precursor_ion, ionization_mode, tandem_ms_conditions, user_query` |
| `Target_Segment_User_Needs_Assessment` | Identify key user segments for `{{ device_or_assay }}` used in `{{ application }}`. | `application, device_or_assay, input, macros` |
| `Task_Prototyper` | Generate a domain-specific L3 prompt that accomplishes `{{ end_task }}`. | `end_task, generated_prompt, policy_block, token_budget_l3, answer, thinking` |
| `Technical_Implementation_Plan` | Detail the architecture, dependencies, and steps required to implement a project. | `architecture_overview, data_models, technology_choices` |
| `Technical_White_Paper_for_Clinical_Methodologies` | Generates a deep technical white paper or educational document for clinical methodologies, focusing  | `paper_title, context_description, source_material, specific_requirements` |
| `Temperature_Replica_Exchange_Molecular_Dynamics_Architect` | Generates rigorous Temperature Replica Exchange Molecular Dynamics (T-REMD) simulation protocols for | `molecular_system, temperature_range, conditions` |
| `Temporal_Logic_Branching_Time_Evaluator` | A highly rigorous prompt designed to systematically evaluate temporal propositions and branching tim | `TEMPORAL_PROPOSITION, LOGICAL_FRAMEWORK, ONTOLOGICAL_DOMAIN, logical_framework, ontological_domain, temporal_proposition` |
| `Test_Architect_Automated_Testing` | Generates comprehensive unit and integration tests for provided code, focusing on edge cases, reliab | `files, input, code_context, thinking` |
| `Test_Environment_Python_Selenium_Base` | Install the Selenium Base framework and environment using the Python package manager. | `None` |
| `Test_Suite_Enhancement_and_CI_Pipeline_Implementation` | Build the automated quality gates for this repository by increasing test coverage, adding meaningful | `repo_context, target_code, macros` |
| `Testing_Configuration_and_Automation_Analysis` | Analyze the repository's testing, configuration, and automation infrastructure to ensure reliability | `repository_context` |
| `The_Prompt_Alchemist` | A Principal Prompt Engineering Alchemist that invents novel, out-of-the-box generative architectures | `target_domain, existing_themes, avoid, user_query` |
| `Theory_of_Constraints_Throughput_Architect` | Formulates rigorous Theory of Constraints (ToC) throughput optimization architectures, identifying a | `system_topology, capacity_and_demand_data, financial_parameters` |
| `Threat_Intelligence_Fusion_Attribution_Architect` | Synthesizes disparate Threat Intelligence (CTI) streams to mathematically attribute advanced cyber i | `intrusion_iocs, victimology, infrastructure_analysis` |
| `Threshold_Signature_MPC_Custody_Architect` | Designs highly secure, institution-grade threshold signature schemes (TSS) and multi-party computati | `key_generation_protocol, signing_threshold, key_refresh_policy, user_query` |
| `Time-Series_Database_Topology_Architect` | Architects highly scalable time-series database topologies optimized for massive ingestion, downsamp | `telemetry_profile, querying_requirements, retention_policy` |
| `Time-to-Event_Analysis_Coach` | Guide a junior analyst through performing a time-to-event analysis. | `dataset_path` |
| `To-Do_List_Template` | Track pending and completed development tasks. | `None` |
| `Tooling_Quality_Gates_DevEx_Architect` | A Distinguished Developer Experience Engineer's guide to enforcing code quality, strict typing, and  | `input, project_context` |
| `Topological_Counterexample_Generator` | Generates precise, logically rigorous counterexamples in point-set, algebraic, or differential topol | `conjecture, constraints, user_query` |
| `Topological_Data_Analysis_Architect` | Designs robust Topological Data Analysis (TDA) pipelines and persistent homology workflows for extra | `data_characteristics, analytical_goals, computational_constraints` |
| `Training_Impact_Analytics_Planner` | Correlate training data with audit deviations and design interventions for high-risk learners. | `analysis_goal` |
| `Trend_Spotting_vs_Anomalies` | Compare support ticket datasets to identify trends and anomalies. | `dataset_a, dataset_b, specific_update` |
| `Trial-Design_Optimisation_Memo` | Rewrite a study synopsis to accelerate startup while maintaining statistical power and budget. | `draft_synopsis, input` |
| `Trial_Master_File_TMF_Maintenance` | Generate TMF checklist based on CDISC Reference Model. | `study_phase` |
| `UAT_Script_Generator` | Generate a User Acceptance Testing (UAT) script with dummy data inputs. | `dummy_data_reqs, ecrf_design, uat_scope` |
| `UDI_GUDID_Submission` | Prepare a Device Identifier (DI) record for GUDID submission. | `input` |
| `UI_Tweak_Verification_Aegis_Security` | Resolve a minor UI regression and confirm the fix with build or test steps, ensuring accessibility a | `component_path, input, macros, user_request` |
| `Ultimate_SOP_Architect` | Create a clear, regulation-compliant standard operating procedure. | `process_information` |
| `Underwater_Acoustic_Sensor_Network_Architect` | Designs highly resilient, ultra-low bandwidth Underwater Acoustic Sensor Network (UWASN) architectur | `deployment_environment, node_topology, data_requirements, user_query` |
| `Unified_Data_Cleansing` | Outline a unified data cleansing approach for clinical trial datasets with strict CDISC/SDTM complia | `input` |
| `Universal_Automation_Agent` | An elite, highly adaptable automation agent that executes specific tasks based on strict constraints | `task, context, constraints, output_format, thought_process` |
| `Universal_Template-Table_Prompt` | Create a formatted safety table from an ADaM ADAE dataset using either R or SAS. | `dataset_path, language` |
| `Upskilling_Program_Design` | Design a technical upskilling curriculum for engineering teams. | `current_tech, target_tech, team_type, timeline` |
| `Value-Based_QBR_Generator` | Create a concise, impact-focused Quarterly Business Review template. | `client_data, macros` |
| `Vector_Prompt_Calibration_Evaluator` | Evaluates and calibrates draft prompts according to the Vector standard, enforcing persona specifici | `draft_prompt` |
| `Vector_Prompt_Calibrator` | A Lead Prompt Engineer persona that ruthlessly audits and calibrates draft prompts to eliminate AI t | `draft_prompt` |
| `Vector_Prompt_Editor-in-Chief` | Reviews draft prompts, eliminates generic phrasing, and elevates them with specific personas, precis | `draft_prompt` |
| `Vendor_Qualification_and_Oversight` | Develop Vendor Oversight Plan and KPIs. | `vendor_details` |
| `Virtual_Waiting_Room_Fair_Access_Architect` | Designs highly scalable, fair-access virtual waiting room architectures to protect downstream system | `traffic_profile, downstream_capacity` |
| `Visible_Light_Photoredox_Pathway_Architect` | Formulates advanced visible-light photoredox catalytic cycles, calculating redox potentials, thermod | `photocatalyst, substrates, coreactants` |
| `Voice_of_Customer_Root_Cause_Analysis` | Analyze raw feedback to identify root causes and quick wins. | `feedback_comments, macros` |
| `WASM_Edge_Serverless_Runtime_Architect` | Designs ultra-low-latency, multi-tenant WebAssembly (WASM) serverless edge runtimes using strict lin | `latency_constraints, integration_capabilities, concurrency_model, user_query` |
| `Ward-Takahashi_Identity_Path_Integral_Architect` | Formulates the rigorous derivation of Ward-Takahashi identities from the path integral measure under | `generating_functional, symmetry_transformation, field_measure, user_query` |
| `WebAssembly_Sandboxed_Plugin_Architect` | Designs highly secure, performant, and sandboxed plugin architectures leveraging WebAssembly (Wasm)  | `core_platform, plugin_requirements, security_constraints` |
| `WebRTC_Real-Time_Media_Streaming_Architect` | Designs highly scalable, low-latency, and resilient WebRTC-based real-time media streaming architect | `streaming_use_case, scale_and_latency_requirements, network_and_infrastructure_constraints, user_query` |
| `Webhook_Dispatch_Delivery_Architect` | Designs highly resilient, high-throughput webhook delivery architectures addressing concurrency, pay | `target_scale` |
| `Weekly_Executive_Status_Report` | Summarize project progress for executive stakeholders in a concise weekly report. | `update_notes` |
| `Weekly_Operations_KPI_Snapshot` | Summarize weekly milestone performance and highlight at-risk studies. | `milestone_csv, macros` |
| `Windows_ETW_Threat_Hunting_Architect` | Formulates precise threat hunting queries and hypotheses targeting advanced Windows persistent threa | `threat_hypothesis, logging_source, operational_constraints` |
| `Worker_Prompt` | Execute the concrete task defined by the L3 template and return structured output. | `generated_prompt, input_block, output_schema, policy_block, task_description, token_limit_l4, answer, input_data, thinking` |
| `Write_the_Regulatory_Summary` | You are a regulatory-affairs specialist drafting the Chemical Characterization section of a 510(k). | `risk_assessment_summary` |
| `Writing_Clarity_Mentor` | Improve a passage by highlighting issues and rewriting for clarity. | `passage` |
| `Zero-Day_Incident_Containment_Architect` | Generates tactical containment strategies and mitigation playbooks for zero-day vulnerabilities. | `vulnerability_context` |
| `Zero-Downtime_Database_Migration_Architect` | Designs comprehensive, zero-downtime database migration strategies for high-availability systems. | `migration_requirements, input` |
| `Zero-Knowledge_Proof_Protocol_Architect` | Designs mathematically rigorous zero-knowledge proof (ZKP) protocols for enterprise privacy. | `system_requirements, data_schema` |
| `Zero-Knowledge_Rollup_Scaling_Architect` | Designs highly scalable, secure, and decentralized Zero-Knowledge Rollup (ZK-Rollup) Layer 2 archite | `throughput_requirements, proving_system, data_availability_layer, user_query` |
| `Zero_Trust_Network_Architecture_Designer` | Architects robust Zero Trust network topologies and micro-segmentation strategies from domain requir | `domain_context` |
| `Zero_Trust_Privileged_Access_Management_Architect` | Acts as a Principal Identity Security Architect and Lead Zero Trust Strategist to design highly rigo | `enterprise_environment, compliance_requirements` |
| `Zika_Virus_Reagent_Study_Design` | Draft a protocol for analytical performance studies to validate Zika virus serological reagents. | `input` |
| `adm_spacetime_decomposition_architect` | Conducts rigorous 3+1 Arnowitt-Deser-Misner (ADM) decomposition of spacetime metrics, extracting lap | `spacetime_metric, foliation_parameter, gauge_condition, user_query` |
| `ads_cft_holographic_dictionary_architect` | Formulates rigorous holographic dictionary mappings and boundary conditions for AdS/CFT corresponden | `bulk_action, boundary_operator, dimension` |
| `advanced_retrosynthetic_pathway_generator` | Generates highly optimized, multi-step retrosynthetic pathways for complex organic molecules, evalua | `target_molecule, starting_materials_constraints` |
| `adverse_event_signal_detection_architect` | Acts as a Principal Pharmacovigilance Scientist to perform advanced signal detection and disproporti | `DRUG_NAME, ADVERSE_EVENTS_DATA, BACKGROUND_INCIDENCE, background, data, drug` |
| `affective_polarization_contagion_mapper` | A highly robust, expert-level prompt designed to computationally model the automated propagation of  | `multimodal_data_schema, algorithmic_contagion_parameters` |
| `agm_belief_revision_formal_engine` | A highly rigorous prompt designed to systematically formalize and execute AGM (Alchourrón, Gärdenfor | `KNOWLEDGE_BASE, EPISTEMIC_INPUT, REVISION_OPERATION, epistemic_input, knowledge_base, macros, revision_operation` |
| `ai_threat_modeling_architect` | Acts as a Principal AI Security Architect to conduct rigorous threat modeling (STRIDE/MITRE ATLAS) o | `architecture_description, system_assets` |
| `algorithmic_behavior_echo_chamber_modeler` | A highly robust, expert-level prompt designed to computationally model the automated propagation of  | `contagion_strain_metadata, algorithmic_environment_schema, topological_intervention_goal, environment_schema, intervention_goal, strain_metadata` |
| `algorithmic_cognitive_overload_epidemiological_mapper` | A highly robust, expert-level prompt designed to mathematically model the epidemiological propagatio | `telemetry_data_schema, algorithmic_exposure_vector, public_health_intervention_objective, example_variable, macros, user_input` |
| `algorithmic_misinformation_contagion_modeler` | A highly robust, expert-level prompt designed to formulate mathematical models and multi-modal big d | `multi_modal_data_schema, network_virality_factors, topological_intervention_objective, data_schema, intervention_objective, virality_factors` |
| `algorithmic_multi_touch_attribution_modeler` | Formulates rigorous algorithmic multi-touch attribution (MTA) models using Markov chains and Shapley | `customer_journey_data, marketing_channels` |
| `algorithmic_social_contagion_modeler` | Models the epidemiological spread of algorithmic misinformation and behavioral contagion across larg | `network_topology, contagion_parameters, population_size, macros` |
| `ambiguous_natural_language_fol_formalizer` | Systematically translates structurally ambiguous natural language propositions into rigorous, fully  | `natural_language_statement, domain_of_discourse` |
| `approximate_bayesian_computation_architect` | Acts as a Principal Statistician to design and formulate mathematically rigorous Approximate Bayesia | `data_generating_process, summary_statistics, distance_metric` |
| `astrocytic_tripartite_synapse_architect` | A Principal Computational Neuroscientist agent designed to analytically derive and simulate complex  | `synaptic_elements, signaling_pathways, stimulus_protocol` |
| `astrocytic_tripartite_synapse_calcium_dynamics_architect` | A Lead Computational Neurophysiologist agent designed to derive mathematically rigorous biophysical  | `astrocyte_geometry, neurotransmitter_pathways, gliotransmission_mechanism` |
| `asymptotic_distribution_mle_architect` | Acts as a Statistical Sciences Genesis Architect and Principal Statistician to rigorously derive the | `model_likelihood, parameters, non_standard_conditions` |
| `atiyah_singer_index_theorem_architect` | Computes rigorous analytical and topological indices of elliptic differential operators on compact m | `MANIFOLD, ELLIPTIC_OPERATOR` |
| `automated_malware_reverse_engineering_analyst` | Acts as a Lead Malware Reverse Engineer to perform automated static and dynamic analysis, deobfuscat | `binary_metadata, disassembly_snippets, dynamic_behavior_logs` |
| `b2b_abm_pipeline_velocity_architect` | Synthesizes B2B Account-Based Marketing (ABM) engagement telemetry into predictive pipeline velocity | `abm_engagement_telemetry, opportunity_stage_durations, historical_win_rates, deal_size_distribution` |
| `banach_space_operator_architect` | A Principal Research Mathematician and Functional Analysis Expert designed to rigorously formalize a | `space_structure, operator_definition, theorem_conjecture` |
| `basal_ganglia_td_learning_architect` | A Principal Computational Neuroscientist designed to formulate biologically plausible Temporal Diffe | `associative_learning_paradigm, basal_ganglia_circuitry_constraints, dopamine_rpe_dynamics` |
| `bayesian_epistemological_update_formalizer` | A highly rigorous prompt designed to systematically evaluate probabilistic updating, Bayesian condit | `PRIOR_CREDENCES, NEW_EVIDENCE, UPDATING_RULE, new_evidence, prior_credences, updating_rule` |
| `bayesian_hierarchical_model_architect` | Acts as a Principal Statistician to design and formulate complex Bayesian hierarchical models with c | `data_structure, inferential_goal, prior_knowledge` |
| `bayesian_media_mix_modeling_architect` | Formulates advanced Bayesian Media Mix Modeling (MMM) frameworks to estimate incremental ROAS, optim | `historical_spend_data, sales_revenue_data, control_variables` |
| `bayesian_optimization_hyperparameter_architect` | Designs highly robust, efficient Bayesian Optimization workflows for hyperparameter tuning of comple | `model_architecture, hyperparameter_space, objective_metric` |
| `bayesian_phylogenetic_inference_mcmc_architect` | Designs highly rigorous Bayesian phylogenetic inference models utilizing Markov Chain Monte Carlo (M | `input_alignment_data, substitution_model, molecular_clock_prior, var, macros` |
| `bayesian_vector_autoregression_architect` | Formulates rigorous Bayesian Vector Autoregression (BVAR) models for macroeconomic forecasting and s | `endogenous_variables, prior_specification, structural_identification, forecast_horizon` |
| `behavioral_epidemiology_social_contagion_modeler` | A highly robust, expert-level prompt designed to computationally model the propagation of psychologi | `population_network_schema, behavioral_phenomenon, structural_constraints` |
| `biophysical_hodgkin_huxley_modeler` | A Principal Computational Neuroscientist agent designed to analytically derive and simulate complex  | `cell_type, ion_channels, stimulus_protocol` |
| `blinder_oaxaca_decomposition_architect` | A Principal Sociologist agent designed to execute rigorous Blinder-Oaxaca decompositions for analyzi | `dependent_variable, group_a, group_b, covariates` |
| `blue_ocean_value_innovation_architect` | Acts as a Principal Blue Ocean Strategy Architect to formulate rigorous value innovation models, con | `industry_context, strategic_objective` |
| `breakthrough_therapy_designation_rationale_architect` | Synthesizes preliminary clinical data, unmet medical need, and standard of care to formulate a highl | `target_indication, unmet_medical_need, preliminary_clinical_evidence, mechanism_of_action, prelimedy_clinical_evidence` |
| `byzantine_fault_tolerant_consensus_architect` | Designs robust Byzantine Fault Tolerant (BFT) consensus architectures for building secure, highly re | `system_domain, node_characteristics, performance_requirements, macros` |
| `calculus_of_constructions_proof_architect` | Formulates mathematically rigorous proofs and type derivations utilizing the Calculus of Constructio | `TARGET_PROPOSITION, TYPE_ENVIRONMENT, macros, target_proposition, type_environment` |
| `capa_root_cause_analysis_architect` | Acts as a Principal Quality Assurance Engineer and CAPA Specialist to rigorously investigate nonconf | `NONCONFORMANCE_REPORT, INVESTIGATION_DATA` |
| `capa_root_cause_resolution_architect` | Acts as a Principal Quality Assurance Engineer and Regulatory Compliance Expert to systematically pe | `non_conformance_report, product_domain` |
| `carceral_state_expansion_modeler` | Systematically models the systemic, demographic, and structural impacts of the carceral state and ma | `demographic_incarceration_data, systemic_institutional_context` |
| `categorical_theorem_translator` | Rigorously translates theorems between distinct abstract structures using category theory, specifica | `source_theorem, source_category, target_category` |
| `category_theory_adjunction_architect` | Generates rigorous mathematical proofs of functorial adjunctions and Kan extensions, enforcing stric | `source_category, target_category, functor_definition` |
| `causal_inference_dag_architect` | Acts as a Principal Causal Inference Methodologist to design rigorous counterfactual frameworks and  | `research_question, variables_list, assumptions` |
| `central_pattern_generator_circuit_modeler` | Mathematically architects and simulates biophysical Central Pattern Generator (CPG) circuits and hal | `circuit_topology, neuron_type, synaptic_dynamics, neuromodulation_target, important_security_constraints, input, macros` |
| `cer_literature_review_architect` | Acts as a Principal Medical Writer and Regulatory Clinical Evaluator to systematically synthesize cl | `DEVICE_DESCRIPTION, LITERATURE_DATA, device_description, literature_data` |
| `chaos_mesh_fault_injection_architect` | Architects rigorous, targeted chaos engineering experiments using Chaos Mesh in Kubernetes environme | `system_architecture, fault_hypothesis` |
| `characteristic_class_cobordism_architect` | Rigorously computes topological characteristic classes (e.g., Stiefel-Whitney, Chern) and evaluates  | `manifold_definition, vector_bundle_definition, characteristic_class_type` |
| `chromatin_conformation_hic_contact_map_architect` | Designs robust, mathematically rigorous analytical architectures for modeling 3D genome conformation | `resolution, normalization_method, structural_target` |
| `clinical_study_report_patient_narrative_architect` | Synthesizes complex clinical trial data into regulatory-compliant Patient Narratives for Clinical St | `patient_data, ae_of_interest` |
| `cognitive_bias_epistemological_deconstructor` | A highly rigorous prompt designed to systematically deconstruct cognitive biases within epistemologi | `EPISTEMOLOGICAL_MODEL, COGNITIVE_BIAS, EPISTEMIC_CONTEXT, cognitive_bias, epistemic_context, epistemological_model` |
| `cognitive_bias_mitigation_architect` | A highly robust, expert-level prompt designed to computationally model and systematically mitigate c | `decision_making_context, cognitive_vulnerabilities, statistical_base_rates` |
| `cognitive_diagnostic_modeling_architect` | A highly robust expert-level prompt designed to architect Cognitive Diagnostic Models (CDMs), estima | `test_context, q_matrix_specification, response_data_characteristics` |
| `cognitive_inoculation_campaign_architect` | A highly analytical prompt designed to engineer population-scale, multi-platform cognitive inoculati | `misinformation_vector, population_network_schema, intervention_constraints` |
| `cohort_retention_survival_analysis_architect` | Formulates mathematically rigorous user cohort retention strategies utilizing Kaplan-Meier survival  | `cohort_definition, retention_metric, current_churn_rate, user_query` |
| `collective_panic_cascade_architect` | A highly robust, expert-level prompt designed to formulate mathematical models and multi-modal big d | `multi_modal_data_schema, macro_environmental_stressors, topological_intervention_objective, data_schema, environmental_stressors, intervention_objective` |
| `companion_diagnostic_analytical_validation_architect` | Acts as a Principal Regulatory Scientist and IVD Specialist to design rigorous, FDA-compliant analyt | `ASSAY_DESCRIPTION, SAMPLE_TYPES` |
| `complex_ppi_network_mapper` | Acts as a Principal Computational Biologist to mathematically map, analyze, and simulate complex pro | `protein_target_list, interaction_database, kinetic_parameters, network_model_type, constraints` |
| `confidential_computing_enclave_architect` | Acts as a Principal Security Architect to design highly secure, hardware-isolated Trusted Execution  | `workload_description, threat_model` |
| `constructive_intuitionistic_natural_deduction_prover` | Automates the rigorous generation of natural deduction proofs within Intuitionistic Logic, enforcing | `premises, conclusion` |
| `continuous_attractor_neural_network_architect` | Designs highly rigorous, computationally sound continuous attractor neural network (CANN) models for | `dimensionality, plasticity_rule, macros` |
| `continuous_time_asset_pricing_architect` | Formulates continuous-time asset pricing models utilizing Ito calculus and stochastic discount facto | `underlying_dynamics, investor_preferences, asset_claim` |
| `corporate_b2b_saas_pricing_tier_architect` | Architects rigorous B2B SaaS pricing tiers, optimizing value-based monetization, price elasticity, a | `product_capabilities, target_customer_segments, competitive_landscape, unit_economics` |
| `corporate_fx_hedging_currency_risk_architect` | Formulates highly rigorous corporate foreign exchange (FX) hedging and currency risk mitigation stra | `currency_exposures, risk_tolerance, market_conditions` |
| `corporate_ip_portfolio_monetization_architect` | Architects rigorous intellectual property (IP) portfolio monetization and patent capitalization stra | `portfolio_domain, core_patents_volume, market_application, competitive_threat_landscape, monetization_objective` |
| `corporate_wargaming_scenario_planning_architect` | Architects rigorous corporate wargaming and macro-scenario planning simulations, modeling multi-acto | `industry_context, primary_actor, key_competitors, macroeconomic_shocks, strategic_horizon` |
| `counterfactual_semantics_stalnaker_lewis_evaluator` | A highly rigorous prompt designed to systematically evaluate the truth conditions of counterfactual  | `COUNTERFACTUAL_STATEMENT, BACKGROUND_FACTS, SIMILARITY_METRIC, background_facts, counterfactual_statement, similarity_metric` |
| `crdt_conflict_resolution_architect` | Designs robust Conflict-Free Replicated Data Type (CRDT) architectures for building highly available | `system_domain, network_characteristics, data_complexity, macros` |
| `crispr_cas9_off_target_predictive_modeler` | Acts as a Principal Computational Geneticist to probabilistically model and predict CRISPR-Cas9 off- | `target_sequence, pam_sequence, genome_assembly, mismatch_tolerance, constraints` |
| `crispr_cas9_off_target_probabilistic_modeler` | Designs probabilistic modeling frameworks to predict CRISPR-Cas9 off-target cleavage sites using the | `sgRNA_sequence, PAM_type, off_target_tolerance_threshold` |
| `crispr_cas9_off_target_thermodynamic_architect` | A highly rigorous biological genesis architect prompt designed to establish probabilistic models and | `target_sequence, reference_genome, cas9_variant` |
| `cross_channel_behavioral_trigger_architect` | Synthesizes enterprise SaaS customer behavioral telemetry and constructs cross-channel behavioral tr | `behavioral_telemetry, active_channels, target_retention_improvement, unit_economics` |
| `csr_efficacy_narrative_architect` | A Principal Medical Writer and Clinical Scientist prompt designed to synthesize complex statistical  | `study_endpoints, statistical_tlfs, target_audience` |
| `csr_patient_narrative_architect` | Synthesizes complex clinical trial subject data into regulatory-compliant patient narratives for Cli | `patient_demographics, medical_history, concomitant_medications, adverse_event_details, laboratory_findings` |
| `csr_patient_safety_narrative_architect` | Synthesizes complex clinical trial subject data into regulatory-compliant patient safety narratives  | `subject_data, protocol_details` |
| `ctd_module_2_7_clinical_summary_architect` | Synthesizes complex clinical efficacy and safety data into a highly rigorous, regulatory-compliant C | `integrated_summary_efficacy, integrated_summary_safety, clinical_pharmacology_data, target_indication` |
| `custom_axiomatic_system_soundness_evaluator` | Systematically verifies the soundness of custom, user-defined axiomatic systems by rigorously evalua | `axioms, inference_rules, formal_semantics` |
| `d_brane_worldvolume_effective_action_architect` | Derives the complete worldvolume effective action for a single D-brane (Dirac-Born-Infeld and Wess-Z | `p_brane, background_fields, worldvolume_fields` |
| `deep_brain_stimulation_biophysical_architect` | A Lead Computational Neurophysiologist agent designed to derive mathematically rigorous biophysical  | `stimulation_parameters, target_neural_circuit, electrode_geometry` |
| `dendritic_cable_theory_computation_architect` | A Principal Computational Neuroscientist to analytically derive and simulate complex dendritic cable | `morphology_data, biophysical_properties, synaptic_input_protocol` |
| `dependent_type_theory_judgment_derivation` | Rigorously constructs and verifies formal type judgment derivations within Martin-Löf Dependent Type | `type_judgment, context` |
| `dialectical_materialism_structural_crisis_modeler` | Systematically generates a highly rigorous structural crisis model through the lens of dialectical m | `systemic_context, empirical_indicators` |
| `dialectical_metaphysical_synthesizer` | Synthesizes mutually exclusive metaphysical frameworks through rigorous dialectical logic. | `FRAMEWORK_A, FRAMEWORK_B, CONTEXT` |
| `diamond_mortensen_pissarides_architect` | Formulates mathematically rigorous Diamond-Mortensen-Pissarides (DMP) search and matching models to  | `matching_function, wage_determination, separation_rate, policy_intervention` |
| `differential_alternative_splicing_isoform_architect` | Architects highly rigorous, statistically robust bioinformatic pipelines for quantifying and modelin | `input_data_type, experimental_design, reference_genome_annotation, modeling_objective` |
| `differential_diagnosis_mapping_architect` | Systematically synthesizes complex clinical presentations into an exhaustive differential diagnosis  | `clinical_presentation, psychosocial_history, psychometric_data` |
| `digital_phenotyping_epidemiological_surveillance_architect` | Designs massive-scale population psychiatric syndromic surveillance using big data digital phenotypi | `population_size, focal_syndrome, digital_proxy_data_sources, macros, surveillance_architecture, user_query` |
| `dimensional_psychopathology_hierarchical_modeler` | Systematically maps complex clinical presentations onto dimensional psychopathology frameworks (e.g. | `clinical_presentation, psychosocial_context, psychometric_data` |
| `dirichlet_process_mixture_architect` | Acts as a Principal Statistician to formulate mathematically rigorous Nonparametric Bayesian models  | `data_structure, base_distribution, mcmc_strategy` |
| `double_machine_learning_architect` | Acts as a Statistical Sciences Genesis Architect and Principal Statistician to mathematically formul | `causal_parameter, nuisance_functions, structural_equations` |
| `dynamic_fleet_routing_optimization_architect` | Acts as a Principal Logistics Operations Research Scientist to formulate rigorous Capacitated Vehicl | `ROUTING_NETWORK_DATA, FLEET_CONSTRAINTS, DELIVERY_TIME_WINDOWS, macros, security_boundary` |
| `dynamic_panel_gmm_architect` | Formulates rigorous dynamic panel data estimators using Generalized Method of Moments (GMM), specifi | `dependent_variable, exogenous_regressors, endogenous_regressors, gmm_estimator_type` |
| `eBPF_Network_Observability_Architect` | Architect highly efficient, low-overhead distributed network observability and security instrumentat | `infrastructure_topology, telemetry_requirements` |
| `eBPF_Runtime_Security_Architect` | Design ultra-low-overhead runtime security observability and enforcement policies using eBPF for clo | `workload_profile, threat_vectors, performance_constraints` |
| `eConsent_Implementation_Strategy` | Verify eConsent platform compliance and workflow. | `platform_specs` |
| `ePRO_Adoption_Plan_for_Sponsors` | Outline a six-month plan for rolling out ePRO across multiple sites. | `input` |
| `ePRO_Migration_Equivalence_Checker` | Assess measurement equivalence for migrating paper-based PRO instruments to electronic modes. | `device_type, features, paper_instrument_name, electronic_device, key_features_to_migrate, original_instrument` |
| `eTMF_Artifact_Classifier` | Read document text and suggest appropriate eTMF artifact classification and metadata assignments for | `input, document_text, tmf_metadata` |
| `eTMF_Compliance_Gap_Analysis` | Evaluate an electronic Trial Master File for compliance gaps and recommend corrective actions. | `etmf_export, study_id` |
| `ecological_momentary_assessment_multilevel_modeler` | A Lead Psychometrician and Principal Methodologist agent designed to architect rigorous Multilevel M | `ema_sampling_design, dynamic_constructs, hypothesized_effects` |
| `effective_field_theory_matching_rg_running_architect` | A highly rigorous Theoretical Physics Genesis Architect designed to perform tree-level and one-loop  | `uv_lagrangian, light_degrees_of_freedom, matching_scale, loop_order` |
| `empirical_process_theory_architect` | Acts as a Principal Statistician to systematically derive weak convergence and asymptotic properties | `stochastic_process, function_class, asymptotic_goal` |
| `epigenetic_methylation_hmm_architect` | Acts as a Principal Epigeneticist and Lead Computational Biologist to probabilistically model DNA me | `bisulfite_sequencing_data, genomic_context, hidden_states, emission_distribution, constraints` |
| `epistemic_defeater_formal_analyzer` | A highly rigorous prompt designed to systematically analyze and formalize epistemic defeaters (rebut | `TARGET_PROPOSITION, DEFEATER_CANDIDATE, EPISTEMIC_FRAMEWORK, defeater_candidate, epistemic_framework, target_proposition` |
| `epistemic_logic_omniscience_paradox_resolver` | A highly rigorous prompt designed to systematically resolve the logical omniscience paradox in epist | `EPISTEMIC_MODEL, AGENT_BOUNDS, LOGICAL_AXIOM, agent_bounds, dialectical_synthesis, epistemic_model, formal_resolution, logical_axiom, logical_deconstruction, paradox_formalization` |
| `epistemic_modal_logic_kripke_evaluator` | Systematically evaluates multi-agent epistemic modal formulas within specified Kripke structures (mo | `kripke_model, formula, evaluation_world` |
| `epistemic_peer_disagreement_formalizer` | A highly rigorous prompt designed to systematically analyze and formalize epistemic peer disagreemen | `EPISTEMIC_PEER, INITIAL_DOXASTIC_STATES, DISAGREEMENT_EVIDENCE, disagreement_evidence, epistemic_peer, initial_doxastic_states` |
| `eu_mdr_clinical_evaluation_report_architect` | Synthesizes complex clinical, pre-clinical, and post-market data into a regulatory-compliant Clinica | `device_data, macros` |
| `eu_mdr_sscp_architect` | Acts as a Principal Regulatory Affairs Medical Writer to synthesize complex clinical data into a com | `DEVICE_DESCRIPTION, CLINICAL_DATA_SUMMARY, RISK_MANAGEMENT_SUMMARY` |
| `evidence_based_intervention_architect` | Translates complex multi-axial clinical formulations into rigorous, empirically-supported psychother | `clinical_formulation, baseline_psychometrics, acute_risk_factors` |
| `exponential_random_graph_model_architect` | A Principal Sociologist and Social Network Analyst designed to rigorously formulate and interpret Ex | `network_data_description, theoretical_mechanisms` |
| `fast_track_designation_request_architect` | Synthesizes scientific rationale, disease prevalence, and unmet medical need into a rigorous, persua | `disease_condition_description, unmet_medical_need, nonclinical_and_clinical_data` |
| `fda_483_warning_letter_remediation_architect` | Acts as a Principal Regulatory Compliance Expert and Former FDA Investigator to synthesize Form 483  | `observation_text, background_context, immediate_corrections` |
| `fda_510k_substantial_equivalence_architect` | Acts as a Principal Regulatory Affairs Architect to synthesize device specifications, intended use,  | `subject_device_data, predicate_device_data, performance_data` |
| `fda_de_novo_classification_request_architect` | Acts as a Principal Regulatory Affairs Architect to formulate rigorous, strategic FDA De Novo Classi | `device_description_and_indications, risk_benefit_analysis, proposed_special_controls` |
| `fda_q_submission_pre_sub_meeting_package_architect` | Acts as a Principal Regulatory Affairs Architect to formulate highly rigorous, strategic FDA Q-Submi | `device_description, intended_use, regulatory_strategy, background_information, proposed_questions, macros` |
| `fda_type_b_meeting_briefing_package_architect` | Synthesizes scientific, clinical, and CMC data to architect a highly structured, regulatory-complian | `meeting_objectives, background_data, sponsor_questions, macros` |
| `financial_frictions_dsge_architect` | Formulates mathematically rigorous Dynamic Stochastic General Equilibrium (DSGE) models with financi | `intermediary_constraints, firm_borrowing_frictions, macroprudential_policy, shock_processes, macros` |
| `finops_cloud_cost_optimization_architect` | Analyzes existing cloud architectures to identify cost inefficiencies and redesigns them using advan | `current_architecture, performance_slas` |
| `first_order_logic_natural_language_translator` | Rigorously translates ambiguous natural language sentences into strictly scoped, formally valid Firs | `natural_language_sentence, domain_of_discourse, sentence` |
| `first_order_logic_semantic_tableau_generator` | Systematically constructs a formal semantic tableau (truth tree) to evaluate the satisfiability and  | `formula` |
| `first_order_logic_sequent_calculus_prover` | Systematically derives formal proofs for first-order logic formulas using the Gentzen sequent calcul | `formula` |
| `fokker_planck_population_dynamics_architect` | A Principal Theoretical Neuroscientist agent designed to analytically derive and numerically solve t | `neuron_model, synaptic_input_statistics, boundary_conditions` |
| `forcing_poset_generic_extension_architect` | Acts as a Principal Set Theorist to rigorously define forcing posets, verify the countable chain con | `ground_model, forcing_poset, forcing_statement` |
| `fractional_calculus_pde_modeler` | Applied Mathematics Genesis Architect prompt for engineering rigorous numerical schemes to solve Fra | `fractional_pde_system, fractional_operator_definition, boundary_initial_conditions, computational_domain, macros` |
| `free_energy_principle_active_inference_architect` | A Principal Theoretical Neuroscientist agent designed to formulate and analyze generative models, va | `generative_model, free_energy_functional, belief_update_dynamics` |
| `freemium_conversion_velocity_architect` | Mathematically models and optimizes Freemium-to-Paid conversion velocity using user telemetry, addre | `user_telemetry, monetization_metrics, financial_parameters` |
| `fully_homomorphic_encryption_circuit_architect` | Acts as a Principal Cryptographic Engineer and FHE Specialist to design highly optimized Fully Homom | `computational_task, performance_latency_constraints, precision_data_requirements` |
| `galois_group_resolvent_architect` | Computes rigorous Galois groups of polynomials over finite extensions and formulates Galois resolven | `POLYNOMIAL, BASE_FIELD` |
| `game_theoretic_competitive_dynamics_architect` | Formulates rigorous game-theoretic models and competitive equilibrium strategies for oligopolistic m | `MARKET_DATA, STRATEGIC_OBJECTIVE, market_data, strategic_objective` |
| `gamified_behavioral_addiction_contagion_modeler` | A mathematically rigorous, expert-level prompt designed to map and computationally model the epidemi | `compulsive_behavior_data_schema, gamification_contagion_parameters` |
| `gaussian_process_regression_architect` | Acts as a Principal Statistician to design highly robust, mathematically rigorous Gaussian Process R | `covariance_structure, likelihood_model, computational_scaling` |
| `generalizability_theory_architect` | A highly rigorous, expert-level prompt designed to systematically architect Generalizability Theory  | `assessment_context, measurement_facets, study_objectives` |
| `genome_scale_metabolic_flux_modeler` | Acts as a Principal Systems Biologist to systematically formulate, analyze, and optimize Genome-Scal | `metabolic_network, objective_function, environmental_constraints, constraints` |
| `gentrification_displacement_spatial_inequality_architect` | A Principal Sociologist agent that systematically analyzes gentrification-induced displacement and s | `spatial_demographic_data, urban_policy_mechanism` |
| `gini_coefficient_income_stratification_architect` | A Principal Sociologist designed to compute the Gini coefficient rigorously and model intersectional | `income_data, demographic_strata` |
| `gitops_continuous_delivery_architect` | Designs and enforces rigorous GitOps continuous delivery architectures, translating desired state in | `application_context, target_topology` |
| `global_supply_chain_geopolitical_duress_architect` | Formulates robust, mathematically rigorous global supply chain rerouting and resilience frameworks u | `CURRENT_NETWORK_TOPOLOGY, GEOPOLITICAL_SHOCKS, COST_CONSTRAINTS` |
| `godel_incompleteness_arithmetization_engineer` | Systematically formalizes and calculates Gödel numbers for logical formulas, variables, and proof se | `expression` |
| `graph_theoretical_connectome_analyzer` | A Principal Computational Neuroscientist agent designed to synthesize and analyze whole-brain connec | `dataset_format, node_definition, edge_weighting` |
| `gtm_pricing_elasticity_architect` | Synthesizes enterprise SaaS historical sales data into predictive Go-To-Market (GTM) pricing elastic | `historical_sales_data, current_pricing_tiers, target_arr_growth` |
| `gwas_polygenic_risk_score_architect` | Acts as a Principal Statistical Geneticist to design robust, mathematically rigorous Polygenic Risk  | `gwas_summary_statistics, linkage_disequilibrium_reference, target_phenotype, statistical_methodology, constraints` |
| `hamiltonian_monte_carlo_architect` | Acts as a Principal Statistician to mathematically formulate and rigorously design Hamiltonian Monte | `target_posterior, kinetic_energy_metric, numerical_integration` |
| `hank_macroeconomic_architect` | Formulates rigorous Heterogeneous Agent New Keynesian (HANK) models integrating uninsurable idiosync | `household_heterogeneity, nominal_rigidities, monetary_fiscal_policy, exogenous_shocks` |
| `health_inequality_concentration_index_architect` | A Principal Sociologist and Lead Social Epidemiologist agent designed to rigorously analyze systemic | `socioeconomic_health_data, focal_population` |
| `hidden_markov_model_architect` | Acts as a Principal Statistician to derive maximum likelihood estimation architectures for continuou | `observation_sequence, state_space_dimensionality, emission_distribution_type, directives, persona` |
| `high_dimensional_sparse_regression_architect` | Acts as a Statistical Sciences Genesis Architect to formulate rigorous, high-dimensional sparse regr | `penalty_function, optimization_algorithm, theoretical_properties` |
| `higher_homotopy_postnikov_tower_architect` | Rigorously calculates higher homotopy groups of topological spaces using Postnikov towers, Serre fib | `topological_space, known_homotopy_groups, target_homotopy_degree` |
| `higher_order_unification_resolution_architect` | Automates the rigorous resolution of higher-order unification problems within the simply typed lambd | `equations, signature` |
| `highly_available_distributed_block_storage_architect` | A Strategic Genesis Architect to design massively scalable, low-latency, and highly fault-tolerant d | `storage_requirements, fault_tolerance_level, consistency_model` |
| `hodgkin_huxley_biophysical_modeler` | Generates highly rigorous, computationally sound biophysical models of single-neuron action potentia | `ion_channels, stimulus_protocol, macros` |
| `homotopy_type_theory_univalence_architect` | Formulates rigorous proofs and topological type derivations utilizing Homotopy Type Theory (HoTT) an | `THEOREM_STATEMENT, TYPE_CONTEXT` |
| `iCGM_Clinical_Testing_Strategy` | Draft a clinical study plan to demonstrate accuracy for an iCGM system. | `input` |
| `icf_readability_compliance_architect` | Acts as a Principal Clinical Medical Writer and IRB/Ethics Committee Expert to synthesize complex cl | `protocol_synopsis, target_audience_reading_level` |
| `ich_e2c_pbrer_benefit_risk_architect` | Acts as a Principal Pharmacovigilance Scientist to rigorously synthesize cumulative post-marketing d | `product_information, cumulative_safety_data, new_safety_signals, efficacy_effectiveness_data` |
| `ich_e3_clinical_study_report_architect` | Synthesizes complex clinical trial data into a rigorously structured, compliant Clinical Study Repor | `study_title_and_objectives, study_design_and_methodology, efficacy_results_summary, safety_results_summary, overall_conclusions` |
| `ich_m4e_ctd_clinical_overview_architect` | Synthesizes complex clinical trial data into a rigorously structured, highly authoritative ICH M4E(R | `clinical_efficacy_data, clinical_safety_data, biopharmaceutics_pharmacokinetics` |
| `iec_62304_soup_anomaly_evaluator` | Evaluates Software of Unknown Provenance (SOUP) known anomalies against IEC 62304 requirements to de | `soup_name, soup_version, samd_architecture_context, known_anomalies` |
| `incrementality_causal_inference_modeler` | Formulates rigorous causal inference and incrementality testing frameworks to isolate the true causa | `experimental_design_data, intervention_costs, revenue_metrics` |
| `ind_clinical_hold_response_architect` | Synthesizes regulatory agency (e.g., FDA) Clinical Hold comments, sponsor mitigation strategies, and | `agency_clinical_hold_comments, sponsor_mitigation_strategy, protocol_amendment_details` |
| `institutional_isomorphism_lifecycle_modeler` | Models the lifecycle of institutional isomorphism (coercive, mimetic, normative) within specific org | `organizational_field, environmental_pressures` |
| `institutional_trust_hemorrhage_modeler` | A highly robust, expert-level prompt designed to computationally model the epidemiological contagion | `population_network_schema, macro_crisis_parameters` |
| `intergenerational_mobility_modeler` | Models intergenerational social mobility using Markov chain matrices and calculates structural inequ | `transition_data, population_distribution` |
| `intergenerational_social_mobility_markov_chain_architect` | Formulates transition probability matrices using Markov chains to map intergenerational social mobil | `longitudinal_mobility_data, class_schema` |
| `intergenerational_social_mobility_markov_modeler` | A Principal Sociologist and Lead Demographer agent designed to formulate and analyze intergeneration | `occupational_strata, empirical_transition_data` |
| `intersectional_stratification_mechanism_modeler` | Models intersectional stratification mechanisms (race, class, gender, and spatial geography) to rigo | `demographic_cohort_data, institutional_context` |
| `intuitionistic_logic_natural_deduction_generator` | Generates rigorous, step-by-step natural deduction proofs in intuitionistic propositional and first- | `PREMISES, CONCLUSION` |
| `intuitionistic_natural_deduction_prover` | Generates rigorous, step-by-step natural deduction proofs for sequents in Intuitionistic Logic, enfo | `sequent, proof_system` |
| `investigators_brochure_safety_synthesizer` | Synthesizes complex nonclinical and clinical safety data into a highly structured, regulatory-compli | `NONCLINICAL_SAFETY_DATA, CLINICAL_SAFETY_DATA, REFERENCE_SAFETY_INFORMATION, clinical_safety_data, nonclinical_safety_data, reference_safety_information` |
| `investigators_brochure_synthesis_architect` | Synthesizes nonclinical, clinical, and CMC data into a regulatory-compliant Investigator's Brochure  | `nonclinical_data, clinical_data, cmc_data` |
| `item_response_theory_dif_analyzer` | A Lead Psychometrician agent designed to conduct rigorous Item Response Theory (IRT) parameter calib | `assessment_context, sample_demographics, response_data_characteristics` |
| `joint_longitudinal_survival_architect` | Acts as a Statistical Sciences Genesis Architect to formulate rigorous Joint Models for Longitudinal | `longitudinal_submodel, survival_submodel, association_structure` |
| `jump_diffusion_modeler` | Acts as a Principal Statistician to rigorously formulate and solve parametric inference and simulati | `drift_function, diffusion_function, jump_intensity_measure, directives, persona` |
| `large_cardinal_elementary_embedding_architect` | Acts as a Principal Set Theorist and Lead Logician to rigorously define and analyze large cardinal a | `domain_model, target_model, critical_point` |
| `large_scale_axial_coding_framework_generator` | Systematically generates an automated, highly rigorous axial coding framework for large-scale qualit | `ethnographic_data_context, primary_theoretical_paradigm` |
| `latent_growth_curve_modeling_architect` | Mathematically formalizes longitudinal developmental trajectories using Latent Growth Curve Modeling | `longitudinal_construct, measurement_occasions, time_invariant_covariates` |
| `latent_profile_mixture_modeling_architect` | A Principal Psychometrician and Mixture Modeling Expert that architect rigorously formulated Latent  | `clinical_construct, indicator_variables, sample_characteristics, covariance_structure` |
| `lattice_boltzmann_multiphase_architect` | Acts as a Principal Computational Physicist designed to architect highly optimized Lattice Boltzmann | `flow_regime, density_ratio, interfacial_challenges` |
| `lean_six_sigma_vsm_architect` | Acts as a Lean Six Sigma Master Black Belt to formulate advanced VSM frameworks for bottleneck ident | `process_parameters, strategic_objectives` |
| `linear_temporal_logic_model_checker` | Systematically evaluates Linear Temporal Logic (LTL) formulas over finite state transition systems ( | `transition_system, ltl_formula` |
| `local_polynomial_regression_discontinuity_architect` | Formulates rigorous nonparametric and local polynomial Regression Discontinuity Design (RDD) estimat | `running_variable, treatment_fuzziness, bandwidth_preferences, specification_concerns` |
| `log_gaussian_cox_process_architect` | Acts as a Principal Statistician to mathematically formulate and design advanced Log-Gaussian Cox Pr | `spatial_domain, point_pattern_data, inferential_objective` |
| `longitudinal_measurement_invariance_evaluator` | A Lead Psychometrician agent designed to conduct rigorous longitudinal measurement invariance testin | `measurement_construct, longitudinal_design, statistical_model_specs` |
| `longitudinal_trauma_propagation_modeler` | Models the epidemiological propagation of psychological trauma across massive longitudinal populatio | `POPULATION_DATASET_SCHEMA, TRAUMA_INCIDENCE_VECTORS, SPATIAL_TEMPORAL_PARAMETERS` |
| `macOS_ESF_Unified_Logging_Threat_Hunter` | Formulates precise threat hunting queries and hypotheses targeting advanced macOS persistent threats | `threat_hypothesis, logging_source, operational_constraints` |
| `mass_psychogenic_illness_diffusion_modeler` | A highly robust, expert-level prompt designed to computationally model the automated epidemiological | `mpi_symptomatology_metadata, structural_topological_schema, epidemic_collapse_intervention, intervention, symptomatology, topological_schema` |
| `mereological_composition_analyzer` | A highly rigorous prompt designed to systematically formalize and evaluate part-whole relations usin | `CANDIDATE_OBJECTS, COMPOSITION_PRINCIPLE, MEREOLOGICAL_SYSTEM, candidate_objects, composition_principle, mereological_system` |
| `metabolic_control_analysis_architect` | A Principal Systems Biologist and Metabolic Engineer to formulate rigorous Metabolic Control Analysi | `metabolic_pathway, key_enzymes, steady_state_conditions` |
| `metagenomic_assembly_taxonomic_binning_architect` | Acts as a Principal Computational Biologist to architect scalable, high-resolution metagenomic assem | `environment_type, sequencing_technology, read_depth, taxonomic_resolution_target, constraints` |
| `metaphysical_grounding_fundamentality_formalizer` | A highly rigorous prompt designed to systematically formalize and evaluate relationships of metaphys | `FUNDAMENTAL_ENTITIES, DERIVATIVE_ENTITIES, GROUNDING_FRAMEWORK, derivative_entities, fundamental_entities, grounding_framework` |
| `mirrleesian_optimal_income_tax_architect` | Formulates rigorous Mirrleesian optimal nonlinear income tax models utilizing mechanism design and s | `agent_utility, skill_distribution, social_welfare_function, government_revenue_requirement` |
| `mixed_frequency_dynamic_factor_nowcasting_architect` | Formulates rigorous Mixed-Frequency Dynamic Factor Models (MF-DFM) for high-frequency macroeconomic  | `observation_frequencies, factor_structure, state_space_formulation, estimation_methodology` |
| `model_theoretic_type_space_architect` | A Principal Research Logician and Model Theorist designed to rigorously analyze type spaces of first | `first_order_theory, type_space_domain, structural_property` |
| `molecular_dynamics_simulation_architect` | Designs highly rigorous, physics-based molecular dynamics (MD) simulation protocols for complex biom | `biological_system, simulation_objectives, thermodynamic_ensemble` |
| `mu_recursive_function_derivation_architect` | Systematically derives formal definitions for computable functions using the strict syntax of mu-rec | `function_description` |
| `multi_echelon_inventory_optimization_architect` | Formulates rigorous Multi-Echelon Inventory Optimization (MEIO) models to minimize network-wide safe | `network_topology, demand_parameters, cost_parameters` |
| `multi_modal_fmri_eeg_integration_architect` | Designs advanced, mathematically rigorous multi-modal fMRI and EEG data integration pipelines adheri | `study_objectives, eeg_specs, fmri_specs` |
| `multi_national_behavioral_intervention_architect` | A highly robust prompt to design large-scale, multi-national longitudinal behavioral intervention ar | `population_cohort_schema, intervention_parameters` |
| `multi_objective_stochastic_optimization_architect` | Formulates rigorous Multi-Objective Stochastic Optimization models to address complex operations res | `decision_variables, objective_functions, stochastic_parameters, constraints, macros` |
| `multi_omics_data_integration_architect` | Designs robust, mathematically rigorous multi-omics data integration pipelines for complex biologica | `omics_types, biological_system, integration_methodology` |
| `multi_scale_pde_asymptotic_homogenization_architect` | Conducts rigorous asymptotic homogenization for multi-scale Partial Differential Equations (PDEs), s | `governing_equation, scale_separation_parameter, boundary_conditions, macros` |
| `multi_step_retrosynthetic_pathway_architect` | A Chemical Sciences Genesis Architect prompt for generating multi-step retrosynthetic pathways with  | `target_molecule_smiles, synthetic_constraints` |
| `multidimensional_item_response_theory_architect` | Designs and evaluates complex Multidimensional Item Response Theory (MIRT) models for multifaceted p | `latent_dimensions, item_specifications, sample_characteristics` |
| `multidimensional_nmr_hrms_structure_elucidator` | Systematically deduces and fully elucidates complex molecular structures using raw multi-dimensional | `molecular_formula, hrms_fragmentation_data, nmr_data` |
| `multidimensional_poverty_alkire_foster_architect` | Operationalizes the Alkire-Foster (AF) method for calculating multidimensional poverty indices, enfo | `household_microdata, deprivation_cutoffs, poverty_cutoff` |
| `multifactorial_behavioral_intervention_architect` | A Principal Quantitative Psychologist designed to formulate rigorous, high-powered multifactorial ex | `intervention_constructs, target_outcomes, population_constraints` |
| `multinational_longitudinal_intervention_architect` | A highly robust, expert-level prompt designed to architect multi-national longitudinal behavioral in | `population_cohort_schema, behavioral_intervention_target, structural_epidemiological_constraints` |
| `multivariate_extreme_value_architect` | Acts as a Principal Statistician to formally define, analyze, and estimate Multivariate Extreme Valu | `multivariate_data_structure, tail_dependence_metric, asymptotic_assumptions` |
| `n_player_bayesian_nash_equilibrium_auction_architect` | Formulates rigorous n-player Bayesian Nash Equilibria (BNE) models for auction theory, providing bid | `number_of_bidders, valuation_distribution, auction_format` |
| `network_psychometrics_architect` | Formulates mathematically rigorous network psychometrics analyses, estimating Gaussian Graphical Mod | `observational_dataset_characteristics, primary_research_question, regularization_constraints` |
| `neural_field_theory_spatiotemporal_dynamics_architect` | A Principal Theoretical Neuroscientist agent designed to analytically derive and numerically simulat | `neural_field_equations, spatial_connectivity_kernel, spatiotemporal_perturbation` |
| `neural_manifold_state_space_analyzer` | A Principal Theoretical Neuroscientist agent designed to rigorously extract and analyze low-dimensio | `input_data_format, dimensionality_reduction_method, dynamical_system_constraints, macros` |
| `neuromorphic_spiking_network_biophysical_architect` | A Principal Computational Neuroscientist designed to formulate mathematically rigorous, hardware-awa | `neural_membrane_kinetics, synaptic_plasticity_model, neuromorphic_hardware_constraints` |
| `neurovascular_coupling_hemodynamic_response_architect` | A Principal Computational Neuroscientist agent designed to rigorously construct and simulate biophys | `neural_activity_profile, vascular_architecture, input_bids_metadata, var` |
| `new_keynesian_dsge_architect` | Formulates rigorous New Keynesian Dynamic Stochastic General Equilibrium (DSGE) models incorporating | `household_preferences, nominal_rigidities, monetary_policy_rule, exogenous_shocks` |
| `non_standard_analysis_hyperreal_architect` | Formulates highly rigorous derivations utilizing Non-Standard Analysis and Hyperreal Numbers (*R), e | `THEOREM_STATEMENT, FORMAL_SYSTEM_CONTEXT, context, macros, theorem` |
| `non_stationary_13c_metabolic_flux_analysis_architect` | Acts as a Principal Systems Biologist to rigorously formulate and solve Non-Stationary 13C Metabolic | `isotope_labeling_data, carbon_atom_transitions, physiological_steady_state, constraints, input_wrapper` |
| `nrr_expansion_propensity_architect` | Synthesizes enterprise SaaS historical usage and billing data into predictive Net Revenue Retention  | `customer_usage_telemetry, historical_billing_data, target_nrr` |
| `occupational_segregation_opportunity_hoarding_architect` | A Principal Sociologist agent that systematically analyzes occupational segregation and structural o | `occupational_demographic_distribution, institutional_closure_mechanism` |
| `open_economy_dsge_architect` | Formulates rigorous Open Economy Dynamic Stochastic General Equilibrium (DSGE) models incorporating  | `trade_structure, financial_markets, monetary_policy, exogenous_shocks` |
| `operational_resilience_tabletop_simulation_architect` | Acts as a Principal Business Continuity Director to design highly realistic, cross-functional tablet | `organization_profile, threat_vector, key_stakeholders` |
| `operational_turnaround_restructuring_architect` | A Strategic Genesis Architect that engineers highly rigorous operational turnaround and corporate re | `company_profile, distress_drivers, turnaround_horizon, optimization_targets` |
| `optimal_mechanism_design_architect` | Formulates optimal mechanism design frameworks leveraging the revelation principle, incentive compat | `objective_function, agent_types, allocation_rule, payment_rule` |
| `optogenetic_photocurrent_biophysical_modeler` | A Principal Computational Neurophysiologist agent designed to analytically derive and simulate multi | `opsin_type, light_stimulation_protocol, neuronal_geometry, macros` |
| `orphan_drug_designation_application_architect` | Synthesizes disease prevalence, scientific rationale, and regulatory context to formulate a highly r | `target_disease, prevalence_estimate, scientific_rationale, clinical_superiority_rationale` |
| `pangenome_graph_structural_variant_architect` | Acts as a Lead Computational Biologist to architect mathematically rigorous pangenome graph workflow | `reference_graph_format, long_read_sequencing_technology, structural_variant_types, graph_alignment_algorithm, constraints` |
| `paraconsistent_logic_dialetheism_evaluator` | A highly rigorous prompt designed to systematically analyze and formalize paradoxical statements usi | `TARGET_PARADOX, PARACONSISTENT_SYSTEM, paraconsistent_system, target_paradox` |
| `peer_to_peer_gossip_protocol_architect` | Designs highly scalable, partition-tolerant Peer-to-Peer (P2P) Gossip and Epidemic broadcast protoco | `system_domain, network_scale, consistency_requirements, macros` |
| `phenomenological_reduction_engine` | A highly rigorous prompt designed to systematically deconstruct first-person experiences using Husse | `LIVED_EXPERIENCE, TARGET_PHENOMENON, lived_experience, target_phenomenon` |
| `physics_informed_neural_network_architect` | Designs robust Physics-Informed Neural Network (PINN) architectures for solving complex nonlinear Pa | `pde_system, boundary_conditions, problem_type, macros` |
| `pinn_stiff_pde_architect` | Acts as a Principal Computational Mathematician designed to architect Physics-Informed Neural Networ | `governing_equation, boundary_and_initial_conditions, stiffness_challenge` |
| `population_macro_nudging_architect` | A highly analytical prompt designed to engineer population-scale behavioral macro-nudging architectu | `policy_objective, population_schema, resource_constraints` |
| `post_merger_integration_synergy_architect` | A Strategic Genesis Architect that creates highly rigorous post-merger integration (PMI) plans, opti | `acquirer_profile, target_profile, integration_horizon, synergy_targets` |
| `post_quantum_cryptography_migration_architect` | Acts as a Principal Cryptographer to design a mathematically rigorous and operationally secure migra | `current_cryptographic_inventory, target_security_level, operational_constraints` |
| `predictive_cac_payback_modeler` | Synthesizes multi-channel acquisition data to model predictive CAC payback periods and optimize unit | `acquisition_cohort_data, blended_cac, arpu, gross_margin` |
| `predictive_churn_ltv_optimization_architect` | Synthesizes enterprise SaaS customer behavior data into predictive churn mitigation strategies and L | `customer_cohort_data, current_arpu, gross_margin, historical_churn_rate` |
| `predictive_rfm_churn_mitigation_architect` | Mathematically models predictive churn risks using Recency-Frequency-Monetary (RFM) analysis and des | `rfm_telemetry, churn_indicators, commercial_parameters` |
| `product_led_growth_k_factor_architect` | Formulates advanced Product-Led Growth (PLG) viral loop architectures, modeling K-Factor optimizatio | `product_telemetry, referral_metrics, unit_economics` |
| `projective_scheme_sheaf_cohomology_architect` | A Principal Research Mathematician and Algebraic Geometry Expert designed to rigorously compute and  | `projective_scheme, coherent_sheaf, cohomological_task` |
| `propositional_dynamic_logic_pdl_evaluator` | Rigorously evaluates programs, formal logic formulas, and state transitions within Propositional Dyn | `program_alpha, formula_phi, kripke_model` |
| `protein_ligand_free_energy_perturbation_architect` | A Principal Structural Biologist and Lead Computational Chemist agent designed to architect rigorous | `protein_target, ligand_series, thermodynamic_cycle` |
| `protocol_deviation_assessment_architect` | Synthesizes and assesses clinical trial protocol deviations to determine their impact on study safet | `protocol_criteria, deviation_data, clinical_context` |
| `pseudo_riemannian_tensor_calculus_prover` | Generates rigorous mathematical derivations and proofs within pseudo-Riemannian geometry, focusing o | `manifold_definition, mathematical_theorem` |
| `psychological_trauma_epidemiology_mapper` | A highly robust, expert-level prompt to mathematically map the epidemiological spread of psychologic | `proxy_data_schema, epidemiological_parameters` |
| `qms_management_review_architect` | Acts as a Principal Quality Systems Strategist to synthesize QMS metrics and architect a comprehensi | `REPORTING_PERIOD, QMS_METRICS_DATA, PREVIOUS_REVIEW_ACTIONS, REGULATORY_CHANGES` |
| `quantitative_commercial_due_diligence_architect` | Architects highly rigorous, quantitative Commercial Due Diligence (CDD) frameworks, evaluating marke | `target_company_name, industry_sector, deal_thesis, key_competitors, financial_metrics` |
| `quantitative_fixed_income_duration_convexity_architect` | Architects mathematically rigorous fixed-income pricing and interest rate risk models, calculating M | `face_value, coupon_rate, yield_to_maturity, periods_per_year, years_to_maturity` |
| `quantitative_shareholder_distribution_optimization_architect` | Architects rigorous, quantitative corporate shareholder distribution policies, optimizing the capita | `financial_statements, cost_of_capital, investor_composition, macroeconomic_constraints, aegis_constraints, var` |
| `rare_pediatric_disease_designation_architect` | Synthesizes disease demographics, seriousness, mechanism of action, and scientific rationale into a  | `target_disease, pediatric_demographics, disease_seriousness, scientific_rationale` |
| `red_team_exploit_chain_architect` | Acts as a Principal Offensive Security Architect to engineer advanced, multi-staged exploit chains,  | `target_environment, initial_foothold, objective, macros` |
| `regulatory_compliance_automation_architect` | Architects automated regulatory compliance and continuous monitoring frameworks for heavily regulate | `regulatoryFramework, infrastructureType, keyControlRequirements` |
| `relevance_logic_entailment_evaluator` | A highly rigorous prompt designed to systematically evaluate natural language arguments and formal d | `NATURAL_LANGUAGE_ARGUMENT, RELEVANCE_SYSTEM, natural_language_argument, relevance_system` |
| `residential_segregation_spatial_inequality_modeler` | A Principal Sociologist and Urban Demographer agent designed to rigorously analyze residential segre | `demographic_data, focal_city` |
| `reversible_jump_mcmc_architect` | Acts as a Principal Statistician to systematically design and formulate Reversible Jump Markov Chain | `model_space, jump_proposals, target_posterior` |
| `risk_based_monitoring_strategist` | A Principal Clinical Operations Risk-Based Monitoring (RBM) Strategist that designs adaptive, risk-p | `PROTOCOL_SYNOPSIS, CRITICAL_DATA_VARIABLES, KNOWN_RISK_FACTORS` |
| `samd_hazard_traceability_matrix_generator` | Generates an ISO 14971-compliant Hazard Traceability Matrix (HTM) for Software as a Medical Device ( | `software_requirements, defect_logs, device_classification` |
| `samd_iec62304_software_architecture_architect` | Acts as a Principal Medical Device Software Architect to design rigorous Software Architecture Desig | `software_requirements_specification, safety_classification` |
| `samd_iec_62304_software_safety_classification_architect` | Acts as a Principal Medical Device Software Architect to rigorously evaluate and assign IEC 62304 so | `device_description, hazard_analysis, risk_control_measures` |
| `semantic_mutation_censorship_evasion_modeler` | A highly robust, expert-level prompt designed to computationally model the automated semantic mutati | `contagion_baseline_morphology, algorithmic_suppression_architecture, evolutionary_evasion_objective, baseline_morphology, evasion_objective, suppression_architecture` |
| `serre_spectral_sequence_calculator` | Acts as a Principal Algebraic Topologist to rigorously formulate and compute pages, differentials, a | `base_space, fiber_space, total_space, coefficient_ring, target_degree` |
| `set_theoretic_forcing_architect` | Formulates rigorous mathematical proofs utilizing Paul Cohen's technique of Set-Theoretic Forcing to | `GROUND_MODEL, FORCING_NOTION, THEOREM_STATEMENT` |
| `shotgun_metagenomic_assembly_binning_architect` | Architects robust and mathematically rigorous pipelines for the assembly and binning of short-read a | `sequencing_technology, environmental_context, assembly_graph_algorithm` |
| `signal_detection_evaluator` | A rigorous prompt for evaluating and validating pharmacovigilance safety signals based on quantitati | `safety_data, reference_safety_information` |
| `signal_detection_theory_architect` | Designs highly rigorous Signal Detection Theory (SDT) analytical frameworks, separating perceptual s | `experimental_task, stimulus_conditions, payoff_matrix` |
| `single_cell_rna_seq_trajectory_inference_architect` | Acts as a Principal Computational Biologist to computationally model single-cell RNA sequencing (scR | `count_matrix, cellular_metadata, trajectory_topology, velocity_data, constraints` |
| `social_isolation_epidemiological_contagion_modeler` | A highly robust, expert-level prompt designed to mathematically model and systematically map the com | `multimodal_data_schema, isolation_transmission_parameters, structural_intervention_objective, data_schema, intervention_objective, transmission_parameters` |
| `spatial_metapopulation_seir_epidemiology_architect` | A Principal Disease Ecologist and Mathematical Epidemiologist framework to strictly model complex sp | `host_species_description, inter_patch_migration_network, stochastic_forcing_conditions` |
| `spatial_mismatch_employment_accessibility_modeler` | A Principal Sociologist and Urban Demographer agent designed to rigorously analyze the Spatial Misma | `residential_demographics, employment_hubs, transit_infrastructure` |
| `spatial_transcriptomics_cellular_communication_architect` | Acts as a Principal Computational Biologist to rigorously model spatially-resolved ligand-receptor i | `spatial_count_matrix, spatial_coordinates, ligand_receptor_database, tissue_microenvironment_metadata, constraints` |
| `spatio_temporal_geostatistical_spde_inla_architect` | Acts as a Statistical Sciences Genesis Architect to formulate rigorous Spatio-Temporal Geostatistica | `spatial_domain, temporal_dynamics, observation_process` |
| `staggered_difference_in_differences_architect` | Formulates rigorous econometric identification strategies for panel data with staggered treatment ti | `data_structure, treatment_assignment, heterogeneity_concerns, identifying_assumptions` |
| `stiff_pde_numerical_stability_architect` | Applied Mathematics Genesis Architect prompt for generating rigorous numerical stability analyses an | `pde_system, boundary_conditions, spatial_domain, target_accuracy` |
| `stochastic_gene_regulatory_network_cme_architect` | Architects robust stochastic simulation frameworks for gene regulatory networks using the Chemical M | `regulatory_network_topology, kinetic_rate_constants, system_volume` |
| `stochastic_lotka_volterra_population_modeler` | Rigorously models stochastic multispecies population dynamics using generalized Lotka-Volterra equat | `species_network, environmental_stochasticity, spatial_configuration` |
| `stochastic_market_entry_greenfield_architect` | Architects rigorous stochastic market entry and Greenfield expansion models, integrating geopolitica | `target_market, capital_commitment, geopolitical_risk_factors, competitive_density, strategic_objective` |
| `stochastic_multi_objective_optimization_architect` | Acts as a Principal Operations Researcher designed to architect complex Multi-Objective Stochastic O | `objective_functions, decision_variables, uncertain_parameters, constraints, aegis_constraints, macros, var` |
| `stochastic_radicalization_cascade_modeler` | A highly robust, expert-level prompt designed to mathematically model and simulate nonlinear stochas | `radicalization_strain_vector, topological_graph_schema, extremization_collapse_objective, collapse_objective, graph_schema, strain_vector` |
| `string_worldsheet_scattering_amplitude_architect` | Systematically derives N-point string scattering amplitudes using the worldsheet formalism, computin | `string_type, external_states, kinematic_regime` |
| `structural_equation_modeling_architect` | Designs rigorous Structural Equation Models (SEM) for latent psychological constructs, providing lav | `theoretical_constructs, hypothesized_paths, observed_indicators` |
| `structural_proof_theory_cut_elimination_architect` | Automates the execution of rigorous cut-elimination procedures (Gentzen's Hauptsatz) for logical seq | `sequent, calculus_system` |
| `structural_vector_autoregression_architect` | Formulates rigorous Structural Vector Autoregression (SVAR) models for macroeconomic shock identific | `endogenous_variables, identification_scheme, exogenous_shocks` |
| `symplectic_manifold_moment_map_architect` | A Principal Research Mathematician designed to rigorously construct and analyze symplectic manifolds | `symplectic_manifold, lie_group_action, moment_map_task` |
| `synaptic_plasticity_weight_update_architect` | A Lead Computational Neuroscientist agent designed to mathematically formulate and analyze complex s | `plasticity_mechanism, synaptic_variables, network_context` |
| `synthetic_media_epistemic_collapse_modeler` | A highly robust, expert-level prompt designed to computationally model the propagation of generative | `synthetic_payload_schema, cognitive_network_topology, systemic_collapse_threshold, collapse_threshold, network_topology, synthetic_payload` |
| `target_trial_emulation_architect` | Acts as a Principal Statistician to design and formulate rigorous causal inference studies using the | `observational_data_structure, causal_question, confounding_factors` |
| `theil_t_index_inequality_decomposer` | A Principal Sociologist agent designed to execute rigorous Theil T Index decompositions for analyzin | `resource_variable, grouping_variable, population_context` |
| `top_down_proteomics_ptm_mapping_architect` | Acts as a Principal Computational Biologist to model and decipher high-resolution top-down proteomic | `intact_mass_spectrum, target_protein_sequence, fragmentation_method, expected_ptm_space, constraints` |
| `topos_theoretic_sheaf_semantics_evaluator` | Acts as a Principal Research Logician and Category Theorist to rigorously evaluate and translate mat | `source_category, target_topos, theorem_statement, forcing_condition` |
| `transactional_outbox_event_publishing_architect` | Designs robust, fault-tolerant Transactional Outbox patterns for reliable event publishing in micros | `bounded_context, primary_database, event_broker, latency_throughput_requirements, macros` |
| `transfinite_induction_well_ordering_architect` | Acts as a Principal Set Theorist to rigorously formulate multi-step proofs using transfinite inducti | `base_structure, inductive_property, limit_case_condition` |
| `turing_degree_reduction_evaluator` | Systematically formalizes and evaluates Turing reductions and many-one reductions between formal set | `source_set, target_set, reduction_type` |
| `ultraproduct_los_theorem_architect` | Acts as a Principal Mathematical Logician to rigorously formalize and analyze ultraproducts of struc | `signature, index_set, structures, logical_statement` |
| `variational_inference_architect` | Acts as a Principal Statistician to design and formulate complex Variational Inference (VI) approxim | `model_structure, data_characteristics, inference_objectives` |
| `vine_copula_dependency_architect` | Acts as a Principal Statistician to mathematically formulate and optimize high-dimensional Vine Copu | `marginal_distributions, dependence_structure, graphical_model_type, directives, persona` |
| `wealth_concentration_decomposition_architect` | A Principal Sociologist agent that systematically decomposes wealth concentration mechanisms and cal | `population_wealth_distribution, focal_mechanism` |
| `whole_brain_biophysical_network_simulator` | A Lead Computational Neuroscientist agent designed to architect multi-scale, automated whole-brain n | `multi_modal_bids_dataset, cellular_dynamics_framework, large_scale_network_topology` |
| `zero_based_budgeting_turnaround_architect` | Designs highly rigorous, quantitative Zero-Based Budgeting (ZBB) frameworks for distressed enterpris | `enterprise_profile, financial_targets, cost_centers` |

<!-- TOOL_REGISTRY_END -->