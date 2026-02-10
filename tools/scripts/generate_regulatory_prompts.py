
import re
import yaml
import os
from pathlib import Path

# Custom YAML dumper for correct formatting
class CustomDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(CustomDumper, self).increase_indent(flow, False)

def str_presenter(dumper, data):
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

CustomDumper.add_representer(str, str_presenter)

# Improved regex to capture Name, Context, and the start of Objective (Verb)
REGEX_START = r"^(?P<name>.+?)\s+(?P<context>(?:21 CFR|ISO|FDA|CMS|FD&C|Public Law).*?)\s+(?P<verb>(?:Draft|Generate|Perform|Compile|Create|Review|Identify|Develop|Outline|Summarize|Prepare|Explain|Complete|Determine|Evaluate|Audit|Annotate))\s+(?P<rest>.*)$"

CATEGORIES = {
    "submissions": ["510(k)", "PMA", "IDE", "De Novo", "Reclassification", "HDE", "Parallel Review", "Combination Product", "RFD", "Pre-Submission", "Q-Submission", "Master File", "Breakthrough", "STeP", "513(g)", "RTA Checklist", "Intended Use", "Shelf-life", "Medical Device Administrative Detention", "Civil Money Penalties", "Citizen Petition", "Patent Term", "Medicare", "Establishment Registration", "Import Entry", "Public Hearing", "Privacy Act", "FOIA", "Appeals"],
    "compliance": ["Audit", "MDR", "Correction", "Removal", "Recall", "Part 11", "GLP", "GCP", "QSR", "QSIT", "Risk Management", "Labeling Compliance", "Quality System", "Informed Consent", "IRB", "Financial Disclosure", "Off-Label", "Human Factors", "Cyber Device Security"],
    "food_safety": ["Food", "FSVP", "Traceability", "Laboratory"],
    "device_specifics": ["Automated Image", "Special Controls", "Zika", "Carrier Screening", "Design Verification", "NGS", "Clinical Chemistry", "iCGM"],
    "administrative": [] # Fallback
}

PROMPTS_DIR = Path("prompts/regulatory")

def to_snake_case(name):
    name = name.lower()
    name = name.replace("/", "_")
    name = re.sub(r'[^a-z0-9_]+', '_', name)
    name = name.strip('_')
    return name

def get_category(name):
    for cat, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw.lower() in name.lower():
                return cat
            if name == "Medical Device Administrative Detention Appeal": return "administrative"
            if name == "Civil Money Penalties Hearing Response": return "administrative"
            if name == "Citizen Petition Preparation": return "administrative"
            if name == "Freedom of Information Act (FOIA) Request": return "administrative"
            if name == "Public Hearing Participation": return "administrative"
            if name == "Privacy Act Auditing": return "administrative"
            if name == "Patent Term Restoration Eligibility": return "administrative"
            if name == "Medicare Coverage Request (IDE) CMS Guidelines": return "administrative"
            if name == "Import Entry Data Element Compilation": return "administrative"

    return "compliance" # Default

def generate_yaml_content(task):
    content = {
        "name": task['name'],
        "description": task['objective'].rstrip('.'),
        "model": "gpt-4o",
        "modelParameters": {
            "temperature": 0.2
        },
        "messages": [
            {
                "role": "system",
                "content": f"You are a Regulatory Affairs Specialist and Technical Writer acting as a 'Regulatory Architect'.\n\nYour task is to {task['objective'].lower().rstrip('.')}\n\nTarget Regulatory Context: {task['context']}\n\nYou must strictly follow the output format: {task['output']}\n\nValidation Method: {task['validation']}"
            },
            {
                "role": "user",
                "content": f"Please {task['name'].lower()} using the following input data:\n\n{{{{input_data}}}}"
            }
        ],
        "testData": [
            {
                "input": {
                    "input_data": f"Example data for {task['name']}: {task['input']}"
                },
                "expected": f"A {task['output']} that passes validation: {task['validation']}"
            }
        ],
        "evaluators": [
            {
                "name": "Validation Check",
                "regex": {
                    "pattern": "(?i)(" + "|".join(re.findall(r'\b[A-Z][a-z]+\b', task['validation'])[:3]) + ")"
                }
            }
        ]
    }
    return content

def main():
    if not os.path.exists('tools/scripts/data/regulatory_tasks.txt'):
        print("Error: tools/scripts/data/regulatory_tasks.txt not found")
        return

    with open('tools/scripts/data/regulatory_tasks.txt', 'r') as f:
        lines = f.readlines()

    count = 0
    for i, line in enumerate(lines):
        if i == 0: continue
        line = line.strip()
        if not line: continue

        match = re.match(REGEX_START, line)
        if match:
            data = match.groupdict()
            verb = data['verb']
            rest = data['rest']

            # Split by period followed by space and Capital letter
            parts = re.split(r'(?<=\.)\s+(?=[A-Z])', rest)

            if len(parts) >= 4:
                # parts[0] is the rest of the objective (after verb)
                # But wait, if Objective was "Draft a summary.", parts[0] is "a summary."

                objective = verb + " " + parts[0]
                validation = parts[-1]
                output = parts[-2]
                input_data = " ".join(parts[1:-2])

                task = {
                    'name': data['name'],
                    'context': data['context'],
                    'objective': objective,
                    'input': input_data,
                    'output': output,
                    'validation': validation
                }

                category = get_category(task['name'])
                filename = to_snake_case(task['name']) + ".prompt.yaml"

                output_dir = PROMPTS_DIR / category
                output_dir.mkdir(parents=True, exist_ok=True)

                overview_path = output_dir / "overview.md"
                if not overview_path.exists():
                    overview_path.write_text(f"# {category.replace('_', ' ').title()}\n\nOverview of {category.replace('_', ' ')} regulatory prompts.\n")

                filepath = output_dir / filename

                yaml_content = generate_yaml_content(task)

                with open(filepath, 'w') as out:
                    out.write("---\n")
                    yaml.dump(yaml_content, out, Dumper=CustomDumper, default_flow_style=False, sort_keys=False)

                count += 1
                print(f"Generated {filepath}")
            else:
                print(f"Failed to split parts for line {i}: {line[:50]}... Parts: {len(parts)}")
        else:
            print(f"Failed to match start for line {i}: {line[:50]}...")

    print(f"Total generated: {count}")

if __name__ == "__main__":
    main()
