import os
import pytest
from promptops.console import (
    ConsoleInterface,
    set_console,
    set_no_color,
    set_json_mode,
    step_header,
    role_message,
    info,
    warn,
    error,
    success,
    json_output,
    ask_input
)

class MockConsole(ConsoleInterface):
    def __init__(self):
        self.prints = []
        self.inputs = []

    def print(self, msg: str):
        self.prints.append(msg)

    def ask_input(self, prompt: str) -> str:
        self.inputs.append(prompt)
        return "mock_input"

@pytest.fixture
def mock_console():
    console = MockConsole()
    set_console(console)
    # reset state
    set_no_color(False)
    set_json_mode(False)
    if "NO_COLOR" in os.environ:
        del os.environ["NO_COLOR"]
    yield console
    # restore state
    set_console(ConsoleInterface())
    set_no_color(False)
    set_json_mode(False)
    if "NO_COLOR" in os.environ:
        del os.environ["NO_COLOR"]

def test_console_interface_ask_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt: 'user_input')
    console = ConsoleInterface()
    assert console.ask_input("prompt") == 'user_input'

def test_ask_input_global(mock_console):
    assert ask_input("question:") == "mock_input"
    assert mock_console.inputs == ["question:"]

def test_set_no_color(mock_console):
    set_no_color(True)
    success("yes")
    assert mock_console.prints == ["Success: yes"]
    
    set_no_color(False)
    mock_console.prints.clear()
    success("yes")
    assert mock_console.prints == ["\033[32mSuccess: yes\033[0m"]

def test_no_color_env_var(mock_console, monkeypatch):
    monkeypatch.setenv("NO_COLOR", "1")
    error("bad")
    assert mock_console.prints == ["Error: bad"]

def test_set_json_mode(mock_console):
    set_json_mode(True)
    info("some info")
    warn("some warning")
    error("some error")
    success("some success")
    step_header("header")
    role_message("user", "hello")
    # In json_mode, standard prints are suppressed
    assert mock_console.prints == []

    json_output({"key": "value"})
    assert "{" in mock_console.prints[0]
    assert '"key": "value"' in mock_console.prints[0]

def test_json_output_disabled(mock_console):
    set_json_mode(False)
    json_output({"key": "value"})
    assert mock_console.prints == []

def test_printing_functions(mock_console):
    info("information")
    assert mock_console.prints[-1] == "information"
    
    warn("warning")
    assert mock_console.prints[-1] == "\033[33mWarning: warning\033[0m"
    
    error("err")
    assert mock_console.prints[-1] == "\033[31mError: err\033[0m"
    
    success("ok")
    assert mock_console.prints[-1] == "\033[32mSuccess: ok\033[0m"
    
    step_header("Step 1")
    assert mock_console.prints[-1] == "=== Step 1 ==="
    
    role_message("assistant", "How can I help?")
    assert mock_console.prints[-1] == "Assistant message:\nHow can I help?"
