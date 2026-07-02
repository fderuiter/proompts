import sys
import os
import glob
import yaml
import json
import streamlit as st
from typing import Any

st.set_page_config(page_title="Workflow Editor", layout="wide")
st.title("Workflow Editor")

from promptops.utils import ROOT
base_dir = str(ROOT)
workflow_files = glob.glob(os.path.join(base_dir, "workflows", "**", "*.workflow.yaml"), recursive=True)
workflow_files = [os.path.relpath(f, base_dir) for f in workflow_files]

prompt_files = glob.glob(os.path.join(base_dir, "prompts", "**", "*.prompt.md"), recursive=True)
prompt_files = [os.path.relpath(f, base_dir) for f in prompt_files]

selected_file = st.selectbox("Select a workflow to edit", ["Create New..."] + workflow_files)

from promptops.utils import load_yaml, save_yaml
from promptops.validation import WorkflowSchema

if selected_file == "Create New...":
    st.subheader("Create New Workflow")
    new_file_path = st.text_input("File Path (e.g., workflows/my_workflow.workflow.yaml)")
    data: dict[str, Any] = {
        "name": "",
        "description": "",
        "inputs": [],
        "steps": []
    }
else:
    new_file_path = selected_file
    file_path = os.path.join(base_dir, selected_file)
    try:
        data = load_yaml(file_path, raw=True)
    except Exception as e:
        st.error(f"Failed to load file: {e}")
        st.stop()
st.subheader(f"Editing: {selected_file}")

# Load schema to dynamically generate UI
schema_path = os.path.join(base_dir, "docs", "schemas", "workflow.schema.json")
schema = {}
if os.path.exists(schema_path):
    with open(schema_path, 'r') as f:
        schema = json.load(f)

properties = schema.get("properties", {})
for field_name, field_info in properties.items():
    if field_name not in ["inputs", "steps"]:
        val = data.get(field_name, "")
        label = field_info.get("description", field_name)
        if field_info.get("type") == "string":
            if "description" in field_name.lower():
                data[field_name] = st.text_area(label, value=val)
            else:
                data[field_name] = st.text_input(label, value=val)
        elif field_info.get("type") == "boolean":
            data[field_name] = st.checkbox(label, value=bool(val))

# Global Inputs Editor
st.subheader("Global Inputs")
if 'wf_inputs' not in st.session_state or st.session_state.get('wf_current_file') != selected_file:
    st.session_state['wf_inputs'] = data.get('inputs', [])
    st.session_state['wf_steps'] = data.get('steps', [])
    st.session_state['wf_current_file'] = selected_file

import pandas as pd
inputs_df = pd.DataFrame(st.session_state['wf_inputs']) if st.session_state['wf_inputs'] else pd.DataFrame(columns=["name", "description"])
edited_inputs_df = st.data_editor(inputs_df, num_rows="dynamic", key="wf_inputs_editor")

st.subheader("Workflow Steps")

def get_prompt_variables(prompt_file_path):
    full_path = os.path.join(base_dir, prompt_file_path)
    p_data = load_yaml(full_path)
    return [v.get('name') for v in p_data.get('variables', [])] if p_data else []

# Collect available output variables from previous steps and global inputs
def get_available_mappings(current_step_index):
    options = [""]
    # Global inputs
    for idx, row in edited_inputs_df.iterrows():
        if pd.notna(row.get('name')):
            options.append(f"{{{{inputs.{row['name']}}}}}")
    
    # Previous steps outputs
    for i in range(current_step_index):
        s_id = st.session_state['wf_steps'][i].get('step_id')
        if s_id:
            options.append(f"{{{{steps.{s_id}.output}}}}")
            
    return options

