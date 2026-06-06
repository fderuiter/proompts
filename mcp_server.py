import sys
import json
import asyncio
import tempfile
import contextlib
import io
import re
import logging
from pathlib import Path
import jsonschema

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
import mcp.types as types

from promptops.utils import iter_prompt_files, load_yaml, extract_template_vars
from promptops.validation import PromptSchema
from promptops.simulation import simulate_prompt

# Setup basic logging to stderr
logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)

PROMPTS_DIR = "prompts"

server = Server("DynamicProompts")
active_session = None
main_loop = None

class PromptDirHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.src_path.endswith('.prompt.yaml'):
            logger.info(f"File change detected: {event.src_path}")
            if active_session and main_loop:
                # Notify clients about tool list change
                asyncio.run_coroutine_threadsafe(
                    active_session.send_tool_list_changed(),
                    main_loop
                )

def get_tool_name(path: Path, content: dict) -> str:
    name = content.get('name')
    if not name:
        name = path.name.replace(".prompt.yaml", "")
        
    name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    name = re.sub(r'_+', '_', name)
    name = name.strip('_')
    
    if len(name) > 64:
        import hashlib
        h = hashlib.md5(str(path).encode()).hexdigest()[:6]
        name = name[:57] + "_" + h
        
    return name

def build_schema(prompt_content):
    variables = prompt_content.get('variables') or prompt_content.get('vars') or prompt_content.get('inputs')
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
    else:
        extracted_vars = extract_template_vars(prompt_content)
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
    active_session = server.request_context.session
    tools = []
    
    logger.info("Scanning for prompt files...")
    for path in iter_prompt_files(PROMPTS_DIR):
        try:
            content = load_yaml(path)
            # Try to validate prompt structure
            PromptSchema(**content)
            
            tool_name = get_tool_name(path, content)
            desc = content.get('description', "A prompt tool")
            if not desc or desc == "Placeholder description" or desc.lower() == "placeholder description":
                desc = "A prompt tool"
                
            input_schema = build_schema(content)
            
            tools.append(types.Tool(
                name=tool_name,
                description=desc,
                inputSchema=input_schema
            ))
        except Exception as e:
            # Skip invalid prompts or log them
            pass
            
    logger.info(f"Discovered {len(tools)} tools.")
    return tools

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict | None) -> list[types.TextContent]:
    global active_session
    active_session = server.request_context.session
    if arguments is None:
        arguments = {}
        
    for path in iter_prompt_files(PROMPTS_DIR):
        try:
            content = load_yaml(path)
        except Exception as e:
            continue
            
        if get_tool_name(path, content) == name:
                
            schema = build_schema(content)
            
            # Schema validation
            try:
                jsonschema.validate(instance=arguments, schema=schema)
            except jsonschema.ValidationError as e:
                raise ValueError(f"Validation Error: {e.message}")
            
            with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=False) as f:
                json.dump(arguments, f)
                temp_file_name = f.name
                
            captured_output = io.StringIO()
            with contextlib.redirect_stdout(captured_output):
                success = simulate_prompt(str(path), temp_file_name)
            
            Path(temp_file_name).unlink()
            
            if not success:
                raise ValueError("Prompt simulation failed")
                
            return [types.TextContent(
                type="text",
                text=captured_output.getvalue()
            )]
            
    raise ValueError(f"Tool not found: {name}")

async def run():
    global main_loop
    main_loop = asyncio.get_running_loop()
    
    observer = Observer()
    handler = PromptDirHandler()
    observer.schedule(handler, path=PROMPTS_DIR, recursive=True)
    observer.start()
    logger.info(f"Started monitoring {PROMPTS_DIR} for changes.")

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
