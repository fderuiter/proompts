import json
import sys
import os

_no_color = False
_json_mode = False

def set_no_color(value: bool):
    global _no_color
    _no_color = value

def set_json_mode(value: bool):
    global _json_mode
    _json_mode = value

def _print(msg: str):
    if _json_mode:
        return
    print(msg)

def _color(msg: str, color_code: str) -> str:
    if _no_color or os.environ.get('NO_COLOR'):
        return msg
    return f"\033[{color_code}m{msg}\033[0m"

def step_header(msg: str):
    _print(f"=== {msg} ===")

def role_message(role: str, msg: str):
    # plain-text label
    _print(f"{role.capitalize()} message:\n{msg}")

def info(msg: str):
    _print(msg)

def warn(msg: str):
    _print(_color(f"Warning: {msg}", "33"))

def error(msg: str):
    _print(_color(f"Error: {msg}", "31"))

def success(msg: str):
    _print(_color(f"Success: {msg}", "32"))

def json_output(data: dict):
    if _json_mode:
        print(json.dumps(data, indent=2))