for i, step in enumerate(st.session_state['wf_steps']):
    with st.expander(f"Step: {step.get('step_id', 'Un-named')}"):
        col1, col2 = st.columns(2)
        with col1:
            step_id = st.text_input(f"Step ID", value=step.get('step_id', ''), key=f"step_id_{i}")
            st.session_state['wf_steps'][i]['step_id'] = step_id
        with col2:
            prompt_idx = 0
            if step.get('prompt_file') in prompt_files:
                prompt_idx = prompt_files.index(step.get('prompt_file'))
            prompt_file = st.selectbox(f"Prompt File", prompt_files, index=prompt_idx, key=f"prompt_file_{i}")
            st.session_state['wf_steps'][i]['prompt_file'] = prompt_file
            
        st.markdown("**Map Inputs (Live Variable Mapping)**")
        required_vars = get_prompt_variables(prompt_file)
        
        if 'map_inputs' not in st.session_state['wf_steps'][i]:
            st.session_state['wf_steps'][i]['map_inputs'] = {}
            
        map_inputs = st.session_state['wf_steps'][i]['map_inputs']
        
        available_mappings = get_available_mappings(i)
        
        for req_var in required_vars:
            current_val = map_inputs.get(req_var, "")
            
            mapping_col1, mapping_col2 = st.columns(2)
            with mapping_col1:
                st.markdown(f"`{req_var}`")
            with mapping_col2:
                # Provide a selectbox for easy picking, but allow custom text input as well
                options = list(available_mappings)
                if current_val and current_val not in options:
                    options.append(current_val)
                    
                sel_index = options.index(current_val) if current_val in options else 0
                selected_mapping = st.selectbox(f"Map for {req_var}", options, index=sel_index, key=f"map_{i}_{req_var}")
                st.session_state['wf_steps'][i]['map_inputs'][req_var] = selected_mapping
                
        st.markdown("**Step Transitions (Next)**")
        if 'next' not in st.session_state['wf_steps'][i]:
            st.session_state['wf_steps'][i]['next'] = []
            
        next_edges = st.session_state['wf_steps'][i]['next']
        if not isinstance(next_edges, list):
            # Normalize to list
            if isinstance(next_edges, str):
                next_edges = [{"target": next_edges}]
            else:
                next_edges = []
            st.session_state['wf_steps'][i]['next'] = next_edges
            
        for e_idx, edge in enumerate(next_edges):
            ecol1, ecol2, ecol3, ecol4 = st.columns([3, 2, 3, 1])
            
            # Logic Builder for condition
            condition_str = edge.get("condition", "")
            cond_var = ""
            cond_op = "Always"
            cond_val = ""
            
            if condition_str:
                import re
                m = re.match(r"\{\%\s*if\s+(.+)\s+(==|!=|>|<|>=|<=)\s+(.+)\s*\%\}true\{\%\s*endif\s*\%\}", condition_str)
                if m:
                    cond_var = m.group(1).strip()
                    cond_op = m.group(2).strip()
                    cond_val = m.group(3).strip().strip("'\"")
                else:
                    cond_op = "Custom Jinja2"
                    cond_val = condition_str
            
            with ecol1:
                if cond_op == "Custom Jinja2":
                    st.text_input("Custom Condition", value=cond_val, key=f"cond_custom_{i}_{e_idx}", disabled=True)
                else:
                    target_var = st.selectbox("Condition Source", [""] + available_mappings, index=(available_mappings.index(f"{{{{{cond_var}}}}}") if f"{{{{{cond_var}}}}}" in available_mappings else 0) if cond_var else 0, key=f"cond_src_{i}_{e_idx}")
            with ecol2:
                selected_op = st.selectbox("Operator", ["Always", "==", "!=", ">", "<", "Custom Jinja2"], index=["Always", "==", "!=", ">", "<", "Custom Jinja2"].index(cond_op) if cond_op in ["Always", "==", "!=", ">", "<", "Custom Jinja2"] else 0, key=f"cond_op_{i}_{e_idx}")
            with ecol3:
                if selected_op not in ["Always", "Custom Jinja2"]:
                    selected_val = st.text_input("Value", value=cond_val, key=f"cond_val_{i}_{e_idx}")
                    if target_var:
                        stripped_var = target_var.replace("{{", "").replace("}}", "")
                        st.session_state['wf_steps'][i]['next'][e_idx]["condition"] = f"{{% if {stripped_var} {selected_op} '{selected_val}' %}}true{{% endif %}}"
                elif selected_op == "Always":
                    if "condition" in st.session_state['wf_steps'][i]['next'][e_idx]:
                        del st.session_state['wf_steps'][i]['next'][e_idx]["condition"]
                        
            with ecol4:
                # Target step
                all_step_ids = [s.get("step_id") for s in st.session_state['wf_steps'] if s.get("step_id")]
                target_idx = all_step_ids.index(edge.get("target")) if edge.get("target") in all_step_ids else 0
                selected_target = st.selectbox("Target", all_step_ids, index=target_idx if all_step_ids else 0, key=f"cond_tgt_{i}_{e_idx}")
                st.session_state['wf_steps'][i]['next'][e_idx]["target"] = selected_target

        if st.button("Add Branch", key=f"add_branch_{i}"):
            st.session_state['wf_steps'][i]['next'].append({"target": ""})
            st.rerun()
            
        if st.button("Remove Step", key=f"del_step_{i}"):
            st.session_state['wf_steps'].pop(i)
            st.rerun()

