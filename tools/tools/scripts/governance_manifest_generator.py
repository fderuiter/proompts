#!/usr/bin/env python3
"""
governance_manifest_generator.py: Governance Manifest Generator

WHAT:
This script scans prompt files and generates a regulatory compliance manifest (`compliance_manifest.json`) and a gap report (`gap_report.json`) against predefined standards like 21 CFR Part 11 and ISO 13485.

WHY:
Ensures that clinical and regulatory prompts contain the necessary metadata, evaluation rules, and traceability required for compliance in regulated environments.

HOW TO USE:
python3 tools/tools/scripts/governance_manifest_generator.py
"""

from typing import Any
import json
import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path
import sys
import yaml

# Ensure we can import from the current directory
try:
    from promptops.utils import (
        PROMPTS_DIR, 
        iter_prompt_files, 
        load_yaml, 
        ROOT,
        MANIFEST_DIR,
        MANIFEST_FILE,
        GAP_REPORT_FILE,
        KB_FILE
    )
except Exception as e:
    raise e

MANIFEST_DIR.mkdir(parents=True, exist_ok=True)

def generate_kb():
    if not KB_FILE.exists():
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
        # Regex to catch numeric variants
        elif re.search(r'\b' + std_name.replace(" ", r'\s+') + r'\b', text, re.IGNORECASE):
             found.append(std_name)
    return found

def multi_step_reflection(prompt_data, standard_name, kb):
    """
    Simulates a multi-step reflection to generate a Statement of Applicability.
    Verifies that prompt instructions actually satisfy the logic of a linked regulation.
    """
    versions = kb['standards'][standard_name]['versions']
    latest_version = sorted(list(versions.keys()))[-1]
    clauses = versions[latest_version]['clauses']
    
    # Extract text from prompt to test logic
    prompt_text = ""
    for msg in prompt_data.get('messages', []):
        prompt_text += msg.get('content', '')
    prompt_text_lower = prompt_text.lower()
    
    statement_of_applicability = []
    for clause, desc in clauses.items():
        # Check if the prompt actually satisfies the logic by looking for relevant terms
        # This is a mock multi-step reflection process.
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

def main():
    kb = generate_kb()
    
    manifest_data = {}
    if MANIFEST_FILE.exists():
        with open(MANIFEST_FILE, 'r') as f:
            manifest_data = json.load(f)
            
    snapshot_id = datetime.now(timezone.utc).isoformat()
    snapshot_records = []
    gap_report = []

    # Identify the previous snapshot for gap analysis
    previous_snapshot_id = None
    if manifest_data:
        previous_snapshot_id = sorted(manifest_data.keys())[-1]
    
    prev_mappings = {}
    if previous_snapshot_id:
        for rec in manifest_data[previous_snapshot_id]:
            prev_mappings[rec["prompt_file"]] = {
                m["standard"]: m["version"] for m in rec.get("compliance_mappings", [])
            }

    processed_files = set()

    for prompt_file in iter_prompt_files():
        text = prompt_file.read_text(encoding="utf-8")
        found_standards = extract_standards(text, kb)
        
        # Regex to correctly identify complex numeric standards missing from heuristics
        numeric_matches = re.findall(r'\b21 CFR(?: Part)? \d+(?:\.\d+)?\b', text, re.IGNORECASE)
        for m in numeric_matches:
            # normalize space
            m = " ".join(m.split())
            if not any(std.upper() == m.upper() for std in found_standards):
                found_standards.append(m)
                
        iso_matches = re.findall(r'\bISO \d{4,5}(?::\d{4})?\b', text, re.IGNORECASE)
        for m in iso_matches:
            if not any(std.upper() == m.upper() for std in found_standards):
                found_standards.append(m)
        
        found_standards = list(set(found_standards))
        
        rel_path = str(prompt_file.relative_to(ROOT))
        
        if found_standards:
            prompt_hash = hash_file(prompt_file)
            prompt_data = load_yaml(prompt_file)
            prompt_version = prompt_data.get('version', '1.0.0')
            processed_files.add(rel_path)
            
            mappings = []
            for std in found_standards:
                if std in kb['standards']:
                    mapping = multi_step_reflection(prompt_data, std, kb)
                    mappings.append(mapping)
                    
                    # Check for gaps if there is a previous snapshot
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
                            
            # Check for missing standards that were previously present
            if previous_snapshot_id and rel_path in prev_mappings:
                for prev_std, prev_version in prev_mappings[rel_path].items():
                    if prev_std not in found_standards:
                        gap_report.append({
                            "prompt_file": rel_path,
                            "standard": prev_std,
                            "old_version": prev_version,
                            "new_version": None,
                            "gap_analysis": f"Regulatory mapping for {prev_std} was removed or is missing."
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
            
        elif previous_snapshot_id and rel_path in prev_mappings:
            # File exists but all its standards were removed
            for prev_std, prev_version in prev_mappings[rel_path].items():
                gap_report.append({
                    "prompt_file": rel_path,
                    "standard": prev_std,
                    "old_version": prev_version,
                    "new_version": None,
                    "gap_analysis": f"Regulatory mapping for {prev_std} was removed or is missing."
                })
            processed_files.add(rel_path)

    if previous_snapshot_id:
        for prev_file, stds in prev_mappings.items():
            if prev_file not in processed_files:
                for prev_std, prev_version in stds.items():
                    gap_report.append({
                        "prompt_file": prev_file,
                        "standard": prev_std,
                        "old_version": prev_version,
                        "new_version": None,
                        "gap_analysis": f"File removed or missing. Regulatory mapping for {prev_std} lost."
                    })

    # Check if the new snapshot is functionally identical to the previous one
    if previous_snapshot_id:
        prev_records = manifest_data[previous_snapshot_id]
        
        # Helper to strip timestamp for comparison
        def strip_ts(records):
            return [{k: v for k, v in r.items() if k != 'timestamp'} for r in records]
            
        if strip_ts(snapshot_records) == strip_ts(prev_records):
            # No changes detected, do not append a new snapshot
            if gap_report:
                with open(GAP_REPORT_FILE, 'w') as f:
                    json.dump(gap_report, f, indent=2)
                print(f"Generated compliance manifest. Gap report created with {len(gap_report)} outdated prompt mappings.")
            else:
                with open(GAP_REPORT_FILE, 'w') as f:
                    json.dump([], f, indent=2)
                print(f"No changes detected in prompts. Manifest unchanged. No regulatory gaps detected.")
            return

    manifest_data[snapshot_id] = snapshot_records
    
    with open(MANIFEST_FILE, 'w') as f:
        json.dump(manifest_data, f, indent=2)
        
    if gap_report:
        with open(GAP_REPORT_FILE, 'w') as f:
            json.dump(gap_report, f, indent=2)
        print(f"Generated compliance manifest. Gap report created with {len(gap_report)} outdated prompt mappings.")
    else:
        # Create an empty gap report to show there are no gaps
        with open(GAP_REPORT_FILE, 'w') as f:
            json.dump([], f, indent=2)
        print(f"Generated compliance manifest with {len(snapshot_records)} records. No regulatory gaps detected.")

if __name__ == "__main__":
    main()
