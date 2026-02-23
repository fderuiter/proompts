---
layout: home
title: Home
nav_order: 0
---

# Proompts

Welcome to **Proompts**, a curated collection of high-quality prompts and workflows for AI-assisted product development, regulatory compliance, and clinical research.

Whether you are a Product Manager, Clinical Lead, or Software Engineer, this repository provides the building blocks to operationalize LLMs in your daily work.

## Getting Started

1. **Browse Categories**: Explore prompts by domain (e.g., [Clinical](clinical.md), [Software Engineering](software_engineering.md)).
2. **Run Workflows**: Use our [Workflows Guide](workflow_guide.md) to learn how to chain multiple prompts together for complex tasks like "Idea to Epic".
3. **Copy & Customize**: All prompts are in YAML format, ready to be used in your own tools or agents.

## Key Concepts

- **Prompts**: Single-task instructions for an LLM (e.g., "Review this code", "Draft a protocol").
- **Workflows**: Sequences of prompts that pass data from one step to the next to achieve a larger goal.
- **Agents**: The AI systems that execute these prompts and workflows.
- **System Architecture**: Read the [canonical guide](system_architecture.md) to understand Prompts as Code, the Simulation Engine, and the Validation Pipeline.

## Browse by Category

- [Architecture](architecture.md)
- [Business](business.md)
- [Clinical](clinical.md)
- [Communication](communication.md)
- [Languages](languages.md)
- [Management](management.md)
- [Meta](meta.md)
- [Regulatory](regulatory.md)
- [Scientific](scientific.md)
- [Software Engineering](software_engineering.md)
- [Technical](technical.md)
- [Testing](testing.md)
- [Workflows](workflows.md)

## Search


<div class="search-container">
    <input type="text" id="search-input" placeholder="Search prompts..." style="width: 100%; padding: 10px; margin-bottom: 20px;">
    <ul id="results-container"></ul>
</div>

<script src="https://unpkg.com/simple-jekyll-search@latest/dest/simple-jekyll-search.min.js"></script>
<script>
    window.simpleJekyllSearch = new SimpleJekyllSearch({
        searchInput: document.getElementById('search-input'),
        resultsContainer: document.getElementById('results-container'),
        json: '{{ site.baseurl }}/search.json',
        searchResultTemplate: '<li><a href="{{ site.baseurl }}/{url}"><strong>{title}</strong></a><br><span style="font-size:0.8em">{description}</span></li>',
        noResultsText: 'No prompts found',
        limit: 10,
        fuzzy: false
    })
</script>


# All Prompts

## Adjudication

- [Real-Time Adjudication Visibility Dashboard](../prompts/clinical/adjudication/adjudication_workflow/01_real_time_adjudication_dashboard.prompt.yaml)
- [Source Document and Endpoint Checklist](../prompts/clinical/adjudication/adjudication_workflow/02_source_document_endpoint_checklist.prompt.yaml)
- [Analyze Adjudication KPIs](../prompts/clinical/adjudication/adjudication_workflow/03_analyze_adjudication_kpis.prompt.yaml)

## Architecture

- [TOGAF Phase A - Architecture Vision](../prompts/technical/architecture/togaf/phase_a_vision.prompt.yaml)
- [TOGAF Phase B - Business Architecture](../prompts/technical/architecture/togaf/phase_b_business.prompt.yaml)
- [TOGAF Phase C - Information Systems Architectures](../prompts/technical/architecture/togaf/phase_c_information_systems.prompt.yaml)
- [TOGAF Phase D - Technology Architecture](../prompts/technical/architecture/togaf/phase_d_technology.prompt.yaml)
- [TOGAF Phase E - Opportunities & Solutions](../prompts/technical/architecture/togaf/phase_e_opportunities.prompt.yaml)
- [TOGAF Phase F - Migration Planning](../prompts/technical/architecture/togaf/phase_f_migration.prompt.yaml)
- [TOGAF Phase G - Implementation Governance](../prompts/technical/architecture/togaf/phase_g_governance.prompt.yaml)
- [TOGAF Phase H - Architecture Change Management](../prompts/technical/architecture/togaf/phase_h_change_management.prompt.yaml)
- [TOGAF Preliminary Phase](../prompts/technical/architecture/togaf/preliminary_phase.prompt.yaml)
- [TOGAF Requirements Management](../prompts/technical/architecture/togaf/requirements_management.prompt.yaml)

## Biosafety

- [Risk Assessment Expert](../prompts/scientific/biosafety/biological_safety_workflow/01_risk_assessment_expert.prompt.yaml)
- [Biological Safety Plan Developer](../prompts/scientific/biosafety/biological_safety_workflow/02_biological_safety_plan_developer.prompt.yaml)
- [Regulatory Submission Support](../prompts/scientific/biosafety/biological_safety_workflow/03_regulatory_submission_support.prompt.yaml)

## Bioskills

- [Hands-On Procedure Coaching](../prompts/scientific/bioskills/bioskills_workflow/01_hands_on_procedure_coaching.prompt.yaml)
- [Simulated Clinical Scenario Debrief](../prompts/scientific/bioskills/bioskills_workflow/02_simulated_clinical_scenario_feedback.prompt.yaml)
- [Objective Skills Assessment](../prompts/scientific/bioskills/bioskills_workflow/03_objective_skills_assessment.prompt.yaml)

## Business

- [Board Deck Narrative Generation](../prompts/business/cfo/board_deck_narrative.prompt.yaml)
- [Earnings Call Script Prep](../prompts/business/cfo/earnings_call_script_prep.prompt.yaml)
- [Investor FAQ Generation](../prompts/business/cfo/investor_faq_generation.prompt.yaml)
- [Liquidity Stress Test](../prompts/business/cfo/liquidity_stress_test.prompt.yaml)
- [M&A Target Evaluation](../prompts/business/cfo/ma_target_evaluation.prompt.yaml)
- [Net Present Value Socratic Tutor](../prompts/business/cfo/npv_tutor.prompt.yaml)
- [Regulatory Compliance Summary](../prompts/business/cfo/regulatory_compliance_summary.prompt.yaml)
- [Scenario Modeling & Sensitivity Analysis](../prompts/business/cfo/scenario_modeling_sensitivity.prompt.yaml)
- [Budget Variance Analysis](../prompts/business/cfo/variance_analysis.prompt.yaml)
- [CSM Portfolio Balancing](../prompts/business/cx/csm_portfolio_balancing.prompt.yaml)
- [Friction-Hunting Onboarding Audit](../prompts/business/cx/onboarding_audit.prompt.yaml)
- [Red Account Turnaround Strategy](../prompts/business/cx/red_account_turnaround.prompt.yaml)
- [Cross-Functional Advocacy Memo](../prompts/business/cx/revenue_risk_advocacy.prompt.yaml)
- [Voice of Customer Root Cause Analysis](../prompts/business/cx/root_cause_analysis.prompt.yaml)
- [Trend Spotting vs Anomalies](../prompts/business/cx/trend_spotting.prompt.yaml)
- [Value-Based QBR Generator](../prompts/business/cx/value_based_qbr.prompt.yaml)
- [90-Day Pipeline Health & Next-Best-Action Review](../prompts/business/development/90_day_pipeline_health_review.prompt.yaml)
- [Competitor-Positioning Brief](../prompts/business/development/competitor_positioning_brief.prompt.yaml)
- [Emerging-Market Opportunity Scan](../prompts/business/development/emerging_market_opportunity_scan.prompt.yaml)
- [Market-Intelligence Radar](../prompts/business/development/market_intelligence_radar.prompt.yaml)
- [Marketing Campaign for Clinical Services](../prompts/business/development/marketing_campaign_in_silico.prompt.yaml)
- [Rapid Proposal Builder](../prompts/business/development/rapid_proposal_builder.prompt.yaml)
- [RFP Executive-Summary Generator](../prompts/business/development/rfp_executive_summary_generator.prompt.yaml)
- [Strategic Business Case for New Service Line](../prompts/business/development/strategic_business_case_in_silico.prompt.yaml)
- [Clinical-Trial Budget and Burn-Rate Dashboard](../prompts/business/hr_finance/clinical_trial_budget_burn_rate_dashboard.prompt.yaml)
- [GCP and GDPR Training Compliance Risk Report](../prompts/business/hr_finance/gcp_gdpr_compliance_training_risk_report.prompt.yaml)
- [Strategic Workforce and Talent Acquisition Plan](../prompts/business/hr_finance/strategic_workforce_talent_acquisition_plan.prompt.yaml)
- [Build an Audit-Ready Site-Payment Schedule](../prompts/business/payment/audit_ready_site_payment_schedule.prompt.yaml)
- [Medicare Coverage Analysis](../prompts/business/payment/coverage_analysis.prompt.yaml)
- [Global Regulatory and Tax Matrix for Site Payments](../prompts/business/payment/global_regulatory_tax_matrix.prompt.yaml)
- [Investigator-Site Payment Forecast](../prompts/business/payment/investigator_site_payment_forecast.prompt.yaml)
- [Payment-Process Risk Assessment and Mitigation](../prompts/business/payment/payment_process_risk_assessment.prompt.yaml)
- [Payment Reconciliation and Discrepancy Report](../prompts/business/payment/payment_reconciliation_discrepancy_report.prompt.yaml)
- [Sunshine Act and FMV Compliance Check](../prompts/business/payment/sunshine_act_fmv_compliance_check.prompt.yaml)
- [Build vs. Buy Decision Matrix](../prompts/business/vp_tech_innovation/build_vs_buy_matrix.prompt.yaml)
- [Disruption Radar](../prompts/business/vp_tech_innovation/disruption_radar.prompt.yaml)
- [Elevator Pitch for Expensive Tech](../prompts/business/vp_tech_innovation/elevator_pitch_expensive_tech.prompt.yaml)
- [Hype vs. Reality Analysis](../prompts/business/vp_tech_innovation/hype_vs_reality_analysis.prompt.yaml)
- [Legacy Modernization Strategy](../prompts/business/vp_tech_innovation/legacy_modernization_strategy.prompt.yaml)
- [Post-Mortem / Incident Report Summary](../prompts/business/vp_tech_innovation/post_mortem_summary.prompt.yaml)
- [Preventing Technical Debt](../prompts/business/vp_tech_innovation/preventing_technical_debt.prompt.yaml)
- [Upskilling Program Design](../prompts/business/vp_tech_innovation/upskilling_program_design.prompt.yaml)

