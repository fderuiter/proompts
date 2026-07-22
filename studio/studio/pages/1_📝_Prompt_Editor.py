import os
import streamlit as st
import pandas as pd

from promptops.validation import PromptSchema

st.set_page_config(page_title="Prompt Editor", layout="wide")
st.title("Prompt Editor")

from studio.helpers import (
    render_schema_form, 
    load_asset_data, 
    validate_and_save_asset,
    get_relative_asset_paths
)
from promptops.utils import ROOT
base_dir = str(ROOT)
prompt_files = get_relative_asset_paths("prompt", extensions=[".prompt.md"])

selected_file = st.selectbox("Select a prompt to edit", ["Create New..."] + prompt_files)

from typing import Dict, Any

if selected_file == "Create New...":
    st.subheader("Create New Prompt")
    new_file_path = st.text_input("File Path (e.g., prompts/my_prompt.prompt.md)")
    data: Dict[str, Any] = {
        "name": "",
        "version": "0.1.0",
        "description": "",
        "metadata": {
            "domain": "general",
            "complexity": "low",
            "tags": ["skill"],
            "status": "active"
        },
        "model": "gpt-4",
        "modelParameters": {"temperature": 0.1, "max_tokens": 1000},
        "variables": [{"name": "input", "description": "User input"}],
        "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "{{input}}"}],
        "testData": [{"inputs": {"input": "test"}, "expected": "Output"}],
        "evaluators": []
    }
else:
    new_file_path = selected_file
    file_path = os.path.join(base_dir, selected_file)
    data = load_asset_data(file_path)
    if not data:
        st.stop()
st.subheader(f"Editing: {selected_file}")

# Dynamically generate basic fields from schema
skip_fields = ["variables", "messages", "testData", "evaluators", "modelParameters", "tools", "output_schema", "last_modified"]

data = render_schema_form(PromptSchema, data, skip_fields=skip_fields)

st.subheader("Model Parameters")
model_params = data.get('modelParameters', {})
col1, col2 = st.columns(2)
with col1:
    temperature = st.number_input("Temperature", min_value=0.0, max_value=2.0, value=float(model_params.get('temperature', 0.1)), step=0.1)
with col2:
    max_tokens = st.number_input("Max Tokens", min_value=1, value=int(model_params.get('max_tokens', 1000)), step=100)

st.subheader("Variables")
variables = data.get('variables', [])
var_df = pd.DataFrame(variables) if variables else pd.DataFrame(columns=["name", "description"])
edited_var_df = st.data_editor(var_df, num_rows="dynamic", key="var_editor")

st.subheader("Messages")
if 'messages' not in st.session_state:
    st.session_state['messages'] = data.get('messages', [])

if 'current_file' not in st.session_state or st.session_state['current_file'] != selected_file:
    st.session_state['current_file'] = selected_file
    st.session_state['messages'] = data.get('messages', [])
    
for i, msg in enumerate(st.session_state['messages']):
    col1, col2, col3 = st.columns([2, 8, 1])
    with col1:
        st.session_state['messages'][i]['role'] = st.selectbox(f"Role {i}", ["system", "user", "assistant"], index=["system", "user", "assistant"].index(msg.get('role', 'user')), key=f"role_{i}")
    with col2:
        st.session_state['messages'][i]['content'] = st.text_area(f"Content {i}", value=msg.get('content', ''), key=f"content_{i}")
        
        btn_col1, btn_col2, btn_col3 = st.columns([2, 2, 6])
        if btn_col1.button("✨ Optimize", key=f"opt_{i}"):
            st.session_state[f"show_opt_diff_{i}"] = True
            st.session_state[f"show_san_diff_{i}"] = False
        if btn_col2.button("🧹 Sanitize", key=f"san_{i}"):
            st.session_state[f"show_san_diff_{i}"] = True
            st.session_state[f"show_opt_diff_{i}"] = False
            
        if st.session_state.get(f"show_opt_diff_{i}"):
            st.markdown("**Optimization Proposed Changes (Side-by-Side):**")
            diff_col1, diff_col2 = st.columns(2)
            original = st.session_state['messages'][i]['content']
            from promptops.utils import optimize_prompt
            proposed = optimize_prompt(original)
            
            with diff_col1:
                st.text_area("Original", value=original, disabled=True, key=f"orig_opt_{i}", height=150)
            with diff_col2:
                st.text_area("Optimized", value=proposed, disabled=True, key=f"prop_opt_{i}", height=150)
                
            ac_col1, ac_col2, _ = st.columns([2, 2, 6])
            if ac_col1.button("✅ Accept", key=f"acc_opt_{i}"):
                st.session_state['messages'][i]['content'] = proposed
                st.session_state[f"content_{i}"] = proposed
                st.session_state[f"show_opt_diff_{i}"] = False
                st.rerun()
            if ac_col2.button("❌ Reject", key=f"rej_opt_{i}"):
                st.session_state[f"show_opt_diff_{i}"] = False
                st.rerun()

        if st.session_state.get(f"show_san_diff_{i}"):
            st.markdown("**Sanitization Proposed Changes (Side-by-Side):**")
            diff_col1, diff_col2 = st.columns(2)
            original = st.session_state['messages'][i]['content']
            from promptops.utils import sanitize_prompt
            proposed = sanitize_prompt(original)
            
            with diff_col1:
                st.text_area("Original", value=original, disabled=True, key=f"orig_san_{i}", height=150)
            with diff_col2:
                st.text_area("Sanitized", value=proposed, disabled=True, key=f"prop_san_{i}", height=150)
                
            ac_col1, ac_col2, _ = st.columns([2, 2, 6])
            if ac_col1.button("✅ Accept", key=f"acc_san_{i}"):
                st.session_state['messages'][i]['content'] = proposed
                st.session_state[f"content_{i}"] = proposed
                st.session_state[f"show_san_diff_{i}"] = False
                st.rerun()
            if ac_col2.button("❌ Reject", key=f"rej_san_{i}"):
                st.session_state[f"show_san_diff_{i}"] = False
                st.rerun()

    with col3:
        if st.button("X", key=f"del_{i}"):
            st.session_state['messages'].pop(i)
            st.rerun()

