import sys
import os
import glob
import yaml
import json
import streamlit as st
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from tools.scripts.validate_prompt_schema import PromptSchema
from pydantic import ValidationError

st.set_page_config(page_title="Prompt Editor", layout="wide")
st.title("Prompt Editor")

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
prompt_files = glob.glob(os.path.join(base_dir, "prompts", "**", "*.prompt.yaml"), recursive=True)
prompt_files = [os.path.relpath(f, base_dir) for f in prompt_files]

selected_file = st.selectbox("Select a prompt to edit", ["Create New..."] + prompt_files)

def load_yaml(path):
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def save_yaml(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True, default_flow_style=False)

if selected_file == "Create New...":
    st.subheader("Create New Prompt")
    new_file_path = st.text_input("File Path (e.g., prompts/my_prompt.prompt.yaml)")
    data = {
        "name": "",
        "version": "0.1.0",
        "description": "",
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

name = st.text_input("Name", value=data.get('name', ''))
description = st.text_area("Description", value=data.get('description', ''))
model = st.text_input("Model", value=data.get('model', ''))

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
test_data_str = st.text_area("Test Data (JSON)", value=json.dumps(data.get('testData', []), indent=2), height=150)
evaluators_str = st.text_area("Evaluators (JSON)", value=json.dumps(data.get('evaluators', []), indent=2), height=100)

if st.button("Save Changes", type="primary"):
    if not new_file_path.endswith('.prompt.yaml'):
        st.error("File path must end with .prompt.yaml")
    else:
        try:
            data['name'] = name
            data['description'] = description
            data['model'] = model
            data['modelParameters'].update({"temperature": temperature, "max_tokens": max_tokens})
            data['variables'] = edited_var_df.to_dict('records')
            data['messages'] = st.session_state['messages']
            data['testData'] = json.loads(test_data_str)
            data['evaluators'] = json.loads(evaluators_str)
            
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
