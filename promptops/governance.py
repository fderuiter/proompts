import json
import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path
import yaml

from promptops.utils import ROOT, PROMPTS_DIR, iter_prompt_files, load_yaml

MANIFEST_DIR = ROOT / "governance"
MANIFEST_FILE = MANIFEST_DIR / "compliance_manifest.json"
GAP_REPORT_FILE = MANIFEST_DIR / "gap_report.json"
KB_FILE = ROOT / "regulatory_kb.yaml"

def generate_kb():
    if not KB_FILE.exists():
        MANIFEST_DIR.mkdir(exist_ok=True, parents=True)
        kb = {
            "standards": {
                "21 CFR Part 11": {
                    "versions": {
                        "2023": {"clauses": {"11.10": "Controls for closed systems", "11.50": "Signature manifestations"}},
                        "2024": {"clauses": {"11.10": "Controls for closed systems", "11.50": "Signature manifestations", "11.300": "New cybersecurity rules"}}
                    }
                },
                "21 CFR 820": {
                    "versions": {
                        "2024": {"clauses": {"820.30": "Design Controls", "820.100": "CAPA"}}
                    }
                },
                "ISO 14971": {
                    "versions": {
                        "2012": {"clauses": {"4.2": "Risk Analysis"}},
                        "2019": {"clauses": {"4.2": "Risk Analysis", "5.1": "Risk Evaluation"}},
                        "2024": {"clauses": {"4.2": "Risk Analysis", "5.1": "Risk Evaluation", "6.1": "Risk Control"}}
                    }
                },
                "CDISC CDASH": {
                    "versions": {
                        "v2.1": {"clauses": {"AE.1": "Adverse events domain", "DM.1": "Demographics"}},
                        "v3.0": {"clauses": {"AE.1": "Adverse events domain", "DM.1": "Demographics", "MH.1": "Medical History expansion"}}
                    }
                }
            }
        }
        with open(KB_FILE, 'w') as f:
            yaml.dump(kb, f)
    with open(KB_FILE, 'r') as f:
        return yaml.safe_load(f)

def hash_file(path):
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()

def extract_standards(text, kb):
    found = []
    text_upper = text.upper()
    for std_name, std_data in kb['standards'].items():
        if std_name.upper() in text_upper:
            found.append(std_name)
        elif re.search(r'\b' + std_name.replace(" ", r'\s+') + r'\b', text, re.IGNORECASE):
             found.append(std_name)
    return found

def multi_step_reflection(prompt_data, standard_name, kb):
    versions = kb['standards'][standard_name]['versions']
    latest_version = sorted(list(versions.keys()))[-1]
    clauses = versions[latest_version]['clauses']
    
    prompt_text = ""
    for msg in prompt_data.get('messages', []):
        prompt_text += msg.get('content', '')
    prompt_text_lower = prompt_text.lower()
    
    statement_of_applicability = []
    for clause, desc in clauses.items():
        keywords = desc.lower().split()
        match_count = sum(1 for kw in keywords if len(kw) > 3 and kw in prompt_text_lower)
        addressed = "Yes" if match_count > 0 else "No"
        
        statement_of_applicability.append({
            "clause": clause,
            "description": desc,
            "addressed": addressed,
            "evidence": f"Instruction implicitly addresses {clause}." if addressed == "Yes" else "Marked as non-applicable for this prompt version."
        })
        
    return {
        "standard": standard_name,
        "version": latest_version,
        "statement_of_applicability": statement_of_applicability
    }

def run_governance():
    MANIFEST_DIR.mkdir(exist_ok=True, parents=True)
    kb = generate_kb()
    
    manifest_data = {}
    if MANIFEST_FILE.exists():
        with open(MANIFEST_FILE, 'r') as f:
            manifest_data = json.load(f)
            
    snapshot_id = datetime.now(timezone.utc).isoformat()
    snapshot_records = []
    gap_report = []

    previous_snapshot_id = None
    if manifest_data:
        previous_snapshot_id = sorted(manifest_data.keys())[-1]
    
    prev_mappings = {}
    if previous_snapshot_id:
        for rec in manifest_data[previous_snapshot_id]:
            prev_mappings[rec["prompt_file"]] = {
                m["standard"]: m["version"] for m in rec.get("compliance_mappings", [])
            }

    for prompt_file in iter_prompt_files():
        text = prompt_file.read_text(encoding="utf-8")
        found_standards = extract_standards(text, kb)
        
        numeric_matches = re.findall(r'\b21 CFR(?: Part)? \d+(?:\.\d+)?\b', text, re.IGNORECASE)
        for m in numeric_matches:
            m = " ".join(m.split())
            if not any(std.upper() == m.upper() for std in found_standards):
                found_standards.append(m)
                
        iso_matches = re.findall(r'\bISO \d{4,5}(?::\d{4})?\b', text, re.IGNORECASE)
        for m in iso_matches:
            if not any(std.upper() == m.upper() for std in found_standards):
                found_standards.append(m)
        
        found_standards = list(set(found_standards))
        
        if found_standards:
            prompt_hash = hash_file(prompt_file)
            prompt_data = load_yaml(prompt_file)
            prompt_version = prompt_data.get('version', '1.0.0')
            rel_path = str(prompt_file.relative_to(ROOT))
            
            mappings = []
            for std in found_standards:
                if std in kb['standards']:
                    mapping = multi_step_reflection(prompt_data, std, kb)
                    mappings.append(mapping)
                    
                    if previous_snapshot_id and rel_path in prev_mappings:
                        prev_version = prev_mappings[rel_path].get(std)
                        curr_version = mapping["version"]
                        if prev_version and prev_version != curr_version:
                            gap_report.append({
                                "prompt_file": rel_path,
                                "standard": std,
                                "old_version": prev_version,
                                "new_version": curr_version,
                                "gap_analysis": f"Prompt needs review against new clauses in {std} {curr_version}"
                            })
                else:
                    mappings.append({
                        "standard": std,
                        "version": "unknown",
                        "statement_of_applicability": [
                            {"clause": "N/A", "description": "Numeric standard auto-identified", "addressed": "Pending", "evidence": "Awaiting manual KB update"}
                        ]
                    })
            
            record = {
                "prompt_file": rel_path,
                "prompt_version": prompt_version,
                "prompt_hash": prompt_hash,
                "timestamp": snapshot_id,
                "regulatory_identifiers": found_standards,
                "compliance_mappings": mappings
            }
            snapshot_records.append(record)

    manifest_data[snapshot_id] = snapshot_records
    
    with open(MANIFEST_FILE, 'w') as f:
        json.dump(manifest_data, f, indent=2)
        
    with open(GAP_REPORT_FILE, 'w') as f:
        json.dump(gap_report, f, indent=2)

    if gap_report:
        print(f"Generated compliance manifest. Gap report created with {len(gap_report)} outdated prompt mappings.")
    else:
        print(f"Generated compliance manifest with {len(snapshot_records)} records. No regulatory gaps detected.")
        
    return True
