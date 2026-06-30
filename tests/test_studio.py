from streamlit.testing.v1 import AppTest
from pathlib import Path
import os
import shutil

STUDIO_DIR = Path(__file__).parent.parent / "studio"
ROOT_DIR = Path(__file__).parent.parent

def test_app_launches():
    at = AppTest.from_file(str(STUDIO_DIR / "studio/app.py"))
    at.run(timeout=15)
    assert not at.exception

def test_prompt_editor_launches_and_saves():
    at = AppTest.from_file(str(STUDIO_DIR / "studio/pages" / "1_📝_Prompt_Editor.py"))
    at.run(timeout=15)
    assert not at.exception

    # Find text inputs
    file_path_ti = None
    for ti in at.text_input:
        if ti.label == "File Path (e.g., prompts/my_prompt.prompt.md)":
            file_path_ti = ti
            break
            
    assert file_path_ti is not None
    file_path_ti.set_value("prompts/test_new.prompt.md")
    
    # Click save
    save_btn = None
    for btn in at.button:
        if btn.label == "Save Changes":
            save_btn = btn
            break
            
    assert save_btn is not None
    save_btn.click().run()
    assert not at.exception
    
    success_found = False
    for el in at.success:
        if "Saved successfully and validated!" in el.value:
            success_found = True
            break
    
    assert success_found, "App did not report successful save"
    
    # Check if file was created
    test_file = ROOT_DIR / "prompts" / "test_new.prompt.md"
    assert test_file.exists()
    test_file.unlink()
    
    # Clean up
    if test_file.exists():
        os.remove(str(test_file))


def test_workflow_editor_launches_and_saves():
    at = AppTest.from_file(str(STUDIO_DIR / "studio/pages" / "2_🔄_Workflow_Editor.py"))
    at.run(timeout=15)
    assert not at.exception

    # Find text inputs
    file_path_ti = None
    for ti in at.text_input:
        if ti.label == "File Path (e.g., workflows/my_workflow.workflow.yaml)":
            file_path_ti = ti
            break
            
    assert file_path_ti is not None
    file_path_ti.set_value("workflows/test_new.workflow.yaml")
    
    # Click save
    save_btn = None
    for btn in at.button:
        if btn.label == "Save Workflow":
            save_btn = btn
            break
            
    assert save_btn is not None
    save_btn.click().run()
    assert not at.exception
    
    success_found = False
    for el in at.success:
        if "Saved workflow successfully and validated!" in el.value:
            success_found = True
            break
    
    assert success_found, "App did not report successful save"
    
    # Check if file was created
    test_file = ROOT_DIR / "workflows" / "test_new.workflow.yaml"
    assert test_file.exists()
    test_file.unlink()
    
    # Clean up
    if test_file.exists():
        os.remove(str(test_file))

