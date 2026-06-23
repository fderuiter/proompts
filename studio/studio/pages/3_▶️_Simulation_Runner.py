import sys
import os
import glob
import streamlit as st

from tools.scripts.run_workflow import run_workflow, load_yaml

st.set_page_config(page_title="Simulation Runner", layout="wide")
st.title("Simulation Runner")
st.markdown("Validate your workflow correctly resolves variables across all steps before final submission.")

from promptops.utils import ROOT
base_dir = str(ROOT)
workflow_files = glob.glob(os.path.join(base_dir, "workflows", "**", "*.workflow.yaml"), recursive=True)
workflow_files = [os.path.relpath(f, base_dir) for f in workflow_files]

selected_file = st.selectbox("Select a workflow to simulate", workflow_files)

if selected_file:
    file_path = os.path.join(base_dir, selected_file)
    data = load_yaml(file_path) or {}
    
    st.subheader("Global Inputs")
    initial_inputs = {}
    
    # Try to determine inputs
    # If the workflow defines `inputs`, list them
    if data and 'inputs' in data:
        for inp in data['inputs']:
            name = inp.get('name', 'unknown')
            desc = inp.get('description', '')
            initial_inputs[name] = st.text_input(f"{name} ({desc})", value="")
            
    if st.button("Run Simulation", type="primary"):
        with st.spinner("Simulating..."):
            try:
                # Capture logs using standard logging
                import logging
                import io
                
                log_stream = io.StringIO()
                handler = logging.StreamHandler(log_stream)
                handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
                
                logger = logging.getLogger('tools.scripts.run_workflow')
                logger.setLevel(logging.DEBUG)
                logger.handlers = [handler]
                
                final_state = run_workflow(file_path, initial_inputs, verbose=True)
                
                st.subheader("Simulation Output")
                st.code(log_stream.getvalue(), language="text")
                
                if final_state:
                    st.success("Simulation finished successfully.")
                    final_output_step_id = data.get('steps', [{}])[-1].get('step_id')
                    if final_output_step_id and final_output_step_id in final_state['steps']:
                        final_output = final_state['steps'][final_output_step_id]['output']
                        st.subheader("Final Workflow Output")
                        st.info(final_output)
            except Exception as e:
                st.error(f"Simulation failed: {e}")

