import os
import re
import yaml

tasks = [
    {
        "Task Name": "510(k) Substantial Equivalence Preparation",
        "Target Regulatory Context": "21 CFR Part 807 Subpart E",
        "Prompt Objective": "Draft a substantial equivalence comparison and summary between a subject device and predicate(s) to demonstrate safety and effectiveness.",
        "Required Input Data": "Device description, indications for use, technological characteristics, performance data, and predicate device identification.",
        "Expected Output Format": "Formal 510(k) Summary or Markdown table as per 21 CFR 807.92.",
        "Validation Method (Inferred)": "Review against 21 CFR 807.87, 807.92, and FDA guidance on evaluating substantial equivalence."
    },
    {
        "Task Name": "Quality System Audit",
        "Target Regulatory Context": "21 CFR Part 820",
        "Prompt Objective": "Generate an internal audit checklist or report focusing on design controls, production processes, and risk-based decision making.",
        "Required Input Data": "Quality Manual, Design History File (DHF) excerpts, SOPs, and previous audit reports.",
        "Expected Output Format": "Formal audit report or Markdown checklist with regulatory citations.",
        "Validation Method (Inferred)": "Verify against requirements in 21 CFR 820 (Subparts B-O) and relevant transition modules (QMSR)."
    },
    {
        "Task Name": "Risk Management Analysis",
        "Target Regulatory Context": "ISO 14971 / 21 CFR 820.30",
        "Prompt Objective": "Perform a risk analysis (e.g., PHA) to identify potential hazards, hazardous situations, and mitigation strategies.",
        "Required Input Data": "Intended use, design specifications, foreseeable misuse, and historical data for similar devices.",
        "Expected Output Format": "Risk Analysis Matrix (Markdown table) including Hazard, Harm, Severity, and Probability.",
        "Validation Method (Inferred)": "Cross-reference with ISO 14971 principles and FDA training modules on Risk Management."
    },
    {
        "Task Name": "IDE Application Preparation",
        "Target Regulatory Context": "21 CFR Part 812",
        "Prompt Objective": "Draft an Investigational Device Exemption (IDE) application, including risk analysis and investigational plans for clinical studies.",
        "Required Input Data": "Investigational plan, report of prior investigations, investigator agreements, and device labeling.",
        "Expected Output Format": "Formal IDE application package following the sequence in 21 CFR 812.25.",
        "Validation Method (Inferred)": "Verify inclusion of all elements required by 21 CFR 812.20 and 812.25."
    },
    {
        "Task Name": "Premarket Approval (PMA) Preparation",
        "Target Regulatory Context": "21 CFR Part 814",
        "Prompt Objective": "Draft a detailed summary of a PMA application, including clinical investigation results and manufacturing history.",
        "Required Input Data": "Clinical results, nonclinical lab data, device characteristics, and marketing history.",
        "Expected Output Format": "Formal structured summary as per 21 CFR 814.20(b)(3).",
        "Validation Method (Inferred)": "Review against specific summary requirements listed in 21 CFR 814.20(b)(3)(i-vi)."
    },
    {
        "Task Name": "PMA Post-approval Reporting",
        "Target Regulatory Context": "21 CFR Part 814.82 / 814.84",
        "Prompt Objective": "Compile a summary of post-approval requirements, including clinical study data, manufacturing changes, and scientific literature.",
        "Required Input Data": "PMA approval order, study data, change logs, and bibliography of recent literature.",
        "Expected Output Format": "Formal report to the Office of Device Evaluation.",
        "Validation Method (Inferred)": "Verify compliance with 21 CFR 814.82 and 814.84 submission requirements."
    },
    {
        "Task Name": "Medical Device Administrative Detention Appeal",
        "Target Regulatory Context": "21 CFR Part 1.402 / 800.55",
        "Prompt Objective": "Draft a written appeal for an administrative detention order issued on a food item or medical device.",
        "Required Input Data": "Detention order number, date received, and verified statement of ownership/proprietary interest.",
        "Expected Output Format": "Formal legal letter.",
        "Validation Method (Inferred)": "Verify submission within the required timeframe (10 days for food, 5 days for devices) per 21 CFR 1.402 or 800.55."
    },
    {
        "Task Name": "Foreign Supplier Verification Program (FSVP) Audit",
        "Target Regulatory Context": "21 CFR Part 1 Subpart L",
        "Prompt Objective": "Draft a summary report of an onsite audit for a foreign food supplier including conclusions and corrective actions.",
        "Required Input Data": "Audit procedures, dates, findings on processes, and records of deficiencies.",
        "Expected Output Format": "Formal audit report in Markdown format.",
        "Validation Method (Inferred)": "Cross-reference against 21 CFR 1.506(e)(1)(i)(D) requirements for audit documentation."
    },
    {
        "Task Name": "Establishment of Food Traceability Plan",
        "Target Regulatory Context": "21 CFR Part 1 Subpart S",
        "Prompt Objective": "Create a structured traceability plan for a facility handling foods on the Food Traceability List.",
        "Required Input Data": "List of foods handled, record maintenance procedures, and contact information.",
        "Expected Output Format": "Structured text document with sections for procedures and identification.",
        "Validation Method (Inferred)": "Ensure all requirements of 21 CFR 1.1315(a) (1-5) are addressed."
    },
    {
        "Task Name": "Food Safety Audit Reporting (Regulatory)",
        "Target Regulatory Context": "21 CFR Part 1 Subpart M",
        "Prompt Objective": "Draft a regulatory audit report for an eligible entity after a food safety audit.",
        "Required Input Data": "Facility identity (FEI), audit dates, scope, and identified deficiencies.",
        "Expected Output Format": "Structured Markdown table or list.",
        "Validation Method (Inferred)": "Verify that all 9 specific data elements listed in 21 CFR 1.652(b) are present."
    },
    {
        "Task Name": "Directed Food Laboratory Order Verification",
        "Target Regulatory Context": "21 CFR Part 1 Subpart R",
        "Prompt Objective": "Review a Directed Food Laboratory Order to identify mandatory testing parameters.",
        "Required Input Data": "FDA issued Directed Food Laboratory Order.",
        "Expected Output Format": "Key-value list of product, environment, methods, and timeframes.",
        "Validation Method (Inferred)": "Compare parameters with specifications in 21 CFR 1.1108(b)."
    },
    {
        "Task Name": "Import Entry Data Element Compilation",
        "Target Regulatory Context": "21 CFR Part 1 Subpart D",
        "Prompt Objective": "Compile required identifying information (510(k), UFI, NDC, NDA) for electronic import entry of drugs or devices.",
        "Required Input Data": "Clearance documentation, registration numbers, and listing information.",
        "Expected Output Format": "JSON object or alphanumeric string.",
        "Validation Method (Inferred)": "Check compliance with 21 CFR 1.74(a) and 1.76(c) for ACE system mapping."
    },
    {
        "Task Name": "Automated Image Assessment System 510(k)",
        "Target Regulatory Context": "21 CFR 866.2190",
        "Prompt Objective": "Draft a detailed device description for an automated image assessment system for microbial colonies.",
        "Required Input Data": "Technology details, software modules, and expert rules for colony assessment.",
        "Expected Output Format": "Formal technical document.",
        "Validation Method (Inferred)": "Verify content against requirements in 21 CFR 866.2190(b)(1)-(5)."
    },
    {
        "Task Name": "Special Controls Labeling Compliance",
        "Target Regulatory Context": "21 CFR 866.3169",
        "Prompt Objective": "Generate mandatory labeling content, including warnings and limitations, for HCV antibody tests.",
        "Required Input Data": "Specimen types, clinical population data, and performance characteristics.",
        "Expected Output Format": "Structured labeling text.",
        "Validation Method (Inferred)": "Cross-check warnings against requirements in 21 CFR 866.3169(b)(1)."
    },
    {
        "Task Name": "Zika Virus Reagent Study Design",
        "Target Regulatory Context": "21 CFR 866.3935",
        "Prompt Objective": "Draft a protocol for analytical performance studies to validate Zika virus serological reagents.",
        "Required Input Data": "Reference material details, cross-reactivity targets, and specimen stability.",
        "Expected Output Format": "Technical study protocol.",
        "Validation Method (Inferred)": "Ensure protocol covers analytical studies mandated by 21 CFR 866.3935(b)(2)(ii)."
    },
    {
        "Task Name": "Carrier Screening System 510(k)",
        "Target Regulatory Context": "21 CFR 866.5940",
        "Prompt Objective": "Compile technical information for an autosomal recessive carrier screening gene mutation detection system.",
        "Required Input Data": "Gene list (HUGO), variant coordinates, and clinical validity evidence.",
        "Expected Output Format": "Comprehensive technical summary report.",
        "Validation Method (Inferred)": "Check against technical info requirements in 21 CFR 866.5940(b)(3)(i)."
    },
    {
        "Task Name": "Design Verification for BCR-ABL Tests",
        "Target Regulatory Context": "21 CFR 866.6060",
        "Prompt Objective": "Outline design verification and validation requirements for a BCR-ABL quantitation test.",
        "Required Input Data": "Variant types, IS conversion methodology, and calibration control data.",
        "Expected Output Format": "Validation checklist or matrix.",
        "Validation Method (Inferred)": "Review against submission requirements in 21 CFR 866.6060(b)(1)."
    },
    {
        "Task Name": "NGS Tumor Profiling Documentation",
        "Target Regulatory Context": "21 CFR 866.6080",
        "Prompt Objective": "Develop documentation supporting the clinical significance of mutations in an NGS-based tumor profiling panel.",
        "Required Input Data": "Somatic mutations, professional guidelines, and method comparison data.",
        "Expected Output Format": "Tabulated summary of mutations categorized by evidence levels.",
        "Validation Method (Inferred)": "Confirm categorization aligns with criteria in 21 CFR 866.6080(b)(1)(v)."
    },
    {
        "Task Name": "Civil Money Penalties Hearing Response",
        "Target Regulatory Context": "21 CFR Part 17",
        "Prompt Objective": "Draft a formal 'Answer' to an FDA complaint seeking civil money penalties.",
        "Required Input Data": "FDA Complaint, alleged violations, and mitigating factors.",
        "Expected Output Format": "Formal legal pleading.",
        "Validation Method (Inferred)": "Review against required contents for an Answer specified in 21 CFR 17.9."
    },
    {
        "Task Name": "Clinical Chemistry Device Classification",
        "Target Regulatory Context": "21 CFR Part 862",
        "Prompt Objective": "Identify classification and regulatory requirements (general/special controls) for a clinical chemistry device.",
        "Required Input Data": "Device name and intended use.",
        "Expected Output Format": "Structured summary identifying FDA Class and regulatory section.",
        "Validation Method (Inferred)": "Verify classification against 21 CFR Part 862 Subparts A-D."
    },
    {
        "Task Name": "iCGM Clinical Testing Strategy",
        "Target Regulatory Context": "21 CFR 862.1355",
        "Prompt Objective": "Draft a clinical study plan to demonstrate accuracy for an iCGM system.",
        "Required Input Data": "Sensor specifications, target population, and wear period details.",
        "Expected Output Format": "Formal clinical study protocol outline.",
        "Validation Method (Inferred)": "Compare against performance bounds listed in 21 CFR 862.1355(b)(1)."
    },
    {
        "Task Name": "Citizen Petition Preparation",
        "Target Regulatory Context": "21 CFR Part 10.30",
        "Prompt Objective": "Draft a Citizen Petition requesting administrative action by the Commissioner.",
        "Required Input Data": "Factual/legal grounds, action requested, and environmental impact assessment.",
        "Expected Output Format": "Structured petition following 21 CFR 10.30(b)(3) format.",
        "Validation Method (Inferred)": "Verify all required sections (Grounds, Certification, etc.) are present."
    },
    {
        "Task Name": "Medical Device Reporting (MDR)",
        "Target Regulatory Context": "21 CFR Part 803",
        "Prompt Objective": "Summarize an adverse event for mandatory electronic submission or develop an MDR SOP.",
        "Required Input Data": "Incident reports, outcome data, and device identification.",
        "Expected Output Format": "Structured summary (eMDR) or numbered SOP document.",
        "Validation Method (Inferred)": "Review against reporting requirements in 21 CFR Part 803 and 803.17."
    },
    {
        "Task Name": "UDI GUDID Submission",
        "Target Regulatory Context": "21 CFR Part 830",
        "Prompt Objective": "Prepare a Device Identifier (DI) record for GUDID submission.",
        "Required Input Data": "Device label, packaging levels, and GTIN data.",
        "Expected Output Format": "Structured data list matching GUDID fields.",
        "Validation Method (Inferred)": "Cross-check fields against GUDID DI Record preparation modules."
    },
    {
        "Task Name": "Freedom of Information Act (FOIA) Request",
        "Target Regulatory Context": "21 CFR Part 20",
        "Prompt Objective": "Draft a request for records regarding a specific 510(k) clearance.",
        "Required Input Data": "Description of records sought and requester contact information.",
        "Expected Output Format": "Formal letter following 21 CFR 20.40.",
        "Validation Method (Inferred)": "Check against 'Search for Records' criteria in Part 20 Subpart C."
    },
    {
        "Task Name": "RTA Checklist Preparation",
        "Target Regulatory Context": "FDA RTA Policy",
        "Prompt Objective": "Annotate the RTA checklist with page numbers and sections where requirements are addressed in a 510(k).",
        "Required Input Data": "Draft 510(k) submission and appropriate FDA RTA checklist.",
        "Expected Output Format": "Annotated checklist with a comment column.",
        "Validation Method (Inferred)": "Verify cited page numbers correspond to final submission PDF."
    },
    {
        "Task Name": "Intended Use and Indications for Use Alignment",
        "Target Regulatory Context": "21 CFR Part 801.4",
        "Prompt Objective": "Review 510(k) drafts to ensure 'Intended Use' and 'Indications for Use' are verbatim and consistent.",
        "Required Input Data": "Full 510(k) draft including labeling and executive summary.",
        "Expected Output Format": "Consistency report identifying discrepancies.",
        "Validation Method (Inferred)": "Cross-reference all labeling statements for exact matches."
    },
    {
        "Task Name": "Shelf-life Study Rationale",
        "Target Regulatory Context": "21 CFR Part 801",
        "Prompt Objective": "Draft a rationale for correlating accelerated aging data with real-time requirements.",
        "Required Input Data": "Material stability data, packaging type, and aging protocols.",
        "Expected Output Format": "Formal technical report.",
        "Validation Method (Inferred)": "Evaluate against FDA standards for shelf-life testing."
    },
    {
        "Task Name": "Labeling Compliance Audit",
        "Target Regulatory Context": "21 CFR Part 801",
        "Prompt Objective": "Audit device labeling for compliance with mandatory elements (Manufacturer, UDI, date formats).",
        "Required Input Data": "Product labels, symbols glossary, and 21 CFR 801 text.",
        "Expected Output Format": "Gap analysis report.",
        "Validation Method (Inferred)": "Inspect label against 21 CFR 801.1 and 801.18."
    },
    {
        "Task Name": "21 CFR Part 14 Auditing",
        "Target Regulatory Context": "21 CFR Part 14",
        "Prompt Objective": "Audit advisory committee meeting minutes for compliance with record-keeping elements.",
        "Required Input Data": "Minutes, attendee list, and information considered.",
        "Expected Output Format": "Markdown compliance checklist.",
        "Validation Method (Inferred)": "Verify presence of items listed in 21 CFR 14.60(b)."
    },
    {
        "Task Name": "Humanitarian Device Exemption (HDE)",
        "Target Regulatory Context": "21 CFR Part 814 Subpart H",
        "Prompt Objective": "Explain why the health benefit of a HUD outweighs the risk of injury.",
        "Required Input Data": "HUD designation and risk-benefit analysis of alternatives.",
        "Expected Output Format": "Formal narrative explanation.",
        "Validation Method (Inferred)": "Check against HDE contents specified in 21 CFR 814.104(b)(3)."
    },
    {
        "Task Name": "Quality System Evaluation (MRA)",
        "Target Regulatory Context": "21 CFR 820 / MRA Subpart B",
        "Prompt Objective": "Generate a quality system evaluation report for a manufacturer under the US-EC MRA.",
        "Required Input Data": "Onsite inspection data and manufacturing records.",
        "Expected Output Format": "Full or abbreviated Quality System Evaluation Report.",
        "Validation Method (Inferred)": "Cross-reference with Joint Sectoral Committee specifications."
    },
    {
        "Task Name": "PMA Supplement (CBE)",
        "Target Regulatory Context": "21 CFR 814.39(d)",
        "Prompt Objective": "Draft a 'Special PMA Supplement - Changes Being Effected' for safety warnings.",
        "Required Input Data": "New safety information and current labeling.",
        "Expected Output Format": "Formal letter marked 'Special PMA Supplement—CBE'.",
        "Validation Method (Inferred)": "Compare against criteria in 21 CFR 814.39(d)(1)-(2)."
    },
    {
        "Task Name": "De Novo Request Preparation",
        "Target Regulatory Context": "21 CFR Part 860 Subpart D",
        "Prompt Objective": "Generate a summary of risks and mitigations for a De Novo classification request.",
        "Required Input Data": "Probable risks and proposed mitigation measures.",
        "Expected Output Format": "Structured table or list.",
        "Validation Method (Inferred)": "Review against 21 CFR 860.220(a)(9)."
    },
    {
        "Task Name": "Correction and Removal Reporting",
        "Target Regulatory Context": "21 CFR Part 806",
        "Prompt Objective": "Draft a written report to FDA for a device correction or removal.",
        "Required Input Data": "UDI, event description, and consignee list.",
        "Expected Output Format": "Formal report following 21 CFR 806.10(c)(1).",
        "Validation Method (Inferred)": "Cross-check fields against 21 CFR 806.10 mandatory info list."
    },
    {
        "Task Name": "Reclassification Petitioning",
        "Target Regulatory Context": "21 CFR Part 860 Subpart C",
        "Prompt Objective": "Prepare a statement of the basis for disagreement with a current device classification.",
        "Required Input Data": "Device type, requested action, and scientific evidence.",
        "Expected Output Format": "Formal petition document.",
        "Validation Method (Inferred)": "Assess if evidence meets standards in 21 CFR 860.7."
    },
    {
        "Task Name": "Public Hearing Participation",
        "Target Regulatory Context": "21 CFR Part 12",
        "Prompt Objective": "Complete a Notice of Participation for a formal evidentiary public hearing.",
        "Required Input Data": "Docket number, contact info, and specific interests.",
        "Expected Output Format": "Standardized form (21 CFR 12.45).",
        "Validation Method (Inferred)": "Confirm submission within 30 days of hearing notice."
    },
    {
        "Task Name": "Privacy Act Auditing",
        "Target Regulatory Context": "21 CFR Part 21.20",
        "Prompt Objective": "Draft a notice for a new FDA Privacy Act Record System.",
        "Required Input Data": "System name, location, and categories of individuals.",
        "Expected Output Format": "Federal Register notice format.",
        "Validation Method (Inferred)": "Compare against requirements in 21 CFR 21.20(b)(1-11)."
    },
    {
        "Task Name": "Informed Consent Exception (Emergency)",
        "Target Regulatory Context": "21 CFR Part 50.24",
        "Prompt Objective": "Draft IRB documentation for an exception from informed consent in emergency research.",
        "Required Input Data": "Clinical protocol and community consultation plans.",
        "Expected Output Format": "IRB justification document.",
        "Validation Method (Inferred)": "Check against 21 CFR 50.24 criteria (a)(1) through (a)(7)."
    },
    {
        "Task Name": "GLP Quality Assurance",
        "Target Regulatory Context": "21 CFR Part 58.35",
        "Prompt Objective": "Prepare a statement for a nonclinical study report certifying inspection dates.",
        "Required Input Data": "Master schedule, protocol, and inspection records.",
        "Expected Output Format": "Signed QA Statement.",
        "Validation Method (Inferred)": "Verify inclusion of dates as required by 21 CFR 58.35(b)(7)."
    },
    {
        "Task Name": "Patent Term Restoration Eligibility",
        "Target Regulatory Context": "21 CFR Part 60",
        "Prompt Objective": "Determine if a medical product's review period qualifies for patent term restoration.",
        "Required Input Data": "Marketing approval date, patent number, and chronology.",
        "Expected Output Format": "Formal eligibility assessment letter.",
        "Validation Method (Inferred)": "Verify calculation logic against 21 CFR 60.10 and 60.22."
    },
    {
        "Task Name": "IRB Protocol Review",
        "Target Regulatory Context": "21 CFR Part 56",
        "Prompt Objective": "Evaluate a clinical investigation protocol to ensure it meets IRB approval criteria.",
        "Required Input Data": "Clinical protocol and informed consent forms.",
        "Expected Output Format": "Checklist of compliance items.",
        "Validation Method (Inferred)": "Verify against approval criteria in 21 CFR 56.111."
    },
    {
        "Task Name": "Medical Device Recall Strategy",
        "Target Regulatory Context": "21 CFR Part 810 / Part 7",
        "Prompt Objective": "Develop a mandatory recall strategy for a device posing health risks.",
        "Required Input Data": "Health hazard evaluation and distribution lists.",
        "Expected Output Format": "Structured strategy document.",
        "Validation Method (Inferred)": "Review against 21 CFR 810.14 and 7.42."
    },
    {
        "Task Name": "Off-Label Information Dissemination",
        "Target Regulatory Context": "21 CFR Part 99",
        "Prompt Objective": "Prepare a mandatory disclosure statement for disseminating peer-reviewed articles on unapproved uses.",
        "Required Input Data": "Journal article and cleared labeling.",
        "Expected Output Format": "Prominently displayed warning statement.",
        "Validation Method (Inferred)": "Confirm statement matches verbatim requirements in 21 CFR 99.103."
    },
    {
        "Task Name": "Part 11 Closed System Audit",
        "Target Regulatory Context": "21 CFR Part 11",
        "Prompt Objective": "Audit a software supplier's closed system for electronic record integrity.",
        "Required Input Data": "Record retrieval protocols and audit trail logs.",
        "Expected Output Format": "Audit report with checklist.",
        "Validation Method (Inferred)": "Compare system features against 21 CFR 11.10."
    },
    {
        "Task Name": "Financial Disclosure Certification",
        "Target Regulatory Context": "21 CFR Part 54",
        "Prompt Objective": "Identify required financial disclosure forms and draft attestations for clinical investigators.",
        "Required Input Data": "Payment records and equity interest data.",
        "Expected Output Format": "FDA Form 3454/3455 or formal letter.",
        "Validation Method (Inferred)": "Cross-reference thresholds ( $25k/$ 50k) against records."
    },
    {
        "Task Name": "Parallel Review Request",
        "Target Regulatory Context": "FDA/CMS Program",
        "Prompt Objective": "Draft an email requesting enrollment in the Parallel Review program.",
        "Required Input Data": "Regulatory history and public health impact statement.",
        "Expected Output Format": "Formal professional email.",
        "Validation Method (Inferred)": "Check against the five enrollment criteria for CDRH/CMS."
    },
    {
        "Task Name": "Combination Product Jurisdiction",
        "Target Regulatory Context": "21 CFR Part 3",
        "Prompt Objective": "Prepare a Request for Designation (RFD) to identify primary FDA jurisdiction.",
        "Required Input Data": "Product composition and Primary Mode of Action (PMOA).",
        "Expected Output Format": "Formal 15-page (max) RFD letter.",
        "Validation Method (Inferred)": "Review PMOA determination against 21 CFR 3.2(m)."
    },
    {
        "Task Name": "Medicare Coverage Request (IDE)",
        "Target Regulatory Context": "CMS Guidelines",
        "Prompt Objective": "Prepare a request packet for CMS reimbursement of an IDE study.",
        "Required Input Data": "FDA IDE approval letter and NCT number.",
        "Expected Output Format": "CMS request letter and crosswalk table.",
        "Validation Method (Inferred)": "Verify against the 10 regulatory Medicare coverage criteria."
    },
    {
        "Task Name": "Cyber Device Security Plan",
        "Target Regulatory Context": "FD&C Act 524B",
        "Prompt Objective": "Draft a postmarket cybersecurity plan and Software Bill of Materials (SBOM).",
        "Required Input Data": "Software architecture and list of components.",
        "Expected Output Format": "Technical documentation for eSTAR.",
        "Validation Method (Inferred)": "Check against FDA Cybersecurity guidance."
    },
    {
        "Task Name": "Human Factors/Usability Summary",
        "Target Regulatory Context": "FDA HF Guidance",
        "Prompt Objective": "Summarize usability testing results to demonstrate minimized use-related risks.",
        "Required Input Data": "Usability test protocols and summative data.",
        "Expected Output Format": "Markdown table or narrative summary.",
        "Validation Method (Inferred)": "Review against 'Applying Human Factors' guidance and IEC 62366."
    }
]

