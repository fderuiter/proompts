import sys
import json
import asyncio
import tempfile
import contextlib
import io
import re
import logging
import glob
from pathlib import Path
import jsonschema

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
import mcp.types as types

from promptops.utils import iter_prompt_files, load_yaml, extract_template_vars, iter_skill_manifests, parse_skill_manifest
from promptops.validation import PromptSchema
from promptops.simulation import simulate_prompt

# Setup basic logging to stderr
logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

PROMPTS_DIR = "prompts"
WORKFLOWS_DIR = "workflows"

server = Server("DynamicProompts")
active_session = None
main_loop = None

class PromptDirHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith('.prompt.yaml') or event.src_path.endswith('skills.md') or event.src_path.endswith('.workflow.yaml'):
            logger.info(f"File change detected: {event.src_path}")
            if active_session and main_loop:
                asyncio.run_coroutine_threadsafe(
                    active_session.send_tool_list_changed(),
                    main_loop
                )

def get_tool_name(path: Path, content: dict) -> str:
    name = content.get('name')
    if not name:
        name = path.name.replace(".prompt.yaml", "").replace(".workflow.yaml", "")
        
    name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')
    
    if len(name) > 64:
        import hashlib
        h = hashlib.md5(str(path).encode()).hexdigest()[:6]
        name = name[:57] + "_" + h
        
    return name

def build_schema(prompt_content_or_vars):
    if isinstance(prompt_content_or_vars, list):
        variables = prompt_content_or_vars
    else:
        variables = prompt_content_or_vars.get('variables') or prompt_content_or_vars.get('vars') or prompt_content_or_vars.get('inputs')

    properties = {}
    required = []
    
    if variables:
        if isinstance(variables, list):
            for var in variables:
                if isinstance(var, dict):
                    name = var.get('name')
                    if not name:
                        continue
                    properties[name] = {
                        "type": "string",
                        "description": var.get('description', f"The {name} input.")
                    }
                    if var.get('required', True):
                        required.append(name)
                elif isinstance(var, str):
                    properties[var] = {
                        "type": "string",
                        "description": f"The {var} input."
                    }
                    required.append(var)
        elif isinstance(variables, dict):
            for name, desc in variables.items():
                properties[name] = {
                    "type": "string",
                    "description": str(desc) if desc else f"The {name} input."
                }
                required.append(name)
    elif isinstance(prompt_content_or_vars, dict):
        extracted_vars = extract_template_vars(prompt_content_or_vars)
        for var in extracted_vars:
            properties[var] = {
                "type": "string",
                "description": f"The {var} input."
            }
            required.append(var)
            
    return {
        "type": "object",
        "properties": properties,
        "required": required
    }

_tool_registry = {}

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    global active_session
    try:
        active_session = server.request_context.session
    except:
        active_session = None
    tools = []
    _tool_registry.clear()
    
    logger.info("Scanning for skill manifests...")
    from promptops.utils import iter_skill_manifests, parse_skill_manifest
    for path in iter_skill_manifests(PROMPTS_DIR):
        try:
            manifest = parse_skill_manifest(path)
            domain = manifest["metadata"].get("domain") or path.parent.name
            for skill in manifest["skills"]:
                stem = re.sub(r'[^a-zA-Z0-9_-]', '_', skill["name"]).lower().strip('_')
                full_name = f"{domain}_{stem}".lower()

                tools.append(types.Tool(
                    name=full_name,
                    description=skill.get("description", "Agent Skill"),
                    inputSchema=build_schema(skill.get("variables", []))
                ))
                _tool_registry[full_name] = {"type": "skill", "path": path, "skill": skill}
        except Exception as e:
            logger.error(f"Error parsing manifest {path}: {e}")

    logger.info("Scanning for workflows...")
    workflow_files = glob.glob(f"{WORKFLOWS_DIR}/**/*.workflow.yaml", recursive=True)
    for wf_path in workflow_files:
        try:
            wf_data = load_yaml(wf_path)
            if not wf_data:
                continue
            wf_path_obj = Path(wf_path)
            domain = wf_path_obj.parent.name
            stem = re.sub(r'[^a-zA-Z0-9_-]', '_', wf_data.get("name", wf_path_obj.stem)).lower().strip('_')
            full_name = f"{domain}_workflow_{stem}".lower()
            
            tools.append(types.Tool(
                name=full_name,
                description=wf_data.get("description", "Multi-step workflow"),
                inputSchema=build_schema(wf_data.get("inputs", []))
            ))
            _tool_registry[full_name] = {"type": "workflow", "path": wf_path, "data": wf_data}
        except Exception as e:
            logger.error(f"Error parsing workflow {wf_path}: {e}")

    logger.info(f"Discovered {len(tools)} tools.")
    return tools

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[types.TextContent]:
    if arguments is None:
        arguments = {}
        
    if name not in _tool_registry:
        raise ValueError(f"Tool not found: {name}")
        
    tool_info = _tool_registry[name]
    from promptops.engine import run
    
    if tool_info["type"] == "workflow":
        wf_path = tool_info["path"]
        logger.info(f"Executing workflow {wf_path} via tool {name}")
        result = run(wf_path, arguments, verbose=False)
        if result and "steps" in result:
            final_step_id = tool_info["data"].get("steps", [{}])[-1].get("step_id")
            if final_step_id and final_step_id in result["steps"]:
                output_text = result["steps"][final_step_id]["output"]
            else:
                output_text = "Workflow executed, but no final output was found."
        else:
            output_text = "Workflow simulation failed."
            
        return [types.TextContent(
            type="text",
            text=f"--- Executing Workflow: {tool_info['data'].get('name', wf_path)} ---\n\n{output_text}"
        )]
    elif tool_info["type"] == "skill":
        skill = tool_info["skill"]
        # Treat skill as a single prompt for consistent rendering using the engine
        # Save a temporary prompt file to execute it through the engine
        with tempfile.NamedTemporaryFile(suffix=".prompt.yaml", mode="w", delete=False) as tmp:
            yaml_content = {
                "name": skill["name"],
                "variables": skill.get("variables", []),
                "messages": [{"role": "system", "content": skill.get("instructions", "")}],
                "testData": [{"vars": arguments, "expected": "Simulation result for tool call"}]
            }
            import yaml
            yaml.dump(yaml_content, tmp)
            tmp_path = tmp.name
            
        try:
            result = run(tmp_path, arguments, verbose=False)
            if result and "steps" in result and "step_1" in result["steps"]:
                output_text = result["steps"]["step_1"]["output"]
            else:
                output_text = "Skill simulation failed."
                
            return [types.TextContent(
                type="text",
                text=f"--- Executing Skill: {skill['name']} ---\n\n{output_text}"
            )]
        finally:
            import os
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

async def run_server():
    global main_loop
    main_loop = asyncio.get_running_loop()
    
    observer = Observer()
    handler = PromptDirHandler()
    observer.schedule(handler, path=PROMPTS_DIR, recursive=True)
    if Path(WORKFLOWS_DIR).exists():
        observer.schedule(handler, path=WORKFLOWS_DIR, recursive=True)
    observer.start()
    logger.info(f"Started monitoring {PROMPTS_DIR} and {WORKFLOWS_DIR} for changes.")

    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="DynamicProompts",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(
                        prompts_changed=True,
                        resources_changed=True,
                        tools_changed=True
                    ),
                    experimental_capabilities={},
                ),
            )
        )
    
    observer.stop()
    observer.join()

if __name__ == "__main__":
    asyncio.run(run_server())
