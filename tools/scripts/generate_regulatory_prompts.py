#!/usr/bin/env python3
"""
Generate regulatory prompts based on a predefined list of tasks.
This script creates prompt files in the appropriate directories under prompts/regulatory/.
"""

import os
import re
import sys
import yaml
from pathlib import Path

# Add the current directory to sys.path to import utils if needed
sys.path.append(str(Path(__file__).parent))

try:
    from utils import PROMPTS_DIR
except ImportError:
    # Fallback if utils not found or running from elsewhere
    PROMPTS_DIR = Path(__file__).resolve().parents[2] / "prompts"

REGULATORY_DIR = PROMPTS_DIR / "regulatory"

class StrPresenter(str):
    pass

def presenter(dumper, data):
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(StrPresenter, presenter)

class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)

TASKS = [
    {
        "name": "510(k) Substantial Equivalence Preparation",
        "context": "21 CFR Part 807 Subpart E",
        "objective": "Draft a substantial equivalence comparison and summary between a subject device and predicate(s) to demonstrate safety and effectiveness.",
        "input": "Device description, indications for use, technological characteristics, performance data, and predicate device identification.",
        "output_format": "Formal 510(k) Summary or Markdown table as per 21 CFR 807.92.",
        "validation": "Review against 21 CFR 807.87, 807.92, and FDA guidance on evaluating substantial equivalence.",
        "category": "submissions"
    },
    {
        "name": "Quality System Audit",
        "context": "21 CFR Part 820",
        "objective": "Generate an internal audit checklist or report focusing on design controls, production processes, and risk-based decision making.",
        "input": "Quality Manual, Design History File (DHF) excerpts, SOPs, and previous audit reports.",
        "output_format": "Formal audit report or Markdown checklist with regulatory citations.",
        "validation": "Verify against requirements in 21 CFR 820 (Subparts B-O) and relevant transition modules (QMSR).",
        "category": "quality"
    },
    {
        "name": "Risk Management Analysis",
        "context": "ISO 14971 / 21 CFR 820.30",
        "objective": "Perform a risk analysis (e.g., PHA) to identify potential hazards, hazardous situations, and mitigation strategies.",
        "input": "Intended use, design specifications, foreseeable misuse, and historical data for similar devices.",
        "output_format": "Risk Analysis Matrix (Markdown table) including Hazard, Harm, Severity, and Probability.",
        "validation": "Cross-reference with ISO 14971 principles and FDA training modules on Risk Management.",
        "category": "quality"
    },
    {
        "name": "IDE Application Preparation",
        "context": "21 CFR Part 812",
        "objective": "Draft an Investigational Device Exemption (IDE) application, including risk analysis and investigational plans for clinical studies.",
        "input": "Investigational plan, report of prior investigations, investigator agreements, and device labeling.",
        "output_format": "Formal IDE application package following the sequence in 21 CFR 812.25.",
        "validation": "Verify inclusion of all elements required by 21 CFR 812.20 and 812.25.",
        "category": "submissions"
    },
    {
        "name": "Premarket Approval (PMA) Preparation",
        "context": "21 CFR Part 814",
        "objective": "Draft a detailed summary of a PMA application, including clinical investigation results and manufacturing history.",
        "input": "Clinical results, nonclinical lab data, device characteristics, and marketing history.",
        "output_format": "Formal structured summary as per 21 CFR 814.20(b)(3).",
        "validation": "Review against specific summary requirements listed in 21 CFR 814.20(b)(3)(i-vi).",
        "category": "submissions"
    },
    {
        "name": "PMA Post-approval Reporting",
        "context": "21 CFR Part 814.82 / 814.84",
        "objective": "Compile a summary of post-approval requirements, including clinical study data, manufacturing changes, and scientific literature.",
        "input": "PMA approval order, study data, change logs, and bibliography of recent literature.",
        "output_format": "Formal report to the Office of Device Evaluation.",
        "validation": "Verify compliance with 21 CFR 814.82 and 814.84 submission requirements.",
        "category": "submissions"
    },
    {
        "name": "Medical Device Administrative Detention Appeal",
        "context": "21 CFR Part 1.402 / 800.55",
        "objective": "Draft a written appeal for an administrative detention order issued on a food item or medical device.",
        "input": "Detention order number, date received, and verified statement of ownership/proprietary interest.",
        "output_format": "Formal legal letter.",
        "validation": "Verify submission within the required timeframe (10 days for food, 5 days for devices) per 21 CFR 1.402 or 800.55.",
        "category": "administrative"
    },
    {
        "name": "Foreign Supplier Verification Program (FSVP) Audit",
        "context": "21 CFR Part 1 Subpart L",
        "objective": "Draft a summary report of an onsite audit for a foreign food supplier including conclusions and corrective actions.",
        "input": "Audit procedures, dates, findings on processes, and records of deficiencies.",
        "output_format": "Formal audit report in Markdown format.",
        "validation": "Cross-reference against 21 CFR 1.506(e)(1)(i)(D) requirements for audit documentation.",
        "category": "food_safety"
    },
    {
        "name": "Establishment of Food Traceability Plan",
        "context": "21 CFR Part 1 Subpart S",
        "objective": "Create a structured traceability plan for a facility handling foods on the Food Traceability List.",
        "input": "List of foods handled, record maintenance procedures, and contact information.",
        "output_format": "Structured text document with sections for procedures and identification.",
        "validation": "Ensure all requirements of 21 CFR 1.1315(a) (1-5) are addressed.",
        "category": "food_safety"
    },
    {
        "name": "Food Safety Audit Reporting (Regulatory)",
        "context": "21 CFR Part 1 Subpart M",
        "objective": "Draft a regulatory audit report for an eligible entity after a food safety audit.",
        "input": "Facility identity (FEI), audit dates, scope, and identified deficiencies.",
        "output_format": "Structured Markdown table or list.",
        "validation": "Verify that all 9 specific data elements listed in 21 CFR 1.652(b) are present.",
        "category": "food_safety"
    },
    {
        "name": "Directed Food Laboratory Order Verification",
        "context": "21 CFR Part 1 Subpart R",
        "objective": "Review a Directed Food Laboratory Order to identify mandatory testing parameters.",
        "input": "FDA issued Directed Food Laboratory Order.",
        "output_format": "Key-value list of product, environment, methods, and timeframes.",
        "validation": "Compare parameters with specifications in 21 CFR 1.1108(b).",
        "category": "food_safety"
    },
    {
        "name": "Import Entry Data Element Compilation",
        "context": "21 CFR Part 1 Subpart D",
        "objective": "Compile required identifying information (510(k), UFI, NDC, NDA) for electronic import entry of drugs or devices.",
        "input": "Clearance documentation, registration numbers, and listing information.",
        "output_format": "JSON object or alphanumeric string.",
        "validation": "Check compliance with 21 CFR 1.74(a) and 1.76(c) for ACE system mapping.",
        "category": "administrative"
    },
    {
        "name": "Automated Image Assessment System 510(k)",
        "context": "21 CFR 866.2190",
        "objective": "Draft a detailed device description for an automated image assessment system for microbial colonies.",
        "input": "Technology details, software modules, and expert rules for colony assessment.",
        "output_format": "Formal technical document.",
        "validation": "Verify content against requirements in 21 CFR 866.2190(b)(1)-(5).",
        "category": "device_specifics"
    },
    {
        "name": "Special Controls Labeling Compliance",
        "context": "21 CFR 866.3169",
        "objective": "Generate mandatory labeling content, including warnings and limitations, for HCV antibody tests.",
        "input": "Specimen types, clinical population data, and performance characteristics.",
        "output_format": "Structured labeling text.",
        "validation": "Cross-check warnings against requirements in 21 CFR 866.3169(b)(1).",
        "category": "device_specifics"
    },
    {
        "name": "Zika Virus Reagent Study Design",
        "context": "21 CFR 866.3935",
        "objective": "Draft a protocol for analytical performance studies to validate Zika virus serological reagents.",
        "input": "Reference material details, cross-reactivity targets, and specimen stability.",
        "output_format": "Technical study protocol.",
        "validation": "Ensure protocol covers analytical studies mandated by 21 CFR 866.3935(b)(2)(ii).",
        "category": "device_specifics"
    },
    {
        "name": "Carrier Screening System 510(k)",
        "context": "21 CFR 866.5940",
        "objective": "Compile technical information for an autosomal recessive carrier screening gene mutation detection system.",
        "input": "Gene list (HUGO), variant coordinates, and clinical validity evidence.",
        "output_format": "Comprehensive technical summary report.",
        "validation": "Check against technical info requirements in 21 CFR 866.5940(b)(3)(i).",
        "category": "device_specifics"
    },
    {
        "name": "Design Verification for BCR-ABL Tests",
        "context": "21 CFR 866.6060",
        "objective": "Outline design verification and validation requirements for a BCR-ABL quantitation test.",
        "input": "Variant types, IS conversion methodology, and calibration control data.",
        "output_format": "Validation checklist or matrix.",
        "validation": "Review against submission requirements in 21 CFR 866.6060(b)(1).",
        "category": "device_specifics"
    },
    {
        "name": "NGS Tumor Profiling Documentation",
        "context": "21 CFR 866.6080",
        "objective": "Develop documentation supporting the clinical significance of mutations in an NGS-based tumor profiling panel.",
        "input": "Somatic mutations, professional guidelines, and method comparison data.",
        "output_format": "Tabulated summary of mutations categorized by evidence levels.",
        "validation": "Confirm categorization aligns with criteria in 21 CFR 866.6080(b)(1)(v).",
        "category": "device_specifics"
    },
    {
        "name": "Civil Money Penalties Hearing Response",
        "context": "21 CFR Part 17",
        "objective": "Draft a formal 'Answer' to an FDA complaint seeking civil money penalties.",
        "input": "FDA Complaint, alleged violations, and mitigating factors.",
        "output_format": "Formal legal pleading.",
        "validation": "Review against required contents for an Answer specified in 21 CFR 17.9.",
        "category": "administrative"
    },
    {
        "name": "Clinical Chemistry Device Classification",
        "context": "21 CFR Part 862",
        "objective": "Identify classification and regulatory requirements (general/special controls) for a clinical chemistry device.",
        "input": "Device name and intended use.",
        "output_format": "Structured summary identifying FDA Class and regulatory section.",
        "validation": "Verify classification against 21 CFR Part 862 Subparts A-D.",
        "category": "device_specifics"
    },
    {
        "name": "iCGM Clinical Testing Strategy",
        "context": "21 CFR 862.1355",
        "objective": "Draft a clinical study plan to demonstrate accuracy for an iCGM system.",
        "input": "Sensor specifications, target population, and wear period details.",
        "output_format": "Formal clinical study protocol outline.",
        "validation": "Compare against performance bounds listed in 21 CFR 862.1355(b)(1).",
        "category": "device_specifics"
    },
    {
        "name": "Citizen Petition Preparation",
        "context": "21 CFR Part 10.30",
        "objective": "Draft a Citizen Petition requesting administrative action by the Commissioner.",
        "input": "Factual/legal grounds, action requested, and environmental impact assessment.",
        "output_format": "Structured petition following 21 CFR 10.30(b)(3) format.",
        "validation": "Verify all required sections (Grounds, Certification, etc.) are present.",
        "category": "administrative"
    },
    {
        "name": "Medical Device Reporting (MDR)",
        "context": "21 CFR Part 803",
        "objective": "Summarize an adverse event for mandatory electronic submission or develop an MDR SOP.",
        "input": "Incident reports, outcome data, and device identification.",
        "output_format": "Structured summary (eMDR) or numbered SOP document.",
        "validation": "Review against reporting requirements in 21 CFR Part 803 and 803.17.",
        "category": "compliance"
    },
    {
        "name": "UDI GUDID Submission",
        "context": "21 CFR Part 830",
        "objective": "Prepare a Device Identifier (DI) record for GUDID submission.",
        "input": "Device label, packaging levels, and GTIN data.",
        "output_format": "Structured data list matching GUDID fields.",
        "validation": "Cross-check fields against GUDID DI Record preparation modules.",
        "category": "submissions"
    },
    {
        "name": "Freedom of Information Act (FOIA) Request",
        "context": "21 CFR Part 20",
        "objective": "Draft a request for records regarding a specific 510(k) clearance.",
        "input": "Description of records sought and requester contact information.",
        "output_format": "Formal letter following 21 CFR 20.40.",
        "validation": "Check against 'Search for Records' criteria in Part 20 Subpart C.",
        "category": "administrative"
    },
    {
        "name": "RTA Checklist Preparation",
        "context": "FDA RTA Policy",
        "objective": "Annotate the RTA checklist with page numbers and sections where requirements are addressed in a 510(k).",
        "input": "Draft 510(k) submission and appropriate FDA RTA checklist.",
        "output_format": "Annotated checklist with a comment column.",
        "validation": "Verify cited page numbers correspond to final submission PDF.",
        "category": "submissions"
    },
    {
        "name": "Intended Use and Indications for Use Alignment",
        "context": "21 CFR Part 801.4",
        "objective": "Review 510(k) drafts to ensure 'Intended Use' and 'Indications for Use' are verbatim and consistent.",
        "input": "Full 510(k) draft including labeling and executive summary.",
        "output_format": "Consistency report identifying discrepancies.",
        "validation": "Cross-reference all labeling statements for exact matches.",
        "category": "adherence"
    },
    {
        "name": "Shelf-life Study Rationale",
        "context": "21 CFR Part 801",
        "objective": "Draft a rationale for correlating accelerated aging data with real-time requirements.",
        "input": "Material stability data, packaging type, and aging protocols.",
        "output_format": "Formal technical report.",
        "validation": "Evaluate against FDA standards for shelf-life testing.",
        "category": "adherence"
    },
    {
        "name": "Labeling Compliance Audit",
        "context": "21 CFR Part 801",
        "objective": "Audit device labeling for compliance with mandatory elements (Manufacturer, UDI, date formats).",
        "input": "Product labels, symbols glossary, and 21 CFR 801 text.",
        "output_format": "Gap analysis report.",
        "validation": "Inspect label against 21 CFR 801.1 and 801.18.",
        "category": "compliance"
    },
    {
        "name": "21 CFR Part 14 Auditing",
        "context": "21 CFR Part 14",
        "objective": "Audit advisory committee meeting minutes for compliance with record-keeping elements.",
        "input": "Minutes, attendee list, and information considered.",
        "output_format": "Markdown compliance checklist.",
        "validation": "Verify presence of items listed in 21 CFR 14.60(b).",
        "category": "administrative"
    },
    {
        "name": "Humanitarian Device Exemption (HDE)",
        "context": "21 CFR Part 814 Subpart H",
        "objective": "Explain why the health benefit of a HUD outweighs the risk of injury.",
        "input": "HUD designation and risk-benefit analysis of alternatives.",
        "output_format": "Formal narrative explanation.",
        "validation": "Check against HDE contents specified in 21 CFR 814.104(b)(3).",
        "category": "submissions"
    },
    {
        "name": "Quality System Evaluation (MRA)",
        "context": "21 CFR 820 / MRA Subpart B",
        "objective": "Generate a quality system evaluation report for a manufacturer under the US-EC MRA.",
        "input": "Onsite inspection data and manufacturing records.",
        "output_format": "Full or abbreviated Quality System Evaluation Report.",
        "validation": "Cross-reference with Joint Sectoral Committee specifications.",
        "category": "quality"
    },
    {
        "name": "PMA Supplement (CBE)",
        "context": "21 CFR 814.39(d)",
        "objective": "Draft a 'Special PMA Supplement - Changes Being Effected' for safety warnings.",
        "input": "New safety information and current labeling.",
        "output_format": "Formal letter marked 'Special PMA Supplement—CBE'.",
        "validation": "Compare against criteria in 21 CFR 814.39(d)(1)-(2).",
        "category": "submissions"
    },
    {
        "name": "De Novo Request Preparation",
        "context": "21 CFR Part 860 Subpart D",
        "objective": "Generate a summary of risks and mitigations for a De Novo classification request.",
        "input": "Probable risks and proposed mitigation measures.",
        "output_format": "Structured table or list.",
        "validation": "Review against 21 CFR 860.220(a)(9).",
        "category": "submissions"
    },
    {
        "name": "Correction and Removal Reporting",
        "context": "21 CFR Part 806",
        "objective": "Draft a written report to FDA for a device correction or removal.",
        "input": "UDI, event description, and consignee list.",
        "output_format": "Formal report following 21 CFR 806.10(c)(1).",
        "validation": "Cross-check fields against 21 CFR 806.10 mandatory info list.",
        "category": "compliance"
    },
    {
        "name": "Reclassification Petitioning",
        "context": "21 CFR Part 860 Subpart C",
        "objective": "Prepare a statement of the basis for disagreement with a current device classification.",
        "input": "Device type, requested action, and scientific evidence.",
        "output_format": "Formal petition document.",
        "validation": "Assess if evidence meets standards in 21 CFR 860.7.",
        "category": "administrative"
    },
    {
        "name": "Public Hearing Participation",
        "context": "21 CFR Part 12",
        "objective": "Complete a Notice of Participation for a formal evidentiary public hearing.",
        "input": "Docket number, contact info, and specific interests.",
        "output_format": "Standardized form (21 CFR 12.45).",
        "validation": "Confirm submission within 30 days of hearing notice.",
        "category": "administrative"
    },
    {
        "name": "Privacy Act Auditing",
        "context": "21 CFR Part 21.20",
        "objective": "Draft a notice for a new FDA Privacy Act Record System.",
        "input": "System name, location, and categories of individuals.",
        "output_format": "Federal Register notice format.",
        "validation": "Compare against requirements in 21 CFR 21.20(b)(1-11).",
        "category": "administrative"
    },
    {
        "name": "Informed Consent Exception (Emergency)",
        "context": "21 CFR Part 50.24",
        "objective": "Draft IRB documentation for an exception from informed consent in emergency research.",
        "input": "Clinical protocol and community consultation plans.",
        "output_format": "IRB justification document.",
        "validation": "Check against 21 CFR 50.24 criteria (a)(1) through (a)(7).",
        "category": "adherence"
    },
    {
        "name": "GLP Quality Assurance",
        "context": "21 CFR Part 58.35",
        "objective": "Prepare a statement for a nonclinical study report certifying inspection dates.",
        "input": "Master schedule, protocol, and inspection records.",
        "output_format": "Signed QA Statement.",
        "validation": "Verify inclusion of dates as required by 21 CFR 58.35(b)(7).",
        "category": "quality"
    },
    {
        "name": "Patent Term Restoration Eligibility",
        "context": "21 CFR Part 60",
        "objective": "Determine if a medical product's review period qualifies for patent term restoration.",
        "input": "Marketing approval date, patent number, and chronology.",
        "output_format": "Formal eligibility assessment letter.",
        "validation": "Verify calculation logic against 21 CFR 60.10 and 60.22.",
        "category": "administrative"
    },
    {
        "name": "IRB Protocol Review",
        "context": "21 CFR Part 56",
        "objective": "Evaluate a clinical investigation protocol to ensure it meets IRB approval criteria.",
        "input": "Clinical protocol and informed consent forms.",
        "output_format": "Checklist of compliance items.",
        "validation": "Verify against approval criteria in 21 CFR 56.111.",
        "category": "compliance"
    },
    {
        "name": "Medical Device Recall Strategy",
        "context": "21 CFR Part 810 / Part 7",
        "objective": "Develop a mandatory recall strategy for a device posing health risks.",
        "input": "Health hazard evaluation and distribution lists.",
        "output_format": "Structured strategy document.",
        "validation": "Review against 21 CFR 810.14 and 7.42.",
        "category": "compliance"
    },
    {
        "name": "Off-Label Information Dissemination",
        "context": "21 CFR Part 99",
        "objective": "Prepare a mandatory disclosure statement for disseminating peer-reviewed articles on unapproved uses.",
        "input": "Journal article and cleared labeling.",
        "output_format": "Prominently displayed warning statement.",
        "validation": "Confirm statement matches verbatim requirements in 21 CFR 99.103.",
        "category": "adherence"
    },
    {
        "name": "Part 11 Closed System Audit",
        "context": "21 CFR Part 11",
        "objective": "Audit a software supplier's closed system for electronic record integrity.",
        "input": "Record retrieval protocols and audit trail logs.",
        "output_format": "Audit report with checklist.",
        "validation": "Compare system features against 21 CFR 11.10.",
        "category": "quality"
    },
    {
        "name": "Financial Disclosure Certification",
        "context": "21 CFR Part 54",
        "objective": "Identify required financial disclosure forms and draft attestations for clinical investigators.",
        "input": "Payment records and equity interest data.",
        "output_format": "FDA Form 3454/3455 or formal letter.",
        "validation": "Cross-reference thresholds ($25k/$50k) against records.",
        "category": "administrative"
    },
    {
        "name": "Parallel Review Request",
        "context": "FDA/CMS Program",
        "objective": "Draft an email requesting enrollment in the Parallel Review program.",
        "input": "Regulatory history and public health impact statement.",
        "output_format": "Formal professional email.",
        "validation": "Check against the five enrollment criteria for CDRH/CMS.",
        "category": "submissions"
    },
    {
        "name": "Combination Product Jurisdiction",
        "context": "21 CFR Part 3",
        "objective": "Prepare a Request for Designation (RFD) to identify primary FDA jurisdiction.",
        "input": "Product composition and Primary Mode of Action (PMOA).",
        "output_format": "Formal 15-page (max) RFD letter.",
        "validation": "Review PMOA determination against 21 CFR 3.2(m).",
        "category": "submissions"
    },
    {
        "name": "Medicare Coverage Request (IDE)",
        "context": "CMS Guidelines",
        "objective": "Prepare a request packet for CMS reimbursement of an IDE study.",
        "input": "FDA IDE approval letter and NCT number.",
        "output_format": "CMS request letter and crosswalk table.",
        "validation": "Verify against the 10 regulatory Medicare coverage criteria.",
        "category": "submissions"
    },
    {
        "name": "Cyber Device Security Plan",
        "context": "FD&C Act 524B",
        "objective": "Draft a postmarket cybersecurity plan and Software Bill of Materials (SBOM).",
        "input": "Software architecture and list of components.",
        "output_format": "Technical documentation for eSTAR.",
        "validation": "Check against FDA Cybersecurity guidance.",
        "category": "compliance"
    },
    {
        "name": "Human Factors/Usability Summary",
        "context": "FDA HF Guidance",
        "objective": "Summarize usability testing results to demonstrate minimized use-related risks.",
        "input": "Usability test protocols and summative data.",
        "output_format": "Markdown table or narrative summary.",
        "validation": "Review against 'Applying Human Factors' guidance and IEC 62366.",
        "category": "adherence"
    }
]

