import sys
import os
import glob
import streamlit as st

from promptops.engine import run as run_workflow
from promptops.utils import load_yaml

st.set_page_config(page_title="Simulation Runner", layout="wide")
st.title("Simulation Runner")
st.markdown("Validate your workflow or prompt correctly resolves variables across all steps before final submission.")

from promptops.utils import ROOT
base_dir = str(ROOT)
asset_files = glob.glob(os.path.join(base_dir, "workflows", "**", "*.workflow.yaml"), recursive=True) + glob.glob(os.path.join(base_dir, "prompts", "**", "*.prompt.yaml"), recursive=True)
asset_files = [os.path.relpath(f, base_dir) for f in asset_files]

selected_file = st.selectbox("Select an asset to simulate", asset_files)

if selected_file:
    file_path = os.path.join(base_dir, selected_file)
    data = load_yaml(file_path) or {}
    
    st.subheader("Global Inputs")
    initial_inputs = {}
    
    # Try to determine inputs
    # If the workflow defines `inputs` or prompt defines `variables`, list them
    vars_list = data.get('inputs') or data.get('variables', [])
    if vars_list:
        if isinstance(vars_list, list):
            for var in vars_list:
                name = var.get('name') if isinstance(var, dict) else var
                desc = var.get('description', '') if isinstance(var, dict) else ''
                if name:
                    initial_inputs[name] = st.text_input(f"{name} ({desc})", value="")
        elif isinstance(vars_list, dict):
            for name, desc in vars_list.items():
                initial_inputs[name] = st.text_input(f"{name} ({desc})", value="")
                
    chaos_mode = st.checkbox("Enable Chaos Mode (Simulate failures and latency)")
            
    if st.button("Run Simulation", type="primary"):
        with st.spinner("Simulating..."):
            try:
                # Capture logs using standard logging
                import logging
                import io
                
                log_stream = io.StringIO()
                handler = logging.StreamHandler(log_stream)
                handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
                
                logger = logging.getLogger('promptops.engine')
                logger.setLevel(logging.DEBUG)
                logger.handlers = [handler]
                
                final_state = run_workflow(file_path, initial_inputs, verbose=True, chaos_mode=chaos_mode)
                
                st.subheader("Simulation Output")
                st.code(log_stream.getvalue(), language="text")
                
                if final_state:
                    st.success("Simulation finished successfully.")
                    if 'steps' in data:
                        final_output_step_id = data.get('steps', [{}])[-1].get('step_id')
                    else:
                        final_output_step_id = 'step_1'
                        
                    if final_output_step_id and final_output_step_id in final_state['steps']:
                        final_output = final_state['steps'][final_output_step_id]['output']
                        st.subheader("Final Workflow Output")
                        st.info(final_output)
            except Exception as e:
                st.error(f"Simulation failed: {e}")

