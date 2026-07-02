import sys
import os
import glob
import streamlit as st
from typing import Any

from promptops.utils import ROOT, load_yaml
from promptops.engine import run_workflow, simulate_prompt_execution

st.set_page_config(page_title="Simulation Runner", layout="wide")
st.title("Simulation Runner")
st.markdown("Validate your assets before final deployment. Choose between single prompts or workflows.")

base_dir = str(ROOT)
workflow_files = glob.glob(os.path.join(base_dir, "workflows", "**", "*.workflow.yaml"), recursive=True)
workflow_files = [os.path.relpath(f, base_dir) for f in workflow_files]

prompt_files = glob.glob(os.path.join(base_dir, "prompts", "**", "*.prompt.yaml"), recursive=True) + glob.glob(os.path.join(base_dir, "prompts", "**", "*.prompt.md"), recursive=True)
prompt_files = [os.path.relpath(f, base_dir) for f in prompt_files]

asset_type = st.radio("Asset Type to Simulate", ["Prompt", "Workflow"])

if asset_type == "Prompt":
    selected_file = st.selectbox("Select a prompt to simulate", prompt_files)
else:
    selected_file = st.selectbox("Select a workflow to simulate", workflow_files)

st.sidebar.subheader("Engine Options")
chaos_mode = st.sidebar.checkbox("Enable Chaos Mode (Simulate 429 errors & latency)", value=False)
strict_mode = st.sidebar.checkbox("Enable Strict Mode", value=False)

if selected_file:
    file_path = os.path.join(base_dir, selected_file)
    data = load_yaml(file_path) or {}
    
    st.subheader("Global Inputs")
    initial_inputs = {}
    
    if asset_type == "Workflow" and 'inputs' in data:
        for inp in data['inputs']:
            name = inp.get('name', 'unknown')
            desc = inp.get('description', '')
            initial_inputs[name] = st.text_input(f"{name} ({desc})", value="")
    elif asset_type == "Prompt":
        from promptops.utils import extract_template_vars
        vars = extract_template_vars(data)
        for var in vars:
            initial_inputs[var] = st.text_input(f"{var}", value="")
            
    if st.button("Run Simulation", type="primary"):
        with st.spinner("Simulating..."):
            try:
                import logging
                import io
                
                log_stream = io.StringIO()
                handler = logging.StreamHandler(log_stream)
                handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
                
                if asset_type == "Workflow":
                    logger = logging.getLogger('promptops.engine')
                else:
                    logger = logging.getLogger('promptops.engine')
                
                logger.setLevel(logging.DEBUG)
                logger.handlers = [handler]
                
                fidelity_report: dict[str, Any] = {}
                
                if asset_type == "Workflow":
                    final_state = run_workflow(file_path, initial_inputs, verbose=True, chaos_mode=chaos_mode, strict_mode=strict_mode, fidelity_report=fidelity_report)
                    st.subheader("Simulation Output Log")
                    st.code(log_stream.getvalue(), language="text")
                    
                    if final_state:
                        st.success("Simulation finished successfully.")
                        final_output_step_id = data.get('steps', [{}])[-1].get('step_id')
                        if final_output_step_id and final_output_step_id in final_state['steps']:
                            final_output = final_state['steps'][final_output_step_id]['output']
                            st.subheader("Final Output")
                            st.info(final_output)
                else:
                    output = simulate_prompt_execution(data, initial_inputs, prompt_file=file_path, chaos_mode=chaos_mode, strict_mode=strict_mode, fidelity_report=fidelity_report)
                    st.subheader("Simulation Output Log")
                    st.code(log_stream.getvalue(), language="text")
                    
                    st.success("Simulation finished successfully.")
                    st.subheader("Final Output")
                    st.info(output)

                st.json(fidelity_report)
                
            except Exception as e:
                st.subheader("Simulation Output Log")
                st.code(log_stream.getvalue(), language="text")
                st.error(f"Simulation failed: {e}")

