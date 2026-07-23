import os
import json
import hashlib
import threading
from datetime import datetime, timezone
from pathlib import Path

LEDGER_PATH = Path("/app/workspace_ledger.json")

_execution_context = threading.local()

def get_ledger_path():
    return LEDGER_PATH

def load_ledger():
    if not LEDGER_PATH.exists():
        return []
    try:
        with open(LEDGER_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        return []

def save_ledger(entries):
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LEDGER_PATH, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2, sort_keys=True)

def calculate_entry_hash(entry, previous_hash):
    # Exclude the "hash" field itself
    data_to_hash = {k: v for k, v in entry.items() if k != "hash"}
    canonical_str = json.dumps(data_to_hash, sort_keys=True)
    hash_input = f"{previous_hash}::{canonical_str}"
    return hashlib.sha256(hash_input.encode('utf-8')).hexdigest()

def validate_ledger_integrity(entries):
    """
    Validates the cryptographic chain of ledger entries.
    Returns (is_valid, broken_index, error_message).
    """
    previous_hash = "0"
    for i, entry in enumerate(entries):
        if "hash" not in entry:
            return False, i, f"Entry at index {i} has no hash."
        
        calculated = calculate_entry_hash(entry, previous_hash)
        if entry["hash"] != calculated:
            return False, i, f"Hash mismatch at index {i}. Expected: {calculated}, Found: {entry['hash']}"
        
        previous_hash = entry["hash"]
    return True, None, "Ledger integrity validated successfully."

def start_step_capture(step_id, prompt_file, inputs):
    _execution_context.current_step = {
        "step_id": step_id,
        "prompt_file": prompt_file,
        "inputs": inputs,
        "safety_evaluations": [],
        "validation_decisions": []
    }

def add_safety_evaluation(eval_name, status, details=None):
    if hasattr(_execution_context, "current_step") and _execution_context.current_step:
        _execution_context.current_step["safety_evaluations"].append({
            "evaluator": eval_name,
            "status": status,
            "details": details
        })

def add_validation_decision(eval_name, status, details=None):
    if hasattr(_execution_context, "current_step") and _execution_context.current_step:
        _execution_context.current_step["validation_decisions"].append({
            "evaluator": eval_name,
            "status": status,
            "details": details
        })

def get_current_step_capture():
    if hasattr(_execution_context, "current_step"):
        return _execution_context.current_step
    return None

def clear_step_capture():
    _execution_context.current_step = None

def record_run(workflow_file, initial_inputs, steps_list, status="Success", error_message=None):
    """
    Records a workflow execution in the workspace lineage ledger.
    """
    entries = load_ledger()
    
    # Check current integrity before appending
    is_valid, broken_index, warn_msg = validate_ledger_integrity(entries)
    if not is_valid:
        print(f"🛑 WARNING: Ledger integrity chain is broken! {warn_msg}")
    
    previous_hash = "0"
    if entries:
        previous_hash = entries[-1].get("hash", "0")
        
    timestamp = datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')
    run_context = f"{workflow_file}::{timestamp}::{json.dumps(initial_inputs, sort_keys=True)}"
    run_id = hashlib.sha256(run_context.encode('utf-8')).hexdigest()[:16]
    
    entry = {
        "run_id": run_id,
        "workflow_file": str(workflow_file),
        "timestamp": timestamp,
        "initial_inputs": initial_inputs,
        "status": status,
        "error_message": error_message,
        "steps": steps_list,
        "signatures": [],
    }
    
    entry["hash"] = calculate_entry_hash(entry, previous_hash)
    entries.append(entry)
    save_ledger(entries)
    return run_id

def sign_run(run_id, username, credentials, comment):
    """
    Submits an authenticated electronic signature for an unsigned ledger run.
    """
    entries = load_ledger()
    for entry in entries:
        if entry["run_id"] == run_id:
            if not username or not credentials:
                raise ValueError("Electronic signature requires both username and credentials.")
                
            timestamp = datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')
            signature = {
                "username": username,
                "comment": comment,
                "timestamp": timestamp
            }
            if "signatures" not in entry:
                entry["signatures"] = []
            entry["signatures"].append(signature)
            
            recalculate_ledger_hashes(entries)
            save_ledger(entries)
            return True
    raise ValueError(f"Run ID {run_id} not found in the ledger.")

def recalculate_ledger_hashes(entries):
    previous_hash = "0"
    for entry in entries:
        entry["hash"] = calculate_entry_hash(entry, previous_hash)
        previous_hash = entry["hash"]
