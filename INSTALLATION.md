# MCPHelper Installation Guide

## Prerequisites

1. **Sublime Text 4** (Build 4000 or higher)
2. **Python 3.6+** (usually included with Sublime Text)
3. **A running MCP Server** with tools like `llm_generate_code_openai` configured

## Installation Methods

### Method 1: Manual Installation (Recommended)

1. **Download the plugin files:**
   - `MCPHelper.py`
   - `MCPHelper.sublime-commands`
   - `MCPHelper.sublime-settings`
   - `Main.sublime-menu`

2. **Copy to Sublime Text Packages directory:**

   **Windows:**

   ```bash
   %APPDATA%\Sublime Text\Packages\User\
   ```

   **macOS:**

   ```bash
   ~/Library/Application Support/Sublime Text/Packages/User/
   ```

   **Linux:**

   ```bash
   ~/.config/sublime-text/Packages/User/
   ```

3. **Restart Sublime Text**

### Method 2: Package Control Installation

1. Install Package Control if you haven't already
2. Open Command Palette (`Ctrl+Shift+P`)
3. Type "Package Control: Install Package"
4. Search for "MCPHelper" and install

## Configuration

### 1. MCP Server Setup

Ensure your MCP server is running and accessible at the configured URL (default: `http://localhost:8000/mcp.json/`)

### 2. Plugin Settings

Open Sublime Text settings:

- Go to `Preferences > Package Settings > MCPHelper > Settings`
- Or edit the settings file directly

**Default settings:**

```json
{
  "mcp_server_url": "http://localhost:8000/mcp.json/",
  "timeout_seconds": 120,
  "show_debug_output": false,
  "default_model": "gpt-4o",
  "default_temperature": 0.2,
  "default_max_tokens": 512
}
```

### 3. MCP Server Tools

Your MCP server should have tools configured like:

```python
@mcp.tool(name="llm_generate_code_openai", description="Generate code using OpenAI")
async def generate_code_openai(params: dict) -> dict:
    # Your OpenAI integration here
    return {"results": [{"data": "generated_code"}]}
```

## Usage

### Command Palette

1. Select code in any file
2. Press `Ctrl+Shift+P`
3. Choose one of:

   - `MCP: Generate Code`
   - `MCP: Review Code`
   - `MCP: Refactor Code`
   - `MCP: Translate Code`

### Menu

1. Select code in any file
2. Go to `MCP Helper` menu
3. Choose your desired action

### Keyboard Shortcuts (Optional)

Add to your keybindings file (`Preferences > Key Bindings`):

```json
[
  {
    "keys": ["ctrl+shift+g"],
    "command": "mcp_generate_code"
  },
  {
    "keys": ["ctrl+shift+r"],
    "command": "mcp_review_code"
  },
  {
    "keys": ["ctrl+shift+f"],
    "command": "mcp_refactor_code"
  },
  {
    "keys": ["ctrl+shift+t"],
    "command": "mcp_translate_code"
  }
]
```

## Troubleshooting

### Common Issues

1. **"Cannot connect to MCP server"**

   - Ensure your MCP server is running
   - Check the URL in settings
   - Verify the server is accessible at the configured endpoint

2. **"MCP Tool Error"**

   - Check your MCP server logs
   - Verify the tool names match your server configuration
   - Ensure API keys are properly configured in your MCP server

3. **"No text selected"**

   - Select some code before running commands
   - Commands require text selection to work

### Debug Mode

Enable debug output in settings:

```json
{
  "show_debug_output": true
}
```

This will show detailed request/response information in the Sublime Text console.

### Console Access

View debug output:

1. Go to `View > Show Console`
2. Look for messages starting with "MCP"

## Support

- Check the [README.md](README.md) for more information
- Ensure your MCP server is properly configured
- Verify all prerequisites are met