category_mapping = {
    "submissions": [
        "510(k) Substantial Equivalence Preparation",
        "IDE Application Preparation",
        "Premarket Approval (PMA) Preparation",
        "PMA Post-approval Reporting",
        "RTA Checklist Preparation",
        "Intended Use and Indications for Use Alignment",
        "Shelf-life Study Rationale",
        "Humanitarian Device Exemption (HDE)",
        "PMA Supplement (CBE)",
        "De Novo Request Preparation",
        "Reclassification Petitioning",
        "Parallel Review Request",
        "Combination Product Jurisdiction",
        "Medicare Coverage Request (IDE)"
    ],
    "compliance": [
        "Quality System Audit",
        "Risk Management Analysis",
        "Medical Device Reporting (MDR)",
        "UDI GUDID Submission",
        "Labeling Compliance Audit",
        "Quality System Evaluation (MRA)",
        "Correction and Removal Reporting",
        "GLP Quality Assurance",
        "IRB Protocol Review",
        "Medical Device Recall Strategy",
        "Off-Label Information Dissemination",
        "Part 11 Closed System Audit",
        "Financial Disclosure Certification",
        "Cyber Device Security Plan",
        "Human Factors/Usability Summary"
    ],
    "food_safety": [
        "Foreign Supplier Verification Program (FSVP) Audit",
        "Establishment of Food Traceability Plan",
        "Food Safety Audit Reporting (Regulatory)",
        "Directed Food Laboratory Order Verification"
    ],
    "device_specifics": [
        "Automated Image Assessment System 510(k)",
        "Special Controls Labeling Compliance",
        "Zika Virus Reagent Study Design",
        "Carrier Screening System 510(k)",
        "Design Verification for BCR-ABL Tests",
        "NGS Tumor Profiling Documentation",
        "Clinical Chemistry Device Classification",
        "iCGM Clinical Testing Strategy"
    ],
    "administrative": [
        "Medical Device Administrative Detention Appeal",
        "Import Entry Data Element Compilation",
        "Civil Money Penalties Hearing Response",
        "Citizen Petition Preparation",
        "Freedom of Information Act (FOIA) Request",
        "21 CFR Part 14 Auditing",
        "Public Hearing Participation",
        "Privacy Act Auditing",
        "Informed Consent Exception (Emergency)",
        "Patent Term Restoration Eligibility"
    ]
}