def to_snake_case(text):
    text = text.lower()
    text = re.sub(r'[\(\)/]+', '_', text)  # Replace (, ), / with _
    text = re.sub(r'[^a-z0-9_]', '_', text) # Replace other non-alnum with _
    text = re.sub(r'_+', '_', text)         # Collapse multiple _
    text = text.strip('_')
    return text

def get_next_number(directory):
    if not directory.exists():
        return 1
    existing = [f for f in directory.glob("*.prompt.yaml")]
    max_num = 0
    for f in existing:
        match = re.match(r'(\d+)_', f.name)
        if match:
            max_num = max(max_num, int(match.group(1)))
    return max_num + 1

def generate_prompt_yaml(task, category_dir):
    snake_name = to_snake_case(task['name'])

    # Check if file already exists with any number
    existing_file = None
    if category_dir.exists():
        for f in category_dir.glob(f"*_{snake_name}.prompt.yaml"):
            existing_file = f
            break

    if existing_file:
        filepath = existing_file
        print(f"Updating existing {filepath}")
    else:
        number = get_next_number(category_dir)
        filename = f"{number:02d}_{snake_name}.prompt.yaml"
        filepath = category_dir / filename
        print(f"Creating new {filepath}")

    content = {
        "name": task['name'],
        "description": task['objective'],
        "model": "gpt-4o",
        "modelParameters": {
            "temperature": 0.5
        },
        "messages": [
            {
                "role": "system",
                "content": StrPresenter(f"""You are an expert Regulatory Affairs Specialist capable of handling complex FDA and ISO compliance tasks.

## Context
{task['context']}

## Objective
{task['objective']}

## Output Format
{task['output_format']}""")
            },
            {
                "role": "user",
                "content": StrPresenter(f"""Please perform the task using the following input data:

<input>
{{{{input}}}}
</input>""")
            }
        ],
        "testData": [
            {
                "input": StrPresenter(f"{task['input']} (Example data)"),
                "expected": "Expected output as per instructions."
            }
        ],
        "evaluators": [
            {
                "name": "Validation Check",
                "regex": f"(?i){re.escape(task['validation'].split()[0])}" if task['validation'] else ".*"
            }
        ]
    }

    with open(filepath, 'w') as f:
        f.write("---\n")
        yaml.dump(content, f, Dumper=IndentDumper, sort_keys=False, width=1000)

def update_overview(directory):
    overview_file = directory / "overview.md"
    title = directory.name.replace("_", " ").title()
    content = f"# {title} Overview\n\n"

    prompts = sorted(directory.glob("*.prompt.yaml"))
    for p in prompts:
        try:
            with open(p, 'r') as f:
                docs = list(yaml.safe_load_all(f))
                data = docs[0] if docs else {}
                name = data.get('name', p.stem)
        except Exception:
            name = p.stem

        content += f"- [{name}]({p.name})\n"

    with open(overview_file, 'w') as f:
        f.write(content)
    print(f"Updated {overview_file}")

def main():
    for task in TASKS:
        category = task.get('category', 'misc')
        category_dir = REGULATORY_DIR / category
        os.makedirs(category_dir, exist_ok=True)

        generate_prompt_yaml(task, category_dir)

    for category_dir in REGULATORY_DIR.iterdir():
        if category_dir.is_dir():
            update_overview(category_dir)

if __name__ == "__main__":
    main()
