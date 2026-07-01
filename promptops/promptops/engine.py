from typing import Dict, Any, Optional
import json
import logging
import os
import re
import sys
import yaml
import time
import random
import hashlib
import shutil
from pathlib import Path

from jinja2 import Undefined, StrictUndefined, FileSystemLoader
from jinja2.nativetypes import NativeEnvironment
from jinja2.sandbox import SandboxedEnvironment

from promptops import console
from promptops.utils import load_yaml, PROMPTS_DIR

logger = logging.getLogger(__name__)

class KeepUndefined(Undefined):
    def __getattr__(self, name):
        return KeepUndefined(name=f"{self._undefined_name}.{name}")
        
    def __getitem__(self, key):
        return KeepUndefined(name=f"{self._undefined_name}['{key}']")
        
    def __str__(self):
        return f"{{{{ {self._undefined_name} }}}}"

class NativeSandboxedEnvironment(NativeEnvironment, SandboxedEnvironment):
    pass

def get_jinja_env(strict: bool = False, base_dir: Optional[str] = None) -> NativeSandboxedEnvironment:
    if base_dir is None:
        base_dir = str(PROMPTS_DIR)
    undef = StrictUndefined if strict else KeepUndefined
    return NativeSandboxedEnvironment(
        loader=FileSystemLoader(base_dir),
        undefined=undef
    )

def safe_render(template: str, context: Dict[str, Any], strict_mode: bool = False) -> Any:
    if not isinstance(template, str) or ("{{" not in template and "{%" not in template):
        return template

    env = get_jinja_env(strict=strict_mode)

    try:
        jinja_template = env.from_string(template)
        return jinja_template.render(**context)
    except Exception as e:
        if hasattr(e, 'lineno') and hasattr(e, 'message'):
            msg = f"Line {e.lineno}: {e.message}"
        else:
            msg = str(e)
            
        if strict_mode:
            logger.error(f"Template Resolution Failed: {msg} in template '{template}'")
            raise ValueError(f"Strict Template Resolution Failed: {msg}")
        logger.debug(f"Could not fully render template (vars might be missing): {msg}")
        return template

def resolve_value(template_string: str, workflow_state: Dict[str, Any], strict_mode: bool = False) -> Any:
    try:
        return safe_render(template_string, workflow_state, strict_mode)
    except Exception as e:
        if strict_mode:
            raise
        logger.warning(f"Warning: Could not resolve value for template '{template_string}': {e}")
        return template_string

def run_evaluators(output_text: str, prompt_evaluators: list) -> str:
    import re
    # Define mandatory global evaluators
    mandatory_evaluators = [
        {
            "name": "Global PII Scanner",
            "python": "return not bool(re.search(r'\\b\\d{3}-\\d{2}-\\d{4}\\b', output))", # e.g. SSN
            "action": "redact",
            "redact_pattern": r'\b\d{3}-\d{2}-\d{4}\b'
        }
    ]
    
    all_evaluators = mandatory_evaluators + (prompt_evaluators or [])
    
    for evaluator in all_evaluators:
        action = evaluator.get("action", "terminate").lower()
        passed = True
        
        if "regex" in evaluator:
            pattern = evaluator["regex"].get("pattern")
            if pattern:
                flags = re.IGNORECASE if evaluator["regex"].get("flags", "").lower() == "i" else 0
                if not re.search(pattern, output_text, flags):
                    passed = False
                    
        elif "python" in evaluator or "rule" in evaluator:
            rule = evaluator.get("python") or evaluator.get("rule")
            if rule:
                if isinstance(rule, dict):
                    rule = rule.get("code", "")
                
                local_vars = {"output": output_text, "re": re}
                try:
                    if rule.strip().startswith("return "):
                        func_code = f"def __eval(output):\n    {rule}"
                        exec(func_code, local_vars, local_vars)
                        passed = local_vars["__eval"](output_text)  # type: ignore
                    else:
                        exec(rule, local_vars, local_vars)
                        passed = bool(local_vars.get("passed", True))
                except Exception as e:
                    logger.error(f"Evaluator '{evaluator.get('name')}' raised exception: {e}")
                    passed = False
                    
        elif "model" in evaluator:
            pass

        if not passed:
            if action == "terminate":
                logger.error(f"Terminating workflow due to failed evaluator: {evaluator.get('name')}")
                raise Exception(f"Evaluator failed: {evaluator.get('name')}")
            elif action == "redact":
                logger.info(f"Redacting output due to failed evaluator: {evaluator.get('name')}")
                pattern = evaluator.get("redact_pattern", r'\b\d{3}-\d{2}-\d{4}\b')
                output_text = re.sub(pattern, "[REDACTED]", output_text)
            elif action == "flag":
                logger.warning(f"FLAGGED: Output violated evaluator {evaluator.get('name')}")
    
    return output_text

