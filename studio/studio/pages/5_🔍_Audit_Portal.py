import os
import streamlit as st
from datetime import datetime, timezone
import pandas as pd

from promptops.utils import ROOT
from promptops import ledger

st.set_page_config(page_title="Studio Audit Portal", layout="wide")
st.title("🔍 Workspace Lineage Ledger & Studio Audit Portal")
st.markdown("---")

# 1. Cryptographic Integrity Check
entries = ledger.load_ledger()
is_valid, broken_idx, error_msg = ledger.validate_ledger_integrity(entries)

if not is_valid:
    st.error(f"🛑 **INTEGRITY VIOLATION DETECTED!** \n\n"
             f"A manual change or deletion has broken the ledger's cryptographic integrity chain! \n\n"
             f"**Details**: {error_msg} (at entry index {broken_idx})", icon="🚨")
else:
    st.success("✅ **Ledger Integrity Chain Verified**: Cryptographic SHA-256 chain is completely intact and secure.", icon="🛡️")

# 2. Controls and Filters
st.subheader("Filter Ledger Audit Log")
col1, col2, col3 = st.columns(3)

with col1:
    sign_filter = st.selectbox(
        "Signature Status",
        ["All", "Signed", "Unsigned"]
    )

with col2:
    status_filter = st.selectbox(
        "Run Execution Status",
        ["All", "Success", "Failed"]
    )

with col3:
    search_query = st.text_input("Search (by Run ID or Workflow File)", value="")

# Filter logic
filtered_entries = []
for entry in entries:
    # Filter by signatures
    is_signed = len(entry.get("signatures", [])) > 0
    if sign_filter == "Signed" and not is_signed:
        continue
    if sign_filter == "Unsigned" and is_signed:
        continue
        
    # Filter by workflow status
    if status_filter == "Success" and entry.get("status") != "Success":
        continue
    if status_filter == "Failed" and entry.get("status") != "Failed":
        continue
        
    # Filter by search query
    query = search_query.lower()
    if query:
        run_id = entry.get("run_id", "").lower()
        wf_file = entry.get("workflow_file", "").lower()
        if query not in run_id and query not in wf_file:
            continue
            
    filtered_entries.append(entry)

# Timeline is displayed reverse-chronologically (newest at the top)
filtered_entries = list(reversed(filtered_entries))

st.subheader(f"Timeline ({len(filtered_entries)} entries found)")

if not filtered_entries:
    st.info("No ledger entries found matching current filter criteria.")
else:
    for entry in filtered_entries:
        run_id = entry.get("run_id")
        timestamp = entry.get("timestamp")
        wf_file = entry.get("workflow_file", "unknown")
        wf_name = os.path.basename(wf_file)
        status = entry.get("status", "Unknown")
        is_signed = len(entry.get("signatures", [])) > 0
        
        status_icon = "🟢" if status == "Success" else "🔴"
        sign_status = "✍️ Signed" if is_signed else "❌ Unsigned"
        
        expander_title = f"{status_icon} [{timestamp}] Run {run_id} - {wf_name} ({status}) - {sign_status}"
        
        with st.expander(expander_title, expanded=False):
            # Display run hash and metadata
            st.markdown(f"**Run ID**: `{run_id}`")
            st.markdown(f"**Workflow File**: `{wf_file}`")
            st.markdown(f"**Cryptographic Signature (SHA-256 Checksum)**: `{entry.get('hash', 'N/A')}`")
            if entry.get("error_message"):
                st.error(f"**Error Details**: {entry.get('error_message')}")
                
            st.markdown("### Initial Inputs")
            st.json(entry.get("initial_inputs", {}))
            
            # Display step-by-step lineage
            st.markdown("### Step Execution Lineage")
            for idx, step in enumerate(entry.get("steps", [])):
                st.markdown(f"#### Step {idx + 1}: `{step.get('step_id')}`")
                st.text(f"Prompt File: {step.get('prompt_file')}")
                
                col_inp, col_out = st.columns(2)
                with col_inp:
                    st.markdown("**Step Inputs**")
                    st.json(step.get("inputs", {}))
                with col_out:
                    st.markdown("**Step Output**")
                    output_val = step.get("output", "")
                    if output_val:
                        st.code(output_val, language="json" if output_val.strip().startswith("{") else None)
                    else:
                        st.info("No output returned.")
                
                # Show safety evaluations
                safety_evals = step.get("safety_evaluations", [])
                if safety_evals:
                    st.markdown("**Safety Evaluations**")
                    df_safety = pd.DataFrame(safety_evals)
                    st.table(df_safety)
                
                # Show validation decisions
                val_decisions = step.get("validation_decisions", [])
                if val_decisions:
                    st.markdown("**Validation Decisions**")
                    df_val = pd.DataFrame(val_decisions)
                    st.table(df_val)
                
                st.markdown("---")
                
            # Electronic Signatures List
            st.markdown("### Electronic Signatures & Compliance Sign-Off")
            signatures = entry.get("signatures", [])
            if signatures:
                for sig in signatures:
                    st.info(f"**Signed by**: `{sig.get('username')}` on `{sig.get('timestamp')}`\n\n"
                            f"**Validation Comment**: {sig.get('comment')}")
            else:
                st.warning("This run is currently Unsigned. It has not been reviewed or signed off for FDA compliance.")
                
            # Signature form
            st.markdown("#### Submit FDA-Compliant Electronic Signature")
            with st.form(key=f"sign_form_{run_id}"):
                col_user, col_cred = st.columns(2)
                with col_user:
                    username = st.text_input("Reviewer/Operator Username", key=f"user_{run_id}")
                with col_cred:
                    credentials = st.text_input("Reviewer Credentials / Password", type="password", key=f"cred_{run_id}")
                    
                comment = st.text_area("Validation Comment / Safety Attestation", key=f"comment_{run_id}")
                
                submit_btn = st.form_submit_button("✍️ Approve & Sign Run")
                
                if submit_btn:
                    if not username or not credentials:
                        st.error("Submission Failed: Both username and authenticated credentials are required to sign.")
                    elif not comment:
                        st.error("Submission Failed: FDA guidelines require a validation comment / safety attestation to sign.")
                    else:
                        try:
                            ledger.sign_run(run_id, username, credentials, comment)
                            st.success(f"Run {run_id} signed successfully!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Sign-off Error: {e}")
