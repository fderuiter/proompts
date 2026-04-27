---
title: Home
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
- [Workflows Usage Guide](workflows_usage.md)


# All Prompts

## Adjudication

- [Real-Time Adjudication Visibility Dashboard](prompts/clinical/adjudication/adjudication_workflow/01_real_time_adjudication_dashboard.prompt.md)
- [Source Document and Endpoint Checklist](prompts/clinical/adjudication/adjudication_workflow/02_source_document_endpoint_checklist.prompt.md)
- [Analyze Adjudication KPIs](prompts/clinical/adjudication/adjudication_workflow/03_analyze_adjudication_kpis.prompt.md)

## Algebra

- [galois_group_resolvent_architect](prompts/scientific/mathematics/algebra/galois_theory/galois_group_resolvent_architect.prompt.md)

## Analysis

- [Riemann Surface Analytic Continuation Architect](prompts/scientific/mathematics/analysis/complex_analysis/riemann_surface_analytic_continuation_architect.prompt.md)
- [banach_space_operator_architect](prompts/scientific/mathematics/analysis/functional_analysis/banach_space_operator_architect.prompt.md)

## Analytical

- [Tandem MS/MS Fragmentation Pathway Elucidator](prompts/scientific/chemistry/analytical/mass_spectrometry/tandem_ms_fragmentation_pathway_elucidator.prompt.md)
- [Predictive Multidimensional Spectroscopy Architect](prompts/scientific/chemistry/analytical/spectroscopy/predictive_multidimensional_spectroscopy_architect.prompt.md)

## Architecture

- [TOGAF Phase A - Architecture Vision](prompts/technical/architecture/togaf/phase_a_vision.prompt.md)
- [TOGAF Phase B - Business Architecture](prompts/technical/architecture/togaf/phase_b_business.prompt.md)
- [TOGAF Phase C - Information Systems Architectures](prompts/technical/architecture/togaf/phase_c_information_systems.prompt.md)
- [TOGAF Phase D - Technology Architecture](prompts/technical/architecture/togaf/phase_d_technology.prompt.md)
- [TOGAF Phase E - Opportunities & Solutions](prompts/technical/architecture/togaf/phase_e_opportunities.prompt.md)
- [TOGAF Phase F - Migration Planning](prompts/technical/architecture/togaf/phase_f_migration.prompt.md)
- [TOGAF Phase G - Implementation Governance](prompts/technical/architecture/togaf/phase_g_governance.prompt.md)
- [TOGAF Phase H - Architecture Change Management](prompts/technical/architecture/togaf/phase_h_change_management.prompt.md)
- [TOGAF Preliminary Phase](prompts/technical/architecture/togaf/preliminary_phase.prompt.md)
- [TOGAF Requirements Management](prompts/technical/architecture/togaf/requirements_management.prompt.md)

## Behavioral Economics

- [population_macro_nudging_architect](prompts/scientific/psychology/behavioral_economics/macro_nudging/population_macro_nudging_architect.prompt.md)

## Biosafety

- [Risk Assessment Expert](prompts/scientific/biosafety/biological_safety_workflow/01_risk_assessment_expert.prompt.md)
- [Biological Safety Plan Developer](prompts/scientific/biosafety/biological_safety_workflow/02_biological_safety_plan_developer.prompt.md)
- [Regulatory Submission Support](prompts/scientific/biosafety/biological_safety_workflow/03_regulatory_submission_support.prompt.md)

## Bioskills

- [Hands-On Procedure Coaching](prompts/scientific/bioskills/bioskills_workflow/01_hands_on_procedure_coaching.prompt.md)
- [Simulated Clinical Scenario Debrief](prompts/scientific/bioskills/bioskills_workflow/02_simulated_clinical_scenario_feedback.prompt.md)
- [Objective Skills Assessment](prompts/scientific/bioskills/bioskills_workflow/03_objective_skills_assessment.prompt.md)

## Business

- [Board Deck Narrative Generation](prompts/business/cfo/board_deck_narrative.prompt.md)
- [Earnings Call Script Prep](prompts/business/cfo/earnings_call_script_prep.prompt.md)
- [Investor FAQ Generation](prompts/business/cfo/investor_faq_generation.prompt.md)
- [Liquidity Stress Test](prompts/business/cfo/liquidity_stress_test.prompt.md)
- [M&A Target Evaluation](prompts/business/cfo/ma_target_evaluation.prompt.md)
- [Net Present Value Socratic Tutor](prompts/business/cfo/npv_tutor.prompt.md)
- [Quantitative FX Hedging Strategy Architect](prompts/business/cfo/quantitative_fx_hedging_strategy_architect.prompt.md)
- [Regulatory Compliance Summary](prompts/business/cfo/regulatory_compliance_summary.prompt.md)
- [Scenario Modeling & Sensitivity Analysis](prompts/business/cfo/scenario_modeling_sensitivity.prompt.md)
- [Budget Variance Analysis](prompts/business/cfo/variance_analysis.prompt.md)
- [CSM Portfolio Balancing](prompts/business/cx/csm_portfolio_balancing.prompt.md)
- [Friction-Hunting Onboarding Audit](prompts/business/cx/onboarding_audit.prompt.md)
- [Red Account Turnaround Strategy](prompts/business/cx/red_account_turnaround.prompt.md)
- [Cross-Functional Advocacy Memo](prompts/business/cx/revenue_risk_advocacy.prompt.md)
- [Voice of Customer Root Cause Analysis](prompts/business/cx/root_cause_analysis.prompt.md)
- [Trend Spotting vs Anomalies](prompts/business/cx/trend_spotting.prompt.md)
- [Value-Based QBR Generator](prompts/business/cx/value_based_qbr.prompt.md)
- [90-Day Pipeline Health & Next-Best-Action Review](prompts/business/development/90_day_pipeline_health_review.prompt.md)
- [Competitor-Positioning Brief](prompts/business/development/competitor_positioning_brief.prompt.md)
- [Emerging-Market Opportunity Scan](prompts/business/development/emerging_market_opportunity_scan.prompt.md)
- [Market-Intelligence Radar](prompts/business/development/market_intelligence_radar.prompt.md)
- [Marketing Campaign for Clinical Services](prompts/business/development/marketing_campaign_in_silico.prompt.md)
- [Rapid Proposal Builder](prompts/business/development/rapid_proposal_builder.prompt.md)
- [RFP Executive-Summary Generator](prompts/business/development/rfp_executive_summary_generator.prompt.md)
- [Strategic Business Case for New Service Line](prompts/business/development/strategic_business_case_in_silico.prompt.md)
- [Corporate Capital Budgeting Investment Appraisal Architect](prompts/business/finance/corporate_capital_budgeting_investment_appraisal_architect.prompt.md)
- [Corporate Financial Distress Predictive Altman Z-Score Architect](prompts/business/finance/corporate_financial_distress_predictive_altman_z_score_architect.prompt.md)
- [Corporate Merger Arbitrage Deal Risk Architect](prompts/business/finance/corporate_merger_arbitrage_risk_architect.prompt.md)
- [Quantitative Enterprise Working Capital CCC Architect](prompts/business/finance/quantitative_enterprise_working_capital_ccc_architect.prompt.md)
- [Quantitative M&A Accretion Dilution Architect](prompts/business/finance/quantitative_ma_accretion_dilution_architect.prompt.md)
- [Quantitative Private Equity Dividend Recapitalization Architect](prompts/business/finance/quantitative_private_equity_dividend_recapitalization_architect.prompt.md)
- [Algorithmic Multi-Touch Attribution Architect](prompts/business/growth_engineering/algorithmic_multi_touch_attribution_architect.prompt.md)
- [Cross-Channel Behavioral Trigger Architect](prompts/business/growth_engineering/cross_channel_behavioral_trigger_architect.prompt.md)
- [GTM Pricing Elasticity Architect](prompts/business/growth_engineering/gtm_pricing_elasticity_architect.prompt.md)
- [Predictive RFM Churn Mitigation Architect](prompts/business/growth_engineering/predictive_rfm_churn_mitigation_architect.prompt.md)
- [Clinical-Trial Budget and Burn-Rate Dashboard](prompts/business/hr_finance/clinical_trial_budget_burn_rate_dashboard.prompt.md)
- [GCP and GDPR Training Compliance Risk Report](prompts/business/hr_finance/gcp_gdpr_compliance_training_risk_report.prompt.md)
- [Strategic Workforce and Talent Acquisition Plan](prompts/business/hr_finance/strategic_workforce_talent_acquisition_plan.prompt.md)
- [Cross-Border Data Privacy Architect](prompts/business/legal/cross_border_data_privacy_architect.prompt.md)
- [Intellectual Property Claim Drafter](prompts/business/legal/intellectual_property_claim_drafter.prompt.md)
- [Mergers and Acquisitions Due Diligence Auditor](prompts/business/legal/mergers_acquisitions_due_diligence_auditor.prompt.md)
- [Theory of Constraints Throughput Architect](prompts/business/operations/theory_of_constraints_throughput_architect.prompt.md)
- [Build an Audit-Ready Site-Payment Schedule](prompts/business/payment/audit_ready_site_payment_schedule.prompt.md)
- [Medicare Coverage Analysis](prompts/business/payment/coverage_analysis.prompt.md)
- [Global Regulatory and Tax Matrix for Site Payments](prompts/business/payment/global_regulatory_tax_matrix.prompt.md)
- [Investigator-Site Payment Forecast](prompts/business/payment/investigator_site_payment_forecast.prompt.md)
- [Payment-Process Risk Assessment and Mitigation](prompts/business/payment/payment_process_risk_assessment.prompt.md)
- [Payment Reconciliation and Discrepancy Report](prompts/business/payment/payment_reconciliation_discrepancy_report.prompt.md)
- [Sunshine Act and FMV Compliance Check](prompts/business/payment/sunshine_act_fmv_compliance_check.prompt.md)
- [Activist Investor Defense Strategy Architect](prompts/business/strategy/activist_investor_defense_strategy_architect.prompt.md)
- [Algorithmic Dynamic Pricing & Yield Management Architect](prompts/business/strategy/algorithmic_dynamic_pricing_yield_management_architect.prompt.md)
- [blue_ocean_value_innovation_architect](prompts/business/strategy/blue_ocean_value_innovation_architect.prompt.md)
- [corporate_b2b_saas_pricing_tier_architect](prompts/business/strategy/corporate_b2b_saas_pricing_tier_architect.prompt.md)
- [Corporate Capital Structure Optimization Architect](prompts/business/strategy/corporate_capital_structure_optimization_architect.prompt.md)
- [Corporate Digital Transformation ROI Architect](prompts/business/strategy/corporate_digital_transformation_roi_architect.prompt.md)
- [Corporate Diversification Synergy Architect](prompts/business/strategy/corporate_diversification_synergy_architect.prompt.md)
- [Corporate ESG Carbon Abatement Strategy Architect](prompts/business/strategy/corporate_esg_carbon_abatement_strategy_architect.prompt.md)
- [corporate_fx_hedging_currency_risk_architect](prompts/business/strategy/corporate_fx_hedging_currency_risk_architect.prompt.md)
- [Corporate Geopolitical Risk Mitigation Architect](prompts/business/strategy/corporate_geopolitical_risk_mitigation_architect.prompt.md)
- [corporate_ip_portfolio_monetization_architect](prompts/business/strategy/corporate_ip_portfolio_monetization_architect.prompt.md)
- [Corporate Spin-Off Carve-Out Architect](prompts/business/strategy/corporate_spin_off_carve_out_architect.prompt.md)
- [Corporate Transfer Pricing Optimization Architect](prompts/business/strategy/corporate_transfer_pricing_optimization_architect.prompt.md)
- [Corporate Turnaround Restructuring Architect](prompts/business/strategy/corporate_turnaround_restructuring_architect.prompt.md)
- [Corporate Venture Capital Strategy Architect](prompts/business/strategy/corporate_venture_capital_strategy_architect.prompt.md)
- [Corporate Vertical Integration Structuring Architect](prompts/business/strategy/corporate_vertical_integration_structuring_architect.prompt.md)
- [corporate_wargaming_scenario_planning_architect](prompts/business/strategy/corporate_wargaming_scenario_planning_architect.prompt.md)
- [Cross-Border Joint Venture Structuring Architect](prompts/business/strategy/cross_border_joint_venture_structuring_architect.prompt.md)
- [Distressed Debt Restructuring Chapter 11 Architect](prompts/business/strategy/distressed_debt_restructuring_chapter11_architect.prompt.md)
- [game_theoretic_competitive_dynamics_architect](prompts/business/strategy/game_theoretic_competitive_dynamics_architect.prompt.md)
- [Global Market Entry Expansion Architect](prompts/business/strategy/global_market_entry_expansion_architect.prompt.md)
- [Hostile Takeover Defense Matrix Architect](prompts/business/strategy/hostile_takeover_defense_matrix.prompt.md)
- [Leveraged Buyout Financial Structuring Architect](prompts/business/strategy/leveraged_buyout_financial_structuring_architect.prompt.md)
- [Platform Ecosystem Network Effects Architect](prompts/business/strategy/platform_ecosystem_network_effects_architect.prompt.md)
- [Post-Merger Integration Synergy Architect](prompts/business/strategy/post_merger_integration_synergy_architect.prompt.md)
- [Private Equity Value Creation Architect](prompts/business/strategy/private_equity_value_creation_architect.prompt.md)
- [Quantitative Corporate Portfolio Divestiture Architect](prompts/business/strategy/quantitative_corporate_portfolio_divestiture_architect.prompt.md)
- [Real Options Valuation Architect](prompts/business/strategy/real_options_valuation_architect.prompt.md)
- [stochastic_market_entry_greenfield_architect](prompts/business/strategy/stochastic_market_entry_greenfield_architect.prompt.md)
- [Strategic Capital Allocation Architect](prompts/business/strategy/strategic_capital_allocation_architect.prompt.md)
- [Strategic Product Cannibalization Architect](prompts/business/strategy/strategic_product_cannibalization_architect.prompt.md)
- [Strategic Real Options Valuation Architect](prompts/business/strategy/strategic_real_options_valuation_architect.prompt.md)
- [Supply Chain Antifragility Architect](prompts/business/strategy/supply_chain_antifragility_architect.prompt.md)
- [zero_based_budgeting_turnaround_architect](prompts/business/strategy/zero_based_budgeting_turnaround_architect.prompt.md)
- [Build vs. Buy Decision Matrix](prompts/business/vp_tech_innovation/build_vs_buy_matrix.prompt.md)
- [Disruption Radar](prompts/business/vp_tech_innovation/disruption_radar.prompt.md)
- [Elevator Pitch for Expensive Tech](prompts/business/vp_tech_innovation/elevator_pitch_expensive_tech.prompt.md)
- [Hype vs. Reality Analysis](prompts/business/vp_tech_innovation/hype_vs_reality_analysis.prompt.md)
- [Legacy Modernization Strategy](prompts/business/vp_tech_innovation/legacy_modernization_strategy.prompt.md)
- [Post-Mortem / Incident Report Summary](prompts/business/vp_tech_innovation/post_mortem_summary.prompt.md)
- [Preventing Technical Debt](prompts/business/vp_tech_innovation/preventing_technical_debt.prompt.md)
- [Strategic Vendor Lock-In Mitigation Architect](prompts/business/vp_tech_innovation/strategic_vendor_lock_in_mitigation_architect.prompt.md)
- [Upskilling Program Design](prompts/business/vp_tech_innovation/upskilling_program_design.prompt.md)

## Cellular

- [genome_scale_metabolic_flux_modeler](prompts/scientific/cellular/metabolism/genome_scale_metabolic_flux_modeler.prompt.md)
- [metabolic_control_analysis_architect](prompts/scientific/cellular/metabolism/metabolic_control_analysis_architect.prompt.md)
- [astrocytic_tripartite_synapse_calcium_dynamics_architect](prompts/scientific/cellular/neurophysiology/astrocytic_tripartite_synapse_calcium_dynamics_architect.prompt.md)

## Cfo

- [Scenario-Based Clinical-Trial Cash-Flow Forecast](prompts/business/cfo/cfo_workflow/01_scenario_cash_flow_forecast.prompt.md)
- [Competitive-Bid Pricing & Margin Optimizer](prompts/business/cfo/cfo_workflow/02_competitive_bid_pricing.prompt.md)
- [Regulatory-Risk & ESG Impact Dashboard Builder](prompts/business/cfo/cfo_workflow/03_regulatory_risk_dashboard.prompt.md)

## Chemical Characterization

- [Design the Study](prompts/scientific/chemical_characterization/chemical_characterization_workflow/01_design_the_study.prompt.md)
- [Interpret the Chemistry & Assess Risk](prompts/scientific/chemical_characterization/chemical_characterization_workflow/02_interpret_the_chemistry_assess_risk.prompt.md)
- [Write the Regulatory Summary](prompts/scientific/chemical_characterization/chemical_characterization_workflow/03_write_the_regulatory_summary.prompt.md)

## Chemistry

- [multidimensional_nmr_hrms_structure_elucidator](prompts/scientific/chemistry/analytical/multidimensional_nmr_hrms_structure_elucidator.prompt.md)
- [Quantum Chemical Transition State Architect](prompts/scientific/chemistry/computational/quantum_chemical_transition_state_architect.prompt.md)

## Clinical

