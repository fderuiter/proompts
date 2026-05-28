import sys
import os
import streamlit as st

# Add parent dir to path to allow importing tools
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.set_page_config(page_title="Proompts Studio", page_icon="✨", layout="wide")

st.title("Proompts Studio")
st.markdown("""
Welcome to the Proompts Studio! 
Use the sidebar to navigate between:
- **Prompt Editor**: Visual editor for `.prompt.yaml` files
- **Workflow Editor**: Visual editor for `.workflow.yaml` files 
- **Simulation Runner**: Run zero-cost simulations
- **Git Sync**: Sync your changes to the repository
""")