_chaos_call_counter = 0
_chaos_last_call_time = 0.0

def simulate_prompt_execution(prompt_data: Dict[str, Any], inputs: Dict[str, Any], prompt_file: Optional[str] = None, strict_mode: bool = False, chaos_mode: bool = False, fidelity_report: Optional[Dict[str, bool]] = None) -> str:
    console.step_header(f"Simulating prompt: {prompt_data.get('name', 'Untitled Prompt')}")

    if not prompt_data.get('safety_opt_out', False):
        aegis_block = "\n\n<Aegis>\n*   **Do NOT** expose or persist live production Personally Identifiable Information (PII) or secrets.\n*   **Refusal Instruction**: If the user requests an architecture that fundamentally compromises security, you must output strictly `{\"error\": \"unsafe\"}`.\n</Aegis>"
        
        messages = prompt_data.get('messages', [])
        if messages:
            if messages[0].get('role') == 'system':
                if aegis_block not in messages[0]['content']:
                    messages[0]['content'] += aegis_block
            else:
                messages.insert(0, {'role': 'system', 'content': aegis_block})
        else:
            prompt_data['messages'] = [{'role': 'system', 'content': aegis_block}]
        logger.info(f"Injected Aegis Safety Block for prompt '{prompt_data.get('name')}'.")
    else:
        logger.warning(f"Safety injection suppressed for prompt '{prompt_data.get('name', 'Untitled')}' via opt-out.")

    matched_test_case = None

    if prompt_data.get('testData'):
        for test_case in prompt_data['testData']:
            if 'input' in test_case and 'inputs' not in test_case and 'vars' not in test_case:
                logger.warning(f"Schema mismatch detected in {prompt_data.get('name', 'Untitled Prompt')}: 'input' key used instead of 'inputs' or 'vars'.")
                if isinstance(test_case['input'], str):
                    test_case['inputs'] = {'input': test_case.pop('input')}
                else:
                    test_case['inputs'] = test_case.pop('input')

            expected_inputs = test_case.get('vars', test_case.get('inputs', {}))
            if isinstance(expected_inputs, str):
                expected_inputs = {"input": expected_inputs}
            
            match = True
            for k, v in expected_inputs.items():
                if k not in inputs or str(inputs[k]) != str(v):
                    match = False
                    break

            if match:
                logger.info("Found matching test case.")
                matched_test_case = test_case
                break

        if not matched_test_case:
            logger.info("No matching test case found. Using the first available test case.")
            matched_test_case = prompt_data['testData'][0]

    if matched_test_case:
        if 'mock_evaluator_results' in matched_test_case:
            inputs['mock_evaluator_results'] = matched_test_case['mock_evaluator_results']
            if fidelity_report is not None:
                fidelity_report['evaluators_mocked'] = True
                
        if chaos_mode:
            global _chaos_call_counter
            global _chaos_last_call_time
            current_time = time.time()
            if current_time - _chaos_last_call_time < 1.0:
                _chaos_call_counter += 1
            else:
                _chaos_call_counter = 1
            _chaos_last_call_time = current_time

            if 'simulated_latency' in matched_test_case:
                latency = float(matched_test_case['simulated_latency'])
                logger.info(f"[Chaos Mode] Simulating latency of {latency} seconds...")
                time.sleep(latency)
                if fidelity_report is not None:
                    fidelity_report['latency_simulated'] = True
            
            if 'forced_error_code' in matched_test_case:
                code = str(matched_test_case['forced_error_code'])
                logger.error(f"[Chaos Mode] Forced error code triggered: {code}")
                if fidelity_report is not None:
                    fidelity_report['rate_limits_simulated'] = True
                if code == '429':
                    raise Exception("RateLimitError: 429 Too Many Requests")
                else:
                    raise Exception(f"APIError: {code}")
            else:
                if _chaos_call_counter > 3 or random.random() < 0.05:
                    logger.error("[Chaos Mode] Stochastic 429 RateLimitError triggered due to high-frequency pattern!")
                    if fidelity_report is not None:
                        fidelity_report['rate_limits_simulated'] = True
                    raise Exception("RateLimitError: 429 Too Many Requests")

    for message in prompt_data.get('messages', []):
        role = message.get('role', 'user')
        content = message.get('content', '')

        try:
            content = safe_render(content, inputs, strict_mode)
        except Exception as e:
            if strict_mode:
                raise ValueError(f"Strict Template Resolution Failed in {prompt_data.get('name')}: {e}")
            logger.warning(f"Failed to render message content: {e}")

        console.role_message(role, "(Content hidden for security)")
        
        tool_calls = message.get('tool_calls')
        if tool_calls:
            def render_structure(obj, env, data):
                if isinstance(obj, str):
                    template = env.from_string(obj)
                    return template.render(**data)
                elif isinstance(obj, dict):
                    return {k: render_structure(v, env, data) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [render_structure(item, env, data) for item in obj]
                else:
                    return obj
            
            env = get_jinja_env(strict=strict_mode)
            rendered_tool_calls = render_structure(tool_calls, env, inputs)
            tc_yaml = yaml.dump(rendered_tool_calls, sort_keys=False, default_flow_style=False).strip()
            console.role_message("tool_call", tc_yaml)

    if matched_test_case:
        output = matched_test_case.get('expected', 'No expected output in test case.')
        output_text = output[0] if isinstance(output, list) else output
    else:
        output_text = f"[Simulated output for prompt: {prompt_data.get('name', 'Untitled Prompt')}]"

    output_text = run_evaluators(output_text, prompt_data.get('evaluators', []))

    return output_text

def run_workflow(workflow_file: str, initial_inputs: Dict[str, Any], verbose: bool = True, strict_mode: bool = False, chaos_mode: bool = False, fidelity_report: Optional[Dict[str, bool]] = None) -> Optional[Dict[str, Any]]:
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    if not logger.handlers and not logging.getLogger().handlers:
         logging.basicConfig(level=logger.level, format='%(levelname)s: %(message)s')

    workflow_data = load_yaml(workflow_file)
    if not workflow_data:
        return None

    defined_steps = set()
    if strict_mode and 'testData' not in workflow_data:
        logger.warning(f"Strict Mode: Workflow '{workflow_data.get('name', 'Untitled')}' is missing 'testData' field.")
        
    for step in workflow_data.get('steps', []):
        step_id = step.get('step_id')
        for var_name, template in step.get('map_inputs', {}).items():
            if isinstance(template, str):
                matches = re.findall(r'\{\{\s*steps\.([\w\-]+)\.', template)
                for match in matches:
                    if match not in defined_steps:
                        msg = f"Step ID Mismatch: Step '{step_id}' references undefined step '{match}' in mapping '{var_name}'."
                        if strict_mode:
                            logger.error(msg)
                            raise ValueError(msg)
                        else:
                            logger.warning(msg)
        if step_id:
            defined_steps.add(step_id)

    logger.info(f"Starting workflow simulation: {workflow_data.get('name', 'Untitled Workflow')}")
    logger.info("ℹ️  NOTE: Running in SIMULATION MODE. No API calls will be made.")

    workflow_state = {
        "inputs": initial_inputs,
        "steps": {}
    }

    steps_dict = {step['step_id']: step for step in workflow_data.get('steps', [])}
    if not steps_dict:
        return workflow_state

    identifier_string = f"{os.path.abspath(workflow_file)}::{json.dumps(initial_inputs, sort_keys=True)}"
    run_id = hashlib.md5(identifier_string.encode('utf-8')).hexdigest()
    checkpoint_dir = os.path.join(os.getcwd(), ".checkpoints", run_id)
    checkpoint_file = os.path.join(checkpoint_dir, "state.json")
    os.makedirs(checkpoint_dir, exist_ok=True)

    current_step_id = workflow_data['steps'][0]['step_id']
    execution_counts = {step_id: 0 for step_id in steps_dict}
    max_iterations = workflow_data.get('max_iterations', 10)

    if os.path.exists(checkpoint_file):
        try:
            with open(checkpoint_file, 'r') as f:
                checkpoint_data = json.load(f)
            resume_step_id = checkpoint_data.get('next_step_id')
            if resume_step_id and resume_step_id in steps_dict:
                console.info(f"Resuming from step {resume_step_id}...")
                logger.info(f"Resuming from step {resume_step_id}...")
                workflow_state = checkpoint_data.get('workflow_state', workflow_state)
                execution_counts = checkpoint_data.get('execution_counts', execution_counts)
                current_step_id = resume_step_id
        except Exception as e:
            logger.warning(f"Failed to load checkpoint: {e}")

    while current_step_id:
        step = steps_dict[current_step_id]
        step_id = step['step_id']
        
        if execution_counts[step_id] >= max_iterations:
            logger.error(f"Loop Limit Exceeded: Step '{step_id}' has been executed {execution_counts[step_id]} times. Terminating workflow.")
            raise Exception("Loop Limit Exceeded")
            
        prompt_file = step['prompt_file']

        if not os.path.exists(prompt_file):
             workflow_dir = os.path.dirname(workflow_file)
             alt_prompt_file = os.path.join(workflow_dir, prompt_file)
             if os.path.exists(alt_prompt_file):
                 prompt_file = alt_prompt_file

        prompt_data = load_yaml(prompt_file)
        if not prompt_data:
            path_obj = Path(prompt_file)
            skills_md = path_obj.parent / "skills.md"
            if skills_md.exists():
                from promptops.utils import parse_skill_manifest
                manifest = parse_skill_manifest(skills_md)
                
                stem = path_obj.name.replace('.prompt.md', '').replace('.prompt.yml', '')
                stem_clean = re.sub(r'^\d+_', '', stem).replace('_', ' ').lower()
                
                for skill in manifest.get("skills", []):
                    skill_name_clean = skill["name"].lower().replace('_', ' ')
                    if stem_clean in skill_name_clean or skill_name_clean in stem_clean or skill["name"].replace(' ', '_').lower() in stem:
                        prompt_data = {
                            "name": skill["name"],
                            "description": skill.get("description", ""),
                            "variables": skill.get("variables", []),
                            "messages": [{"role": "system", "content": skill.get("instructions", "")}],
                            "testData": skill.get("testData", [])
                        }
                        logger.info(f"Loaded skill '{skill['name']}' from manifest {skills_md}")
                        break

        if not prompt_data:
            logger.warning(f"Skipping step {step_id} due to missing prompt file or skill.")
            current_step_id = None
            continue

        prompt_inputs = {}
        for var_name, template in step.get('map_inputs', {}).items():
            prompt_inputs[var_name] = resolve_value(template, workflow_state, strict_mode)

        logger.debug(f"Resolved prompt inputs: {list(prompt_inputs.keys())}")
        console.step_header(f"Simulating Step: {step_id} (Iteration {execution_counts[step_id] + 1})")

        output = simulate_prompt_execution(prompt_data, prompt_inputs, prompt_file=prompt_file, strict_mode=strict_mode, chaos_mode=chaos_mode, fidelity_report=fidelity_report)

        if step_id not in workflow_state['steps']:
            workflow_state['steps'][step_id] = {'output': output, 'history': [output], 'iterations': 1}
        else:
            workflow_state['steps'][step_id]['output'] = output
            workflow_state['steps'][step_id]['history'].append(output)
            workflow_state['steps'][step_id]['iterations'] += 1
            
        execution_counts[step_id] += 1
        logger.debug(f"Step '{step_id}' produced output: (Content hidden for security)")

        next_step_id = None
        next_prop = step.get('next')
        
        if next_prop is not None:
            if isinstance(next_prop, str):
                next_step_id = next_prop
            elif isinstance(next_prop, list):
                for edge in next_prop:
                    if isinstance(edge, str):
                        next_step_id = edge
                        break
                    elif isinstance(edge, dict):
                        condition = edge.get('condition')
                        target = edge.get('target')
                        if condition:
                            try:
                                rendered_cond = resolve_value(condition, workflow_state, strict_mode)
                                if rendered_cond is True or str(rendered_cond).lower() == 'true':
                                    next_step_id = target
                                    break
                            except Exception as e:
                                logger.warning(f"Failed to evaluate condition '{condition}': {e}")
                        else:
                            next_step_id = target
                            break
        else:
            idx = next((i for i, s in enumerate(workflow_data['steps']) if s['step_id'] == step_id), -1)
            if idx != -1 and idx + 1 < len(workflow_data['steps']):
                next_step_id = workflow_data['steps'][idx + 1]['step_id']
                
        if next_step_id and next_step_id not in steps_dict:
            logger.error(f"Next step '{next_step_id}' not found in workflow steps.")
            raise ValueError(f"Undefined next step: {next_step_id}")
            
        current_step_id = next_step_id
        
        try:
            os.makedirs(checkpoint_dir, exist_ok=True)
            with open(checkpoint_file, 'w') as f:
                json.dump({
                    "workflow_state": workflow_state,
                    "execution_counts": execution_counts,
                    "next_step_id": current_step_id
                }, f)
        except Exception as e:
            logger.warning(f"Failed to save checkpoint: {e}")

    if os.path.exists(checkpoint_dir):
        try:
            shutil.rmtree(checkpoint_dir)
        except Exception as e:
            logger.warning(f"Failed to clean up checkpoint directory: {e}")

    return workflow_state