if st.button("Add Step"):
    st.session_state['wf_steps'].append({"step_id": f"step_{len(st.session_state['wf_steps'])+1}", "prompt_file": prompt_files[0] if prompt_files else "", "map_inputs": {}})
    st.rerun()

st.subheader("Visualizer")
steps = st.session_state['wf_steps']

if steps:
    graph = "digraph G {\n"
    graph += "  rankdir=LR;\n"
    graph += "  node [shape=box, style=filled, fillcolor=lightblue];\n"
    
    # Track which steps output are used
    for step in steps:
        step_id = step.get('step_id', 'unknown')
        p_file = os.path.basename(step.get("prompt_file", ""))
        graph += f'  "{step_id}" [label="{step_id}\\n({p_file})"];\n'
        
        # Draw control flow edges based on 'next'
        for next_edge in step.get('next', []):
            if isinstance(next_edge, dict) and next_edge.get('target'):
                target = next_edge.get('target')
                condition = "conditional" if next_edge.get('condition') else "unconditional"
                graph += f'  "{step_id}" -> "{target}" [color="red", style="dashed", label="{condition}"];\n'
            elif isinstance(next_edge, str) and next_edge:
                graph += f'  "{step_id}" -> "{next_edge}" [color="red", style="dashed", label="unconditional"];\n'
        
        # Draw edges based on inputs
        for input_var, input_val in step.get('map_inputs', {}).items():
            if isinstance(input_val, str) and input_val.startswith('{{') and input_val.endswith('}}'):
                inner = input_val[2:-2].strip()
                if inner.startswith('steps.'):
                    parts = inner.split('.')
                    if len(parts) >= 2:
                        source_step = parts[1]
                        graph += f'  "{source_step}" -> "{step_id}" [label="{input_var}"];\n'
                elif inner.startswith('inputs.'):
                    parts = inner.split('.')
                    if len(parts) >= 2:
                        source_input = parts[1]
                        graph += f'  "INPUT_{source_input}" [shape=ellipse, fillcolor=lightgreen];\n'
                        graph += f'  "INPUT_{source_input}" -> "{step_id}" [label="{input_var}"];\n'
                        
    graph += "}\n"
    st.graphviz_chart(graph)
else:
    st.info("No steps defined yet.")

if st.button("Save Workflow", type="primary"):
    if not new_file_path.endswith('.workflow.yaml'):
        st.error("File path must end with .workflow.yaml")
    else:
        try:
            data['inputs'] = edited_inputs_df.to_dict('records')
            data['steps'] = st.session_state['wf_steps']
            
            # Real-time validation using Pydantic
            WorkflowSchema(**data)
                
            full_path = os.path.join(base_dir, new_file_path)
            save_yaml(full_path, data)
            st.success("Saved workflow successfully and validated!")
        except Exception as e:
            st.error(f"Error: {e}")

