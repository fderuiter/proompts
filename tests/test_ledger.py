import os
import json
import pytest
from pathlib import Path
from promptops.engine import run_workflow
from promptops.ledger import (
    get_ledger_path,
    load_ledger,
    save_ledger,
    validate_ledger_integrity,
    sign_run,
    calculate_entry_hash
)

@pytest.fixture(autouse=True)
def clean_ledger():
    """Backup existing ledger, clean for test, restore after."""
    ledger_path = get_ledger_path()
    backup_path = ledger_path.with_name("workspace_ledger.json.bak")
    
    # Backup
    has_backup = False
    if ledger_path.exists():
        ledger_path.rename(backup_path)
        has_backup = True
    elif backup_path.exists():
        backup_path.unlink()
        
    yield
    
    # Clean up test ledger
    if ledger_path.exists():
        ledger_path.unlink()
        
    # Restore backup
    if has_backup:
        backup_path.rename(ledger_path)

def test_ledger_flow_success(tmp_path):
    # 1. Create temporary prompt file
    prompt_file = tmp_path / "test.prompt.yaml"
    prompt_content = {
        "name": "Clinical Safety Analysis",
        "description": "Scans patient report for safety signals.",
        "model": "gpt-4",
        "modelParameters": {"temperature": 0.0},
        "metadata": {"domain": "clinical", "complexity": "low"},
        "variables": [
            {"name": "patient_report", "description": "Raw clinical patient notes", "required": True}
        ],
        "messages": [
            {"role": "system", "content": "You are a clinical safety reviewer."},
            {"role": "user", "content": "Analyze report: {{ patient_report }}"}
        ],
        "testData": [],
        "evaluators": [
            {
                "name": "Global PII Scanner",
                "python": "return not bool(re.search(r'\\b\\d{3}-\\d{2}-\\d{4}\\b', output))",
                "action": "redact"
            },
            {
                "name": "Length Check",
                "python": "return len(output) > 5",
                "action": "terminate"
            }
        ]
    }
    with open(prompt_file, 'w', encoding='utf-8') as f:
        json.dump(prompt_content, f)

    # 2. Create temporary workflow file
    workflow_file = tmp_path / "safety.workflow.yaml"
    workflow_content = {
        "name": "FDA Compliance Lineage Workflow",
        "description": "A workflow designed for secure safety logging.",
        "inputs": [
            {"name": "notes", "description": "Clinical trial notes"}
        ],
        "steps": [
            {
                "step_id": "step1",
                "prompt_file": str(prompt_file),
                "map_inputs": {
                    "patient_report": "{{ inputs.notes }}"
                }
            }
        ]
    }
    with open(workflow_file, 'w', encoding='utf-8') as f:
        json.dump(workflow_content, f)

    # 3. Run workflow in simulation mode
    initial_inputs = {"notes": "Patient reports mild headache but no severe adverse events."}
    run_workflow(str(workflow_file), initial_inputs, verbose=False)

    # 4. Assert ledger was written successfully
    ledger_path = get_ledger_path()
    assert ledger_path.exists()

    entries = load_ledger()
    assert len(entries) == 1
    
    entry = entries[0]
    assert "run_id" in entry
    assert "timestamp" in entry
    assert "hash" in entry
    assert entry["status"] == "Success"
    assert entry["workflow_file"] == str(workflow_file)

    # Check steps detail
    assert len(entry["steps"]) == 1
    step_log = entry["steps"][0]
    assert step_log["step_id"] == "step1"
    assert "safety_evaluations" in step_log
    assert "validation_decisions" in step_log

    # 5. Check cryptographic chain integrity
    is_valid, broken_idx, msg = validate_ledger_integrity(entries)
    assert is_valid is True

def test_ledger_flow_tampering_warning(tmp_path):
    # Record a run
    prompt_file = tmp_path / "test.prompt.yaml"
    with open(prompt_file, 'w', encoding='utf-8') as f:
        json.dump({
            "name": "Test Prompt", "description": "desc", "model": "gpt-4",
            "modelParameters": {"temperature": 0.0}, "metadata": {"domain": "clinical", "complexity": "low"},
            "variables": [], "messages": [{"role": "system", "content": "hi"}, {"role": "user", "content": "hi"}],
            "testData": [], "evaluators": []
        }, f)

    workflow_file = tmp_path / "test.workflow.yaml"
    with open(workflow_file, 'w', encoding='utf-8') as f:
        json.dump({
            "name": "Test Workflow", "steps": [{"step_id": "s1", "prompt_file": str(prompt_file), "map_inputs": {}}]
        }, f)

    run_workflow(str(workflow_file), {}, verbose=False)
    
    entries = load_ledger()
    assert len(entries) == 1
    is_valid, _, _ = validate_ledger_integrity(entries)
    assert is_valid is True

    # Manually tamper with the ledger
    entries[0]["status"] = "Tampered Status"
    save_ledger(entries)

    # Re-verify integrity (should fail)
    tampered_entries = load_ledger()
    is_valid, broken_idx, msg = validate_ledger_integrity(tampered_entries)
    assert is_valid is False
    assert broken_idx == 0

def test_ledger_flow_signatures(tmp_path):
    # Record a run
    prompt_file = tmp_path / "test.prompt.yaml"
    with open(prompt_file, 'w', encoding='utf-8') as f:
        json.dump({
            "name": "Test Prompt", "description": "desc", "model": "gpt-4",
            "modelParameters": {"temperature": 0.0}, "metadata": {"domain": "clinical", "complexity": "low"},
            "variables": [], "messages": [{"role": "system", "content": "hi"}, {"role": "user", "content": "hi"}],
            "testData": [], "evaluators": []
        }, f)

    workflow_file = tmp_path / "test.workflow.yaml"
    with open(workflow_file, 'w', encoding='utf-8') as f:
        json.dump({
            "name": "Test Workflow", "steps": [{"step_id": "s1", "prompt_file": str(prompt_file), "map_inputs": {}}]
        }, f)

    state = run_workflow(str(workflow_file), {}, verbose=False)
    assert state is not None
    run_id = state["run_id"]
    assert run_id is not None

    # Sign the run
    signed = sign_run(
        run_id=run_id,
        username="reviewer123",
        credentials="secure_credentials",
        comment="FDA compliant sign-off."
    )
    assert signed is True

    # Load and check signature
    entries = load_ledger()
    entry = entries[0]
    assert len(entry["signatures"]) == 1
    sig = entry["signatures"][0]
    assert sig["username"] == "reviewer123"
    assert sig["comment"] == "FDA compliant sign-off."

    # Validate integrity should still pass because the chain gets correctly updated on signing
    is_valid, _, _ = validate_ledger_integrity(entries)
    assert is_valid is True

    # Signing with missing credentials should fail
    with pytest.raises(ValueError):
        sign_run(run_id=run_id, username="", credentials="abc", comment="no user")
        
    with pytest.raises(ValueError):
        sign_run(run_id=run_id, username="user", credentials="", comment="no creds")
