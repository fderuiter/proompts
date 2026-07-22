import subprocess
import sys
import asyncio
import logging
from pathlib import Path
from typing import Any

from promptops.utils import get_tool_name_mcp

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
import mcp.types as types

from promptops.utils import load_yaml, extract_template_vars, WORKFLOWS_DIR, PROMPTS_DIR
from promptops.validation import ProomptsValidationError

# Setup basic logging to stderr
logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)


server = Server("DynamicProompts")
active_session = None
main_loop = None

class PromptDirHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith(('.prompt.yaml', '.prompt.yml', '.prompt.md', 'skills.md', '.workflow.yaml', '.workflow.yml')):
            logger.info(f"File change detected: {event.src_path}")
            # Trigger document rebuild without blocking
            subprocess.Popen(["uv", "run", "promptops", "docs"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if active_session and main_loop:
                asyncio.run_coroutine_threadsafe(
                    active_session.send_tool_list_changed(),
                    main_loop
                )


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

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    global active_session
    try:
        active_session = server.request_context.session
    except:
        active_session = None
    tools = []
    
    logger.info("Scanning for skill manifests...")
    from promptops.utils import iter_skill_manifests, parse_skill_manifest, iter_prompt_files, iter_workflow_files, WORKFLOWS_DIR
    for path in iter_skill_manifests(PROMPTS_DIR):
        try:
            manifest = parse_skill_manifest(path)
            manifest["metadata"].get("domain") or path.parent.name
            for skill in manifest["skills"]:
                full_name = get_tool_name_mcp(path, skill)

                tools.append(types.Tool(
                    name=full_name,
                    description=skill.get("description", "Agent Skill"),
                    inputSchema=build_schema(skill.get("variables", []))
                ))
        except Exception as e:
            logger.error(f"Error parsing manifest {path}: {e}")

    logger.info("Scanning for individual prompt files...")
    for path in iter_prompt_files(PROMPTS_DIR):
        try:
            content = load_yaml(path)
            if not content: continue
            name = get_tool_name_mcp(path, content)
            tools.append(types.Tool(
                name=name,
                description=content.get("description", "Prompt Tool"),
                inputSchema=build_schema(content)
            ))
        except Exception as e:
            logger.error(f"Error parsing prompt {path}: {e}")

    logger.info("Scanning for workflow files...")
    for path in iter_workflow_files(WORKFLOWS_DIR):
        try:
            content = load_yaml(path)
            if not content: continue
            name = get_tool_name_mcp(path, content)
            tools.append(types.Tool(
                name=name,
                description=content.get("description", "Workflow Tool"),
                inputSchema=build_schema(content)
            ))
        except Exception as e:
            logger.error(f"Error parsing workflow {path}: {e}")

    logger.info(f"Discovered {len(tools)} tools.")
    return tools

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[types.TextContent]:
    if arguments is None:
        arguments = {}
        
    from promptops.utils import iter_skill_manifests, parse_skill_manifest, iter_prompt_files, iter_workflow_files, WORKFLOWS_DIR
    from promptops.engine import simulate_prompt_execution, run_workflow

    for path in iter_prompt_files(PROMPTS_DIR):
        try:
            content = load_yaml(path)
            if content and get_tool_name_mcp(path, content) == name:
                try:
                    fidelity: dict[str, Any] = {}
                    out = simulate_prompt_execution(content, arguments, prompt_file=str(path), strict_mode=False, chaos_mode=False, fidelity_report=fidelity)
                    return [types.TextContent(type="text", text=f"--- Executing Prompt: {content.get('name')} ---\n\n{out}")]
                except ProomptsValidationError as e:
                    return [types.TextContent(type="text", text=f"--- Validation Error ---\n\nResponse validation failed for '{name}': {e}")]
                except Exception as e:
                    return [types.TextContent(type="text", text=f"--- Execution Error ---\n\nExecution failed for '{name}': {e}")]
        except:
            continue

    for path in iter_workflow_files(WORKFLOWS_DIR):
        try:
            content = load_yaml(path)
            if content and get_tool_name_mcp(path, content) == name:
                try:
                    fidelity = {}
                    state = run_workflow(str(path), arguments, verbose=False, strict_mode=False, chaos_mode=False, fidelity_report=fidelity)
                    out = ""
                    if state:
                        final_output_step_id = content.get('steps', [{}])[-1].get('step_id')
                        if final_output_step_id and final_output_step_id in state['steps']:
                            out = state['steps'][final_output_step_id]['output']
                    return [types.TextContent(type="text", text=f"--- Executing Workflow: {content.get('name')} ---\n\n{out}")]
                except ProomptsValidationError as e:
                    return [types.TextContent(type="text", text=f"--- Validation Error ---\n\nResponse validation failed for '{name}': {e}")]
                except Exception as e:
                    return [types.TextContent(type="text", text=f"--- Execution Error ---\n\nExecution failed for '{name}': {e}")]
        except:
            continue

    # Check skill manifests
    for path in iter_skill_manifests(PROMPTS_DIR):
        try:
            manifest = parse_skill_manifest(path)
            manifest["metadata"].get("domain") or path.parent.name
            for skill in manifest["skills"]:
                full_name = get_tool_name_mcp(path, skill)

                if full_name == name:
                    try:
                        content = {
                            "name": skill["name"],
                            "description": skill.get("description", ""),
                            "variables": skill.get("variables", []),
                            "messages": [{"role": "system", "content": skill.get("instructions", "")}],
                            "testData": skill.get("testData", [])
                        }
                        fidelity = {}
                        out = simulate_prompt_execution(content, arguments, prompt_file=str(path), strict_mode=False, chaos_mode=False, fidelity_report=fidelity)
                        return [types.TextContent(
                            type="text",
                            text=f"--- Executing Skill: {skill['name']} ---\n\n{out}"
                        )]
                    except ProomptsValidationError as e:
                        return [types.TextContent(type="text", text=f"--- Validation Error ---\n\nResponse validation failed for '{name}': {e}")]
                    except Exception as e:
                        return [types.TextContent(type="text", text=f"--- Execution Error ---\n\nExecution failed for '{name}': {e}")]
        except:
            continue

    raise ValueError(f"Tool not found: {name}")

async def run():
    global main_loop
    main_loop = asyncio.get_running_loop()
    
    observer = Observer()
    handler = PromptDirHandler()
    
    # Watch prompts directory
    observer.schedule(handler, path=str(PROMPTS_DIR), recursive=True)
    logger.info(f"Started monitoring {PROMPTS_DIR} for changes.")
    
    # Watch workflows directory
    workflows_path = str(WORKFLOWS_DIR)
    if Path(workflows_path).exists():
        observer.schedule(handler, path=workflows_path, recursive=True)
        logger.info(f"Started monitoring {workflows_path} for changes.")
        
    observer.start()

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
    asyncio.run(run())