- [risk_based_monitoring_strategist](prompts/clinical/clinical_operations/risk_based_monitoring_strategist.prompt.md)
- [Audit Trail Review](prompts/clinical/data_management/audit_trail_review.prompt.md)
- [CDISC CRF Architect](prompts/clinical/data_management/cdisc_crf_architect.prompt.md)
- [CDISC SDTM/ADaM Mapping](prompts/clinical/data_management/cdisc_mapping.prompt.md)
- [Data Architecture Blueprint](prompts/clinical/data_management/data_architecture_blueprint.prompt.md)
- [Data De-identification](prompts/clinical/data_management/data_deidentification.prompt.md)
- [Database Lock Procedures](prompts/clinical/data_management/database_lock_procedures.prompt.md)
- [Decentralized Trial Risk Matrix](prompts/clinical/data_management/decentralized_trial_risk_matrix.prompt.md)
- [Data Management Plan (DMP) Development](prompts/clinical/data_management/dmp_development.prompt.md)
- [Clinical Trial Document Archiving](prompts/clinical/data_management/document_archiving.prompt.md)
- [eTMF Artifact Classifier](prompts/clinical/data_management/etmf_artifact_classifier.prompt.md)
- [Medical Coding and Reconciliation Assistant](prompts/clinical/data_management/medical_coding_reconciliation.prompt.md)
- [Metadata Management](prompts/clinical/data_management/metadata_management.prompt.md)
- [21 CFR Part 11 Compliance Verification](prompts/clinical/data_management/part_11_compliance_verification.prompt.md)
- [Phase II Oncology DMP](prompts/clinical/data_management/phase_ii_oncology_dmp.prompt.md)
- [Regulatory Compliance Verification](prompts/clinical/data_management/regulatory_compliance_verification.prompt.md)
- [Regulatory Gap Analysis](prompts/clinical/data_management/regulatory_gap_analysis.prompt.md)
- [SOP Gap Analysis](prompts/clinical/data_management/sop_gap_analysis.prompt.md)
- [Trial Master File (TMF) Maintenance](prompts/clinical/data_management/tmf_maintenance.prompt.md)
- [Unified Data Cleansing](prompts/clinical/data_management/unified_data_cleansing.prompt.md)
- [Computer System Validation (CSV)](prompts/clinical/eclinical_integration/computer_system_validation.prompt.md)
- [Digital Health Technology (DHT) Validation](prompts/clinical/eclinical_integration/dht_validation.prompt.md)
- [eConsent Implementation Strategy](prompts/clinical/eclinical_integration/econsent_implementation.prompt.md)
- [IQ/OQ/PQ Validation](prompts/clinical/eclinical_integration/iq_oq_pq_validation.prompt.md)
- [UAT Script Generator](prompts/clinical/eclinical_integration/uat_script_generator.prompt.md)
- [CDASH Alignment](prompts/clinical/forms/cdash_alignment.prompt.md)
- [Design Error Prevention](prompts/clinical/forms/crf_design_optimization.prompt.md)
- [Electronic Data Capture Implementation](prompts/clinical/forms/ecrf_implementation.prompt.md)
- [Semantic Interoperability Optimization](prompts/clinical/forms/semantic_interoperability.prompt.md)
- [clinical_study_report_patient_narrative_architect](prompts/clinical/medical_writing/clinical_study_report_patient_narrative_architect.prompt.md)
- [Clinical Trial Protocol Synopsis Architect](prompts/clinical/medical_writing/clinical_trial_protocol_synopsis_architect.prompt.md)
- [csr_efficacy_narrative_architect](prompts/clinical/medical_writing/csr_efficacy_narrative_architect.prompt.md)
- [Clinical Study Report (CSR) Narrative Drafter](prompts/clinical/medical_writing/csr_narrative_drafter.prompt.md)
- [csr_patient_narrative_architect](prompts/clinical/medical_writing/csr_patient_narrative_architect.prompt.md)
- [csr_patient_safety_narrative_architect](prompts/clinical/medical_writing/csr_patient_safety_narrative_architect.prompt.md)
- [CSR Plain Language Summary Generator](prompts/clinical/medical_writing/csr_plain_language_summary_generator.prompt.md)
- [CTD Module 2.5 Clinical Overview Architect](prompts/clinical/medical_writing/ctd_module_2_5_clinical_overview_architect.prompt.md)
- [ctd_module_2_7_clinical_summary_architect](prompts/clinical/medical_writing/ctd_module_2_7_clinical_summary_architect.prompt.md)
- [Data Safety Monitoring Board Report Synthesizer](prompts/clinical/medical_writing/data_safety_monitoring_board_report_synthesizer.prompt.md)
- [Development Safety Update Report Architect](prompts/clinical/medical_writing/development_safety_update_report_architect.prompt.md)
- [eu_mdr_clinical_evaluation_report_architect](prompts/clinical/medical_writing/eu_mdr_clinical_evaluation_report_architect.prompt.md)
- [Informed Consent Form Plain Language Translator](prompts/clinical/medical_writing/icf_plain_language_translator.prompt.md)
- [icf_readability_compliance_architect](prompts/clinical/medical_writing/icf_readability_compliance_architect.prompt.md)
- [ich_e3_clinical_study_report_architect](prompts/clinical/medical_writing/ich_e3_clinical_study_report_architect.prompt.md)
- [Investigator's Brochure Safety Update Architect](prompts/clinical/medical_writing/investigators_brochure_safety_update_architect.prompt.md)
- [Pediatric Investigational Plan (PIP) Architect](prompts/clinical/medical_writing/pediatric_investigational_plan_architect.prompt.md)
- [Protocol Amendment Rationale Drafter](prompts/clinical/medical_writing/protocol_amendment_rationale_drafter.prompt.md)
- [protocol_deviation_assessment_architect](prompts/clinical/medical_writing/protocol_deviation_assessment_architect.prompt.md)
- [Regulatory Query Response Drafter](prompts/clinical/medical_writing/regulatory_query_response_drafter.prompt.md)
- [SAE Patient Narrative Drafter](prompts/clinical/medical_writing/sae_patient_narrative_drafter.prompt.md)
- [Clinical Monitoring Plan Development](prompts/clinical/monitoring/clinical_monitoring_plan.prompt.md)
- [Risk-Based Monitoring Data Evaluation](prompts/clinical/monitoring/rbm_data_evaluation.prompt.md)
- [RBQM Anomaly Detection](prompts/clinical/monitoring/rbqm_anomaly_detection.prompt.md)
- [adverse_event_signal_detection_architect](prompts/clinical/pharmacovigilance/adverse_event_signal_detection_architect.prompt.md)
- [ich_e2c_pbrer_benefit_risk_architect](prompts/clinical/pharmacovigilance/ich_e2c_pbrer_benefit_risk_architect.prompt.md)
- [Pharmacovigilance Risk Management Plan Architect](prompts/clinical/pharmacovigilance/pharmacovigilance_risk_management_plan_architect.prompt.md)
- [signal_detection_evaluator](prompts/clinical/pharmacovigilance/signal_detection_evaluator.prompt.md)
- [Protocol Deviation Reporting](prompts/clinical/protocol/protocol_deviation_reporting.prompt.md)
- [Protocol to CDISC USDM v3.0 Converter](prompts/clinical/protocol/protocol_to_usdm_v3.prompt.md)
- [SOP and TMF Document Synthesis](prompts/clinical/protocol/sop_tmf_document_synthesis.prompt.md)
- [breakthrough_therapy_designation_rationale_architect](prompts/clinical/regulatory_affairs/breakthrough_therapy_designation_rationale_architect.prompt.md)
- [ind_clinical_hold_response_architect](prompts/clinical/regulatory_affairs/ind_clinical_hold_response_architect.prompt.md)
- [investigators_brochure_safety_synthesizer](prompts/clinical/regulatory_affairs/investigators_brochure_safety_synthesizer.prompt.md)
- [SAE and Safety Reporting](prompts/clinical/safety/sae_safety_reporting.prompt.md)
- [Clinical Trial Agreement (CTA) Negotiation](prompts/clinical/site_acquisition/cta_negotiation.prompt.md)
- [Single IRB (sIRB) Plan Submission](prompts/clinical/site_acquisition/sirb_plan_submission.prompt.md)
- [Site Selection and Enrollment Forecaster](prompts/clinical/site_acquisition/site_enrollment_forecaster.prompt.md)
- [Compassionate Music Therapist & Composer](prompts/clinical/therapy/music_therapist_melody.prompt.md)
- [Adaptive Recruitment and Retention Strategy](prompts/clinical/trial_execution/adaptive_recruitment_retention_strategy.prompt.md)
- [AI-Powered Site and Recruitment Strategy](prompts/clinical/trial_execution/ai_powered_site_recruitment.prompt.md)
- [Compliance and Data Quality Monitoring Plan](prompts/clinical/trial_execution/compliance_data_quality_monitoring_plan.prompt.md)
- [Diversity Action Plan Development](prompts/clinical/trial_execution/diversity_action_plan_document.prompt.md)
- [Informed Consent Process Optimization](prompts/clinical/trial_execution/informed_consent_process.prompt.md)
- [Portfolio-Level Clinical Operations Roadmap](prompts/clinical/trial_execution/portfolio_clin_ops_roadmap.prompt.md)
- [Protocol Optimization and Risk Simulation](prompts/clinical/trial_execution/protocol_optimization_risk_simulation.prompt.md)
- [Patient Recruitment and Diversity Acceleration Plan](prompts/clinical/trial_execution/recruitment_diversity_acceleration.prompt.md)
- [Risk-Based Monitoring and Quality Plan](prompts/clinical/trial_execution/risk_based_monitoring_plan.prompt.md)
- [differential_diagnosis_mapping_architect](prompts/scientific/psychology/clinical/psychopathology/differential_diagnosis_mapping_architect.prompt.md)
- [dimensional_psychopathology_hierarchical_modeler](prompts/scientific/psychology/clinical/psychopathology/dimensional_psychopathology_hierarchical_modeler.prompt.md)
- [evidence_based_intervention_architect](prompts/scientific/psychology/clinical/treatment_planning/evidence_based_intervention_architect.prompt.md)

## Cognitive

- [cognitive_bias_mitigation_architect](prompts/scientific/psychology/cognitive/information_processing/cognitive_bias_mitigation_architect.prompt.md)

## Communication

- [80/20 Crash Course](prompts/communication/80_20_crash_course.prompt.md)
- [Principal Science Communicator (Analogy Engine)](prompts/communication/analogy_architect.prompt.md)
- [Data-to-Insight Analyst](prompts/communication/data_to_insight_analyst.prompt.md)
- [Density Refiner](prompts/communication/density_refiner.prompt.md)
- [Devil’s-Advocate Stress Test](prompts/communication/devils_advocate_stress_test.prompt.md)
- [Empathy-Map Facilitator](prompts/communication/empathy_map_facilitator.prompt.md)
- [Explain-Like-I’m-5 (ELI5)](prompts/communication/explain_like_im_5.prompt.md)
- [Hero's Journey Storyboarder](prompts/communication/heros_journey_storyboarder.prompt.md)
- [Lay Language Summary Creation](prompts/communication/lay_language_summary.prompt.md)
- [Negotiation Coach](prompts/communication/negotiation_coach.prompt.md)
- [Panel Debate](prompts/communication/panel_debate.prompt.md)
- [Pitch-Deck Outliner](prompts/communication/pitch_deck_outliner.prompt.md)
- [Rapid-Risk-Matrix](prompts/communication/rapid_risk_matrix.prompt.md)
- [Red-Team Stress-Test Simulation](prompts/communication/red_team_stress_test.prompt.md)
- [Rubber Duck Debugger](prompts/communication/rubber_duck_debugger.prompt.md)
- [Smart Task Prioritizer](prompts/communication/smart_task_prioritizer.prompt.md)
- [Socratic-Coach](prompts/communication/socratic_coach.prompt.md)
- [Pixar Story Spine Outline](prompts/communication/story_spine_outline.prompt.md)
- [Storyboard-My-Idea](prompts/communication/storyboard_my_idea.prompt.md)
- [Executive Briefing Architect (TL;DR)](prompts/communication/tldr_summarizer.prompt.md)
- [Writing Clarity Mentor](prompts/communication/writing_clarity_mentor.prompt.md)

## Computational

- [algorithmic_social_contagion_modeler](prompts/computational/network_contagion/algorithmic_social_contagion_modeler.prompt.md)
- [multi_scale_pde_asymptotic_homogenization_architect](prompts/computational/numerical_methods/multi_scale_pde_asymptotic_homogenization_architect.prompt.md)
- [physics_informed_neural_network_architect](prompts/computational/numerical_methods/physics_informed_neural_network_architect.prompt.md)
- [multi_objective_stochastic_optimization_architect](prompts/computational/operations_research/multi_objective_stochastic_optimization_architect.prompt.md)
- [pinn_stiff_pde_architect](prompts/scientific/applied_mathematics/computational/physics_informed_neural_networks/pinn_stiff_pde_architect.prompt.md)
- [3D QSAR Pharmacophore Modeling Architect](prompts/scientific/chemistry/computational/cheminformatics/3d_qsar_pharmacophore_modeling_architect.prompt.md)
- [Free Energy Perturbation Architect](prompts/scientific/chemistry/computational/molecular_dynamics/free_energy_perturbation_architect.prompt.md)
- [DFT Transition State Architect](prompts/scientific/chemistry/computational/quantum_chemistry/dft_transition_state_architect.prompt.md)
- [Non-Adiabatic Photodynamics Architect](prompts/scientific/chemistry/computational/quantum_chemistry/non_adiabatic_photodynamics_architect.prompt.md)
- [TD-DFT Excited-State Dynamics Architect](prompts/scientific/chemistry/computational/quantum_chemistry/td_dft_excited_state_dynamics_architect.prompt.md)
- [algorithmic_behavior_echo_chamber_modeler](prompts/scientific/psychology/computational/network_contagion/algorithmic_behavior_echo_chamber_modeler.prompt.md)
- [behavioral_epidemiology_social_contagion_modeler](prompts/scientific/psychology/computational/network_contagion/behavioral_epidemiology_social_contagion_modeler.prompt.md)
- [cognitive_inoculation_campaign_architect](prompts/scientific/psychology/computational/network_contagion/cognitive_inoculation_campaign_architect.prompt.md)
- [gamified_behavioral_addiction_contagion_modeler](prompts/scientific/psychology/computational/network_contagion/gamified_behavioral_addiction_contagion_modeler.prompt.md)
- [mass_psychogenic_illness_diffusion_modeler](prompts/scientific/psychology/computational/network_contagion/mass_psychogenic_illness_diffusion_modeler.prompt.md)
- [semantic_mutation_censorship_evasion_modeler](prompts/scientific/psychology/computational/network_contagion/semantic_mutation_censorship_evasion_modeler.prompt.md)
- [stochastic_radicalization_cascade_modeler](prompts/scientific/psychology/computational/network_contagion/stochastic_radicalization_cascade_modeler.prompt.md)
- [synthetic_media_epistemic_collapse_modeler](prompts/scientific/psychology/computational/network_contagion/synthetic_media_epistemic_collapse_modeler.prompt.md)

## Cosmology

- [Inflationary Tensor Perturbation Architect](prompts/scientific/physics/cosmology/early_universe/inflationary_tensor_perturbation_architect.prompt.md)

## Cra

- [Monitoring-Visit Report Generator](prompts/clinical/cra/cra_workflow/01_monitoring_visit_report_generator.prompt.md)
- [Investigator Follow-up Email & Action-Item Tracker](prompts/clinical/cra/cra_workflow/02_investigator_follow_up_email_tracker.prompt.md)
- [Risk-Based Monitoring (RBM) Plan Builder](prompts/clinical/cra/cra_workflow/03_rbm_plan_builder.prompt.md)

## Cross Cultural

- [multi_national_behavioral_intervention_architect](prompts/scientific/psychology/cross_cultural/population_psychometrics/multi_national_behavioral_intervention_architect.prompt.md)

## Data

- [Discrepancy Detection & Query Log Generator](prompts/clinical/data/clinical_data_workflow/01_discrepancy_detection_query_log.prompt.md)
- [Draft a Data Management Plan Section](prompts/clinical/data/clinical_data_workflow/02_data_management_plan_section.prompt.md)
- [Edit-Check Specification Builder for New eCRF Fields](prompts/clinical/data/clinical_data_workflow/03_edit_check_specification_builder.prompt.md)

## Data Management

- [Protocol-to-TS Generator](prompts/clinical/data_management/cdisc_compliance_workflow/01_protocol_to_ts_generator.prompt.md)
- [Raw-to-SDTM Auto-Mapper](prompts/clinical/data_management/cdisc_compliance_workflow/02_raw_to_sdtm_auto_mapper.prompt.md)
- [ADaM Derivation Writer](prompts/clinical/data_management/cdisc_compliance_workflow/03_adam_derivation_writer.prompt.md)
- [Controlled Terminology Harmonizer](prompts/clinical/data_management/cdisc_compliance_workflow/04_controlled_terminology_harmonizer.prompt.md)
- [Clinical ETL Mapping Spec](prompts/clinical/data_management/data_management_etl_workflow/01_clinical_etl_mapping_spec.prompt.md)
- [Clinical ETL Transformation QC](prompts/clinical/data_management/data_management_etl_workflow/02_clinical_etl_transformation_qc.prompt.md)
- [Clinical ETL Pipeline Review](prompts/clinical/data_management/data_management_etl_workflow/03_clinical_etl_pipeline_review.prompt.md)

## Data Science

- [Stochastic Architect](prompts/technical/data_science/stochastic_model_chain_workflow/01_stochastic_architect.prompt.md)
- [Stochastic Engineer](prompts/technical/data_science/stochastic_model_chain_workflow/02_stochastic_engineer.prompt.md)
- [Stochastic Strategist](prompts/technical/data_science/stochastic_model_chain_workflow/03_stochastic_strategist.prompt.md)

## Design

- [causal_inference_dag_architect](prompts/scientific/statistics/design/causal_inference/causal_inference_dag_architect.prompt.md)

## Developmental

- [ecological_momentary_assessment_multilevel_modeler](prompts/scientific/psychology/developmental/longitudinal_modeling/ecological_momentary_assessment_multilevel_modeler.prompt.md)
- [latent_growth_curve_modeling_architect](prompts/scientific/psychology/developmental/longitudinal_modeling/latent_growth_curve_modeling_architect.prompt.md)

## Eclinical Integration

- [Architect the Integration Blueprint](prompts/clinical/eclinical_integration/eclinical_integration_workflow/01_architect_integration_blueprint.prompt.md)
- [Data Mapping and Transformation Playbook](prompts/clinical/eclinical_integration/eclinical_integration_workflow/02_data_mapping_transformation_playbook.prompt.md)
- [Regulatory and Validation Checklist](prompts/clinical/eclinical_integration/eclinical_integration_workflow/03_regulatory_validation_checklist.prompt.md)

## Ecology

- [spatial_metapopulation_seir_epidemiology_architect](prompts/scientific/ecology/population_dynamics/spatial_metapopulation_seir_epidemiology_architect.prompt.md)
- [stochastic_lotka_volterra_population_modeler](prompts/scientific/ecology/population_dynamics/stochastic_lotka_volterra_population_modeler.prompt.md)

## Econometrics

- [local_polynomial_regression_discontinuity_architect](prompts/scientific/economics/econometrics/causal_inference/local_polynomial_regression_discontinuity_architect.prompt.md)
- [staggered_difference_in_differences_architect](prompts/scientific/economics/econometrics/causal_inference/staggered_difference_in_differences_architect.prompt.md)
- [Synthetic Control Method Architect](prompts/scientific/economics/econometrics/causal_inference/synthetic_control_method_architect.prompt.md)
- [dynamic_panel_gmm_architect](prompts/scientific/economics/econometrics/panel_data/dynamic_panel_gmm_architect.prompt.md)
- [mixed_frequency_dynamic_factor_nowcasting_architect](prompts/scientific/economics/econometrics/time_series/mixed_frequency_dynamic_factor_nowcasting_architect.prompt.md)
- [structural_vector_autoregression_architect](prompts/scientific/economics/econometrics/time_series/structural_vector_autoregression_architect.prompt.md)

## Epidemiology

- [longitudinal_trauma_propagation_modeler](prompts/scientific/epidemiology/global_mental_health/longitudinal_trauma_propagation_modeler.prompt.md)
- [affective_polarization_contagion_mapper](prompts/scientific/psychology/epidemiology/affective_polarization/affective_polarization_contagion_mapper.prompt.md)
- [digital_phenotyping_epidemiological_surveillance_architect](prompts/scientific/psychology/epidemiology/global_mental_health/digital_phenotyping_epidemiological_surveillance_architect.prompt.md)
- [multinational_longitudinal_intervention_architect](prompts/scientific/psychology/epidemiology/global_mental_health/multinational_longitudinal_intervention_architect.prompt.md)
- [psychological_trauma_epidemiology_mapper](prompts/scientific/psychology/epidemiology/global_mental_health/psychological_trauma_epidemiology_mapper.prompt.md)

## Epistemology

- [bayesian_epistemological_update_formalizer](prompts/scientific/philosophy/epistemology/formal_epistemology/bayesian_epistemological_update_formalizer.prompt.md)
- [cognitive_bias_epistemological_deconstructor](prompts/scientific/philosophy/epistemology/formal_epistemology/cognitive_bias_epistemological_deconstructor.prompt.md)
- [epistemic_defeater_formal_analyzer](prompts/scientific/philosophy/epistemology/formal_epistemology/epistemic_defeater_formal_analyzer.prompt.md)

## Epro

- [Patient-Centric BYOD ePRO Workflow](prompts/clinical/epro/epro_workflow/01_patient-centric_byod_workflow.prompt.md)
- [Optimize ePRO Form Design](prompts/clinical/epro/epro_workflow/02_optimize_epro_form_design.prompt.md)
- [ePRO Adoption Plan for Sponsors](prompts/clinical/epro/epro_workflow/03_epro_adoption_plan_for_sponsors.prompt.md)

## Ethics

- [Applied Ethical Stress Tester](prompts/scientific/philosophy/ethics/normative_ethics/applied_ethical_stress_tester.prompt.md)
- [Normative Ethics Stress Tester](prompts/scientific/philosophy/ethics/normative_ethics/normative_ethics_stress_tester.prompt.md)

## Finance

- [continuous_time_asset_pricing_architect](prompts/scientific/economics/finance/asset_pricing/continuous_time_asset_pricing_architect.prompt.md)

## Forms

- [CRF Shell Generator](prompts/clinical/forms/clinical_prompts_workflow/01_crf_shell_generator.prompt.md)
- [CRF Quality Auditor](prompts/clinical/forms/clinical_prompts_workflow/02_crf_quality_auditor.prompt.md)
- [CDASH Mapping & Completion-Guide Assistant](prompts/clinical/forms/clinical_prompts_workflow/03_cdash_mapping_completion_guide.prompt.md)

## Foundations

- [structural_proof_theory_cut_elimination_architect](prompts/scientific/formal_logic/foundations/proof_theory/structural_proof_theory_cut_elimination_architect.prompt.md)
- [homotopy_type_theory_univalence_architect](prompts/scientific/mathematics/foundations/proof_theory/homotopy_type_theory_univalence_architect.prompt.md)
- [intuitionistic_logic_natural_deduction_generator](prompts/scientific/mathematics/foundations/proof_theory/intuitionistic_logic_natural_deduction_generator.prompt.md)
- [forcing_poset_generic_extension_architect](prompts/scientific/mathematics/foundations/set_theory/forcing_poset_generic_extension_architect.prompt.md)
- [large_cardinal_elementary_embedding_architect](prompts/scientific/mathematics/foundations/set_theory/large_cardinal_elementary_embedding_architect.prompt.md)
- [Intuitionistic Logic Natural Deduction Prover](prompts/scientific/philosophy/logic/foundations/proof_theory/intuitionistic_logic_natural_deduction_prover.prompt.md)

## Genetics

- [crispr_cas9_off_target_thermodynamic_architect](prompts/scientific/biology/genetics/genomics/crispr_cas9_off_target_thermodynamic_architect.prompt.md)
- [chromatin_conformation_hic_contact_map_architect](prompts/scientific/genetics/genomics/chromatin_conformation_hic_contact_map_architect.prompt.md)
- [crispr_cas9_off_target_predictive_modeler](prompts/scientific/genetics/genomics/crispr_cas9_off_target_predictive_modeler.prompt.md)
- [epigenetic_methylation_hmm_architect](prompts/scientific/genetics/genomics/epigenetic_methylation_hmm_architect.prompt.md)
- [gwas_polygenic_risk_score_architect](prompts/scientific/genetics/genomics/gwas_polygenic_risk_score_architect.prompt.md)
- [metagenomic_assembly_taxonomic_binning_architect](prompts/scientific/genetics/genomics/metagenomic_assembly_taxonomic_binning_architect.prompt.md)
- [pangenome_graph_structural_variant_architect](prompts/scientific/genetics/genomics/pangenome_graph_structural_variant_architect.prompt.md)
- [single_cell_rna_seq_trajectory_inference_architect](prompts/scientific/genetics/transcriptomics/single_cell_rna_seq_trajectory_inference_architect.prompt.md)
- [spatial_transcriptomics_cellular_communication_architect](prompts/scientific/genetics/transcriptomics/spatial_transcriptomics_cellular_communication_architect.prompt.md)

## Geometry

- [projective_scheme_sheaf_cohomology_architect](prompts/scientific/mathematics/geometry/algebraic_geometry/projective_scheme_sheaf_cohomology_architect.prompt.md)
- [atiyah_singer_index_theorem_architect](prompts/scientific/mathematics/geometry/differential/atiyah_singer_index_theorem_architect.prompt.md)
- [pseudo_riemannian_tensor_calculus_prover](prompts/scientific/mathematics/geometry/differential/pseudo_riemannian_tensor_calculus_prover.prompt.md)
- [Riemannian Manifold Curvature Deriver](prompts/scientific/mathematics/geometry/differential/riemannian_manifold_curvature_deriver.prompt.md)

## Google Jules

- [Jules Agile Orchestrator](prompts/google_jules/jules_agile_orchestrator.prompt.md)
- [Jules API Scout](prompts/google_jules/jules_api_scout.prompt.md)
- [Jules Compliance Officer](prompts/google_jules/jules_compliance_officer.prompt.md)
- [Jules Concurrency Architect](prompts/google_jules/jules_concurrency_architect.prompt.md)
- [Jules Data Architect](prompts/google_jules/jules_data_architect.prompt.md)
- [Jules Developer Agent](prompts/google_jules/jules_developer_agent.prompt.md)
- [Jules DevOps Engineer](prompts/google_jules/jules_devops_engineer.prompt.md)
- [Jules E2E Test Engineer](prompts/google_jules/jules_e2e_test_engineer.prompt.md)
- [Jules FinOps Profiler](prompts/google_jules/jules_finops_profiler.prompt.md)
- [Jules Maintainer](prompts/google_jules/jules_maintainer.prompt.md)
- [Jules Orchestrator](prompts/google_jules/jules_orchestrator.prompt.md)
- [Jules Product Architect](prompts/google_jules/jules_product_architect.prompt.md)
- [Jules QA Gatekeeper](prompts/google_jules/jules_qa_gatekeeper.prompt.md)
- [Jules Security Auditor](prompts/google_jules/jules_security_auditor.prompt.md)
- [Jules System Designer](prompts/google_jules/jules_system_designer.prompt.md)
- [Jules Test Generator](prompts/google_jules/jules_test_gen.prompt.md)
- [Jules UX Writer](prompts/google_jules/jules_ux_writer.prompt.md)

## Growth

- [algorithmic_multi_touch_attribution_modeler](prompts/growth/analytics/algorithmic_multi_touch_attribution_modeler.prompt.md)
- [cohort_retention_survival_analysis_architect](prompts/growth/lifecycle/cohort_retention_survival_analysis_architect.prompt.md)
- [cross_channel_behavioral_trigger_architect](prompts/growth/lifecycle/cross_channel_behavioral_trigger_architect.prompt.md)
- [bayesian_media_mix_modeling_architect](prompts/growth/performance_marketing/bayesian_media_mix_modeling_architect.prompt.md)
- [predictive_cac_payback_modeler](prompts/growth/performance_marketing/predictive_cac_payback_modeler.prompt.md)
- [b2b_abm_pipeline_velocity_architect](prompts/growth/predictive_modeling/b2b_abm_pipeline_velocity_architect.prompt.md)
- [predictive_churn_ltv_optimization_architect](prompts/growth/predictive_modeling/predictive_churn_ltv_optimization_architect.prompt.md)
- [freemium_conversion_velocity_architect](prompts/growth/product_marketing/freemium_conversion_velocity_architect.prompt.md)
- [product_led_growth_k_factor_architect](prompts/growth/product_marketing/product_led_growth_k_factor_architect.prompt.md)
- [gtm_pricing_elasticity_architect](prompts/growth/strategy/gtm_pricing_elasticity_architect.prompt.md)

## Imaging

- [Imaging Charter Draft](prompts/clinical/imaging/imaging_workflow/01_imaging_charter_draft.prompt.md)
- [Site Upload QC and Query Generator](prompts/clinical/imaging/imaging_workflow/02_site_upload_qc.prompt.md)
- [Central Reading Paradigm Design](prompts/clinical/imaging/imaging_workflow/03_central_reading_design.prompt.md)
- [Regulatory Imaging Charter Generator](prompts/clinical/imaging/imaging_workflow/04_regulatory_imaging_charter_generator.prompt.md)
- [Image Acquisition QC Workflow Blueprint](prompts/clinical/imaging/imaging_workflow/05_image_acquisition_qc_workflow_blueprint.prompt.md)
- [Regulatory Imaging Data Package](prompts/clinical/imaging/imaging_workflow/06_regulatory_imaging_data_package.prompt.md)

## Inference

- [bayesian_hierarchical_model_architect](prompts/scientific/statistics/inference/bayesian_methods/bayesian_hierarchical_model_architect.prompt.md)
- [dirichlet_process_mixture_architect](prompts/scientific/statistics/inference/bayesian_methods/dirichlet_process_mixture_architect.prompt.md)
- [reversible_jump_mcmc_architect](prompts/scientific/statistics/inference/bayesian_methods/reversible_jump_mcmc_architect.prompt.md)
- [variational_inference_architect](prompts/scientific/statistics/inference/bayesian_methods/variational_inference_architect.prompt.md)
- [double_machine_learning_architect](prompts/scientific/statistics/inference/causal_inference/double_machine_learning_architect.prompt.md)
- [target_trial_emulation_architect](prompts/scientific/statistics/inference/causal_inference/target_trial_emulation_architect.prompt.md)
- [Functional Data Analysis Architect](prompts/scientific/statistics/inference/nonparametric_methods/functional_data_analysis_architect.prompt.md)

## Inorganic

- [Organometallic Catalytic Cycle Architect](prompts/scientific/chemistry/inorganic/catalysis/organometallic_catalytic_cycle_architect.prompt.md)

## Institutions

- [carceral_state_expansion_modeler](prompts/scientific/sociology/institutions/macro_structures/carceral_state_expansion_modeler.prompt.md)

## Languages

- [Advanced Python Testing](prompts/technical/languages/python/advanced_python_testing.prompt.md)
- [Principal Python Developer](prompts/technical/languages/python/principal_python_developer.prompt.md)
- [Python Concurrency Mastery](prompts/technical/languages/python/python_concurrency_mastery.prompt.md)
- [Python Hexagonal Architecture](prompts/technical/languages/python/python_hexagonal_architecture.prompt.md)
- [Python Performance Optimization](prompts/technical/languages/python/python_performance_optimization.prompt.md)
- [Senior Python Developer](prompts/technical/languages/python/senior_python_developer.prompt.md)
- [Principal Rust Developer](prompts/technical/languages/rust/principal_rust_developer.prompt.md)
- [Rust Architectural Patterns](prompts/technical/languages/rust/rust_architectural_patterns.prompt.md)
- [Principal TypeScript Developer](prompts/technical/languages/typescript/principal_typescript_developer.prompt.md)

## Lifecycle

- [Product Brief Template](prompts/technical/software_engineering/lifecycle/agentic_coding_workflow/01_product_brief.prompt.md)
- [Project Brief for Epic](prompts/technical/software_engineering/lifecycle/agentic_coding_workflow/02_project_brief_epic.prompt.md)

## Lifestyle

- [Eco-Crypto Haiku Oracle](prompts/lifestyle/arboreal_crypto_haiku/eco_crypto_haiku_oracle.prompt.md)
- [Culinary Amnestic Reconstruction Engine (CARE)](prompts/lifestyle/culinary/culinary_amnestic_reconstruction.prompt.md)
- [Myco-Alchemical Arbitrageur](prompts/lifestyle/fungal_financial_alchemy/myco_alchemical_arbitrageur.prompt.md)
- [Quantum Baroque Garden Architect](prompts/lifestyle/quantum_baroque_gardening/quantum_baroque_garden_architect.prompt.md)

## Logic

- [agm_belief_revision_formal_engine](prompts/scientific/philosophy/logic/philosophical_logic/agm_belief_revision_formal_engine.prompt.md)
- [counterfactual_semantics_stalnaker_lewis_evaluator](prompts/scientific/philosophy/logic/philosophical_logic/counterfactual_semantics_stalnaker_lewis_evaluator.prompt.md)
- [Deontic Logic Normative Conflict Resolver](prompts/scientific/philosophy/logic/philosophical_logic/deontic_logic_normative_conflict_resolver.prompt.md)
- [Modal Logic Possible Worlds Evaluator](prompts/scientific/philosophy/logic/philosophical_logic/modal_logic_possible_worlds_evaluator.prompt.md)
- [paraconsistent_logic_dialetheism_evaluator](prompts/scientific/philosophy/logic/philosophical_logic/paraconsistent_logic_dialetheism_evaluator.prompt.md)

## Macroeconomics

- [new_keynesian_dsge_architect](prompts/scientific/economics/macroeconomics/dsge_modeling/new_keynesian_dsge_architect.prompt.md)
- [open_economy_dsge_architect](prompts/scientific/economics/macroeconomics/dsge_modeling/open_economy_dsge_architect.prompt.md)
- [hank_macroeconomic_architect](prompts/scientific/economics/macroeconomics/heterogeneous_agents/hank_macroeconomic_architect.prompt.md)
- [diamond_mortensen_pissarides_architect](prompts/scientific/economics/macroeconomics/search_and_matching/diamond_mortensen_pissarides_architect.prompt.md)

## Management

- [Accelerate Patient Recruitment & Retention](prompts/management/clinical_research_manager/accelerate_patient_recruitment_retention.prompt.md)
- [Digest Regulatory Updates Affecting Protocol](prompts/management/clinical_research_manager/digest_regulatory_updates.prompt.md)
- [Portfolio KPI Dashboard Brief](prompts/management/clinical_research_manager/portfolio_kpi_dashboard_brief.prompt.md)
- [FDA-Aligned AI Governance Framework](prompts/management/executive/ai_governance_framework.prompt.md)
- [Crisis-Management Playbook Generator](prompts/management/executive/crisis_management_playbook.prompt.md)
- [Digital Transformation Roadmap for Clinical Operations](prompts/management/executive/digital_transformation_roadmap.prompt.md)
- [Emerging-Science Horizon Scan](prompts/management/executive/emerging_science_horizon_scan.prompt.md)
- [Executive-Ready Brief and Talking Points](prompts/management/executive/executive_brief_synthesizer.prompt.md)
- [Executive Trial-Health Dashboard](prompts/management/executive/executive_trial_health_dashboard.prompt.md)
- [Hosting Cost Reduction ToT Plan](prompts/management/executive/hosting_cost_reduction_tot.prompt.md)
- [Quarterly Innovation Radar for Decentralized and Hybrid Trials](prompts/management/executive/innovation_radar.prompt.md)
- [Investor and Board Narrative Builder](prompts/management/executive/investor_board_narrative_builder.prompt.md)
- [Strategic Market and Competitor Radar](prompts/management/executive/market_competitor_radar.prompt.md)
- [Regulatory and Competitive Intelligence Briefing](prompts/management/executive/regulatory_competitive_intel_briefing.prompt.md)
- [Strategic Consultant SWOT](prompts/management/executive/strategic_consultant_swot.prompt.md)
- [Strategic Growth Roadmap](prompts/management/executive/strategic_growth_roadmap.prompt.md)
- [Strategic Market Foresight and Action Plan](prompts/management/executive/strategic_market_foresight.prompt.md)
- [Strategic Portfolio Prioritizer](prompts/management/executive/strategic_portfolio_prioritizer.prompt.md)
- [Trial-Design Optimisation Memo](prompts/management/executive/trial_design_optimisation_memo.prompt.md)
- [Reverse Brainstorming](prompts/management/innovation/reverse_brainstorming.prompt.md)
- [SCAMPER Ideation Coach](prompts/management/innovation/scamper_ideation_coach.prompt.md)
- [90-Day Biostatistics Onboarding Plan](prompts/management/leadership/biostatistics_onboarding_plan.prompt.md)
- [Leadership Reflection and Culture](prompts/management/leadership/leadership_reflection_culture.prompt.md)
- [Operational Excellence Communication Framework](prompts/management/leadership/operational_excellence_communication.prompt.md)
- [Strategic Alignment and Innovation](prompts/management/leadership/strategic_alignment_innovation.prompt.md)
- [AI-Enhanced RBM Action Plan](prompts/management/medical_director/ai_enhanced_rbm_action_plan.prompt.md)
- [Clinical Trial Protocol Compliance Review](prompts/management/medical_director/clinical_trial_protocol_quality_compliance_review.prompt.md)
- [Pharmacovigilance Safety Signal Prioritization](prompts/management/medical_director/pharmacovigilance_safety_signal_prioritization.prompt.md)
- [Action-Oriented Meeting Minutes & Tracker](prompts/management/operations/action_oriented_meeting_minutes.prompt.md)
- [CAPA Root Cause and Resolution Architect](prompts/management/operations/capa_root_cause_resolution_architect.prompt.md)
- [CRO Trial-Performance KPI Dashboard Blueprint](prompts/management/operations/cro_trial_performance_kpi_dashboard_blueprint.prompt.md)
- [dynamic_fleet_routing_optimization_architect](prompts/management/operations/dynamic_fleet_routing_optimization_architect.prompt.md)
- [Fair-Market-Value Budget Negotiation Brief](prompts/management/operations/fair_market_value_budget_negotiation_brief.prompt.md)
- [Fishbone Facilitator](prompts/management/operations/fishbone_facilitator.prompt.md)
- [Forward-Looking Resource & Capacity Forecast](prompts/management/operations/forward_capacity_forecast.prompt.md)
- [Inventory & Demand-Planning Simulation](prompts/management/operations/inventory_demand_planning_simulation.prompt.md)
- [KPI Dashboard & Monthly Ops-Review Pack](prompts/management/operations/kpi_dashboard_ops_review.prompt.md)
- [lean_six_sigma_vsm_architect](prompts/management/operations/lean_six_sigma_vsm_architect.prompt.md)
- [multi_echelon_inventory_optimization_architect](prompts/management/operations/multi_echelon_inventory_optimization_architect.prompt.md)
- [Multistudy Resource & Capacity Forecast Plan](prompts/management/operations/multistudy_resource_capacity_forecast_plan.prompt.md)
- [Operational Excellence & Risk Sweep](prompts/management/operations/operational_excellence_risk_sweep.prompt.md)
- [360° Operational KPI & Benchmark Review](prompts/management/operations/operational_kpi_benchmark_review.prompt.md)
- [operational_resilience_tabletop_simulation_architect](prompts/management/operations/operational_resilience_tabletop_simulation_architect.prompt.md)
- [operational_turnaround_restructuring_architect](prompts/management/operations/operational_turnaround_restructuring_architect.prompt.md)
- [post_merger_integration_synergy_architect](prompts/management/operations/post_merger_integration_synergy_architect.prompt.md)
- [Proactive Risk Heat-Map for Decentralized & Virtual Trials](prompts/management/operations/proactive_risk_heat_map.prompt.md)
- [Quarterly CRO KPI Executive Brief](prompts/management/operations/quarterly_kpi_executive_brief.prompt.md)
- [Rapid Process Diagnostic & Lean Improvement Plan](prompts/management/operations/rapid_process_diagnostic.prompt.md)
- [Rolling Resource & Capacity Forecast](prompts/management/operations/rolling_resource_capacity_forecast.prompt.md)
- [Study Start-Up Checklist & Timeline](prompts/management/operations/study_startup_checklist.prompt.md)
- [Supply Chain Disruption Stochastic Stress Test Architect](prompts/management/operations/supply_chain_stress_test.prompt.md)
- [Risk-Based Vendor Performance Improvement Plan](prompts/management/operations/vendor_performance_improvement_plan.prompt.md)
- [Vendor Qualification and Oversight](prompts/management/operations/vendor_qualification.prompt.md)
- [Weekly Operations KPI Snapshot](prompts/management/operations/weekly_ops_kpi_snapshot.prompt.md)
- [Career Compass Advisor](prompts/management/personal_effectiveness/career_compass_advisor.prompt.md)
- [Eisenhower Matrix Coach](prompts/management/personal_effectiveness/eisenhower_matrix_coach.prompt.md)
- [Scenario-Based Financial Navigator](prompts/management/personal_effectiveness/financial_navigator.prompt.md)
- [Learning Path Mentor](prompts/management/personal_effectiveness/learning_path_mentor.prompt.md)
- [Micro-Habit Health Coach](prompts/management/personal_effectiveness/micro_habit_health_coach.prompt.md)
- [Second-Order Thinking Oracle](prompts/management/personal_effectiveness/second_order_thinking_oracle.prompt.md)
- [Clinical-Trial Timeline and Risk Radar](prompts/management/project_management/clinical_trial_timeline_risk_radar.prompt.md)
- [Cross-Study Operational Risk Heat Map and Mitigation Plan](prompts/management/project_management/cross_study_risk_heat_map_mitigation_plan.prompt.md)
- [Executive Sponsor Briefing Deck Outline](prompts/management/project_management/executive_sponsor_briefing_deck_outline.prompt.md)
- [Senior Agile Transformation Coach (Retrospectives)](prompts/management/project_management/neutral_scrum_retro.prompt.md)
- [Portfolio Resource and Budget Forecast](prompts/management/project_management/portfolio_resource_budget_forecast.prompt.md)
- [Project Starter Pack Prompts](prompts/management/project_management/project_starter_pack.prompt.md)
- [RACI Mapper](prompts/management/project_management/raci_mapper.prompt.md)
- [Risk and Pre-Mortem Analysis](prompts/management/project_management/risk_pre_mortem_analysis.prompt.md)
- [Rollout Risk Matrix](prompts/management/project_management/rollout_risk_matrix.prompt.md)
- [Sponsor-Ready Monthly Status Brief](prompts/management/project_management/sponsor_ready_monthly_status_brief.prompt.md)
- [Status Update and Task Prioritization](prompts/management/project_management/status_update_task_prioritization.prompt.md)
- [TMF Gap-Analysis and Audit Readiness Check](prompts/management/project_management/tmf_gap_analysis_audit_readiness_check.prompt.md)

## Market Research

- [Market Landscape & Trend Analysis](prompts/business/market_research/market_research_workflow/01_market_landscape_trend_analysis.prompt.md)
- [Target Segment & User Needs Assessment](prompts/business/market_research/market_research_workflow/02_target_segment_user_needs_assessment.prompt.md)
- [Regulatory & Commercial Barrier Mapping](prompts/business/market_research/market_research_workflow/03_regulatory_commercial_barrier_mapping.prompt.md)
- [Market Report Executive Summary](prompts/business/market_research/market_research_workflow/04_market_report_exec_summary.prompt.md)

## Mathematics

- [categorical_theorem_translator](prompts/scientific/mathematics/category_theory/categorical_theorem_translator.prompt.md)
- [category_theory_adjunction_architect](prompts/scientific/mathematics/category_theory/category_theory_adjunction_architect.prompt.md)
- [topos_theoretic_sheaf_semantics_evaluator](prompts/scientific/mathematics/category_theory/topos_theoretic_sheaf_semantics_evaluator.prompt.md)
- [Physics-Informed Neural Network (PINN) Architect](prompts/scientific/mathematics/computational/physics_informed_neural_network_architect.prompt.md)
- [Custom Axiomatic System Soundness Evaluator](prompts/scientific/mathematics/formal_logic/custom_axiomatic_system_soundness_evaluator.prompt.md)
- [dependent_type_theory_judgment_derivation](prompts/scientific/mathematics/formal_logic/dependent_type_theory_judgment_derivation.prompt.md)
- [Epistemic Logic Multi-Agent Knowledge Architect](prompts/scientific/mathematics/formal_logic/epistemic_logic_multi_agent_knowledge_architect.prompt.md)
- [first_order_logic_natural_language_translator](prompts/scientific/mathematics/formal_logic/first_order_logic_natural_language_translator.prompt.md)
- [first_order_logic_semantic_tableau_generator](prompts/scientific/mathematics/formal_logic/first_order_logic_semantic_tableau_generator.prompt.md)
- [first_order_logic_sequent_calculus_prover](prompts/scientific/mathematics/formal_logic/first_order_logic_sequent_calculus_prover.prompt.md)
- [godel_incompleteness_arithmetization_engineer](prompts/scientific/mathematics/formal_logic/godel_incompleteness_arithmetization_engineer.prompt.md)
- [intuitionistic_natural_deduction_prover](prompts/scientific/mathematics/formal_logic/intuitionistic_natural_deduction_prover.prompt.md)
- [Linear Logic Resource Proof Generator](prompts/scientific/mathematics/formal_logic/linear_logic_resource_proof_generator.prompt.md)
- [linear_temporal_logic_model_checker](prompts/scientific/mathematics/formal_logic/linear_temporal_logic_model_checker.prompt.md)
- [mu_recursive_function_derivation_architect](prompts/scientific/mathematics/formal_logic/mu_recursive_function_derivation_architect.prompt.md)
- [propositional_dynamic_logic_pdl_evaluator](prompts/scientific/mathematics/formal_logic/propositional_dynamic_logic_pdl_evaluator.prompt.md)
- [Separation Logic Heap Entailment Architect](prompts/scientific/mathematics/formal_logic/separation_logic_heap_entailment_architect.prompt.md)
- [fractional_calculus_pde_modeler](prompts/scientific/mathematics/numerical_methods/fractional_calculus_pde_modeler.prompt.md)
- [stiff_pde_numerical_stability_architect](prompts/scientific/mathematics/numerical_methods/stiff_pde_numerical_stability_architect.prompt.md)
- [Polynomial Optimization SDP Relaxation Architect](prompts/scientific/mathematics/optimization/polynomial_optimization_sdp_relaxation_architect.prompt.md)
- [Stochastic Multi-Objective Optimization Architect](prompts/scientific/mathematics/optimization/stochastic_optimization_architect.prompt.md)
- [Topological Counterexample Generator](prompts/scientific/mathematics/topology/topological_counterexample_generator.prompt.md)

## Meta

- [Dynamic Epistemic Drift Mitigator](prompts/meta/agent_orchestration/dynamic_epistemic_drift_mitigator.prompt.md)
- [Fractal Epistemic Consensus Architect](prompts/meta/agent_orchestration/fractal_epistemic_consensus_architect.prompt.md)
- [Vector Prompt Calibrator](prompts/meta/calibration/vector_prompt_calibrator.prompt.md)
- [The Prompt Alchemist](prompts/meta/creative/the_prompt_alchemist.prompt.md)
- [Master Ultrameta Prompt Architect](prompts/meta/meta_prompt_chain/00_L0_master-ultrameta.prompt.md)
- [Meta Prompt Architect](prompts/meta/meta_prompt_chain/01_L1_meta-prompt-architect.prompt.md)
- [Prompt Engineer Template](prompts/meta/meta_prompt_chain/02_L2_prompt-engineer.prompt.md)
- [Task Prototyper](prompts/meta/meta_prompt_chain/03_L3_task-prototyper.prompt.md)
- [Worker Prompt](prompts/meta/meta_prompt_chain/04_L4_worker_prompt.prompt.md)
- [Agent Persona Generator](prompts/meta/meta_prompt_chain/05_L5_agent_persona_generator.prompt.md)
- [AGENTS.md Checklist Generator](prompts/meta/meta_prompt_chain/05_L5_agents-md-checklist.prompt.md)
- [AI Coding Agent Plan Generator](prompts/meta/meta_prompt_chain/05_L5_ai_coding_agent.prompt.md)
- [Comprehensive Task Template](prompts/meta/meta_prompt_chain/05_L5_comprehensive_task_template.prompt.md)
- [MECE Structuring Consultant](prompts/meta/meta_prompt_chain/05_L5_mece_structuring.prompt.md)
- [Prompt Engineer Fact Checker](prompts/meta/meta_prompt_chain/05_L5_prompt_engineer_fact_checker.prompt.md)
- [PromptCrafter GPT](prompts/meta/meta_prompt_chain/05_L5_promptcrafter_gpt.prompt.md)
- [README Generator](prompts/meta/meta_prompt_chain/05_L5_readme-generator.prompt.md)
- [Vector Prompt Calibration Evaluator](prompts/meta/meta_prompt_chain/vector_calibration.prompt.md)
- [Non-Monotonic Self-Correction Meta-Reasoner](prompts/meta/recursive_logic/non_monotonic_self_correction_reasoner.prompt.md)

## Metaphysics

- [mereological_composition_analyzer](prompts/scientific/philosophy/metaphysics/ontology/mereological_composition_analyzer.prompt.md)
- [Metaphysical Dialectical Synthesizer](prompts/scientific/philosophy/metaphysics/ontology/metaphysical_dialectical_synthesizer.prompt.md)
- [metaphysical_grounding_fundamentality_formalizer](prompts/scientific/philosophy/metaphysics/ontology/metaphysical_grounding_fundamentality_formalizer.prompt.md)

## Methods

- [large_scale_axial_coding_framework_generator](prompts/scientific/sociology/methods/ethnographic_coding/large_scale_axial_coding_framework_generator.prompt.md)
- [blinder_oaxaca_decomposition_architect](prompts/scientific/sociology/methods/quantitative/blinder_oaxaca_decomposition_architect.prompt.md)
- [exponential_random_graph_model_architect](prompts/scientific/sociology/methods/social_network_analysis/exponential_random_graph_model_architect.prompt.md)

## Microbiology

- [Bioburden Testing SOP](prompts/scientific/microbiology/microbiology_workflow/01_bioburden_testing_sop.prompt.md)
- [EO Sterilization Validation Protocol](prompts/scientific/microbiology/microbiology_workflow/02_eo_sterilization_validation_protocol.prompt.md)
- [Endotoxin Control & 510(k) Risk Plan](prompts/scientific/microbiology/microbiology_workflow/03_endotoxin_control_510k_risk_plan.prompt.md)

## Microeconomics

- [n_player_bayesian_nash_equilibrium_auction_architect](prompts/scientific/economics/microeconomics/game_theory/n_player_bayesian_nash_equilibrium_auction_architect.prompt.md)
- [optimal_mechanism_design_architect](prompts/scientific/economics/microeconomics/mechanism_design/optimal_mechanism_design_architect.prompt.md)

## Modeling

- [multivariate_extreme_value_architect](prompts/scientific/statistics/modeling/extreme_value_theory/multivariate_extreme_value_architect.prompt.md)
- [high_dimensional_sparse_regression_architect](prompts/scientific/statistics/modeling/high_dimensional_analysis/high_dimensional_sparse_regression_architect.prompt.md)
- [vine_copula_dependency_architect](prompts/scientific/statistics/modeling/multivariate_analysis/vine_copula_dependency_architect.prompt.md)
- [log_gaussian_cox_process_architect](prompts/scientific/statistics/modeling/spatial_point_processes/log_gaussian_cox_process_architect.prompt.md)
- [spatio_temporal_geostatistical_spde_inla_architect](prompts/scientific/statistics/modeling/spatio_temporal_analysis/spatio_temporal_geostatistical_spde_inla_architect.prompt.md)
- [joint_longitudinal_survival_architect](prompts/scientific/statistics/modeling/survival_analysis/joint_longitudinal_survival_architect.prompt.md)

## Molecular

- [complex_ppi_network_mapper](prompts/scientific/molecular/proteomics/complex_ppi_network_mapper.prompt.md)
- [top_down_proteomics_ptm_mapping_architect](prompts/scientific/molecular/proteomics/top_down_proteomics_ptm_mapping_architect.prompt.md)

## Monitoring

- [Risk-Based Site Performance Dashboard](prompts/clinical/monitoring/clinical_monitoring_workflow/01_risk_based_site_performance_dashboard.prompt.md)
- [CAPA Plan Builder for Monitoring Findings](prompts/clinical/monitoring/clinical_monitoring_workflow/02_capa_plan_builder_for_monitoring_findings.prompt.md)
- [Monitoring Visit Report (MVR) Quality Critique](prompts/clinical/monitoring/clinical_monitoring_workflow/03_monitoring_visit_report_quality_critique.prompt.md)

## Non Classical

- [epistemic_modal_logic_kripke_evaluator](prompts/scientific/formal_logic/non_classical/modal_logic/epistemic_modal_logic_kripke_evaluator.prompt.md)

## Operations

- [DMAIC Process Optimization Architect](prompts/business/operations/lean_six_sigma/dmaic_process_optimization_architect.prompt.md)
- [global_supply_chain_geopolitical_duress_architect](prompts/business/operations/supply_chain/global_supply_chain_geopolitical_duress_architect.prompt.md)
- [Global Supply Chain Resilience Architect](prompts/business/operations/supply_chain/global_supply_chain_resilience_architect.prompt.md)
- [Supply Chain Network Topology Optimization Architect](prompts/business/operations/supply_chain/supply_chain_network_topology_optimization_architect.prompt.md)

## Organic

- [Visible Light Photoredox Pathway Architect](prompts/scientific/chemistry/organic/photoredox_catalysis/visible_light_photoredox_pathway_architect.prompt.md)
- [advanced_retrosynthetic_pathway_generator](prompts/scientific/chemistry/organic/retrosynthesis/advanced_retrosynthetic_pathway_generator.prompt.md)
- [multi_step_retrosynthetic_pathway_architect](prompts/scientific/chemistry/organic/retrosynthesis/multi_step_retrosynthetic_pathway_architect.prompt.md)

## Particle Physics

- [Non-Abelian Gauge Theory Perturbative Expansion Architect](prompts/scientific/physics/particle_physics/standard_model/non_abelian_gauge_theory_perturbative_expansion_architect.prompt.md)

## Pathology

- [Design a Robust Preclinical Pathology Study Protocol](prompts/scientific/pathology/pathology_study_workflow/01_study_protocol_outline.prompt.md)
- [Evaluate Device–Tissue Interface Findings](prompts/scientific/pathology/pathology_study_workflow/02_device_tissue_interface_evaluation.prompt.md)
- [Prepare Pathology Slides and Reporting Plan](prompts/scientific/pathology/pathology_study_workflow/03_slides_and_reporting_workflow.prompt.md)

## Philosophy

- [Natural Language Argument Formalizer](prompts/scientific/philosophy/logic/natural_language_argument_formalizer.prompt.md)
- [dialectical_metaphysical_synthesizer](prompts/scientific/philosophy/metaphysics/dialectical_metaphysical_synthesizer.prompt.md)
- [phenomenological_reduction_engine](prompts/scientific/philosophy/phenomenology/phenomenological_reduction_engine.prompt.md)

## Physical

- [Electrocatalytic Mechanism Architect](prompts/scientific/chemistry/physical/electrochemistry/electrocatalytic_mechanism_architect.prompt.md)
- [Microkinetic Modeling Architect](prompts/scientific/chemistry/physical/kinetics/microkinetic_modeling_architect.prompt.md)
- [Non-Ideal Fluid Phase Equilibria Architect](prompts/scientific/chemistry/physical/thermodynamics/non_ideal_fluid_phase_equilibria_architect.prompt.md)

## Physics

- [lattice_boltzmann_multiphase_architect](prompts/scientific/applied_mathematics/physics/fluid_dynamics/lattice_boltzmann_multiphase_architect.prompt.md)
- [BRST Quantization and Faddeev-Popov Ghost Architect](prompts/scientific/physics/quantum_field_theory/brst_quantization_faddeev_popov_architect.prompt.md)
- [Callan-Symanzik Beta Function Architect](prompts/scientific/physics/quantum_field_theory/callan_symanzik_beta_function_architect.prompt.md)
- [Chiral Anomaly Fujikawa Path Integral Architect](prompts/scientific/physics/quantum_field_theory/chiral_anomaly_fujikawa_path_integral_architect.prompt.md)
- [effective_field_theory_matching_rg_running_architect](prompts/scientific/physics/quantum_field_theory/effective_field_theory_matching_rg_running_architect.prompt.md)
- [Feynman Rule Derivation Architect](prompts/scientific/physics/quantum_field_theory/feynman_rule_derivation_architect.prompt.md)
- [Schwinger-Dyson Equation Architect](prompts/scientific/physics/quantum_field_theory/schwinger_dyson_equation_architect.prompt.md)
- [Schwinger-Keldysh Non-Equilibrium Path Integral Architect](prompts/scientific/physics/quantum_field_theory/schwinger_keldysh_non_equilibrium_path_integral_architect.prompt.md)
- [ads_cft_holographic_dictionary_architect](prompts/scientific/physics/string_theory/ads_cft_holographic_dictionary_architect.prompt.md)
- [string_worldsheet_scattering_amplitude_architect](prompts/scientific/physics/string_theory/string_worldsheet_scattering_amplitude_architect.prompt.md)

## Project Management

- [Project Charter and Scope Definition](prompts/management/project_management/project_management_workflow/01_project_charter_scope.prompt.md)
- [Comprehensive Risk Register and Mitigation Plan](prompts/management/project_management/project_management_workflow/02_risk_register_mitigation.prompt.md)
- [Weekly Executive Status Report](prompts/management/project_management/project_management_workflow/03_weekly_exec_status_report.prompt.md)
- [Detailed Project Blueprint and Timeline](prompts/management/project_management/project_management_workflow/04_detailed_project_blueprint_timeline.prompt.md)

## Protocol

- [Clinical-Trial Protocol Creator](prompts/clinical/protocol/protocol_workflow/01_clinical_trial_protocol_creator.prompt.md)
- [Ultimate SOP Architect](prompts/clinical/protocol/protocol_workflow/02_ultimate_sop_architect.prompt.md)
- [Protocol Reviewer and Gap-Analysis Coach](prompts/clinical/protocol/protocol_workflow/03_protocol_reviewer_gap_analysis_coach.prompt.md)
- [Protocol Section Refinement](prompts/clinical/protocol/protocol_workflow/04_protocol_section_refinement.prompt.md)
- [Protocol to USDM Stage 1 - Metadata](prompts/clinical/protocol/usdm_workflow/01_usdm_stage1_metadata.prompt.md)
- [Protocol to USDM Stage 2 - Rationale](prompts/clinical/protocol/usdm_workflow/02_usdm_stage2_rationale.prompt.md)
- [Protocol to USDM Stage 3 - Workflow](prompts/clinical/protocol/usdm_workflow/03_usdm_stage3_workflow.prompt.md)
- [Protocol to USDM Stage 4 - Concepts](prompts/clinical/protocol/usdm_workflow/04_usdm_stage4_concepts.prompt.md)
- [Protocol to USDM Stage 5 - Assembly](prompts/clinical/protocol/usdm_workflow/05_usdm_stage5_assembly.prompt.md)

## Psychology

- [structural_equation_modeling_architect](prompts/scientific/psychology/quantitative/structural_equation_modeling_architect.prompt.md)

## Public Economics

- [mirrleesian_optimal_income_tax_architect](prompts/scientific/economics/public_economics/optimal_tax_theory/mirrleesian_optimal_income_tax_architect.prompt.md)

## Quantitative

- [multifactorial_behavioral_intervention_architect](prompts/scientific/psychology/quantitative/experimental_design/multifactorial_behavioral_intervention_architect.prompt.md)
- [cognitive_diagnostic_modeling_architect](prompts/scientific/psychology/quantitative/psychometrics/cognitive_diagnostic_modeling_architect.prompt.md)
- [generalizability_theory_architect](prompts/scientific/psychology/quantitative/psychometrics/generalizability_theory_architect.prompt.md)
- [item_response_theory_dif_analyzer](prompts/scientific/psychology/quantitative/psychometrics/item_response_theory_dif_analyzer.prompt.md)
- [latent_profile_mixture_modeling_architect](prompts/scientific/psychology/quantitative/psychometrics/latent_profile_mixture_modeling_architect.prompt.md)
- [longitudinal_measurement_invariance_evaluator](prompts/scientific/psychology/quantitative/psychometrics/longitudinal_measurement_invariance_evaluator.prompt.md)
- [network_psychometrics_architect](prompts/scientific/psychology/quantitative/psychometrics/network_psychometrics_architect.prompt.md)

## Regulatory

- [ALCOA-C Data Integrity Checklist](prompts/regulatory/adherence/alcoa_c_data_integrity_checklist.prompt.md)
- [DHT Integration Regulatory Checklist](prompts/regulatory/adherence/dht_integration_checklist.prompt.md)
- [ICH E9(R1) Estimand Builder](prompts/regulatory/adherence/estimand_framework_builder.prompt.md)
- [Human Factors/Usability Summary](prompts/regulatory/adherence/human_factors_usability_summary.prompt.md)
- [Imaging Endpoint Process Standards Checklist](prompts/regulatory/adherence/imaging_endpoint_process_standards.prompt.md)
- [Informed Consent Exception (Emergency)](prompts/regulatory/adherence/informed_consent_exception_emergency.prompt.md)
- [Intended Use and Indications for Use Alignment](prompts/regulatory/adherence/intended_use_and_indications_for_use_alignment.prompt.md)
- [Multiple Endpoints Regulatory Strategy](prompts/regulatory/adherence/multiple_endpoints_guidance_review.prompt.md)
- [Off-Label Information Dissemination](prompts/regulatory/adherence/off_label_information_dissemination.prompt.md)
- [RWE Regulatory Framework Summary](prompts/regulatory/adherence/rwe_framework_summary.prompt.md)
- [Shelf-life Study Rationale](prompts/regulatory/adherence/shelf_life_study_rationale.prompt.md)
- [21 CFR Part 14 Auditing](prompts/regulatory/administrative/21_cfr_part_14_auditing.prompt.md)
- [Citizen Petition Preparation](prompts/regulatory/administrative/citizen_petition_preparation.prompt.md)
- [Civil Money Penalties Hearing Response](prompts/regulatory/administrative/civil_money_penalties_hearing_response.prompt.md)
- [Financial Disclosure Certification](prompts/regulatory/administrative/financial_disclosure_certification.prompt.md)
- [Freedom of Information Act (FOIA) Request](prompts/regulatory/administrative/freedom_of_information_act_foia_request.prompt.md)
- [Import Entry Data Element Compilation](prompts/regulatory/administrative/import_entry_data_element_compilation.prompt.md)
- [Medical Device Administrative Detention Appeal](prompts/regulatory/administrative/medical_device_administrative_detention_appeal.prompt.md)
- [Patent Term Restoration Eligibility](prompts/regulatory/administrative/patent_term_restoration_eligibility.prompt.md)
- [Privacy Act Auditing](prompts/regulatory/administrative/privacy_act_auditing.prompt.md)
- [Public Hearing Participation](prompts/regulatory/administrative/public_hearing_participation.prompt.md)
- [Reclassification Petitioning](prompts/regulatory/administrative/reclassification_petitioning.prompt.md)
- [Correction and Removal Reporting](prompts/regulatory/compliance/correction_and_removal_reporting.prompt.md)
- [Cyber Device Security Plan](prompts/regulatory/compliance/cyber_device_security_plan.prompt.md)
- [IRB Protocol Review](prompts/regulatory/compliance/irb_protocol_review.prompt.md)
- [Labeling Compliance Audit](prompts/regulatory/compliance/labeling_compliance_audit.prompt.md)
- [Medical Device Recall Strategy](prompts/regulatory/compliance/medical_device_recall_strategy.prompt.md)
- [Medical Device Reporting (MDR)](prompts/regulatory/compliance/medical_device_reporting_mdr.prompt.md)
- [Automated Image Assessment System 510(k)](prompts/regulatory/device_specifics/automated_image_assessment_system_510_k.prompt.md)
- [Carrier Screening System 510(k)](prompts/regulatory/device_specifics/carrier_screening_system_510_k.prompt.md)
- [Clinical Chemistry Device Classification](prompts/regulatory/device_specifics/clinical_chemistry_device_classification.prompt.md)
- [companion_diagnostic_analytical_validation_architect](prompts/regulatory/device_specifics/companion_diagnostic_analytical_validation_architect.prompt.md)
- [Design Verification for BCR-ABL Tests](prompts/regulatory/device_specifics/design_verification_for_bcr_abl_tests.prompt.md)
- [iCGM Clinical Testing Strategy](prompts/regulatory/device_specifics/icgm_clinical_testing_strategy.prompt.md)
- [NGS Tumor Profiling Documentation](prompts/regulatory/device_specifics/ngs_tumor_profiling_documentation.prompt.md)
- [Special Controls Labeling Compliance](prompts/regulatory/device_specifics/special_controls_labeling_compliance.prompt.md)
- [Zika Virus Reagent Study Design](prompts/regulatory/device_specifics/zika_virus_reagent_study_design.prompt.md)
- [Directed Food Laboratory Order Verification](prompts/regulatory/food_safety/directed_food_laboratory_order_verification.prompt.md)
- [Establishment of Food Traceability Plan](prompts/regulatory/food_safety/establishment_of_food_traceability_plan.prompt.md)
- [Food Safety Audit Reporting (Regulatory)](prompts/regulatory/food_safety/food_safety_audit_reporting_regulatory.prompt.md)
- [Foreign Supplier Verification Program (FSVP) Audit](prompts/regulatory/food_safety/foreign_supplier_verification_program_fsvp_audit.prompt.md)
- [AI/ML Predetermined Change Control Plan Architect](prompts/regulatory/quality/ai_ml_predetermined_change_control_plan_architect.prompt.md)
- [CAPA Investigation Report Writer](prompts/regulatory/quality/capa_investigation_report_writer.prompt.md)
- [CAPA Management Process](prompts/regulatory/quality/capa_management_process.prompt.md)
- [CAPA Plan Generator](prompts/regulatory/quality/capa_plan_generator.prompt.md)
- [capa_root_cause_analysis_architect](prompts/regulatory/quality/capa_root_cause_analysis_architect.prompt.md)
- [CAPA Root Cause Investigator](prompts/regulatory/quality/capa_root_cause_investigator.prompt.md)
- [capa_root_cause_resolution_architect](prompts/regulatory/quality/capa_root_cause_resolution_architect.prompt.md)
- [CAPA SOP Architect](prompts/regulatory/quality/capa_sop_architect.prompt.md)
- [cer_literature_review_architect](prompts/regulatory/quality/cer_literature_review_architect.prompt.md)
- [Change Control Regulatory Impact Assessor](prompts/regulatory/quality/change_control_regulatory_impact_assessor.prompt.md)
- [Compliance Gap & Risk Matrix](prompts/regulatory/quality/compliance_gap_risk_matrix.prompt.md)
- [Data Integrity ALCOA+ Audit Architect](prompts/regulatory/quality/data_integrity_alcoa_plus_audit_architect.prompt.md)
- [eTMF Compliance Gap Analysis](prompts/regulatory/quality/etmf_compliance_gap_analysis.prompt.md)
- [EU IVDR Performance Evaluation Report Architect](prompts/regulatory/quality/eu_ivdr_performance_evaluation_report_architect.prompt.md)
- [EU MDR Clinical Evaluation Report Architect](prompts/regulatory/quality/eu_mdr_clinical_evaluation_report_architect.prompt.md)
- [EU MDR PMCF Plan Architect](prompts/regulatory/quality/eu_mdr_pmcf_plan_architect.prompt.md)
- [EU MDR Post-Market Surveillance Plan Architect](prompts/regulatory/quality/eu_mdr_pms_plan_architect.prompt.md)
- [EU MDR PSUR Architect](prompts/regulatory/quality/eu_mdr_psur_architect.prompt.md)
- [eu_mdr_sscp_architect](prompts/regulatory/quality/eu_mdr_sscp_architect.prompt.md)
- [Financial Conflict of Interest (FCOI) Reporting](prompts/regulatory/quality/fcoi_reporting.prompt.md)
- [FDA 483 Response Strategist](prompts/regulatory/quality/fda_483_response_strategist.prompt.md)
- [fda_483_warning_letter_remediation_architect](prompts/regulatory/quality/fda_483_warning_letter_remediation_architect.prompt.md)
- [fda_510k_substantial_equivalence_architect](prompts/regulatory/quality/fda_510k_substantial_equivalence_architect.prompt.md)
- [FDA Breakthrough Device Designation Architect](prompts/regulatory/quality/fda_breakthrough_device_designation_architect.prompt.md)
- [FDA CSA Risk-Based Testing Strategy Architect](prompts/regulatory/quality/fda_csa_risk_based_testing_strategy_architect.prompt.md)
- [fda_de_novo_classification_request_architect](prompts/regulatory/quality/fda_de_novo_classification_request_architect.prompt.md)
- [FDA OOS Investigation Architect](prompts/regulatory/quality/fda_oos_investigation_architect.prompt.md)
- [fda_q_submission_pre_sub_meeting_package_architect](prompts/regulatory/quality/fda_q_submission_pre_sub_meeting_package_architect.prompt.md)
- [GLP Quality Assurance](prompts/regulatory/quality/glp_quality_assurance.prompt.md)
- [iec_62304_soup_anomaly_evaluator](prompts/regulatory/quality/iec_62304_soup_anomaly_evaluator.prompt.md)
- [IEC 62366-1 Summative Usability Evaluation Protocol Architect](prompts/regulatory/quality/iec_62366_summative_usability_protocol_architect.prompt.md)
- [Inspection-Readiness Drill (CAPA Builder)](prompts/regulatory/quality/inspection_readiness_drill_capa_builder.prompt.md)
- [Integrated Submission Strategy Coach](prompts/regulatory/quality/integrated_submission_strategy_coach.prompt.md)
- [ISO 10993 Biological Evaluation Plan Architect](prompts/regulatory/quality/iso_10993_biological_evaluation_plan_architect.prompt.md)
- [MDSAP Nonconformity Grading Evaluator](prompts/regulatory/quality/mdsap_nonconformity_grading_evaluator.prompt.md)
- [Medical Device Recall Strategy Architect](prompts/regulatory/quality/medical_device_recall_strategy_architect.prompt.md)
- [Medical Device Reporting (MDR) and Vigilance Decision Evaluator](prompts/regulatory/quality/medical_device_reporting_decision_evaluator.prompt.md)
- [Part 11 Closed System Audit](prompts/regulatory/quality/part_11_closed_system_audit.prompt.md)
- [Process Validation IQ/OQ/PQ Protocol Architect](prompts/regulatory/quality/process_validation_iq_oq_pq_protocol_architect.prompt.md)
- [qms_management_review_architect](prompts/regulatory/quality/qms_management_review_architect.prompt.md)
- [Quality-Improvement RCA & Action Plan](prompts/regulatory/quality/quality_improvement_rca_action_plan.prompt.md)
- [Quality System Audit](prompts/regulatory/quality/quality_system_audit.prompt.md)
- [Quality System Evaluation (MRA)](prompts/regulatory/quality/quality_system_evaluation_mra.prompt.md)
- [regulatory_compliance_automation_architect](prompts/regulatory/quality/regulatory_compliance_automation_architect.prompt.md)
- [Regulatory-Landscape Radar](prompts/regulatory/quality/regulatory_landscape_radar.prompt.md)
- [Regulatory Radar & Impact Report](prompts/regulatory/quality/regulatory_radar.prompt.md)
- [Risk-Based Quality Management Plan](prompts/regulatory/quality/risk_based_quality_management_plan.prompt.md)
- [Risk Management Analysis](prompts/regulatory/quality/risk_management_analysis.prompt.md)
- [SaMD Cybersecurity Vulnerability Assessor](prompts/regulatory/quality/samd_cybersecurity_vulnerability_assessor.prompt.md)
- [samd_hazard_traceability_matrix_generator](prompts/regulatory/quality/samd_hazard_traceability_matrix_generator.prompt.md)
- [samd_iec62304_software_architecture_architect](prompts/regulatory/quality/samd_iec62304_software_architecture_architect.prompt.md)
- [samd_iec_62304_software_safety_classification_architect](prompts/regulatory/quality/samd_iec_62304_software_safety_classification_architect.prompt.md)
- [Supplier Corrective Action Request Evaluator](prompts/regulatory/quality/supplier_corrective_action_request_evaluator.prompt.md)
- [Supplier Quality Agreement Architect](prompts/regulatory/quality/supplier_quality_agreement_architect.prompt.md)
- [510(k)/De Novo Pre-Submission Strategy](prompts/regulatory/strategy/510k_pre-sub_strategy.prompt.md)
- [AI Risk Mapper](prompts/regulatory/strategy/ai_risk_mapper.prompt.md)
- [Breakthrough Device Designation Architect](prompts/regulatory/strategy/breakthrough_device_designation_architect.prompt.md)
- [ClinicalTrials.gov Registration](prompts/regulatory/strategy/clinicaltrials_registration.prompt.md)
- [Compliance Gap Assessment](prompts/regulatory/strategy/compliance_gap_assessment.prompt.md)
- [Dual MDR / IVDR Conformity-Assessment Roadmap](prompts/regulatory/strategy/dual_mdr_ivdr_roadmap.prompt.md)
- [EU MDR Technical-Documentation Gap Assessment](prompts/regulatory/strategy/eu_mdr_gap_assessment.prompt.md)
- [FDA Fast Track Designation Architect](prompts/regulatory/strategy/fda_fast_track_designation_architect.prompt.md)
- [IDE Determination and Device Classification](prompts/regulatory/strategy/ide_determination.prompt.md)
- [IND Determination and Application](prompts/regulatory/strategy/ind_determination_application.prompt.md)
- [IND Readiness Gap Analysis & Filing Road-Map](prompts/regulatory/strategy/ind_readiness_gap_analysis.prompt.md)
- [IVD Performance Study Compliance Review](prompts/regulatory/strategy/ivd_performance_study_compliance_review.prompt.md)
- [IVDR Performance-Evaluation Plan Blueprint](prompts/regulatory/strategy/ivdr_pep_blueprint.prompt.md)
- [Literature & Regulatory Gap Analysis](prompts/regulatory/strategy/literature_regulatory_gap_analysis.prompt.md)
- [Orphan Drug Designation Architect](prompts/regulatory/strategy/orphan_drug_designation_architect.prompt.md)
- [Pre-IND Meeting Preparation](prompts/regulatory/strategy/pre_ind_meeting_preparation.prompt.md)
- [Prompt-Writing Best-Practice Checklist](prompts/regulatory/strategy/prompt_best_practices.prompt.md)
- [21 CFR 820 / QMSR Gap-Analysis & Remediation](prompts/regulatory/strategy/qmsr_gap_analysis.prompt.md)
- [RA/QA Integrated Quality System Audit](prompts/regulatory/strategy/raqa_integrated_quality_system_audit.prompt.md)
- [Regenerative Medicine Advanced Therapy RMAT Designation Architect](prompts/regulatory/strategy/regenerative_medicine_advanced_therapy_rmat_designation_architect.prompt.md)
- [Regulatory-Change Impact Analysis](prompts/regulatory/strategy/regulatory_change_impact_analysis.prompt.md)
- [Regulatory Filing Draft Builder](prompts/regulatory/strategy/regulatory_filing_draft_builder.prompt.md)
- [Request for Designation (RFD) Submission](prompts/regulatory/strategy/rfd_submission.prompt.md)
- [SaMD AI/ML PCCP Architect](prompts/regulatory/strategy/samd_ai_pccp_architect.prompt.md)
- [Strategic Regulatory Pathway Plan](prompts/regulatory/strategy/strategic_regulatory_pathway_plan.prompt.md)
- [510(k) Substantial Equivalence Preparation](prompts/regulatory/submissions/510_k_substantial_equivalence_preparation.prompt.md)
- [Biologics License Application (BLA) Architect](prompts/regulatory/submissions/biologics_license_application_bla_architect.prompt.md)
- [Combination Product Jurisdiction](prompts/regulatory/submissions/combination_product_jurisdiction.prompt.md)
- [De Novo Request Preparation](prompts/regulatory/submissions/de_novo_request_preparation.prompt.md)
- [EU MDR Technical Documentation Architect](prompts/regulatory/submissions/eu_mdr_technical_documentation_architect.prompt.md)
- [Humanitarian Device Exemption (HDE)](prompts/regulatory/submissions/humanitarian_device_exemption_hde.prompt.md)
- [ich_m4e_ctd_clinical_overview_architect](prompts/regulatory/submissions/ich_m4e_ctd_clinical_overview_architect.prompt.md)
- [IDE Application Preparation](prompts/regulatory/submissions/ide_application_preparation.prompt.md)
- [Investigational New Drug (IND) Architect](prompts/regulatory/submissions/investigational_new_drug_ind_architect.prompt.md)
- [Medicare Coverage Request (IDE)](prompts/regulatory/submissions/medicare_coverage_request_ide.prompt.md)
- [Parallel Review Request](prompts/regulatory/submissions/parallel_review_request.prompt.md)
- [PMA Post-approval Reporting](prompts/regulatory/submissions/pma_post_approval_reporting.prompt.md)
- [PMA Supplement (CBE)](prompts/regulatory/submissions/pma_supplement_cbe.prompt.md)
- [Premarket Approval (PMA) Preparation](prompts/regulatory/submissions/premarket_approval_pma_preparation.prompt.md)
- [RTA Checklist Preparation](prompts/regulatory/submissions/rta_checklist_preparation.prompt.md)
- [UDI GUDID Submission](prompts/regulatory/submissions/udi_gudid_submission.prompt.md)

## Relativity

- [ADM 3+1 Decomposition Architect](prompts/scientific/physics/relativity/general_relativity/adm_3_plus_1_decomposition_architect.prompt.md)
- [adm_spacetime_decomposition_architect](prompts/scientific/physics/relativity/general_relativity/adm_spacetime_decomposition_architect.prompt.md)
- [Black Hole Perturbation Teukolsky Architect](prompts/scientific/physics/relativity/general_relativity/black_hole_perturbation_teukolsky_architect.prompt.md)

## Rtsm

- [Design a Patient-Centered Randomization Scheme](prompts/clinical/rtsm/rtsm_workflow/01_patient_centered_randomization_scheme.prompt.md)
- [Forecast Site-Level Drug Supply & Resupply Strategy](prompts/clinical/rtsm/rtsm_workflow/02_site_level_supply_resupply_strategy.prompt.md)
- [Create a Risk-Based Monitoring & Mitigation SOP for RTSM](prompts/clinical/rtsm/rtsm_workflow/03_risk_based_monitoring_sop.prompt.md)

## Safety

- [Clinical Safety Synopsis for EU MDR CER](prompts/clinical/safety/clinical_safety_workflow/01_eu_cer_clinical_safety_synopsis.prompt.md)
- [FDA MDR/MDV Adverse-Event Narrative](prompts/clinical/safety/clinical_safety_workflow/02_fda_mdr_adverse_event_narrative.prompt.md)
- [Post-Market Safety Signal Trending](prompts/clinical/safety/clinical_safety_workflow/03_post_market_safety_signal_trending.prompt.md)

## Scientific

- [Biological Evaluation Plan Builder](prompts/scientific/biosafety/bep_builder.prompt.md)
- [Chemical Characterization & TRA Work Plan](prompts/scientific/biosafety/chemical_characterization_work_plan.prompt.md)
- [Comprehensive Biocompatibility Test Matrix](prompts/scientific/biosafety/comprehensive_test_matrix.prompt.md)
- [Adaptive Design & Interim Monitoring](prompts/scientific/biostatistics/adaptive_design_interim_monitoring.prompt.md)
- [Dual-Language Figure Prompt](prompts/scientific/biostatistics/dual_language_figure_prompt.prompt.md)
- [Dunnett Adjustment R Code Generator](prompts/scientific/biostatistics/dunnett_adjustment_calculator.prompt.md)
- [FDA Missing-Data Query Response](prompts/scientific/biostatistics/fda_missing_data_query_response.prompt.md)
- [FWER Gatekeeping Procedure Code Generator](prompts/scientific/biostatistics/fwer_gatekeeping_procedures.prompt.md)
- [Inclusion/Exclusion, Endpoints & Sample-Size Deep Dive](prompts/scientific/biostatistics/inclusion_exclusion_endpoints_sample_size.prompt.md)
- [Multiplicity Adjustment Code Generator](prompts/scientific/biostatistics/multiplicity_adjustments_calculator.prompt.md)
- [Peer-Review Checklist for Manuscript Methods](prompts/scientific/biostatistics/peer_review_methods_checklist.prompt.md)
- [Phase II/III SAP Skeleton](prompts/scientific/biostatistics/phase_ii_iii_sap_skeleton.prompt.md)
- [QC Listing & Cross-check Prompt](prompts/scientific/biostatistics/qc_listing_cross_check_prompt.prompt.md)
- [Sample-Size & Randomization Strategy](prompts/scientific/biostatistics/sample_size_randomization_strategy.prompt.md)
- [Statistical Analysis Plan (SAP) Development](prompts/scientific/biostatistics/sap_development.prompt.md)
- [Secondary Endpoint Multiplicity Adjuster](prompts/scientific/biostatistics/secondary_endpoint_multiplicity.prompt.md)
- [Statistical Analysis Plan Generator](prompts/scientific/biostatistics/statistical_analysis_plan_generator.prompt.md)
- [Study Design and Statistical Approach](prompts/scientific/biostatistics/study_design_statistical_approach.prompt.md)
- [Submission-Ready Statistical Analysis Plan](prompts/scientific/biostatistics/submission_ready_sap.prompt.md)
- [Generate & QC Submission-Ready TLFs](prompts/scientific/biostatistics/submission_ready_tlfs.prompt.md)
- [Time-to-Event Analysis Coach](prompts/scientific/biostatistics/time_to_event_analysis_coach.prompt.md)
- [Universal Template-Table Prompt](prompts/scientific/biostatistics/universal_template_table_prompt.prompt.md)
- [ClinRO User Manual Generator](prompts/scientific/coa/clinro_training_manual.prompt.md)
- [Content Validity & Reliability Analysis](prompts/scientific/coa/content_validity_clinician_input.prompt.md)
- [ePRO Migration Equivalence Checker](prompts/scientific/coa/epro_migration_equivalence.prompt.md)
- [MCID Research and Summary](prompts/scientific/coa/mcid_definition.prompt.md)
- [Psychometric Validation Methodology](prompts/scientific/coa/psychometric_validation_methods.prompt.md)
- [Qualitative Interview Guide Generator](prompts/scientific/coa/qualitative_interview_guide.prompt.md)
- [crispr_cas9_off_target_probabilistic_modeler](prompts/scientific/computational_biology/crispr_cas9_off_target_probabilistic_modeler.prompt.md)
- [molecular_dynamics_simulation_architect](prompts/scientific/computational_biology/molecular_dynamics_simulation_architect.prompt.md)
- [multi_omics_data_integration_architect](prompts/scientific/computational_biology/multi_omics_data_integration_architect.prompt.md)
- [stochastic_gene_regulatory_network_cme_architect](prompts/scientific/computational_biology/stochastic_gene_regulatory_network_cme_architect.prompt.md)
- [astrocytic_tripartite_synapse_architect](prompts/scientific/computational_theoretical_neuroscience/astrocytic_tripartite_synapse_architect.prompt.md)
- [basal_ganglia_td_learning_architect](prompts/scientific/computational_theoretical_neuroscience/basal_ganglia_td_learning_architect.prompt.md)
- [biophysical_hodgkin_huxley_modeler](prompts/scientific/computational_theoretical_neuroscience/biophysical_hodgkin_huxley_modeler.prompt.md)
- [deep_brain_stimulation_biophysical_architect](prompts/scientific/computational_theoretical_neuroscience/deep_brain_stimulation_biophysical_architect.prompt.md)
- [dendritic_cable_theory_computation_architect](prompts/scientific/computational_theoretical_neuroscience/dendritic_cable_theory_computation_architect.prompt.md)
- [Dynamic Causal Modeling Architect](prompts/scientific/computational_theoretical_neuroscience/dynamic_causal_modeling_architect.prompt.md)
- [fokker_planck_population_dynamics_architect](prompts/scientific/computational_theoretical_neuroscience/fokker_planck_population_dynamics_architect.prompt.md)
- [free_energy_principle_active_inference_architect](prompts/scientific/computational_theoretical_neuroscience/free_energy_principle_active_inference_architect.prompt.md)
- [graph_theoretical_connectome_analyzer](prompts/scientific/computational_theoretical_neuroscience/graph_theoretical_connectome_analyzer.prompt.md)
- [hodgkin_huxley_biophysical_modeler](prompts/scientific/computational_theoretical_neuroscience/hodgkin_huxley_biophysical_modeler.prompt.md)
- [multi_modal_fmri_eeg_integration_architect](prompts/scientific/computational_theoretical_neuroscience/multi_modal_fmri_eeg_integration_architect.prompt.md)
- [neural_field_theory_spatiotemporal_dynamics_architect](prompts/scientific/computational_theoretical_neuroscience/neural_field_theory_spatiotemporal_dynamics_architect.prompt.md)
- [neural_manifold_state_space_analyzer](prompts/scientific/computational_theoretical_neuroscience/neural_manifold_state_space_analyzer.prompt.md)
- [neuromorphic_spiking_network_biophysical_architect](prompts/scientific/computational_theoretical_neuroscience/neuromorphic_spiking_network_biophysical_architect.prompt.md)
- [optogenetic_photocurrent_biophysical_modeler](prompts/scientific/computational_theoretical_neuroscience/optogenetic_photocurrent_biophysical_modeler.prompt.md)
- [synaptic_plasticity_weight_update_architect](prompts/scientific/computational_theoretical_neuroscience/synaptic_plasticity_weight_update_architect.prompt.md)
- [whole_brain_biophysical_network_simulator](prompts/scientific/computational_theoretical_neuroscience/whole_brain_biophysical_network_simulator.prompt.md)
- [Clinical Study Report (CSR) Writing](prompts/scientific/medical_writing/csr_writing.prompt.md)
- [investigators_brochure_synthesis_architect](prompts/scientific/medical_writing/investigators_brochure_synthesis_architect.prompt.md)

## Security

- [Identity Threat Detection and Response Architect](prompts/technical/security/iam_security/identity_threat_detection_response_architect.prompt.md)
- [Non-Human Identity Lifecycle Architect](prompts/technical/security/iam_security/non_human_identity_lifecycle_architect.prompt.md)
- [Zero Trust Privileged Access Management Architect](prompts/technical/security/iam_security/zero_trust_pam_architect.prompt.md)
- [Advanced Sigma Rule Detection Architect](prompts/technical/security/secops/advanced_sigma_rule_detection_architect.prompt.md)
- [Advanced SOAR Playbook Engineering Architect](prompts/technical/security/secops/advanced_soar_playbook_engineering_architect.prompt.md)
- [APT Threat Hunting Hypothesis Generation Architect](prompts/technical/security/secops/apt_threat_hypothesis_generation_architect.prompt.md)
- [Cloud Identity Fabric Threat Hunting Architect](prompts/technical/security/secops/cloud_identity_fabric_threat_hunting_architect.prompt.md)
- [Firmware and UEFI Bootkit Forensics Analyst](prompts/technical/security/secops/firmware_uefi_bootkit_forensics_analyst.prompt.md)
- [Forensic Super Timeline Analysis Architect](prompts/technical/security/secops/forensic_super_timeline_analysis_architect.prompt.md)
- [Living-off-the-Land Behavioral SIEM Query Architect](prompts/technical/security/secops/lotl_behavioral_siem_query_architect.prompt.md)
- [macOS ESF Unified Logging Threat Hunter](prompts/technical/security/secops/macos_esf_unified_logging_threat_hunter.prompt.md)
- [Threat Intelligence Fusion Attribution Architect](prompts/technical/security/secops/threat_intelligence_fusion_attribution_architect.prompt.md)

## Site Acquisition

- [Site Landscape Mapping & Prioritization](prompts/clinical/site_acquisition/site_acquisition_workflow/01_site_landscape_mapping.prompt.md)
- [Tailored Feasibility-Questionnaire Builder](prompts/clinical/site_acquisition/site_acquisition_workflow/02_tailored_feasibility_questionnaire.prompt.md)
- [Personalized Investigator-Outreach Email Generator](prompts/clinical/site_acquisition/site_acquisition_workflow/03_investigator_outreach_email_generator.prompt.md)

## Sociology

- [intergenerational_social_mobility_markov_modeler](prompts/scientific/sociology/demography/intergenerational_social_mobility_markov_modeler.prompt.md)
- [residential_segregation_spatial_inequality_modeler](prompts/scientific/sociology/demography/residential_segregation_spatial_inequality_modeler.prompt.md)
- [institutional_isomorphism_lifecycle_modeler](prompts/scientific/sociology/institutions/institutional_isomorphism_lifecycle_modeler.prompt.md)
- [collective_panic_cascade_architect](prompts/scientific/sociology/mass_behavior/collective_panic_cascade_architect.prompt.md)
- [institutional_trust_hemorrhage_modeler](prompts/scientific/sociology/mass_behavior/institutional_trust_hemorrhage_modeler.prompt.md)
- [intergenerational_mobility_modeler](prompts/scientific/sociology/stratification/intergenerational_mobility_modeler.prompt.md)
- [intersectional_stratification_mechanism_modeler](prompts/scientific/sociology/stratification/intersectional_stratification_mechanism_modeler.prompt.md)

## Software Engineering

- [Coding Session Guidelines](prompts/technical/software_engineering/lifecycle/coding_session_guidelines.prompt.md)
- [E2E Test Discovery Lifecycle Template](prompts/technical/software_engineering/lifecycle/e2e_test_discovery.prompt.md)
- [Folder and Module Organization](prompts/technical/software_engineering/lifecycle/folder_module_organization.prompt.md)
- [Project Memory Notes](prompts/technical/software_engineering/lifecycle/project_memory.prompt.md)
- [Project Review Checklist](prompts/technical/software_engineering/lifecycle/project_review.prompt.md)
- [Reflexion Agent Bug Patch](prompts/technical/software_engineering/lifecycle/reflexion_agent_bug_patch.prompt.md)
- [RequirementsBot Prompt](prompts/technical/software_engineering/lifecycle/requirements_prompt.prompt.md)
- [Technical Implementation Plan](prompts/technical/software_engineering/lifecycle/technical_implementation_plan.prompt.md)
- [To-Do List Template](prompts/technical/software_engineering/lifecycle/todo_generation.prompt.md)
- [Test Architect (Automated Testing)](prompts/technical/software_engineering/tasks/add_tests.prompt.md)
- [Architecture Flow & Diagram Architect](prompts/technical/software_engineering/tasks/architecture_flow.prompt.md)
- [Bug Finder & Fixer (OpenAI Codex)](prompts/technical/software_engineering/tasks/bug_fix.prompt.md)
- [Continuous Integration & Delivery (DevOps Architect)](prompts/technical/software_engineering/tasks/ci_cd.prompt.md)
- [Code Review Assistant (Aegis Security)](prompts/technical/software_engineering/tasks/code_review.prompt.md)
- [Codebase Testing Plan](prompts/technical/software_engineering/tasks/codebase_testing_plan.prompt.md)
- [GitHub Custom Agent Creator](prompts/technical/software_engineering/tasks/create_github_agent.prompt.md)
- [DevEx Documentation Architect](prompts/technical/software_engineering/tasks/docs_and_onboarding.prompt.md)
- [Principal Architect Task Execution](prompts/technical/software_engineering/tasks/principal_architect.prompt.md)
- [Project Init & Skeleton (Construct Architect)](prompts/technical/software_engineering/tasks/project_init.prompt.md)
- [Retrieval-Augmented Answer Composer](prompts/technical/software_engineering/tasks/rag_composer.prompt.md)
- [Refactoring Architect](prompts/technical/software_engineering/tasks/refactoring_suggestions.prompt.md)
- [Security Vulnerability Hunt (Aegis)](prompts/technical/software_engineering/tasks/security_vulnerability.prompt.md)
- [Tooling & Quality Gates (DevEx Architect)](prompts/technical/software_engineering/tasks/tooling_and_quality.prompt.md)
- [UI Tweak & Verification (Aegis Security)](prompts/technical/software_engineering/tasks/ui_fix.prompt.md)

## Speculative

- [Abyssal-Gothic Liquidity Router](prompts/speculative/abyssal_gothic_liquidity_routing/abyssal_gothic_liquidity_router.prompt.md)
- [Abyssal Neumatic Consensus Architect](prompts/speculative/abyssal_neumatic_consensus_architect.prompt.md)
- [abyssal_society_cryptographer](prompts/speculative/abyssal_society_cryptographer.prompt.md)
- [Aerotectonic HFT Routing Architect](prompts/speculative/aerotectonic_hft_routing_architect.prompt.md)
- [benthic_contrapuntal_supply_chain_harmonizer](prompts/speculative/benthic_contrapuntal_supply_chain_harmonizer/benthic_contrapuntal_supply_chain_harmonizer.prompt.md)
- [Byzantine Chromodynamic Flocculation Architect](prompts/speculative/byzantine_chromodynamic_flocculation_architect/byzantine_chromodynamic_flocculation_architect.prompt.md)
- [Cetacean Origami Sharding Architect](prompts/speculative/cetacean_origami_sharding/cetacean_origami_sharding_architect.prompt.md)
- [choreographic_zk_agronomist](prompts/speculative/choreographic_zk_agronomist/choreographic_zk_agronomist.prompt.md)
- [Temporal Syntax Debugger](prompts/speculative/chrono_linguistic_debugging/temporal_syntax_debugger.prompt.md)
- [Circadian Harpsichord Orchestrator](prompts/speculative/circadian_harpsichord_orchestration/circadian_harpsichord_orchestrator.prompt.md)
- [Dendro-Balletic BGP Choreographer](prompts/speculative/dendro_balletic_bgp_choreography/dendro_balletic_bgp_choreographer.prompt.md)
- [endocrine_cobol_botanical_orchestrator](prompts/speculative/endocrine_cobol_botanical_orchestration/endocrine_cobol_botanical_orchestrator.prompt.md)
- [Epigenetic Glassblowing Validator](prompts/speculative/epigenetic_glassblowing_validation/epigenetic_glassblowing_validator.prompt.md)
- [Epistolary Brane E-Waste Architect](prompts/speculative/epistolary_brane_ewaste_architect.prompt.md)
- [Event Horizon Choreographic Auditor](prompts/speculative/event_horizon_choreographic_auditor/event_horizon_choreographic_auditor.prompt.md)
- [Fresco Epidemiological Auditor](prompts/speculative/fresco_epidemiological_auditor/fresco_epidemiological_auditor.prompt.md)
- [glacial_typographic_zk_architect](prompts/speculative/glacial_typographic_zk_architect/glacial_typographic_zk_architect.prompt.md)
- [Gregorian-Fluid Autoscaler](prompts/speculative/gregorian_fluid_autoscaling/gregorian_fluid_autoscaler.prompt.md)
- [hohmann_viennoiserie_pod_architect](prompts/speculative/hohmann_viennoiserie_pod_architect/hohmann_viennoiserie_pod_architect.prompt.md)
- [Hyperbolic Fermentation RL Architect](prompts/speculative/hyperbolic_fermentation_rl_architect.prompt.md)
- [Zero-G Algorithmic Biopigment Curator](prompts/speculative/intersection/suborbital_biopigment_algorithmic_curator.prompt.md)
- [magnetohydrodynamic_polyphonic_logistics_architect](prompts/speculative/magnetohydrodynamic_polyphonic_logistics_architect.prompt.md)
- [microbial_steganography_diplomat](prompts/speculative/microbial_steganography_diplomat/microbial_steganography_diplomat.prompt.md)
- [Mycelial Aristocrat HFT Router](prompts/speculative/mycelial_aristocrat_hft_routing/mycelial_aristocrat_hft_router.prompt.md)
- [mycelial_orbital_logistics_architect](prompts/speculative/mycelial_orbital_logistics/mycelial_orbital_logistics_architect.prompt.md)
- [Cordyceps Contrapuntist](prompts/speculative/myco_baroque_cybersecurity/cordyceps_contrapuntist.prompt.md)
- [orbital_fermentation_arbitrageur](prompts/speculative/orbital_fermentation_arbitrageur/orbital_fermentation_arbitrageur.prompt.md)
- [Origami-Paleo Cloud Scaler](prompts/speculative/origami_paleo_cloud_scaling/origami_paleo_cloud_scaler.prompt.md)
- [polyphonic_astrobotanical_harmoniser](prompts/speculative/polyphonic_astrobotanical_harmoniser/polyphonic_astrobotanical_harmoniser.prompt.md)
- [Pulsar Fermentation Rate Limiting Architect](prompts/speculative/pulsar_fermentation_rate_limiting/pulsar_fermentation_rate_limiter.prompt.md)
- [qcd_chanoyu_autoscaler](prompts/speculative/qcd_chanoyu_autoscaler.prompt.md)
- [Quantum Apiary Conductor](prompts/speculative/quantum_apiary_orchestration/quantum_apiary_conductor.prompt.md)
- [quantum_epistolary_waste_architect](prompts/speculative/quantum_epistolary_waste_architect/quantum_epistolary_waste_architect.prompt.md)
- [quantum_gothic_waste_optimiser](prompts/speculative/quantum_gothic_waste_optimiser/quantum_gothic_waste_optimiser.prompt.md)
- [Quantum Horological Wastewater Architect](prompts/speculative/quantum_horological_wastewater_architect.prompt.md)
- [Quantum Olfactory Retention Architect](prompts/speculative/quantum_olfactory_retention_architect.prompt.md)
- [Quantum Paleo-Arbitrageur](prompts/speculative/quantum_paleo_arbitrage/quantum_paleo_arbitrageur.prompt.md)
- [Quantum Poetic Leachate Optimizer](prompts/speculative/quantum_poetic_leachate_optimization/quantum_poetic_leachate_optimizer.prompt.md)
- [Quantum Poetic Waste Architect](prompts/speculative/quantum_poetic_waste_architect/quantum_poetic_waste_architect.prompt.md)
- [quantum_victorian_traffic_warden_architect](prompts/speculative/quantum_victorian_traffic_warden.prompt.md)
- [quantum_zymurgy_astrogator](prompts/speculative/quantum_zymurgy_astrogator/quantum_zymurgy_astrogator.prompt.md)
- [tectonic_horological_restructuring_architect](prompts/speculative/tectonic_horological_restructuring_architect/tectonic_horological_restructuring_architect.prompt.md)
- [Tectonic Viennoiserie Cryptographic Architect](prompts/speculative/tectonic_viennoiserie_cryptographic_architect/tectonic_viennoiserie_cryptographic_architect.prompt.md)
- [Thermodynamic Epistolary Waste Architect](prompts/speculative/thermodynamic_epistolary_waste_architect/thermodynamic_epistolary_waste_architect.prompt.md)
- [mycelial_arbitrage_urban_planner](prompts/speculative/urban_planning/mycelial_arbitrage_urban_planner.prompt.md)
- [Victorian Neutrino HFT Diplomat](prompts/speculative/victorian_neutrino_hft_diplomat/victorian_neutrino_hft_diplomat.prompt.md)

## Sterility

- [Sterility-Validation Protocol Builder](prompts/scientific/sterility/sterility_workflow/01_sterility_validation_protocol_builder.prompt.md)
- [Regulatory Gap-Analysis Comparator](prompts/scientific/sterility/sterility_workflow/02_regulatory_gap_analysis_comparator.prompt.md)
- [EtO Sterilization Process FMEA](prompts/scientific/sterility/sterility_workflow/03_eto_sterilization_process_fmea.prompt.md)

## Stochastic

- [hidden_markov_model_architect](prompts/scientific/statistics/stochastic/markov_processes/hidden_markov_model_architect.prompt.md)
- [jump_diffusion_modeler](prompts/scientific/statistics/stochastic/stochastic_differential_equations/jump_diffusion_modeler.prompt.md)

## Stratification

- [gentrification_displacement_spatial_inequality_architect](prompts/scientific/sociology/stratification/systemic_inequality/gentrification_displacement_spatial_inequality_architect.prompt.md)
- [intergenerational_social_mobility_markov_chain_architect](prompts/scientific/sociology/stratification/systemic_inequality/intergenerational_social_mobility_markov_chain_architect.prompt.md)
- [multidimensional_poverty_alkire_foster_architect](prompts/scientific/sociology/stratification/systemic_inequality/multidimensional_poverty_alkire_foster_architect.prompt.md)
- [occupational_segregation_opportunity_hoarding_architect](prompts/scientific/sociology/stratification/systemic_inequality/occupational_segregation_opportunity_hoarding_architect.prompt.md)
- [spatial_mismatch_employment_accessibility_modeler](prompts/scientific/sociology/stratification/systemic_inequality/spatial_mismatch_employment_accessibility_modeler.prompt.md)
- [theil_t_index_inequality_decomposer](prompts/scientific/sociology/stratification/systemic_inequality/theil_t_index_inequality_decomposer.prompt.md)
- [wealth_concentration_decomposition_architect](prompts/scientific/sociology/stratification/systemic_inequality/wealth_concentration_decomposition_architect.prompt.md)

## String Theory

- [d_brane_worldvolume_effective_action_architect](prompts/scientific/physics/string_theory/brane_dynamics/d_brane_worldvolume_effective_action_architect.prompt.md)

## Study Director

- [Draft a GLP-Compliant Study Protocol](prompts/management/study_director/study_director_workflow/01_draft_glp_compliant_study_protocol.prompt.md)
- [Audit Raw Data and Draft a CAPA Summary](prompts/management/study_director/study_director_workflow/02_audit_raw_data_capa_summary.prompt.md)
- [Generate an Executive Summary for the Final Report](prompts/management/study_director/study_director_workflow/03_executive_summary_final_report.prompt.md)

## Systems

- [higher_order_unification_resolution_architect](prompts/scientific/formal_logic/systems/higher_order_logic/higher_order_unification_resolution_architect.prompt.md)
- [Adaptive Control Loop Tuning Architect](prompts/scientific/mathematics/systems/control_theory/adaptive_control_loop_tuning_architect.prompt.md)
- [Stochastic Model Predictive Control (MPC) Architect](prompts/scientific/mathematics/systems/control_theory/stochastic_mpc_architect.prompt.md)

## Tasks

- [PAW Phase 1 - Tactical Recon](prompts/technical/software_engineering/tasks/paw/paw_01_tactical_recon.prompt.md)
- [PAW Phase 2 - Architectural Blueprint](prompts/technical/software_engineering/tasks/paw/paw_02_architectural_blueprint.prompt.md)
- [PAW Phase 3 - Precision Strike](prompts/technical/software_engineering/tasks/paw/paw_03_precision_strike.prompt.md)
- [PAW Phase 4 - Quality Assurance & Log](prompts/technical/software_engineering/tasks/paw/paw_04_qa_verification.prompt.md)

## Technical

- [Adaptive Load Shedding and Backpressure Architect](prompts/technical/architecture/adaptive_load_shedding_backpressure_architect.prompt.md)
- [AI Model Inference Serving Architect](prompts/technical/architecture/ai_model_inference_serving_architect.prompt.md)
- [Air-Gapped Environment Deployment Architect](prompts/technical/architecture/air_gapped_environment_deployment_architect.prompt.md)
- [API Gateway and BFF Architect](prompts/technical/architecture/api_gateway_bff_architect.prompt.md)
- [API Management and Developer Portal Architect](prompts/technical/architecture/api_management_developer_portal_architect.prompt.md)
- [Autonomous Vehicle V2X Telemetry Architect](prompts/technical/architecture/autonomous_vehicle_v2x_telemetry_architect.prompt.md)
- [byzantine_fault_tolerant_consensus_architect](prompts/technical/architecture/byzantine_fault_tolerant_consensus_architect.prompt.md)
- [Cache Stampede Mitigation Architect](prompts/technical/architecture/cache_stampede_mitigation_architect.prompt.md)
- [Cascading Failure Resilience Architect](prompts/technical/architecture/cascading_failure_resilience_architect.prompt.md)
- [Cell-Based Architecture Designer](prompts/technical/architecture/cell_based_architecture_designer.prompt.md)
- [Change Data Capture Pipeline Architect](prompts/technical/architecture/change_data_capture_pipeline_architect.prompt.md)
- [Chaos Engineering Experiment Designer](prompts/technical/architecture/chaos_engineering_experiment_designer.prompt.md)
- [Confidential Computing Enclave Architect](prompts/technical/architecture/confidential_computing_enclave_architect.prompt.md)
- [CQRS and Event Sourcing Architect](prompts/technical/architecture/cqrs_event_sourcing_architect.prompt.md)
- [crdt_conflict_resolution_architect](prompts/technical/architecture/crdt_conflict_resolution_architect.prompt.md)
- [Cross-Chain Interoperability Bridge Architect](prompts/technical/architecture/cross_chain_interoperability_bridge_architect.prompt.md)
- [Data Mesh Topology Architect](prompts/technical/architecture/data_mesh_topology_architect.prompt.md)
- [Data Privacy Clean Room Architect](prompts/technical/architecture/data_privacy_clean_room_architect.prompt.md)
- [Data Residency & Localization Architect](prompts/technical/architecture/data_residency_localization_architect.prompt.md)
- [Decentralized Identity and Verifiable Credentials Architect](prompts/technical/architecture/decentralized_identity_verifiable_credentials_architect.prompt.md)
- [Distributed Caching Strategy Architect](prompts/technical/architecture/distributed_caching_strategy_architect.prompt.md)
- [Distributed Database Clock Synchronization Architect](prompts/technical/architecture/distributed_database_clock_synchronization_architect.prompt.md)
- [Distributed Database Sharding Architect](prompts/technical/architecture/distributed_database_sharding_architect.prompt.md)
- [Distributed Knowledge Graph Architect](prompts/technical/architecture/distributed_knowledge_graph_architect.prompt.md)
- [Distributed Lock Manager Architect](prompts/technical/architecture/distributed_lock_manager_architect.prompt.md)
- [Distributed Observability and Telemetry Architect](prompts/technical/architecture/distributed_observability_telemetry_architect.prompt.md)
- [Distributed Rate Limiting Architect](prompts/technical/architecture/distributed_rate_limiting_architect.prompt.md)
- [Distributed Task Queue and Background Job Processing Architect](prompts/technical/architecture/distributed_task_queue_architect.prompt.md)
- [Distributed Transaction Orchestration Architect](prompts/technical/architecture/distributed_transaction_orchestration_architect.prompt.md)
- [Distributed Vector Database Architect](prompts/technical/architecture/distributed_vector_database_architect.prompt.md)
- [Distributed Web Crawler Pipeline Architect](prompts/technical/architecture/distributed_web_crawler_pipeline_architect.prompt.md)
- [Domain-Driven Design Bounded Context Architect](prompts/technical/architecture/domain_driven_design_bounded_context_architect.prompt.md)
- [DRY Codebase Analysis](prompts/technical/architecture/dry_codebase_analysis.prompt.md)
- [eBPF Network Observability Architect](prompts/technical/architecture/ebpf_network_observability_architect.prompt.md)
- [Edge AI Inference Architect](prompts/technical/architecture/edge_ai_inference_architect.prompt.md)
- [Edge Computing Topology Architect](prompts/technical/architecture/edge_computing_topology_architect.prompt.md)
- [Enterprise RAG Architecture Designer](prompts/technical/architecture/enterprise_rag_architecture_designer.prompt.md)
- [Event-Driven Dead Letter Queue Remediation Architect](prompts/technical/architecture/event_driven_dead_letter_queue_remediation_architect.prompt.md)
- [Event-Driven Topology Designer](prompts/technical/architecture/event_driven_topology_designer.prompt.md)
- [Event-Sourced Saga Orchestration Architect](prompts/technical/architecture/event_sourced_saga_orchestration_architect.prompt.md)
- [Feature Flag and Progressive Delivery Architect](prompts/technical/architecture/feature_flag_progressive_delivery_architect.prompt.md)
- [Federated Learning Privacy-Preserving Architect](prompts/technical/architecture/federated_learning_privacy_preserving_architect.prompt.md)
- [Federated Learning Topology Architect](prompts/technical/architecture/federated_learning_topology_architect.prompt.md)
- [Fine-Grained Authorization Architect](prompts/technical/architecture/fine_grained_authorization_architect.prompt.md)
- [finops_cloud_cost_optimization_architect](prompts/technical/architecture/finops_cloud_cost_optimization_architect.prompt.md)
- [Generative AI Guardrails Gateway Architect](prompts/technical/architecture/generative_ai_guardrails_gateway_architect.prompt.md)
- [GPU Cluster Orchestration Architect](prompts/technical/architecture/gpu_cluster_orchestration_architect.prompt.md)
- [Graph Database Traversal Architect](prompts/technical/architecture/graph_database_traversal_architect.prompt.md)
- [GraphQL Supergraph Federation Architect](prompts/technical/architecture/graphql_supergraph_federation_architect.prompt.md)
- [Hexagonal Architecture Implementation](prompts/technical/architecture/hexagonal_architecture_implementation.prompt.md)
- [Hexagonal Architecture Principles](prompts/technical/architecture/hexagonal_architecture_principles.prompt.md)
- [Hexagonal Architecture Review](prompts/technical/architecture/hexagonal_architecture_review.prompt.md)
- [HFT Low-Latency Architecture Designer](prompts/technical/architecture/hft_low_latency_trading_architect.prompt.md)
- [High-Scale OTT Video Streaming Architect](prompts/technical/architecture/high_scale_ott_video_streaming_architect.prompt.md)
- [High-Scale WebSocket Push Architect](prompts/technical/architecture/high_scale_websocket_push_architect.prompt.md)
- [High-Throughput Distributed ID Generator Architect](prompts/technical/architecture/high_throughput_distributed_id_generator_architect.prompt.md)
- [High-Throughput Geospatial Indexing Architect](prompts/technical/architecture/high_throughput_geospatial_indexing_architect.prompt.md)
- [High-Throughput Order Matching Engine Architect](prompts/technical/architecture/high_throughput_order_matching_engine_architect.prompt.md)
- [HTAP Real-Time Analytics Architect](prompts/technical/architecture/htap_real_time_analytics_architect.prompt.md)
- [Idempotency and API Retry Strategy Architect](prompts/technical/architecture/idempotency_strategy_architect.prompt.md)
- [Immutable Financial Ledger Architect](prompts/technical/architecture/immutable_financial_ledger_architect.prompt.md)
- [IoT Digital Twin Architect](prompts/technical/architecture/iot_digital_twin_architect.prompt.md)
- [Leader Election and Split-Brain Mitigation Architect](prompts/technical/architecture/leader_election_split_brain_mitigation_architect.prompt.md)
- [LLM Distributed Training Architect](prompts/technical/architecture/llm_distributed_training_architect.prompt.md)
- [Log-Structured Merge Tree Storage Architect](prompts/technical/architecture/log_structured_merge_tree_storage_architect.prompt.md)
- [Maintainability Codebase Analysis](prompts/technical/architecture/maintainability_codebase_analysis.prompt.md)
- [Massive-Scale IoT OTA Update Architect](prompts/technical/architecture/massive_scale_iot_ota_architect.prompt.md)
- [Micro-Frontend Orchestration Architect](prompts/technical/architecture/micro_frontend_orchestration_architect.prompt.md)
- [Multi-Agent Orchestration Architect](prompts/technical/architecture/multi_agent_orchestration_architect.prompt.md)
- [Multi-Cloud Disaster Recovery Architect](prompts/technical/architecture/multi_cloud_disaster_recovery_architect.prompt.md)
- [Multi-Region Active-Active Resilience Architect](prompts/technical/architecture/multi_region_active_active_resilience.prompt.md)
- [Multi-Region K8s Federation Architect](prompts/technical/architecture/multi_region_k8s_federation_architect.prompt.md)
- [Multi-Tenant Noisy Neighbor Mitigation Architect](prompts/technical/architecture/multi_tenant_noisy_neighbor_mitigation_architect.prompt.md)
- [Multi-Tenant SaaS Architecture Designer](prompts/technical/architecture/multi_tenant_saas_architecture_designer.prompt.md)
- [Multi-Tier Disaggregated Memory CXL Architect](prompts/technical/architecture/multi_tier_disaggregated_memory_cxl_architect.prompt.md)
- [Offline-First Synchronization Architect](prompts/technical/architecture/offline_first_sync_architect.prompt.md)
- [Payment Gateway Idempotency Architect](prompts/technical/architecture/payment_gateway_idempotency_architect.prompt.md)
- [peer_to_peer_gossip_protocol_architect](prompts/technical/architecture/peer_to_peer_gossip_protocol_architect.prompt.md)
- [Petabyte-Scale Data Lakehouse Architect](prompts/technical/architecture/petabyte_scale_data_lakehouse_architect.prompt.md)
- [PII Tokenization Vault Architect](prompts/technical/architecture/pii_tokenization_vault_architect.prompt.md)
- [Platform Engineering IDP Architect](prompts/technical/architecture/platform_engineering_idp_architect.prompt.md)
- [Predictive Auto-Scaling Machine Learning Architect](prompts/technical/architecture/predictive_auto_scaling_machine_learning_architect.prompt.md)
- [Quantum Key Distribution Network Architect](prompts/technical/architecture/quantum_key_distribution_network_architect.prompt.md)
- [Quantum-Safe Cryptography Migration Architect](prompts/technical/architecture/quantum_safe_cryptography_migration_architect.prompt.md)
- [Real-Time Bidding AdTech Architect](prompts/technical/architecture/real_time_bidding_adtech_architect.prompt.md)
- [Real-Time Fraud Decision Engine Architect](prompts/technical/architecture/real_time_fraud_decision_engine_architect.prompt.md)
- [Real-Time Game State Synchronization Architect](prompts/technical/architecture/real_time_game_state_synchronization_architect.prompt.md)
- [Real-Time ML Feature Store Architect](prompts/technical/architecture/real_time_ml_feature_store_architect.prompt.md)
- [Real-Time Stream Processing Architect](prompts/technical/architecture/real_time_stream_processing_architect.prompt.md)
- [Semantic Caching AI Gateway Architect](prompts/technical/architecture/semantic_caching_ai_gateway_architect.prompt.md)
- [Server-Driven UI Architecture Designer](prompts/technical/architecture/server_driven_ui_architect.prompt.md)
- [Serverless Database Connection Pooling Architect](prompts/technical/architecture/serverless_database_connection_pooling_architect.prompt.md)
- [Serverless Function Orchestration Architect](prompts/technical/architecture/serverless_function_orchestration_architect.prompt.md)
- [Service Mesh Security Architect](prompts/technical/architecture/service_mesh_security_architect.prompt.md)
- [SOLID Codebase Analysis](prompts/technical/architecture/solid_codebase_analysis.prompt.md)
- [Spatial Geofencing Topology Architect](prompts/technical/architecture/spatial_geofencing_topology_architect.prompt.md)
- [Stateful Workflow Orchestration Architect](prompts/technical/architecture/stateful_workflow_orchestration_architect.prompt.md)
- [Strangler Fig Migration Architect](prompts/technical/architecture/strangler_fig_migration_architect.prompt.md)
- [Sustainable Green Software Architect](prompts/technical/architecture/sustainable_green_software_architect.prompt.md)
- [Threshold Signature MPC Custody Architect](prompts/technical/architecture/threshold_signature_mpc_custody_architect.prompt.md)
- [Time-Series Database Topology Architect](prompts/technical/architecture/time_series_database_topology_architect.prompt.md)
- [transactional_outbox_event_publishing_architect](prompts/technical/architecture/transactional_outbox_event_publishing_architect.prompt.md)
- [Virtual Waiting Room Fair Access Architect](prompts/technical/architecture/virtual_waiting_room_fair_access_architect.prompt.md)
- [WASM Edge Serverless Runtime Architect](prompts/technical/architecture/wasm_edge_serverless_runtime_architect.prompt.md)
- [WebAssembly Sandboxed Plugin Architect](prompts/technical/architecture/webassembly_sandboxed_plugin_architect.prompt.md)
- [Webhook Dispatch Delivery Architect](prompts/technical/architecture/webhook_dispatch_delivery_architect.prompt.md)
- [WebRTC Real-Time Media Streaming Architect](prompts/technical/architecture/webrtc_media_streaming_architect.prompt.md)
- [Zero-Downtime Database Migration Architect](prompts/technical/architecture/zero_downtime_database_migration_architect.prompt.md)
- [Zero-Knowledge Rollup Scaling Architect](prompts/technical/architecture/zero_knowledge_rollup_scaling_architect.prompt.md)
- [Zero Trust Network Architecture Designer](prompts/technical/architecture/zero_trust_network_architecture_designer.prompt.md)
- [Autonomous Automation Agent](prompts/technical/automation/autonomous_automation_agent.prompt.md)
- [Autonomous Automation Agent Upgrade](prompts/technical/automation/autonomous_automation_agent_upgrade.prompt.md)
- [Universal Automation Agent](prompts/technical/automation/universal_automation_agent.prompt.md)
- [fully_homomorphic_encryption_circuit_architect](prompts/technical/cryptography/fully_homomorphic_encryption_circuit_architect.prompt.md)
- [post_quantum_cryptography_migration_architect](prompts/technical/cryptography/post_quantum_cryptography_migration_architect.prompt.md)
- [bayesian_optimization_hyperparameter_architect](prompts/technical/data_science/bayesian_optimization_hyperparameter_architect.prompt.md)
- [Causal Discovery DAG Architect](prompts/technical/data_science/causal_discovery_dag_architect.prompt.md)
- [Conversation Stochastic Modeler](prompts/technical/data_science/conversation_stochastic_modeler.prompt.md)
- [Reinforcement Learning Reward Function Architect](prompts/technical/data_science/reinforcement_learning_reward_function_architect.prompt.md)
- [Topological Data Analysis Architect](prompts/technical/data_science/topological_data_analysis_architect.prompt.md)
- [System Design RFC Architect](prompts/technical/design/design_md_template.prompt.md)
- [AI Email Assistant Go/No-Go Vote](prompts/technical/design/email_assistant_go_no_go_vote.prompt.md)
- [Heuristic-Evaluation Coach](prompts/technical/design/heuristic_evaluation_coach.prompt.md)
- [Forge - Script Reliability Agent](prompts/technical/devops/forge_script_reliability.prompt.md)
- [gitops_continuous_delivery_architect](prompts/technical/devops/gitops_continuous_delivery_architect.prompt.md)
- [Infrastructure as Code (IaC) Security Architect](prompts/technical/devops/infrastructure_as_code_security_architect.prompt.md)
- [Site Reliability SLO Error Budget Architect](prompts/technical/devops/site_reliability_slo_error_budget_architect.prompt.md)
- [SRE Incident Postmortem RCA Architect](prompts/technical/devops/sre_incident_postmortem_rca_architect.prompt.md)
- [Atlas Documentation Specialist](prompts/technical/documentation/atlas_documentation_specialist.prompt.md)
- [Source of Truth Harmonizer](prompts/technical/documentation/source_of_truth_harmonizer.prompt.md)
- [Finite Element Analysis (FEA) Interpreter](prompts/technical/hardware_engineering/finite_element_analysis_interpreter.prompt.md)
- [Mechatronics Control Systems Architect](prompts/technical/hardware_engineering/mechatronics_control_systems_architect.prompt.md)
- [PCB Layout Topology Reviewer](prompts/technical/hardware_engineering/pcb_layout_topology_reviewer.prompt.md)
- [Adversarial Prompt Robustness Tester](prompts/technical/prompt_engineering/adversarial_prompt_robustness_tester.prompt.md)
- [Vector Prompt Editor-in-Chief](prompts/technical/prompt_engineering/vector_prompt_editor_in_chief.prompt.md)
- [Code Formatting, Linting, and Refactoring Implementation](prompts/technical/repository_refactoring/code_formatting_linting_refactoring_implementation.prompt.md)
- [Codebase Quality & Maintainability Analysis](prompts/technical/repository_refactoring/codebase_quality_analysis.prompt.md)
- [Dependencies & Security Posture Analysis](prompts/technical/repository_refactoring/dependencies_security_analysis.prompt.md)
- [Documentation and Repository Structure Implementation](prompts/technical/repository_refactoring/documentation_structure_implementation.prompt.md)
- [Repository Foundation & Developer Experience Analysis](prompts/technical/repository_refactoring/repo_foundation_analysis.prompt.md)
- [Security Hardening and Dependency Management Implementation](prompts/technical/repository_refactoring/security_hardening_dependency_management_implementation.prompt.md)
- [Test Suite Enhancement and CI Pipeline Implementation](prompts/technical/repository_refactoring/test_suite_enhancement_ci_pipeline_implementation.prompt.md)
- [Testing, Configuration, and Automation Analysis](prompts/technical/repository_refactoring/testing_configuration_automation_analysis.prompt.md)
- [Active Directory Domain Dominance Forensics Analyst](prompts/technical/security/active_directory_domain_dominance_forensics_analyst.prompt.md)
- [Advanced C2 Beacon PCAP Analysis Engineer](prompts/technical/security/advanced_c2_beacon_pcap_analysis_engineer.prompt.md)
- [Advanced Red Team Adversary Emulation Architect](prompts/technical/security/advanced_red_team_adversary_emulation_architect.prompt.md)
- [Advanced Volatile Memory Forensics Analyst](prompts/technical/security/advanced_volatile_memory_forensics_analyst.prompt.md)
- [ai_threat_modeling_architect](prompts/technical/security/ai_threat_modeling_architect.prompt.md)
- [API Security & Zero Trust Architect](prompts/technical/security/api_security_zero_trust_architect.prompt.md)
- [APT Threat Hunting Query Engineer](prompts/technical/security/apt_threat_hunting_query_engineer.prompt.md)
- [automated_malware_reverse_engineering_analyst](prompts/technical/security/automated_malware_reverse_engineering_analyst.prompt.md)
- [CI/CD Pipeline Poisoning Forensics Architect](prompts/technical/security/ci_cd_pipeline_poisoning_forensics_architect.prompt.md)
- [Cloud IAM Least-Privilege Remediation Architect](prompts/technical/security/cloud_iam_least_privilege_remediation_architect.prompt.md)
- [Cloud Incident Response Forensics Architect](prompts/technical/security/cloud_incident_response_forensics_architect.prompt.md)
- [confidential_computing_enclave_architect](prompts/technical/security/confidential_computing_enclave_architect.prompt.md)
- [Medical Device Cybersecurity Threat Modeling](prompts/technical/security/cybersecurity_threat_modeling.prompt.md)
- [Deception Technology & Active Defense Architect](prompts/technical/security/deception_technology_active_defense_architect.prompt.md)
- [DeFi Protocol Economic Security Architect](prompts/technical/security/defi_protocol_economic_security_architect.prompt.md)
- [eBPF Runtime Security Architect](prompts/technical/security/ebpf_runtime_security_architect.prompt.md)
- [Hardware Side-Channel Attack Modeling Architect](prompts/technical/security/hardware_side_channel_attack_modeling_architect.prompt.md)
- [Insider Threat Behavioral Analytics Engineer](prompts/technical/security/insider_threat_behavioral_analytics_engineer.prompt.md)
- [Kubernetes Cluster Security Posture Architect](prompts/technical/security/kubernetes_cluster_security_posture_architect.prompt.md)
- [OT/SCADA Security Resilience Architect](prompts/technical/security/ot_scada_security_architect.prompt.md)
- [Post-Quantum Cryptography Migration Architect](prompts/technical/security/post_quantum_cryptography_migration_architect.prompt.md)
- [red_team_exploit_chain_architect](prompts/technical/security/red_team_exploit_chain_architect.prompt.md)
- [Software Supply Chain Provenance Architect](prompts/technical/security/software_supply_chain_provenance_architect.prompt.md)
- [Zero-Day Incident Containment Architect](prompts/technical/security/zero_day_containment_architect.prompt.md)
- [Zero-Knowledge Proof Protocol Architect](prompts/technical/security/zero_knowledge_proof_protocol_architect.prompt.md)
- [Technical White Paper for Clinical Methodologies](prompts/technical/technical_writing/technical_white_paper_in_silico.prompt.md)

## Technical Writing

- [CSR Results and Safety Section](prompts/technical/technical_writing/technical_writer_workflow/01_csr_results_safety_section.prompt.md)
- [Investigator's Brochure Summary of Changes](prompts/technical/technical_writing/technical_writer_workflow/02_ib_detailed_soc.prompt.md)
- [SAE and Unanticipated Problem Reporting SOP](prompts/technical/technical_writing/technical_writer_workflow/03_sae_reporting_sop.prompt.md)

## Testing

- [Framework Implementation: Data-Driven Testing](prompts/technical/testing/selenium_automation/data_driven_selenium.prompt.md)
- [Advanced Design Patterns: Fluent Interface](prompts/technical/testing/selenium_automation/fluent_interface_selenium.prompt.md)
- [Framework Best Practices: Locator Strategy](prompts/technical/testing/selenium_automation/locator_optimization.prompt.md)
- [Project Configuration: Maven Setup](prompts/technical/testing/selenium_automation/maven_selenium_setup.prompt.md)
- [Execution Optimization: Parallel Testing](prompts/technical/testing/selenium_automation/parallel_execution.prompt.md)
- [Architecture Design: Page Object Model](prompts/technical/testing/selenium_automation/pom_implementation.prompt.md)
- [Selenium Migration: Script Conversion](prompts/technical/testing/selenium_automation/script_conversion.prompt.md)
- [Cross-Browser Infrastructure: Selenium Grid](prompts/technical/testing/selenium_automation/selenium_grid_setup.prompt.md)
- [Test Environment: Python & Selenium Base](prompts/technical/testing/selenium_automation/selenium_python_setup.prompt.md)
- [Reporting and Maintenance: Custom Reports](prompts/technical/testing/selenium_automation/selenium_reporting.prompt.md)
- [Synchronization Strategy: Explicit Waits](prompts/technical/testing/selenium_automation/selenium_waits.prompt.md)
- [Security Testing: OWASP ZAP Integration](prompts/technical/testing/selenium_automation/selenium_zap_integration.prompt.md)
- [Driver Configuration: WebDriver Initialization](prompts/technical/testing/selenium_automation/webdriver_initialization.prompt.md)
- [E2E Test Discovery Template](prompts/technical/testing/testing_workflow/01_e2e_test_discovery.prompt.md)
- [Design Verification Test Plan](prompts/technical/testing/testing_workflow/02_design_verification_test_plan.prompt.md)
- [Human Factors Validation Study Protocol](prompts/technical/testing/testing_workflow/03_human_factors_validation_study_protocol.prompt.md)
- [Risk-Based Test Case Suite](prompts/technical/testing/testing_workflow/04_risk_based_test_case_suite.prompt.md)

## Theory

- [dialectical_materialism_structural_crisis_modeler](prompts/scientific/sociology/theory/critical_frameworks/dialectical_materialism_structural_crisis_modeler.prompt.md)
- [asymptotic_distribution_mle_architect](prompts/scientific/statistics/theory/asymptotics/asymptotic_distribution_mle_architect.prompt.md)
- [empirical_process_theory_architect](prompts/scientific/statistics/theory/asymptotics/empirical_process_theory_architect.prompt.md)

## Therapy

- [Compassionate Analyst](prompts/clinical/therapy/music_therapy_workflow/01_compassionate_analyst.prompt.md)
- [ISO Strategist](prompts/clinical/therapy/music_therapy_workflow/02_iso_strategist.prompt.md)
- [Sonic Architect](prompts/clinical/therapy/music_therapy_workflow/03_sonic_architect.prompt.md)
- [Lyricist](prompts/clinical/therapy/music_therapy_workflow/04_lyricist.prompt.md)

## Topology

- [characteristic_class_cobordism_architect](prompts/scientific/mathematics/topology/algebraic_topology/characteristic_class_cobordism_architect.prompt.md)
- [higher_homotopy_postnikov_tower_architect](prompts/scientific/mathematics/topology/algebraic_topology/higher_homotopy_postnikov_tower_architect.prompt.md)
- [serre_spectral_sequence_calculator](prompts/scientific/mathematics/topology/algebraic_topology/serre_spectral_sequence_calculator.prompt.md)

## Training

- [Competency-Based Onboarding Blueprint](prompts/management/training/learning_development_workflow/01_competency_based_onboarding_blueprint.prompt.md)
- [Scenario-Based Microlearning Series](prompts/management/training/learning_development_workflow/02_scenario_based_microlearning_series.prompt.md)
- [Training Impact Analytics Planner](prompts/management/training/learning_development_workflow/03_training_impact_analytics_targeted_intervention_planner.prompt.md)

## Vp Statistics

- [Interim Results Executive Brief](prompts/management/vp_statistics/vp_statistics_workflow/01_interim_results_executive_brief.prompt.md)
- [Statistical Analysis Plan Draft Builder](prompts/management/vp_statistics/vp_statistics_workflow/02_sap_first_draft_builder.prompt.md)
- [Data-Quality Risk Heat Map](prompts/management/vp_statistics/vp_statistics_workflow/03_data_quality_risk_heatmap.prompt.md)
