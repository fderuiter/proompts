# Agent Integration via Model Context Protocol (MCP)

This guide explains how to connect the Proompts repository to your local AI agents (such as Claude Desktop) using the Model Context Protocol (MCP). By configuring the internal MCP server, you can dynamically expose the prompt library as actionable tools for your agent.

## Prerequisites

Before configuring the MCP server, ensure your local environment meets the following technical requirements:

- **Python Version:** Python 3.10 or higher
- **Required Libraries:**
  - `mcp` (>= 1.27.2)
  - `watchdog` (>= 6.0.0)
  - `promptops` (internal toolkit)

*Note: All dependencies are installed automatically when you run `pip install -r requirements.txt` in an active virtual environment.*

## Configuring Claude Desktop

The repository includes a dedicated CLI utility to generate the necessary configuration for Claude Desktop. This utility handles platform-specific pathing and sets up the server command automatically.

### Step-by-Step Walkthrough

1. **Initialize Your Environment:**
   Ensure your virtual environment is active and dependencies are installed.
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Generate the Configuration JSON:**
   Run the `promptops` agent config command to generate the required JSON structure for Claude Desktop. 
   ```bash
   promptops agent config --dir prompts
   ```

3. **Update Claude Desktop Config:**
   Copy the output JSON and paste it into your Claude Desktop configuration file.
   - **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

4. **Restart Claude Desktop:**
   Restart the Claude Desktop application to establish the connection with the newly configured MCP server.

## Auditing Tools with Discovery CLI

The prompt library uses naming conventions and `skills.md` manifests to dynamically map prompt files to tool names. Because these mappings can truncate long names or override them via manifests, you can audit the current state of your tools using the discovery command.

### Running the Discovery Report

To see exactly which prompts are exposed and how their tool names are generated, run:

```bash
promptops agent discovery --dir prompts
```

This will output a comprehensive report showing:
- **Tool Name Transformations:** Details on how original prompt names were reformatted or truncated to comply with tool naming rules.
- **Overridden Tools:** Identifies which prompts are being overridden by custom instructions defined in `skills.md` files.

## Server Implementation Details

For developers looking to understand or modify the underlying server, the MCP server is implemented in [`mcp_server.py`](https://github.com/fderuiter/proompts/blob/main/mcp_server.py) at the root of the repository. It uses `watchdog` to monitor the `prompts/` directory for live changes and automatically notifies the client when tools are updated.


<!-- TOOL_REGISTRY_START -->
<div id="tool-explorer"></div>
<script src="../js/explorer.js"></script>
<!-- TOOL_REGISTRY_END -->