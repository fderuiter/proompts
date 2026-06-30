import sys
import os
import glob
import yaml
import json
import streamlit as st
import pandas as pd

from tools.scripts.validate_prompt_schema import PromptSchema
from pydantic import ValidationError

st.set_page_config(page_title="Prompt Editor", layout="wide")
st.title("Prompt Editor")

from promptops.utils import ROOT
base_dir = str(ROOT)
prompt_files = glob.glob(os.path.join(base_dir, "prompts", "**", "*.prompt.md"), recursive=True)
prompt_files = [os.path.relpath(f, base_dir) for f in prompt_files]

selected_file = st.selectbox("Select a prompt to edit", ["Create New..."] + prompt_files)

from typing import Dict, Any

def load_yaml(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        return yaml.safe_load(f) or {}

def save_yaml(path: str, data: Dict[str, Any]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True, default_flow_style=False)

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
            "tags": ["skill"]
        },
        "model": "gpt-4",
        "modelParameters": {"temperature": 0.7, "max_tokens": 1000},
        "variables": [{"name": "input", "description": "User input"}],
        "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "{{input}}"}],
        "testData": [{"inputs": {"input": "test"}, "expected": "Output"}],
        "evaluators": []
    }
else:
    new_file_path = selected_file
    file_path = os.path.join(base_dir, selected_file)
    try:
        data = load_yaml(file_path)
    except Exception as e:
        st.error(f"Failed to load file: {e}")
        st.stop()
st.subheader(f"Editing: {selected_file}")

# Dynamically generate basic fields from schema
basic_fields = ['name', 'description', 'model', 'version', 'safety_opt_out']
for field_name in basic_fields:
    field_info = PromptSchema.model_fields.get(field_name)
    if not field_info: continue
    
    label = field_info.description or field_name
    val = data.get(field_name, field_info.default if field_info.default is not ... else "")
    
    import typing
    # Handle typing for Pydantic 2
    if getattr(field_info.annotation, '__origin__', None) is typing.Union and type(None) in getattr(field_info.annotation, '__args__', []):
        type_hint = getattr(field_info.annotation, '__args__')[0]
    else:
        type_hint = field_info.annotation
        
    if type_hint == str:
        if field_name == "description":
            data[field_name] = st.text_area(label, value=val or "")
        else:
            data[field_name] = st.text_input(label, value=val or "")
    elif type_hint == bool:
        data[field_name] = st.checkbox(label, value=bool(val))

st.subheader("Model Parameters")
model_params = data.get('modelParameters', {})
col1, col2 = st.columns(2)
with col1:
    temperature = st.number_input("Temperature", min_value=0.0, max_value=2.0, value=float(model_params.get('temperature', 0.7)), step=0.1)
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
            
            # Pre-parse common patterns from existing python strings
            py_logic = ev.get('python', '')
            eval_type = "Custom Python"
            eval_target = ""
            eval_value = ""
            
            if py_logic.startswith("len(output) > ") and py_logic[14:].isdigit():
                eval_type = "Length >"
                eval_value = py_logic[14:]
            elif py_logic.startswith("len(output) < ") and py_logic[14:].isdigit():
                eval_type = "Length <"
                eval_value = py_logic[14:]
            elif " in output" in py_logic and py_logic.startswith("'") and py_logic.split("'")[1]:
                eval_type = "Contains"
                eval_value = py_logic.split("'")[1]
            elif " not in output" in py_logic and py_logic.startswith("'"):
                eval_type = "Does Not Contain"
                eval_value = py_logic.split("'")[1]
            elif py_logic.startswith("re.search(") and "output" in py_logic:
                eval_type = "Regex Match"
                try:
                    eval_value = py_logic.split("r'")[1].split("',")[0]
                except:
                    eval_value = ""
            
            subcol1, subcol2 = st.columns(2)
            with subcol1:
                sel_type = st.selectbox("Rule Type", ["Contains", "Does Not Contain", "Regex Match", "Length >", "Length <", "Custom Python"], index=["Contains", "Does Not Contain", "Regex Match", "Length >", "Length <", "Custom Python"].index(eval_type) if eval_type in ["Contains", "Does Not Contain", "Regex Match", "Length >", "Length <", "Custom Python"] else 5, key=f"ev_type_{i}")
            
            with subcol2:
                if sel_type != "Custom Python":
                    val = st.text_input("Value", value=eval_value, key=f"ev_val_{i}")
                    if sel_type == "Contains":
                        st.session_state['evaluators'][i]['python'] = f"'{val}' in output"
                    elif sel_type == "Does Not Contain":
                        st.session_state['evaluators'][i]['python'] = f"'{val}' not in output"
                    elif sel_type == "Regex Match":
                        st.session_state['evaluators'][i]['python'] = f"re.search(r'{val}', output)"
                    elif sel_type == "Length >":
                        st.session_state['evaluators'][i]['python'] = f"len(output) > {val if val.isdigit() else 0}"
                    elif sel_type == "Length <":
                        st.session_state['evaluators'][i]['python'] = f"len(output) < {val if val.isdigit() else 0}"
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
        try:
            data['modelParameters'].update({"temperature": temperature, "max_tokens": max_tokens})
            data['variables'] = edited_var_df.to_dict('records')
            data['messages'] = st.session_state['messages']
            data['testData'] = st.session_state['testData']
            data['evaluators'] = st.session_state['evaluators']

            
            # Real-time validation
            PromptSchema(**data)
            
            full_path = os.path.join(base_dir, new_file_path)
            save_yaml(full_path, data)
            st.success("Saved successfully and validated!")
        except json.JSONDecodeError as e:
            st.error(f"JSON Parsing Error: {e}")
        except ValidationError as e:
            st.error("Validation Error: " + str(e))
        except Exception as e:
            st.error(f"Error: {e}")
