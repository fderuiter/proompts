import os
import subprocess
import streamlit as st

st.set_page_config(page_title="Git Sync", layout="wide")
st.title("Git Sync")
st.markdown("Save & Sync your local changes to the repository.")

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
    return result

st.subheader("Current Status")
status_result = run_cmd("git status --short")
if status_result.stdout.strip():
    st.code(status_result.stdout)
else:
    st.info("No changes to sync.")

commit_msg = st.text_input("Commit Message", value="Update prompts via Proompts Studio")

if st.button("Save & Sync", type="primary"):
    with st.spinner("Syncing..."):
        # Git add
        add_result = run_cmd("git add prompts/ workflows/")
        
        # Git commit
        commit_result = run_cmd(f'git commit -m "{commit_msg}"')
        
        # Git push
        push_result = run_cmd("git push")
        
        if push_result.returncode == 0:
            st.success("Successfully synced changes to remote repository!")
            st.code(push_result.stdout)
        else:
            st.error("Push failed.")
            st.code(push_result.stderr)
            
            if "nothing to commit" in commit_result.stdout:
                st.warning("Nothing to commit.")