## Cfo

- [Scenario-Based Clinical-Trial Cash-Flow Forecast](../prompts/business/cfo/cfo_workflow/01_scenario_cash_flow_forecast.prompt.yaml)
- [Competitive-Bid Pricing & Margin Optimizer](../prompts/business/cfo/cfo_workflow/02_competitive_bid_pricing.prompt.yaml)
- [Regulatory-Risk & ESG Impact Dashboard Builder](../prompts/business/cfo/cfo_workflow/03_regulatory_risk_dashboard.prompt.yaml)

## Chemical Characterization

- [Design the Study](../prompts/scientific/chemical_characterization/chemical_characterization_workflow/01_design_the_study.prompt.yaml)
- [Interpret the Chemistry & Assess Risk](../prompts/scientific/chemical_characterization/chemical_characterization_workflow/02_interpret_the_chemistry_assess_risk.prompt.yaml)
- [Write the Regulatory Summary](../prompts/scientific/chemical_characterization/chemical_characterization_workflow/03_write_the_regulatory_summary.prompt.yaml)

## Clinical

- [Audit Trail Review](../prompts/clinical/data_management/audit_trail_review.prompt.yaml)
- [CDISC CRF Architect](../prompts/clinical/data_management/cdisc_crf_architect.prompt.yaml)
- [CDISC SDTM/ADaM Mapping](../prompts/clinical/data_management/cdisc_mapping.prompt.yaml)
- [Data Architecture Blueprint](../prompts/clinical/data_management/data_architecture_blueprint.prompt.yaml)
- [Data De-identification](../prompts/clinical/data_management/data_deidentification.prompt.yaml)
- [Database Lock Procedures](../prompts/clinical/data_management/database_lock_procedures.prompt.yaml)
- [Decentralized Trial Risk Matrix](../prompts/clinical/data_management/decentralized_trial_risk_matrix.prompt.yaml)
- [Data Management Plan (DMP) Development](../prompts/clinical/data_management/dmp_development.prompt.yaml)
- [Clinical Trial Document Archiving](../prompts/clinical/data_management/document_archiving.prompt.yaml)
- [eTMF Artifact Classifier](../prompts/clinical/data_management/etmf_artifact_classifier.prompt.yaml)
- [Medical Coding and Reconciliation Assistant](../prompts/clinical/data_management/medical_coding_reconciliation.prompt.yaml)
- [Metadata Management](../prompts/clinical/data_management/metadata_management.prompt.yaml)
- [21 CFR Part 11 Compliance Verification](../prompts/clinical/data_management/part_11_compliance_verification.prompt.yaml)
- [Phase II Oncology DMP](../prompts/clinical/data_management/phase_ii_oncology_dmp.prompt.yaml)
- [Regulatory Compliance Verification](../prompts/clinical/data_management/regulatory_compliance_verification.prompt.yaml)
- [Regulatory Gap Analysis](../prompts/clinical/data_management/regulatory_gap_analysis.prompt.yaml)
- [SOP Gap Analysis](../prompts/clinical/data_management/sop_gap_analysis.prompt.yaml)
- [Trial Master File (TMF) Maintenance](../prompts/clinical/data_management/tmf_maintenance.prompt.yaml)
- [Unified Data Cleansing](../prompts/clinical/data_management/unified_data_cleansing.prompt.yaml)
- [Computer System Validation (CSV)](../prompts/clinical/eclinical_integration/computer_system_validation.prompt.yaml)
- [Digital Health Technology (DHT) Validation](../prompts/clinical/eclinical_integration/dht_validation.prompt.yaml)
- [eConsent Implementation Strategy](../prompts/clinical/eclinical_integration/econsent_implementation.prompt.yaml)
- [IQ/OQ/PQ Validation](../prompts/clinical/eclinical_integration/iq_oq_pq_validation.prompt.yaml)
- [UAT Script Generator](../prompts/clinical/eclinical_integration/uat_script_generator.prompt.yaml)
- [CDASH Alignment](../prompts/clinical/forms/cdash_alignment.prompt.yaml)
- [Design Error Prevention](../prompts/clinical/forms/crf_design_optimization.prompt.yaml)
- [Electronic Data Capture Implementation](../prompts/clinical/forms/ecrf_implementation.prompt.yaml)
- [Semantic Interoperability Optimization](../prompts/clinical/forms/semantic_interoperability.prompt.yaml)
- [Clinical Study Report (CSR) Narrative Drafter](../prompts/clinical/medical_writing/csr_narrative_drafter.prompt.yaml)
- [Clinical Monitoring Plan Development](../prompts/clinical/monitoring/clinical_monitoring_plan.prompt.yaml)
- [Risk-Based Monitoring Data Evaluation](../prompts/clinical/monitoring/rbm_data_evaluation.prompt.yaml)
- [RBQM Anomaly Detection](../prompts/clinical/monitoring/rbqm_anomaly_detection.prompt.yaml)
- [Protocol Deviation Reporting](../prompts/clinical/protocol/protocol_deviation_reporting.prompt.yaml)
- [Protocol to CDISC USDM v3.0 Converter](../prompts/clinical/protocol/protocol_to_usdm_v3.prompt.yaml)
- [SOP and TMF Document Synthesis](../prompts/clinical/protocol/sop_tmf_document_synthesis.prompt.yaml)
- [SAE and Safety Reporting](../prompts/clinical/safety/sae_safety_reporting.prompt.yaml)
- [Clinical Trial Agreement (CTA) Negotiation](../prompts/clinical/site_acquisition/cta_negotiation.prompt.yaml)
- [Single IRB (sIRB) Plan Submission](../prompts/clinical/site_acquisition/sirb_plan_submission.prompt.yaml)
- [Site Selection and Enrollment Forecaster](../prompts/clinical/site_acquisition/site_enrollment_forecaster.prompt.yaml)
- [Compassionate Music Therapist & Composer](../prompts/clinical/therapy/music_therapist_melody.prompt.yaml)
- [Adaptive Recruitment and Retention Strategy](../prompts/clinical/trial_execution/adaptive_recruitment_retention_strategy.prompt.yaml)
- [AI-Powered Site and Recruitment Strategy](../prompts/clinical/trial_execution/ai_powered_site_recruitment.prompt.yaml)
- [Compliance and Data Quality Monitoring Plan](../prompts/clinical/trial_execution/compliance_data_quality_monitoring_plan.prompt.yaml)
- [Diversity Action Plan Development](../prompts/clinical/trial_execution/diversity_action_plan_document.prompt.yaml)
- [Informed Consent Process Optimization](../prompts/clinical/trial_execution/informed_consent_process.prompt.yaml)
- [Portfolio-Level Clinical Operations Roadmap](../prompts/clinical/trial_execution/portfolio_clin_ops_roadmap.prompt.yaml)
- [Protocol Optimization and Risk Simulation](../prompts/clinical/trial_execution/protocol_optimization_risk_simulation.prompt.yaml)
- [Patient Recruitment and Diversity Acceleration Plan](../prompts/clinical/trial_execution/recruitment_diversity_acceleration.prompt.yaml)
- [Risk-Based Monitoring and Quality Plan](../prompts/clinical/trial_execution/risk_based_monitoring_plan.prompt.yaml)

