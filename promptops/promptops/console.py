"""Module docstring."""
import json
import os

_no_color = False
_json_mode = False

class ConsoleInterface:
    """Missing docstring."""
    def print(self, msg: str):
        """Missing docstring."""
        print(msg)
    def ask_input(self, prompt: str) -> str:
        """Missing docstring."""
        return input(prompt)

_current_console = ConsoleInterface()

def set_console(console: ConsoleInterface):
    """Missing docstring."""
    global _current_console
    _current_console = console

def set_no_color(value: bool):
    """Missing docstring."""
    global _no_color
    _no_color = value

def set_json_mode(value: bool):
    """Missing docstring."""
    global _json_mode
    _json_mode = value

def _print(msg: str):
    """Missing docstring."""
    if _json_mode:
        return
    _current_console.print(msg)

def ask_input(prompt: str) -> str:
    """Missing docstring."""
    return _current_console.ask_input(prompt)

def _color(msg: str, color_code: str) -> str:
    """Missing docstring."""
    if _no_color or os.environ.get('NO_COLOR'):
        return msg
    return f"\033[{color_code}m{msg}\033[0m"

def step_header(msg: str):
    """Missing docstring."""
    _print(f"=== {msg} ===")

def role_message(role: str, msg: str):
    """Missing docstring."""
    # plain-text label
    _print(f"{role.capitalize()} message:\n{msg}")

def info(msg: str):
    """Missing docstring."""
    _print(msg)

def warn(msg: str):
    """Missing docstring."""
    _print(_color(f"Warning: {msg}", "33"))

def error(msg: str):
    """Missing docstring."""
    _print(_color(f"Error: {msg}", "31"))

def success(msg: str):
    """Missing docstring."""
    _print(_color(f"Success: {msg}", "32"))

def json_output(data: dict):
    """Missing docstring."""
    if _json_mode:
        _current_console.print(json.dumps(data, indent=2))