def to_snake_case(text):
    text = re.sub(r'[\(\)]', '', text)
    text = re.sub(r'[\s\-/]+', '_', text)
    return text.lower()

def generate_prompts():
    base_dir = "prompts/regulatory"

    # Reverse mapping for easy lookup
    task_category = {}
    for cat, titles in category_mapping.items():
        for title in titles:
            task_category[title] = cat

    # Group tasks by category to handle numbering
    tasks_by_category = {cat: [] for cat in category_mapping}

    for task in tasks:
        name = task["Task Name"]
        if name in task_category:
            tasks_by_category[task_category[name]].append(task)
        else:
            print(f"Warning: Task '{name}' not mapped to any category.")

    for category, category_tasks in tasks_by_category.items():
        dir_path = os.path.join(base_dir, category)
        os.makedirs(dir_path, exist_ok=True)

        # Sort tasks to ensure deterministic order (though list order is preserved)
        # category_tasks.sort(key=lambda x: x["Task Name"])

        for i, task in enumerate(category_tasks):
            file_number = f"{i+1:02d}"
            snake_name = to_snake_case(task["Task Name"])
            filename = f"{file_number}_{snake_name}.prompt.yaml"
            filepath = os.path.join(dir_path, filename)

            prompt_content = {
                "name": task["Task Name"],
                "description": task["Prompt Objective"],
                "model": "gpt-4o",
                "modelParameters": {
                    "temperature": 0.2
                },
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            f"You are a Regulatory Affairs Expert specializing in {task['Target Regulatory Context']}.\n"
                            f"Your task is to: {task['Prompt Objective']}\n\n"
                            f"Input Data Required: {task['Required Input Data']}\n"
                            f"Expected Output Format: {task['Expected Output Format']}\n"
                            f"Validation Criteria: {task['Validation Method (Inferred)']}\n\n"
                            "Ensure strict adherence to the specified regulations."
                        )
                    },
                    {
                        "role": "user",
                        "content": (
                            "Please draft the required documentation based on the following details:\n\n"
                            "{{input_data}}"
                        )
                    }
                ],
                "testData": [
                    {
                        "input": {
                            "input_data": f"Example data for {task['Task Name']}..."
                        },
                        "expected": f"A valid {task['Expected Output Format']} compliant with {task['Target Regulatory Context']}."
                    }
                ],
                "evaluators": [
                    {
                        "name": "Compliance Check",
                        "regex": {
                            "pattern": f"(?i)({re.escape(task['Target Regulatory Context'].split()[0])})" # Basic check for reg mention
                        }
                    }
                ]
            }

            # Custom Dumper to handle list indentation correctly for yamllint
            class IndentDumper(yaml.Dumper):
                def increase_indent(self, flow=False, indentless=False):
                    return super(IndentDumper, self).increase_indent(flow, False)

            with open(filepath, 'w') as f:
                f.write("---\n")
                yaml.dump(prompt_content, f, Dumper=IndentDumper, sort_keys=False, width=1000)

            print(f"Generated: {filepath}")

if __name__ == "__main__":
    generate_prompts()