if st.button("Add Message"):
    st.session_state['messages'].append({"role": "user", "content": ""})
    st.rerun()

st.subheader("Test Data & Evaluators")

if 'testData' not in st.session_state:
    st.session_state['testData'] = data.get('testData', [])
if 'evaluators' not in st.session_state:
    st.session_state['evaluators'] = data.get('evaluators', [])

if 'current_file_td' not in st.session_state or st.session_state['current_file_td'] != selected_file:
    st.session_state['current_file_td'] = selected_file
    st.session_state['testData'] = data.get('testData', [])
    st.session_state['evaluators'] = data.get('evaluators', [])

st.markdown("### Test Data")
for i, td in enumerate(st.session_state['testData']):
    with st.expander(f"Test Case {i+1}"):
        col1, col2, col3 = st.columns([4, 4, 1])
        with col1:
            st.markdown("**Inputs**")
            inputs_json = td.get('inputs', td.get('input', {}))
            
            # Dynamically generate fields based on defined variables
            updated_inputs = {}
            for var in data.get('variables', []):
                var_name = var.get('name')
                if var_name:
                    updated_inputs[var_name] = st.text_input(f"{var_name}", value=inputs_json.get(var_name, ""), key=f"td_inputs_{i}_{var_name}")
            
            if 'input' in td:
                st.session_state['testData'][i]['input'] = updated_inputs
            else:
                st.session_state['testData'][i]['inputs'] = updated_inputs
        with col2:
            st.session_state['testData'][i]['expected'] = st.text_area(f"Expected Output", value=str(td.get('expected', '')), key=f"td_expected_{i}")
        with col3:
            if st.button("X", key=f"del_td_{i}"):
                st.session_state['testData'].pop(i)
                st.rerun()

if st.button("Add Test Case"):
    st.session_state['testData'].append({"inputs": {}, "expected": ""})
    st.rerun()

st.markdown("### Evaluators")
for i, ev in enumerate(st.session_state['evaluators']):
    with st.expander(f"Evaluator: {ev.get('name', 'New')}"):
        col1, col2, col3 = st.columns([3, 6, 1])
        with col1:
            st.session_state['evaluators'][i]['name'] = st.text_input(f"Name", value=ev.get('name', ''), key=f"ev_name_{i}")
        with col2:
            st.markdown("**Logic Builder**")
            
            from promptops.validation import EvaluatorRule
            
            py_logic = ev.get('python', '')
            rule = EvaluatorRule.from_python_expression(py_logic)
            eval_type = rule.rule_type
            eval_value = rule.value
            
            subcol1, subcol2 = st.columns(2)
            with subcol1:
                sel_type = st.selectbox("Rule Type", ["Contains", "Does Not Contain", "Regex Match", "Length >", "Length <", "Custom Python"], index=["Contains", "Does Not Contain", "Regex Match", "Length >", "Length <", "Custom Python"].index(eval_type) if eval_type in ["Contains", "Does Not Contain", "Regex Match", "Length >", "Length <", "Custom Python"] else 5, key=f"ev_type_{i}")
            
            with subcol2:
                if sel_type != "Custom Python":
                    val = st.text_input("Value", value=eval_value, key=f"ev_val_{i}")
                    new_rule = EvaluatorRule(rule_type=sel_type, value=val)
                    st.session_state['evaluators'][i]['python'] = new_rule.to_python_expression()
                else:
                    st.session_state['evaluators'][i]['python'] = st.text_area("Custom Python", value=py_logic, key=f"ev_py_{i}")
        with col3:
            if st.button("X", key=f"del_ev_{i}"):
                st.session_state['evaluators'].pop(i)
                st.rerun()

if st.button("Add Evaluator"):
    st.session_state['evaluators'].append({"name": "", "python": ""})
    st.rerun()

if st.button("Save Changes", type="primary"):
    if not new_file_path.endswith('.prompt.md'):
        st.error("File path must end with .prompt.md")
    else:
        data['modelParameters'].update({"temperature": temperature, "max_tokens": max_tokens})
        data['variables'] = edited_var_df.to_dict('records')
        data['messages'] = st.session_state['messages']
        data['testData'] = st.session_state['testData']
        data['evaluators'] = st.session_state['evaluators']
        
        full_path = os.path.join(base_dir, new_file_path)
        validate_and_save_asset(full_path, data, PromptSchema, success_message="Saved successfully and validated!")

