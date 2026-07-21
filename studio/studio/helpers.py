import os
import streamlit as st
from typing import Dict, Any, Type, List, Callable
from pydantic import BaseModel, ValidationError
import json

from promptops.utils import ROOT, iter_prompt_files, iter_workflow_files, load_yaml, save_yaml

def get_relative_asset_paths(asset_type: str, extensions: List[str] = None) -> list[str]:
    """
    Scans the workspace for prompt or workflow files, returning a sorted list of relative paths.
    Conforms to the standard workspace traverser.
    """
    base_dir = str(ROOT)
    if asset_type.lower() == "prompt":
        files = list(iter_prompt_files())
    elif asset_type.lower() == "workflow":
        files = list(iter_workflow_files())
    else:
        raise ValueError(f"Unknown asset type: {asset_type}")
        
    if extensions:
        files = [f for f in files if any(str(f).endswith(ext) for ext in extensions)]
    
    return sorted([os.path.relpath(str(f), base_dir) for f in files])

def render_file_selector(asset_type: str, key: str, label: str = None, extensions: List[str] = None) -> str:
    """
    Renders a unified selectbox for prompt or workflow files using relative paths.
    """
    paths = get_relative_asset_paths(asset_type, extensions=extensions)
    if not label:
        label = f"Select a {asset_type.lower()} file"
    return st.selectbox(label, options=paths, key=key)

def render_schema_form(
    schema_class: Type[BaseModel],
    data: Dict[str, Any],
    skip_fields: List[str] = None,
    key_prefix: str = ""
) -> Dict[str, Any]:
    """
    Dynamically generates Streamlit inputs from a Pydantic model's JSON schema.
    """
    if skip_fields is None:
        skip_fields = []
        
    schema = schema_class.model_json_schema()
    properties = schema.get("properties", {})
    
    for field_name, field_info in properties.items():
        if field_name in skip_fields:
            continue
            
        val = data.get(field_name, "")
        
        # Determine the label to use
        if "title" in field_info:
            label = field_info["title"]
        elif "description" in field_info and field_info["description"]:
            label = field_info["description"]
        else:
            label = field_name
            
        if field_name == "metadata":
            st.subheader("Metadata")
            if "metadata" not in data or not data["metadata"]:
                data["metadata"] = {}
                
            meta_schema = {}
            if "$defs" in schema:
                for def_name, def_schema in schema["$defs"].items():
                    if "Metadata" in def_name:
                        meta_schema = def_schema.get("properties", {})
                        break
                        
            for m_key, m_info in meta_schema.items():
                m_val = data["metadata"].get(m_key, m_info.get("default", ""))
                m_label = m_info.get("title", m_key)
                if m_info.get("type") == "boolean":
                    data["metadata"][m_key] = st.checkbox(m_label, value=bool(m_val), key=f"{key_prefix}meta_{m_key}")
                elif m_info.get("type") == "array":
                    m_val_str = ", ".join(m_val) if isinstance(m_val, list) else ""
                    res = st.text_input(m_label, value=m_val_str, key=f"{key_prefix}meta_{m_key}")
                    data["metadata"][m_key] = [x.strip() for x in res.split(",") if x.strip()]
                else:
                    data["metadata"][m_key] = st.text_input(m_label, value=m_val, key=f"{key_prefix}meta_{m_key}")
        elif field_info.get("type") == "string":
            if field_name == "description" or "description" in field_name.lower():
                data[field_name] = st.text_area(label, value=val, key=f"{key_prefix}{field_name}")
            else:
                data[field_name] = st.text_input(label, value=val, key=f"{key_prefix}{field_name}")
        elif field_info.get("type") == "boolean":
            data[field_name] = st.checkbox(label, value=bool(val), key=f"{key_prefix}{field_name}")
            
    return data

def load_asset_data(file_path: str, raw: bool = True) -> Dict[str, Any]:
    """Loads and returns YAML data. Standardizes error displays."""
    try:
        if os.path.exists(file_path):
            return load_yaml(file_path, raw=raw) or {}
    except Exception as e:
        st.error(f"Failed to load file: {e}")
    return {}

def validate_and_save_asset(
    file_path: str,
    data: Dict[str, Any],
    schema_class: Type[BaseModel],
    save_callback: Callable = None,
    success_message: str = None
) -> bool:
    """
    Validates data against the Pydantic schema_class.
    If valid, saves/serializes YAML to disk, or runs the custom save_callback (if any).
    Displays success/error notifications to the user in a consistent Streamlit banner style.
    """
    try:
        # Validate using Pydantic model instantiation
        schema_class(**data)
        
        # Save operation
        if save_callback:
            save_callback(file_path, data)
        else:
            save_yaml(file_path, data)
            
        msg = success_message or f"Successfully saved and validated {os.path.basename(file_path)}!"
        st.success(msg)
        return True
    except json.JSONDecodeError as e:
        st.error(f"JSON Parsing Error: {e}")
        return False
    except ValidationError as e:
        st.error("Validation Error: " + str(e))
        return False
    except Exception as e:
        st.error(f"Error: {e}")
        return False