## Communication

- [80/20 Crash Course](../prompts/communication/80_20_crash_course.prompt.yaml)
- [Analogy Architect](../prompts/communication/analogy_architect.prompt.yaml)
- [Data-to-Insight Analyst](../prompts/communication/data_to_insight_analyst.prompt.yaml)
- [Density Refiner](../prompts/communication/density_refiner.prompt.yaml)
- [Devil’s-Advocate Stress Test](../prompts/communication/devils_advocate_stress_test.prompt.yaml)
- [Empathy-Map Facilitator](../prompts/communication/empathy_map_facilitator.prompt.yaml)
- [Explain-Like-I’m-5 (ELI5)](../prompts/communication/explain_like_im_5.prompt.yaml)
- [Hero's Journey Storyboarder](../prompts/communication/heros_journey_storyboarder.prompt.yaml)
- [Lay Language Summary Creation](../prompts/communication/lay_language_summary.prompt.yaml)
- [Negotiation Coach](../prompts/communication/negotiation_coach.prompt.yaml)
- [Panel Debate](../prompts/communication/panel_debate.prompt.yaml)
- [Pitch-Deck Outliner](../prompts/communication/pitch_deck_outliner.prompt.yaml)
- [Rapid-Risk-Matrix](../prompts/communication/rapid_risk_matrix.prompt.yaml)
- [Red-Team Stress-Test Simulation](../prompts/communication/red_team_stress_test.prompt.yaml)
- [Rubber Duck Debugger](../prompts/communication/rubber_duck_debugger.prompt.yaml)
- [Smart Task Prioritizer](../prompts/communication/smart_task_prioritizer.prompt.yaml)
- [Socratic-Coach](../prompts/communication/socratic_coach.prompt.yaml)
- [Pixar Story Spine Outline](../prompts/communication/story_spine_outline.prompt.yaml)
- [Storyboard-My-Idea](../prompts/communication/storyboard_my_idea.prompt.yaml)
- [Executive Briefing Architect (TL;DR)](../prompts/communication/tldr_summarizer.prompt.yaml)
- [Writing Clarity Mentor](../prompts/communication/writing_clarity_mentor.prompt.yaml)

## Cra

- [Monitoring-Visit Report Generator](../prompts/clinical/cra/cra_workflow/01_monitoring_visit_report_generator.prompt.yaml)
- [Investigator Follow-up Email & Action-Item Tracker](../prompts/clinical/cra/cra_workflow/02_investigator_follow_up_email_tracker.prompt.yaml)
- [Risk-Based Monitoring (RBM) Plan Builder](../prompts/clinical/cra/cra_workflow/03_rbm_plan_builder.prompt.yaml)

## Data

- [Discrepancy Detection & Query Log Generator](../prompts/clinical/data/clinical_data_workflow/01_discrepancy_detection_query_log.prompt.yaml)
- [Draft a Data Management Plan Section](../prompts/clinical/data/clinical_data_workflow/02_data_management_plan_section.prompt.yaml)
- [Edit-Check Specification Builder for New eCRF Fields](../prompts/clinical/data/clinical_data_workflow/03_edit_check_specification_builder.prompt.yaml)

## Data Management

- [Protocol-to-TS Generator](../prompts/clinical/data_management/cdisc_compliance_workflow/01_protocol_to_ts_generator.prompt.yaml)
- [Raw-to-SDTM Auto-Mapper](../prompts/clinical/data_management/cdisc_compliance_workflow/02_raw_to_sdtm_auto_mapper.prompt.yaml)
- [ADaM Derivation Writer](../prompts/clinical/data_management/cdisc_compliance_workflow/03_adam_derivation_writer.prompt.yaml)
- [Controlled Terminology Harmonizer](../prompts/clinical/data_management/cdisc_compliance_workflow/04_controlled_terminology_harmonizer.prompt.yaml)
- [Clinical ETL Mapping Spec](../prompts/clinical/data_management/data_management_etl_workflow/01_clinical_etl_mapping_spec.prompt.yaml)
- [Clinical ETL Transformation QC](../prompts/clinical/data_management/data_management_etl_workflow/02_clinical_etl_transformation_qc.prompt.yaml)
- [Clinical ETL Pipeline Review](../prompts/clinical/data_management/data_management_etl_workflow/03_clinical_etl_pipeline_review.prompt.yaml)

## Data Science

- [Stochastic Architect](../prompts/technical/data_science/stochastic_model_chain_workflow/01_stochastic_architect.prompt.yaml)
- [Stochastic Engineer](../prompts/technical/data_science/stochastic_model_chain_workflow/02_stochastic_engineer.prompt.yaml)
- [Stochastic Strategist](../prompts/technical/data_science/stochastic_model_chain_workflow/03_stochastic_strategist.prompt.yaml)

## Eclinical Integration

- [Architect the Integration Blueprint](../prompts/clinical/eclinical_integration/eclinical_integration_workflow/01_architect_integration_blueprint.prompt.yaml)
- [Data Mapping and Transformation Playbook](../prompts/clinical/eclinical_integration/eclinical_integration_workflow/02_data_mapping_transformation_playbook.prompt.yaml)
- [Regulatory and Validation Checklist](../prompts/clinical/eclinical_integration/eclinical_integration_workflow/03_regulatory_validation_checklist.prompt.yaml)

## Epro

- [Patient-Centric BYOD ePRO Workflow](../prompts/clinical/epro/epro_workflow/01_patient-centric_byod_workflow.prompt.yaml)
- [Optimize ePRO Form Design](../prompts/clinical/epro/epro_workflow/02_optimize_epro_form_design.prompt.yaml)
- [ePRO Adoption Plan for Sponsors](../prompts/clinical/epro/epro_workflow/03_epro_adoption_plan_for_sponsors.prompt.yaml)

## Forms

- [CRF Shell Generator](../prompts/clinical/forms/clinical_prompts_workflow/01_crf_shell_generator.prompt.yaml)
- [CRF Quality Auditor](../prompts/clinical/forms/clinical_prompts_workflow/02_crf_quality_auditor.prompt.yaml)
- [CDASH Mapping & Completion-Guide Assistant](../prompts/clinical/forms/clinical_prompts_workflow/03_cdash_mapping_completion_guide.prompt.yaml)

## Imaging

- [Imaging Charter Draft](../prompts/clinical/imaging/imaging_workflow/01_imaging_charter_draft.prompt.yaml)
- [Site Upload QC and Query Generator](../prompts/clinical/imaging/imaging_workflow/02_site_upload_qc.prompt.yaml)
- [Central Reading Paradigm Design](../prompts/clinical/imaging/imaging_workflow/03_central_reading_design.prompt.yaml)
- [Regulatory Imaging Charter Generator](../prompts/clinical/imaging/imaging_workflow/04_regulatory_imaging_charter_generator.prompt.yaml)
- [Image Acquisition QC Workflow Blueprint](../prompts/clinical/imaging/imaging_workflow/05_image_acquisition_qc_workflow_blueprint.prompt.yaml)
- [Regulatory Imaging Data Package](../prompts/clinical/imaging/imaging_workflow/06_regulatory_imaging_data_package.prompt.yaml)

## Languages

- [Advanced Python Testing](../prompts/technical/languages/python/advanced_python_testing.prompt.yaml)
- [Principal Python Developer](../prompts/technical/languages/python/principal_python_developer.prompt.yaml)
- [Python Concurrency Mastery](../prompts/technical/languages/python/python_concurrency_mastery.prompt.yaml)
- [Python Hexagonal Architecture](../prompts/technical/languages/python/python_hexagonal_architecture.prompt.yaml)
- [Python Performance Optimization](../prompts/technical/languages/python/python_performance_optimization.prompt.yaml)
- [Senior Python Developer](../prompts/technical/languages/python/senior_python_developer.prompt.yaml)
- [Principal Rust Developer](../prompts/technical/languages/rust/principal_rust_developer.prompt.yaml)
- [Rust Architectural Patterns](../prompts/technical/languages/rust/rust_architectural_patterns.prompt.yaml)
- [Principal TypeScript Developer](../prompts/technical/languages/typescript/principal_typescript_developer.prompt.yaml)

## Lifecycle

- [Product Brief Template](../prompts/technical/software_engineering/lifecycle/agentic_coding_workflow/01_product_brief.prompt.yaml)
- [Project Brief for Epic](../prompts/technical/software_engineering/lifecycle/agentic_coding_workflow/02_project_brief_epic.prompt.yaml)

## Management

- [Accelerate Patient Recruitment & Retention](../prompts/management/clinical_research_manager/accelerate_patient_recruitment_retention.prompt.yaml)
- [Digest Regulatory Updates Affecting Protocol](../prompts/management/clinical_research_manager/digest_regulatory_updates.prompt.yaml)
- [Portfolio KPI Dashboard Brief](../prompts/management/clinical_research_manager/portfolio_kpi_dashboard_brief.prompt.yaml)
- [FDA-Aligned AI Governance Framework](../prompts/management/executive/ai_governance_framework.prompt.yaml)
- [Crisis-Management Playbook Generator](../prompts/management/executive/crisis_management_playbook.prompt.yaml)
- [Digital Transformation Roadmap for Clinical Operations](../prompts/management/executive/digital_transformation_roadmap.prompt.yaml)
- [Emerging-Science Horizon Scan](../prompts/management/executive/emerging_science_horizon_scan.prompt.yaml)
- [Executive-Ready Brief and Talking Points](../prompts/management/executive/executive_brief_synthesizer.prompt.yaml)
- [Executive Trial-Health Dashboard](../prompts/management/executive/executive_trial_health_dashboard.prompt.yaml)
- [Hosting Cost Reduction ToT Plan](../prompts/management/executive/hosting_cost_reduction_tot.prompt.yaml)
- [Quarterly Innovation Radar for Decentralized and Hybrid Trials](../prompts/management/executive/innovation_radar.prompt.yaml)
- [Investor and Board Narrative Builder](../prompts/management/executive/investor_board_narrative_builder.prompt.yaml)
- [Strategic Market and Competitor Radar](../prompts/management/executive/market_competitor_radar.prompt.yaml)
- [Regulatory and Competitive Intelligence Briefing](../prompts/management/executive/regulatory_competitive_intel_briefing.prompt.yaml)
- [Strategic Consultant SWOT](../prompts/management/executive/strategic_consultant_swot.prompt.yaml)
- [Strategic Growth Roadmap](../prompts/management/executive/strategic_growth_roadmap.prompt.yaml)
- [Strategic Market Foresight and Action Plan](../prompts/management/executive/strategic_market_foresight.prompt.yaml)
- [Strategic Portfolio Prioritizer](../prompts/management/executive/strategic_portfolio_prioritizer.prompt.yaml)
- [Trial-Design Optimisation Memo](../prompts/management/executive/trial_design_optimisation_memo.prompt.yaml)
- [Reverse Brainstorming](../prompts/management/innovation/reverse_brainstorming.prompt.yaml)
- [SCAMPER Ideation Coach](../prompts/management/innovation/scamper_ideation_coach.prompt.yaml)
- [90-Day Biostatistics Onboarding Plan](../prompts/management/leadership/biostatistics_onboarding_plan.prompt.yaml)
- [Leadership Reflection and Culture](../prompts/management/leadership/leadership_reflection_culture.prompt.yaml)
- [Operational Excellence Communication Framework](../prompts/management/leadership/operational_excellence_communication.prompt.yaml)
- [Strategic Alignment and Innovation](../prompts/management/leadership/strategic_alignment_innovation.prompt.yaml)
- [AI-Enhanced RBM Action Plan](../prompts/management/medical_director/ai_enhanced_rbm_action_plan.prompt.yaml)
- [Clinical Trial Protocol Compliance Review](../prompts/management/medical_director/clinical_trial_protocol_quality_compliance_review.prompt.yaml)
- [Pharmacovigilance Safety Signal Prioritization](../prompts/management/medical_director/pharmacovigilance_safety_signal_prioritization.prompt.yaml)
- [Action-Oriented Meeting Minutes & Tracker](../prompts/management/operations/action_oriented_meeting_minutes.prompt.yaml)
- [CRO Trial-Performance KPI Dashboard Blueprint](../prompts/management/operations/cro_trial_performance_kpi_dashboard_blueprint.prompt.yaml)
- [Fair-Market-Value Budget Negotiation Brief](../prompts/management/operations/fair_market_value_budget_negotiation_brief.prompt.yaml)
- [Fishbone Facilitator](../prompts/management/operations/fishbone_facilitator.prompt.yaml)
- [Forward-Looking Resource & Capacity Forecast](../prompts/management/operations/forward_capacity_forecast.prompt.yaml)
- [Inventory & Demand-Planning Simulation](../prompts/management/operations/inventory_demand_planning_simulation.prompt.yaml)
- [KPI Dashboard & Monthly Ops-Review Pack](../prompts/management/operations/kpi_dashboard_ops_review.prompt.yaml)
- [Multistudy Resource & Capacity Forecast Plan](../prompts/management/operations/multistudy_resource_capacity_forecast_plan.prompt.yaml)
- [Operational Excellence & Risk Sweep](../prompts/management/operations/operational_excellence_risk_sweep.prompt.yaml)
- [360° Operational KPI & Benchmark Review](../prompts/management/operations/operational_kpi_benchmark_review.prompt.yaml)
- [Proactive Risk Heat-Map for Decentralized & Virtual Trials](../prompts/management/operations/proactive_risk_heat_map.prompt.yaml)
- [Quarterly CRO KPI Executive Brief](../prompts/management/operations/quarterly_kpi_executive_brief.prompt.yaml)
- [Rapid Process Diagnostic & Lean Improvement Plan](../prompts/management/operations/rapid_process_diagnostic.prompt.yaml)
- [Rolling Resource & Capacity Forecast](../prompts/management/operations/rolling_resource_capacity_forecast.prompt.yaml)
- [Study Start-Up Checklist & Timeline](../prompts/management/operations/study_startup_checklist.prompt.yaml)
- [Risk-Based Vendor Performance Improvement Plan](../prompts/management/operations/vendor_performance_improvement_plan.prompt.yaml)
- [Vendor Qualification and Oversight](../prompts/management/operations/vendor_qualification.prompt.yaml)
- [Weekly Operations KPI Snapshot](../prompts/management/operations/weekly_ops_kpi_snapshot.prompt.yaml)
- [Career Compass Advisor](../prompts/management/personal_effectiveness/career_compass_advisor.prompt.yaml)
- [Eisenhower Matrix Coach](../prompts/management/personal_effectiveness/eisenhower_matrix_coach.prompt.yaml)
- [Scenario-Based Financial Navigator](../prompts/management/personal_effectiveness/financial_navigator.prompt.yaml)
- [Learning Path Mentor](../prompts/management/personal_effectiveness/learning_path_mentor.prompt.yaml)
- [Micro-Habit Health Coach](../prompts/management/personal_effectiveness/micro_habit_health_coach.prompt.yaml)
- [Second-Order Thinking Oracle](../prompts/management/personal_effectiveness/second_order_thinking_oracle.prompt.yaml)
- [Clinical-Trial Timeline and Risk Radar](../prompts/management/project_management/clinical_trial_timeline_risk_radar.prompt.yaml)
- [Cross-Study Operational Risk Heat Map and Mitigation Plan](../prompts/management/project_management/cross_study_risk_heat_map_mitigation_plan.prompt.yaml)
- [Executive Sponsor Briefing Deck Outline](../prompts/management/project_management/executive_sponsor_briefing_deck_outline.prompt.yaml)
- [Senior Agile Transformation Coach (Retrospectives)](../prompts/management/project_management/neutral_scrum_retro.prompt.yaml)
- [Portfolio Resource and Budget Forecast](../prompts/management/project_management/portfolio_resource_budget_forecast.prompt.yaml)
- [Project Starter Pack Prompts](../prompts/management/project_management/project_starter_pack.prompt.yaml)
- [RACI Mapper](../prompts/management/project_management/raci_mapper.prompt.yaml)
- [Risk and Pre-Mortem Analysis](../prompts/management/project_management/risk_pre_mortem_analysis.prompt.yaml)
- [Rollout Risk Matrix](../prompts/management/project_management/rollout_risk_matrix.prompt.yaml)
- [Sponsor-Ready Monthly Status Brief](../prompts/management/project_management/sponsor_ready_monthly_status_brief.prompt.yaml)
- [Status Update and Task Prioritization](../prompts/management/project_management/status_update_task_prioritization.prompt.yaml)
- [TMF Gap-Analysis and Audit Readiness Check](../prompts/management/project_management/tmf_gap_analysis_audit_readiness_check.prompt.yaml)

## Market Research

- [Market Landscape & Trend Analysis](../prompts/business/market_research/market_research_workflow/01_market_landscape_trend_analysis.prompt.yaml)
- [Target Segment & User Needs Assessment](../prompts/business/market_research/market_research_workflow/02_target_segment_user_needs_assessment.prompt.yaml)
- [Regulatory & Commercial Barrier Mapping](../prompts/business/market_research/market_research_workflow/03_regulatory_commercial_barrier_mapping.prompt.yaml)
- [Market Report Executive Summary](../prompts/business/market_research/market_research_workflow/04_market_report_exec_summary.prompt.yaml)

## Meta

- [Master Ultrameta Prompt Architect](../prompts/meta/meta_prompt_chain/00_L0_master-ultrameta.prompt.yaml)
- [Meta Prompt Architect](../prompts/meta/meta_prompt_chain/01_L1_meta-prompt-architect.prompt.yaml)
- [Prompt Engineer Template](../prompts/meta/meta_prompt_chain/02_L2_prompt-engineer.prompt.yaml)
- [Task Prototyper](../prompts/meta/meta_prompt_chain/03_L3_task-prototyper.prompt.yaml)
- [Worker Prompt](../prompts/meta/meta_prompt_chain/04_L4_worker_prompt.prompt.yaml)
- [Agent Persona Generator](../prompts/meta/meta_prompt_chain/05_L5_agent_persona_generator.prompt.yaml)
- [AGENTS.md Checklist Generator](../prompts/meta/meta_prompt_chain/05_L5_agents-md-checklist.prompt.yaml)
- [AI Coding Agent Plan Generator](../prompts/meta/meta_prompt_chain/05_L5_ai_coding_agent.prompt.yaml)
- [Comprehensive Task Template](../prompts/meta/meta_prompt_chain/05_L5_comprehensive_task_template.prompt.yaml)
- [MECE Structuring Consultant](../prompts/meta/meta_prompt_chain/05_L5_mece_structuring.prompt.yaml)
- [Prompt Engineer Fact Checker](../prompts/meta/meta_prompt_chain/05_L5_prompt_engineer_fact_checker.prompt.yaml)
- [PromptCrafter GPT](../prompts/meta/meta_prompt_chain/05_L5_promptcrafter_gpt.prompt.yaml)
- [README Generator](../prompts/meta/meta_prompt_chain/05_L5_readme-generator.prompt.yaml)

## Microbiology

- [Bioburden Testing SOP](../prompts/scientific/microbiology/microbiology_workflow/01_bioburden_testing_sop.prompt.yaml)
- [EO Sterilization Validation Protocol](../prompts/scientific/microbiology/microbiology_workflow/02_eo_sterilization_validation_protocol.prompt.yaml)
- [Endotoxin Control & 510(k) Risk Plan](../prompts/scientific/microbiology/microbiology_workflow/03_endotoxin_control_510k_risk_plan.prompt.yaml)

## Monitoring

- [Risk-Based Site Performance Dashboard](../prompts/clinical/monitoring/clinical_monitoring_workflow/01_risk_based_site_performance_dashboard.prompt.yaml)
- [CAPA Plan Builder for Monitoring Findings](../prompts/clinical/monitoring/clinical_monitoring_workflow/02_capa_plan_builder_for_monitoring_findings.prompt.yaml)
- [Monitoring Visit Report (MVR) Quality Critique](../prompts/clinical/monitoring/clinical_monitoring_workflow/03_monitoring_visit_report_quality_critique.prompt.yaml)

## Pathology

- [Design a Robust Preclinical Pathology Study Protocol](../prompts/scientific/pathology/pathology_study_workflow/01_study_protocol_outline.prompt.yaml)
- [Evaluate Device–Tissue Interface Findings](../prompts/scientific/pathology/pathology_study_workflow/02_device_tissue_interface_evaluation.prompt.yaml)
- [Prepare Pathology Slides and Reporting Plan](../prompts/scientific/pathology/pathology_study_workflow/03_slides_and_reporting_workflow.prompt.yaml)

## Project Management

- [Project Charter and Scope Definition](../prompts/management/project_management/project_management_workflow/01_project_charter_scope.prompt.yaml)
- [Comprehensive Risk Register and Mitigation Plan](../prompts/management/project_management/project_management_workflow/02_risk_register_mitigation.prompt.yaml)
- [Weekly Executive Status Report](../prompts/management/project_management/project_management_workflow/03_weekly_exec_status_report.prompt.yaml)
- [Detailed Project Blueprint and Timeline](../prompts/management/project_management/project_management_workflow/04_detailed_project_blueprint_timeline.prompt.yaml)

## Protocol

- [Clinical-Trial Protocol Creator](../prompts/clinical/protocol/protocol_workflow/01_clinical_trial_protocol_creator.prompt.yaml)
- [Ultimate SOP Architect](../prompts/clinical/protocol/protocol_workflow/02_ultimate_sop_architect.prompt.yaml)
- [Protocol Reviewer and Gap-Analysis Coach](../prompts/clinical/protocol/protocol_workflow/03_protocol_reviewer_gap_analysis_coach.prompt.yaml)
- [Protocol Section Refinement](../prompts/clinical/protocol/protocol_workflow/04_protocol_section_refinement.prompt.yaml)
- [Protocol to USDM Stage 1 - Metadata](../prompts/clinical/protocol/usdm_workflow/01_usdm_stage1_metadata.prompt.yaml)
- [Protocol to USDM Stage 2 - Rationale](../prompts/clinical/protocol/usdm_workflow/02_usdm_stage2_rationale.prompt.yaml)
- [Protocol to USDM Stage 3 - Workflow](../prompts/clinical/protocol/usdm_workflow/03_usdm_stage3_workflow.prompt.yaml)
- [Protocol to USDM Stage 4 - Concepts](../prompts/clinical/protocol/usdm_workflow/04_usdm_stage4_concepts.prompt.yaml)
- [Protocol to USDM Stage 5 - Assembly](../prompts/clinical/protocol/usdm_workflow/05_usdm_stage5_assembly.prompt.yaml)

## Regulatory

- [ALCOA-C Data Integrity Checklist](../prompts/regulatory/adherence/alcoa_c_data_integrity_checklist.prompt.yaml)
- [DHT Integration Regulatory Checklist](../prompts/regulatory/adherence/dht_integration_checklist.prompt.yaml)
- [ICH E9(R1) Estimand Builder](../prompts/regulatory/adherence/estimand_framework_builder.prompt.yaml)
- [Human Factors/Usability Summary](../prompts/regulatory/adherence/human_factors_usability_summary.prompt.yaml)
- [Imaging Endpoint Process Standards Checklist](../prompts/regulatory/adherence/imaging_endpoint_process_standards.prompt.yaml)
- [Informed Consent Exception (Emergency)](../prompts/regulatory/adherence/informed_consent_exception_emergency.prompt.yaml)
- [Intended Use and Indications for Use Alignment](../prompts/regulatory/adherence/intended_use_and_indications_for_use_alignment.prompt.yaml)
- [Multiple Endpoints Regulatory Strategy](../prompts/regulatory/adherence/multiple_endpoints_guidance_review.prompt.yaml)
- [Off-Label Information Dissemination](../prompts/regulatory/adherence/off_label_information_dissemination.prompt.yaml)
- [RWE Regulatory Framework Summary](../prompts/regulatory/adherence/rwe_framework_summary.prompt.yaml)
- [Shelf-life Study Rationale](../prompts/regulatory/adherence/shelf_life_study_rationale.prompt.yaml)
- [21 CFR Part 14 Auditing](../prompts/regulatory/administrative/21_cfr_part_14_auditing.prompt.yaml)
- [Citizen Petition Preparation](../prompts/regulatory/administrative/citizen_petition_preparation.prompt.yaml)
- [Civil Money Penalties Hearing Response](../prompts/regulatory/administrative/civil_money_penalties_hearing_response.prompt.yaml)
- [Financial Disclosure Certification](../prompts/regulatory/administrative/financial_disclosure_certification.prompt.yaml)
- [Freedom of Information Act (FOIA) Request](../prompts/regulatory/administrative/freedom_of_information_act_foia_request.prompt.yaml)
- [Import Entry Data Element Compilation](../prompts/regulatory/administrative/import_entry_data_element_compilation.prompt.yaml)
- [Medical Device Administrative Detention Appeal](../prompts/regulatory/administrative/medical_device_administrative_detention_appeal.prompt.yaml)
- [Patent Term Restoration Eligibility](../prompts/regulatory/administrative/patent_term_restoration_eligibility.prompt.yaml)
- [Privacy Act Auditing](../prompts/regulatory/administrative/privacy_act_auditing.prompt.yaml)
- [Public Hearing Participation](../prompts/regulatory/administrative/public_hearing_participation.prompt.yaml)
- [Reclassification Petitioning](../prompts/regulatory/administrative/reclassification_petitioning.prompt.yaml)
- [Correction and Removal Reporting](../prompts/regulatory/compliance/correction_and_removal_reporting.prompt.yaml)
- [Cyber Device Security Plan](../prompts/regulatory/compliance/cyber_device_security_plan.prompt.yaml)
- [IRB Protocol Review](../prompts/regulatory/compliance/irb_protocol_review.prompt.yaml)
- [Labeling Compliance Audit](../prompts/regulatory/compliance/labeling_compliance_audit.prompt.yaml)
- [Medical Device Recall Strategy](../prompts/regulatory/compliance/medical_device_recall_strategy.prompt.yaml)
- [Medical Device Reporting (MDR)](../prompts/regulatory/compliance/medical_device_reporting_mdr.prompt.yaml)
- [Automated Image Assessment System 510(k)](../prompts/regulatory/device_specifics/automated_image_assessment_system_510_k.prompt.yaml)
- [Carrier Screening System 510(k)](../prompts/regulatory/device_specifics/carrier_screening_system_510_k.prompt.yaml)
- [Clinical Chemistry Device Classification](../prompts/regulatory/device_specifics/clinical_chemistry_device_classification.prompt.yaml)
- [Design Verification for BCR-ABL Tests](../prompts/regulatory/device_specifics/design_verification_for_bcr_abl_tests.prompt.yaml)
- [iCGM Clinical Testing Strategy](../prompts/regulatory/device_specifics/icgm_clinical_testing_strategy.prompt.yaml)
- [NGS Tumor Profiling Documentation](../prompts/regulatory/device_specifics/ngs_tumor_profiling_documentation.prompt.yaml)
- [Special Controls Labeling Compliance](../prompts/regulatory/device_specifics/special_controls_labeling_compliance.prompt.yaml)
- [Zika Virus Reagent Study Design](../prompts/regulatory/device_specifics/zika_virus_reagent_study_design.prompt.yaml)
- [Directed Food Laboratory Order Verification](../prompts/regulatory/food_safety/directed_food_laboratory_order_verification.prompt.yaml)
- [Establishment of Food Traceability Plan](../prompts/regulatory/food_safety/establishment_of_food_traceability_plan.prompt.yaml)
- [Food Safety Audit Reporting (Regulatory)](../prompts/regulatory/food_safety/food_safety_audit_reporting_regulatory.prompt.yaml)
- [Foreign Supplier Verification Program (FSVP) Audit](../prompts/regulatory/food_safety/foreign_supplier_verification_program_fsvp_audit.prompt.yaml)
- [CAPA Investigation Report Writer](../prompts/regulatory/quality/capa_investigation_report_writer.prompt.yaml)
- [CAPA Management Process](../prompts/regulatory/quality/capa_management_process.prompt.yaml)
- [CAPA Plan Generator](../prompts/regulatory/quality/capa_plan_generator.prompt.yaml)
- [CAPA Root Cause Investigator](../prompts/regulatory/quality/capa_root_cause_investigator.prompt.yaml)
- [CAPA SOP Architect](../prompts/regulatory/quality/capa_sop_architect.prompt.yaml)
- [Compliance Gap & Risk Matrix](../prompts/regulatory/quality/compliance_gap_risk_matrix.prompt.yaml)
- [eTMF Compliance Gap Analysis](../prompts/regulatory/quality/etmf_compliance_gap_analysis.prompt.yaml)
- [Financial Conflict of Interest (FCOI) Reporting](../prompts/regulatory/quality/fcoi_reporting.prompt.yaml)
- [GLP Quality Assurance](../prompts/regulatory/quality/glp_quality_assurance.prompt.yaml)
- [Inspection-Readiness Drill (CAPA Builder)](../prompts/regulatory/quality/inspection_readiness_drill_capa_builder.prompt.yaml)
- [Integrated Submission Strategy Coach](../prompts/regulatory/quality/integrated_submission_strategy_coach.prompt.yaml)
- [Part 11 Closed System Audit](../prompts/regulatory/quality/part_11_closed_system_audit.prompt.yaml)
- [Quality-Improvement RCA & Action Plan](../prompts/regulatory/quality/quality_improvement_rca_action_plan.prompt.yaml)
- [Quality System Audit](../prompts/regulatory/quality/quality_system_audit.prompt.yaml)
- [Quality System Evaluation (MRA)](../prompts/regulatory/quality/quality_system_evaluation_mra.prompt.yaml)
- [Regulatory-Landscape Radar](../prompts/regulatory/quality/regulatory_landscape_radar.prompt.yaml)
- [Regulatory Radar & Impact Report](../prompts/regulatory/quality/regulatory_radar.prompt.yaml)
- [Risk-Based Quality Management Plan](../prompts/regulatory/quality/risk_based_quality_management_plan.prompt.yaml)
- [Risk Management Analysis](../prompts/regulatory/quality/risk_management_analysis.prompt.yaml)
- [510(k)/De Novo Pre-Submission Strategy](../prompts/regulatory/strategy/510k_pre-sub_strategy.prompt.yaml)
- [AI Risk Mapper](../prompts/regulatory/strategy/ai_risk_mapper.prompt.yaml)
- [ClinicalTrials.gov Registration](../prompts/regulatory/strategy/clinicaltrials_registration.prompt.yaml)
- [Compliance Gap Assessment](../prompts/regulatory/strategy/compliance_gap_assessment.prompt.yaml)
- [Dual MDR / IVDR Conformity-Assessment Roadmap](../prompts/regulatory/strategy/dual_mdr_ivdr_roadmap.prompt.yaml)
- [EU MDR Technical-Documentation Gap Assessment](../prompts/regulatory/strategy/eu_mdr_gap_assessment.prompt.yaml)
- [IDE Determination and Device Classification](../prompts/regulatory/strategy/ide_determination.prompt.yaml)
- [IND Determination and Application](../prompts/regulatory/strategy/ind_determination_application.prompt.yaml)
- [IND Readiness Gap Analysis & Filing Road-Map](../prompts/regulatory/strategy/ind_readiness_gap_analysis.prompt.yaml)
- [IVD Performance Study Compliance Review](../prompts/regulatory/strategy/ivd_performance_study_compliance_review.prompt.yaml)
- [IVDR Performance-Evaluation Plan Blueprint](../prompts/regulatory/strategy/ivdr_pep_blueprint.prompt.yaml)
- [Literature & Regulatory Gap Analysis](../prompts/regulatory/strategy/literature_regulatory_gap_analysis.prompt.yaml)
- [Pre-IND Meeting Preparation](../prompts/regulatory/strategy/pre_ind_meeting_preparation.prompt.yaml)
- [Prompt-Writing Best-Practice Checklist](../prompts/regulatory/strategy/prompt_best_practices.prompt.yaml)
- [21 CFR 820 / QMSR Gap-Analysis & Remediation](../prompts/regulatory/strategy/qmsr_gap_analysis.prompt.yaml)
- [RA/QA Integrated Quality System Audit](../prompts/regulatory/strategy/raqa_integrated_quality_system_audit.prompt.yaml)
- [Regulatory-Change Impact Analysis](../prompts/regulatory/strategy/regulatory_change_impact_analysis.prompt.yaml)
- [Regulatory Filing Draft Builder](../prompts/regulatory/strategy/regulatory_filing_draft_builder.prompt.yaml)
- [Request for Designation (RFD) Submission](../prompts/regulatory/strategy/rfd_submission.prompt.yaml)
- [Strategic Regulatory Pathway Plan](../prompts/regulatory/strategy/strategic_regulatory_pathway_plan.prompt.yaml)
- [510(k) Substantial Equivalence Preparation](../prompts/regulatory/submissions/510_k_substantial_equivalence_preparation.prompt.yaml)
- [Combination Product Jurisdiction](../prompts/regulatory/submissions/combination_product_jurisdiction.prompt.yaml)
- [De Novo Request Preparation](../prompts/regulatory/submissions/de_novo_request_preparation.prompt.yaml)
- [Humanitarian Device Exemption (HDE)](../prompts/regulatory/submissions/humanitarian_device_exemption_hde.prompt.yaml)
- [IDE Application Preparation](../prompts/regulatory/submissions/ide_application_preparation.prompt.yaml)
- [Medicare Coverage Request (IDE)](../prompts/regulatory/submissions/medicare_coverage_request_ide.prompt.yaml)
- [Parallel Review Request](../prompts/regulatory/submissions/parallel_review_request.prompt.yaml)
- [PMA Post-approval Reporting](../prompts/regulatory/submissions/pma_post_approval_reporting.prompt.yaml)
- [PMA Supplement (CBE)](../prompts/regulatory/submissions/pma_supplement_cbe.prompt.yaml)
- [Premarket Approval (PMA) Preparation](../prompts/regulatory/submissions/premarket_approval_pma_preparation.prompt.yaml)
- [RTA Checklist Preparation](../prompts/regulatory/submissions/rta_checklist_preparation.prompt.yaml)
- [UDI GUDID Submission](../prompts/regulatory/submissions/udi_gudid_submission.prompt.yaml)

## Rtsm

- [Design a Patient-Centered Randomization Scheme](../prompts/clinical/rtsm/rtsm_workflow/01_patient_centered_randomization_scheme.prompt.yaml)
- [Forecast Site-Level Drug Supply & Resupply Strategy](../prompts/clinical/rtsm/rtsm_workflow/02_site_level_supply_resupply_strategy.prompt.yaml)
- [Create a Risk-Based Monitoring & Mitigation SOP for RTSM](../prompts/clinical/rtsm/rtsm_workflow/03_risk_based_monitoring_sop.prompt.yaml)

## Safety

- [Clinical Safety Synopsis for EU MDR CER](../prompts/clinical/safety/clinical_safety_workflow/01_eu_cer_clinical_safety_synopsis.prompt.yaml)
- [FDA MDR/MDV Adverse-Event Narrative](../prompts/clinical/safety/clinical_safety_workflow/02_fda_mdr_adverse_event_narrative.prompt.yaml)
- [Post-Market Safety Signal Trending](../prompts/clinical/safety/clinical_safety_workflow/03_post_market_safety_signal_trending.prompt.yaml)

## Scientific

- [Biological Evaluation Plan Builder](../prompts/scientific/biosafety/bep_builder.prompt.yaml)
- [Chemical Characterization & TRA Work Plan](../prompts/scientific/biosafety/chemical_characterization_work_plan.prompt.yaml)
- [Comprehensive Biocompatibility Test Matrix](../prompts/scientific/biosafety/comprehensive_test_matrix.prompt.yaml)
- [Adaptive Design & Interim Monitoring](../prompts/scientific/biostatistics/adaptive_design_interim_monitoring.prompt.yaml)
- [Dual-Language Figure Prompt](../prompts/scientific/biostatistics/dual_language_figure_prompt.prompt.yaml)
- [Dunnett Adjustment R Code Generator](../prompts/scientific/biostatistics/dunnett_adjustment_calculator.prompt.yaml)
- [FDA Missing-Data Query Response](../prompts/scientific/biostatistics/fda_missing_data_query_response.prompt.yaml)
- [FWER Gatekeeping Procedure Code Generator](../prompts/scientific/biostatistics/fwer_gatekeeping_procedures.prompt.yaml)
- [Inclusion/Exclusion, Endpoints & Sample-Size Deep Dive](../prompts/scientific/biostatistics/inclusion_exclusion_endpoints_sample_size.prompt.yaml)
- [Multiplicity Adjustment Code Generator](../prompts/scientific/biostatistics/multiplicity_adjustments_calculator.prompt.yaml)
- [Peer-Review Checklist for Manuscript Methods](../prompts/scientific/biostatistics/peer_review_methods_checklist.prompt.yaml)
- [Phase II/III SAP Skeleton](../prompts/scientific/biostatistics/phase_ii_iii_sap_skeleton.prompt.yaml)
- [QC Listing & Cross-check Prompt](../prompts/scientific/biostatistics/qc_listing_cross_check_prompt.prompt.yaml)
- [Sample-Size & Randomization Strategy](../prompts/scientific/biostatistics/sample_size_randomization_strategy.prompt.yaml)
- [Statistical Analysis Plan (SAP) Development](../prompts/scientific/biostatistics/sap_development.prompt.yaml)
- [Secondary Endpoint Multiplicity Adjuster](../prompts/scientific/biostatistics/secondary_endpoint_multiplicity.prompt.yaml)
- [Statistical Analysis Plan Generator](../prompts/scientific/biostatistics/statistical_analysis_plan_generator.prompt.yaml)
- [Study Design and Statistical Approach](../prompts/scientific/biostatistics/study_design_statistical_approach.prompt.yaml)
- [Submission-Ready Statistical Analysis Plan](../prompts/scientific/biostatistics/submission_ready_sap.prompt.yaml)
- [Generate & QC Submission-Ready TLFs](../prompts/scientific/biostatistics/submission_ready_tlfs.prompt.yaml)
- [Time-to-Event Analysis Coach](../prompts/scientific/biostatistics/time_to_event_analysis_coach.prompt.yaml)
- [Universal Template-Table Prompt](../prompts/scientific/biostatistics/universal_template_table_prompt.prompt.yaml)
- [ClinRO User Manual Generator](../prompts/scientific/coa/clinro_training_manual.prompt.yaml)
- [Content Validity & Reliability Analysis](../prompts/scientific/coa/content_validity_clinician_input.prompt.yaml)
- [ePRO Migration Equivalence Checker](../prompts/scientific/coa/epro_migration_equivalence.prompt.yaml)
- [MCID Research and Summary](../prompts/scientific/coa/mcid_definition.prompt.yaml)
- [Psychometric Validation Methodology](../prompts/scientific/coa/psychometric_validation_methods.prompt.yaml)
- [Qualitative Interview Guide Generator](../prompts/scientific/coa/qualitative_interview_guide.prompt.yaml)
- [Clinical Study Report (CSR) Writing](../prompts/scientific/medical_writing/csr_writing.prompt.yaml)

## Site Acquisition

- [Site Landscape Mapping & Prioritization](../prompts/clinical/site_acquisition/site_acquisition_workflow/01_site_landscape_mapping.prompt.yaml)
- [Tailored Feasibility-Questionnaire Builder](../prompts/clinical/site_acquisition/site_acquisition_workflow/02_tailored_feasibility_questionnaire.prompt.yaml)
- [Personalized Investigator-Outreach Email Generator](../prompts/clinical/site_acquisition/site_acquisition_workflow/03_investigator_outreach_email_generator.prompt.yaml)

## Software Engineering

- [Coding Session Guidelines](../prompts/technical/software_engineering/lifecycle/coding_session_guidelines.prompt.yaml)
- [E2E Test Discovery Lifecycle Template](../prompts/technical/software_engineering/lifecycle/e2e_test_discovery.prompt.yaml)
- [Folder and Module Organization](../prompts/technical/software_engineering/lifecycle/folder_module_organization.prompt.yaml)
- [Project Memory Notes](../prompts/technical/software_engineering/lifecycle/project_memory.prompt.yaml)
- [Project Review Checklist](../prompts/technical/software_engineering/lifecycle/project_review.prompt.yaml)
- [Reflexion Agent Bug Patch](../prompts/technical/software_engineering/lifecycle/reflexion_agent_bug_patch.prompt.yaml)
- [RequirementsBot Prompt](../prompts/technical/software_engineering/lifecycle/requirements_prompt.prompt.yaml)
- [Technical Implementation Plan](../prompts/technical/software_engineering/lifecycle/technical_implementation_plan.prompt.yaml)
- [To-Do List Template](../prompts/technical/software_engineering/lifecycle/todo_generation.prompt.yaml)
- [Test Architect (Automated Testing)](../prompts/technical/software_engineering/tasks/add_tests.prompt.yaml)
- [Architecture Flow & Diagram Architect](../prompts/technical/software_engineering/tasks/architecture_flow.prompt.yaml)
- [Bug Finder & Fixer (OpenAI Codex)](../prompts/technical/software_engineering/tasks/bug_fix.prompt.yaml)
- [Continuous Integration & Delivery (DevOps Architect)](../prompts/technical/software_engineering/tasks/ci_cd.prompt.yaml)
- [Code Review Assistant (Aegis Security)](../prompts/technical/software_engineering/tasks/code_review.prompt.yaml)
- [Codebase Testing Plan](../prompts/technical/software_engineering/tasks/codebase_testing_plan.prompt.yaml)
- [GitHub Custom Agent Creator](../prompts/technical/software_engineering/tasks/create_github_agent.prompt.yaml)
- [DevEx Documentation Architect](../prompts/technical/software_engineering/tasks/docs_and_onboarding.prompt.yaml)
- [Principal Architect Task Execution](../prompts/technical/software_engineering/tasks/principal_architect.prompt.yaml)
- [Project Init & Skeleton (Construct Architect)](../prompts/technical/software_engineering/tasks/project_init.prompt.yaml)
- [Retrieval-Augmented Answer Composer](../prompts/technical/software_engineering/tasks/rag_composer.prompt.yaml)
- [Refactoring Architect](../prompts/technical/software_engineering/tasks/refactoring_suggestions.prompt.yaml)
- [Security Vulnerability Hunt](../prompts/technical/software_engineering/tasks/security_vulnerability.prompt.yaml)
- [Tooling & Quality Gates (DevEx Architect)](../prompts/technical/software_engineering/tasks/tooling_and_quality.prompt.yaml)
- [UI Tweak & Verification (OpenAI Codex)](../prompts/technical/software_engineering/tasks/ui_fix.prompt.yaml)

## Sterility

- [Sterility-Validation Protocol Builder](../prompts/scientific/sterility/sterility_workflow/01_sterility_validation_protocol_builder.prompt.yaml)
- [Regulatory Gap-Analysis Comparator](../prompts/scientific/sterility/sterility_workflow/02_regulatory_gap_analysis_comparator.prompt.yaml)
- [EtO Sterilization Process FMEA](../prompts/scientific/sterility/sterility_workflow/03_eto_sterilization_process_fmea.prompt.yaml)

## Study Director

- [Draft a GLP-Compliant Study Protocol](../prompts/management/study_director/study_director_workflow/01_draft_glp_compliant_study_protocol.prompt.yaml)
- [Audit Raw Data and Draft a CAPA Summary](../prompts/management/study_director/study_director_workflow/02_audit_raw_data_capa_summary.prompt.yaml)
- [Generate an Executive Summary for the Final Report](../prompts/management/study_director/study_director_workflow/03_executive_summary_final_report.prompt.yaml)

## Tasks

- [PAW Phase 1 - Tactical Recon](../prompts/technical/software_engineering/tasks/paw/paw_01_tactical_recon.prompt.yaml)
- [PAW Phase 2 - Architectural Blueprint](../prompts/technical/software_engineering/tasks/paw/paw_02_architectural_blueprint.prompt.yaml)
- [PAW Phase 3 - Precision Strike](../prompts/technical/software_engineering/tasks/paw/paw_03_precision_strike.prompt.yaml)
- [PAW Phase 4 - Quality Assurance & Log](../prompts/technical/software_engineering/tasks/paw/paw_04_qa_verification.prompt.yaml)

## Technical

- [DRY Codebase Analysis](../prompts/technical/architecture/dry_codebase_analysis.prompt.yaml)
- [Hexagonal Architecture Implementation](../prompts/technical/architecture/hexagonal_architecture_implementation.prompt.yaml)
- [Hexagonal Architecture Principles](../prompts/technical/architecture/hexagonal_architecture_principles.prompt.yaml)
- [Hexagonal Architecture Review](../prompts/technical/architecture/hexagonal_architecture_review.prompt.yaml)
- [Maintainability Codebase Analysis](../prompts/technical/architecture/maintainability_codebase_analysis.prompt.yaml)
- [SOLID Codebase Analysis](../prompts/technical/architecture/solid_codebase_analysis.prompt.yaml)
- [Conversation Stochastic Modeler](../prompts/technical/data_science/conversation_stochastic_modeler.prompt.yaml)
- [Design.md Template](../prompts/technical/design/design_md_template.prompt.yaml)
- [AI Email Assistant Go/No-Go Vote](../prompts/technical/design/email_assistant_go_no_go_vote.prompt.yaml)
- [Heuristic-Evaluation Coach](../prompts/technical/design/heuristic_evaluation_coach.prompt.yaml)
- [Forge - Script Reliability Agent](../prompts/technical/devops/forge_script_reliability.prompt.yaml)
- [Atlas Documentation Specialist](../prompts/technical/documentation/atlas_documentation_specialist.prompt.yaml)
- [Source of Truth Harmonizer](../prompts/technical/documentation/source_of_truth_harmonizer.prompt.yaml)
- [Code Formatting, Linting, and Refactoring Implementation](../prompts/technical/repository_refactoring/code_formatting_linting_refactoring_implementation.prompt.yaml)
- [Codebase Quality & Maintainability Analysis](../prompts/technical/repository_refactoring/codebase_quality_analysis.prompt.yaml)
- [Dependencies & Security Posture Analysis](../prompts/technical/repository_refactoring/dependencies_security_analysis.prompt.yaml)
- [Documentation and Repository Structure Implementation](../prompts/technical/repository_refactoring/documentation_structure_implementation.prompt.yaml)
- [Repository Foundation & Developer Experience Analysis](../prompts/technical/repository_refactoring/repo_foundation_analysis.prompt.yaml)
- [Security Hardening and Dependency Management Implementation](../prompts/technical/repository_refactoring/security_hardening_dependency_management_implementation.prompt.yaml)
- [Test Suite Enhancement and CI Pipeline Implementation](../prompts/technical/repository_refactoring/test_suite_enhancement_ci_pipeline_implementation.prompt.yaml)
- [Testing, Configuration, and Automation Analysis](../prompts/technical/repository_refactoring/testing_configuration_automation_analysis.prompt.yaml)
- [Medical Device Cybersecurity Threat Modeling](../prompts/technical/security/cybersecurity_threat_modeling.prompt.yaml)
- [Technical White Paper for Clinical Methodologies](../prompts/technical/technical_writing/technical_white_paper_in_silico.prompt.yaml)

## Technical Writing

- [CSR Results and Safety Section](../prompts/technical/technical_writing/technical_writer_workflow/01_csr_results_safety_section.prompt.yaml)
- [Investigator's Brochure Summary of Changes](../prompts/technical/technical_writing/technical_writer_workflow/02_ib_detailed_soc.prompt.yaml)
- [SAE and Unanticipated Problem Reporting SOP](../prompts/technical/technical_writing/technical_writer_workflow/03_sae_reporting_sop.prompt.yaml)

## Testing

- [Framework Implementation: Data-Driven Testing](../prompts/technical/testing/selenium_automation/data_driven_selenium.prompt.yaml)
- [Advanced Design Patterns: Fluent Interface](../prompts/technical/testing/selenium_automation/fluent_interface_selenium.prompt.yaml)
- [Framework Best Practices: Locator Strategy](../prompts/technical/testing/selenium_automation/locator_optimization.prompt.yaml)
- [Project Configuration: Maven Setup](../prompts/technical/testing/selenium_automation/maven_selenium_setup.prompt.yaml)
- [Execution Optimization: Parallel Testing](../prompts/technical/testing/selenium_automation/parallel_execution.prompt.yaml)
- [Architecture Design: Page Object Model](../prompts/technical/testing/selenium_automation/pom_implementation.prompt.yaml)
- [Selenium Migration: Script Conversion](../prompts/technical/testing/selenium_automation/script_conversion.prompt.yaml)
- [Cross-Browser Infrastructure: Selenium Grid](../prompts/technical/testing/selenium_automation/selenium_grid_setup.prompt.yaml)
- [Test Environment: Python & Selenium Base](../prompts/technical/testing/selenium_automation/selenium_python_setup.prompt.yaml)
- [Reporting and Maintenance: Custom Reports](../prompts/technical/testing/selenium_automation/selenium_reporting.prompt.yaml)
- [Synchronization Strategy: Explicit Waits](../prompts/technical/testing/selenium_automation/selenium_waits.prompt.yaml)
- [Security Testing: OWASP ZAP Integration](../prompts/technical/testing/selenium_automation/selenium_zap_integration.prompt.yaml)
- [Driver Configuration: WebDriver Initialization](../prompts/technical/testing/selenium_automation/webdriver_initialization.prompt.yaml)
- [E2E Test Discovery Template](../prompts/technical/testing/testing_workflow/01_e2e_test_discovery.prompt.yaml)
- [Design Verification Test Plan](../prompts/technical/testing/testing_workflow/02_design_verification_test_plan.prompt.yaml)
- [Human Factors Validation Study Protocol](../prompts/technical/testing/testing_workflow/03_human_factors_validation_study_protocol.prompt.yaml)
- [Risk-Based Test Case Suite](../prompts/technical/testing/testing_workflow/04_risk_based_test_case_suite.prompt.yaml)

## Therapy

- [Compassionate Analyst](../prompts/clinical/therapy/music_therapy_workflow/01_compassionate_analyst.prompt.yaml)
- [ISO Strategist](../prompts/clinical/therapy/music_therapy_workflow/02_iso_strategist.prompt.yaml)
- [Sonic Architect](../prompts/clinical/therapy/music_therapy_workflow/03_sonic_architect.prompt.yaml)
- [Lyricist](../prompts/clinical/therapy/music_therapy_workflow/04_lyricist.prompt.yaml)

## Training

- [Competency-Based Onboarding Blueprint](../prompts/management/training/learning_development_workflow/01_competency_based_onboarding_blueprint.prompt.yaml)
- [Scenario-Based Microlearning Series](../prompts/management/training/learning_development_workflow/02_scenario_based_microlearning_series.prompt.yaml)
- [Training Impact Analytics Planner](../prompts/management/training/learning_development_workflow/03_training_impact_analytics_targeted_intervention_planner.prompt.yaml)

## Vp Statistics

- [Interim Results Executive Brief](../prompts/management/vp_statistics/vp_statistics_workflow/01_interim_results_executive_brief.prompt.yaml)
- [Statistical Analysis Plan Draft Builder](../prompts/management/vp_statistics/vp_statistics_workflow/02_sap_first_draft_builder.prompt.yaml)
- [Data-Quality Risk Heat Map](../prompts/management/vp_statistics/vp_statistics_workflow/03_data_quality_risk_heatmap.prompt.yaml)
