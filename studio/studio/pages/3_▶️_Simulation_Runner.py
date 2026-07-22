import os
import streamlit as st
import threading
import queue
import time
import logging
import io

from promptops.utils import ROOT
from studio.helpers import render_file_selector, load_asset_data
from promptops.engine import run_workflow, simulate_prompt_execution
from promptops.console import ConsoleInterface, set_console
from streamlit.runtime.scriptrunner import add_script_run_ctx

st.set_page_config(page_title="Simulation Runner", layout="wide")
st.title("Simulation Runner")
st.markdown("Validate your assets before final deployment. Choose between single prompts or workflows.")

class StreamlitThreadConsole(ConsoleInterface):
    def __init__(self, log_stream, in_q, out_q):
        self.log_stream = log_stream
        self.in_q = in_q
        self.out_q = out_q

    def print(self, msg: str):
        self.log_stream.write(msg + "\n")

    def ask_input(self, prompt: str) -> str:
        self.out_q.put({"type": "input", "prompt": prompt})
        while True:
            try:
                res = self.in_q.get(timeout=0.5)
                return res
            except queue.Empty:
                pass

base_dir = str(ROOT)

asset_type = st.radio("Asset Type to Simulate", ["Prompt", "Workflow"])

if asset_type == "Prompt":
    selected_file = render_file_selector("prompt", key="sim_prompt")
else:
    selected_file = render_file_selector("workflow", key="sim_workflow")

st.sidebar.subheader("Engine Options")
chaos_mode = st.sidebar.checkbox("Enable Chaos Mode (Simulate 429 errors & latency)", value=False)
strict_mode = st.sidebar.checkbox("Enable Strict Mode", value=False)

if 'sim_state' not in st.session_state:
    st.session_state.sim_state = 'idle'  # idle, running, waiting_input, done, error
    st.session_state.in_q = queue.Queue()
    st.session_state.out_q = queue.Queue()
    st.session_state.log_stream = io.StringIO()
    st.session_state.sim_thread = None
    st.session_state.pending_prompt = ""
    st.session_state.final_result = None
    st.session_state.fidelity_report = {}

if selected_file:
    file_path = os.path.join(base_dir, selected_file)
    data = load_asset_data(file_path, raw=False)
    
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
            
    if st.button("Run Simulation", type="primary") and st.session_state.sim_state in ['idle', 'done', 'error']:
        st.session_state.sim_state = 'running'
        st.session_state.in_q = queue.Queue()
        st.session_state.out_q = queue.Queue()
        st.session_state.log_stream = io.StringIO()
        st.session_state.final_result = None
        st.session_state.fidelity_report = {}
        st.session_state.error = None
        
        def target():
            try:
                # setup console
                c = StreamlitThreadConsole(st.session_state.log_stream, st.session_state.in_q, st.session_state.out_q)
                set_console(c)
                
                handler = logging.StreamHandler(st.session_state.log_stream)
                handler.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
                logger = logging.getLogger('promptops.engine')
                logger.setLevel(logging.DEBUG)
                logger.handlers = [handler]
                
                if asset_type == "Workflow":
                    final_state = run_workflow(file_path, initial_inputs, verbose=True, chaos_mode=chaos_mode, strict_mode=strict_mode, fidelity_report=st.session_state.fidelity_report)
                    st.session_state.out_q.put({"type": "done", "result": final_state})
                else:
                    output = simulate_prompt_execution(data, initial_inputs, prompt_file=file_path, chaos_mode=chaos_mode, strict_mode=strict_mode, fidelity_report=st.session_state.fidelity_report)
                    st.session_state.out_q.put({"type": "done", "result": output})
            except Exception as e:
                st.session_state.out_q.put({"type": "error", "error": str(e)})

        t = threading.Thread(target=target)
        add_script_run_ctx(t)
        t.start()
        st.session_state.sim_thread = t
        st.rerun()

    if st.session_state.sim_state == 'running':
        st.info("Simulation is running...")
        # Polling the out_q
        while True:
            try:
                msg = st.session_state.out_q.get(timeout=0.1)
                if msg["type"] == "input":
                    st.session_state.sim_state = 'waiting_input'
                    st.session_state.pending_prompt = msg["prompt"]
                    st.rerun()
                elif msg["type"] == "done":
                    st.session_state.sim_state = 'done'
                    st.session_state.final_result = msg["result"]
                    st.rerun()
                elif msg["type"] == "error":
                    st.session_state.sim_state = 'error'
                    st.session_state.error = msg["error"]
                    st.rerun()
            except queue.Empty:
                if not st.session_state.sim_thread.is_alive():
                    st.session_state.sim_state = 'error'
                    st.session_state.error = "Thread died unexpectedly"
                    st.rerun()
                # we just wait and rerun to keep polling
                time.sleep(0.5)
                st.rerun()

    elif st.session_state.sim_state == 'waiting_input':
        st.warning(f"Engine requires input: {st.session_state.pending_prompt}")
        user_input = st.text_area("Correction / Input:")
        if st.button("Submit Input"):
            st.session_state.in_q.put(user_input)
            st.session_state.sim_state = 'running'
            st.rerun()

    elif st.session_state.sim_state == 'done':
        st.subheader("Simulation Output Log")
        st.code(st.session_state.log_stream.getvalue(), language="text")
        st.success("Simulation finished successfully.")
        st.subheader("Final Output")
        
        res = st.session_state.final_result
        if asset_type == "Workflow" and res:
            final_output_step_id = data.get('steps', [{}])[-1].get('step_id')
            if final_output_step_id and final_output_step_id in res.get('steps', {}):
                final_output = res['steps'][final_output_step_id]['output']
                st.info(final_output)
        else:
            st.info(res)
            
        st.json(st.session_state.fidelity_report)
        
        if st.button("Reset"):
            st.session_state.sim_state = 'idle'
            st.rerun()

    elif st.session_state.sim_state == 'error':
        st.subheader("Simulation Output Log")
        st.code(st.session_state.log_stream.getvalue(), language="text")
        st.error(f"Simulation failed: {st.session_state.error}")
        if st.button("Reset"):
            st.session_state.sim_state = 'idle'
            st.rerun()
