# MCPHelper v1.0.1 - Second Release

## 🎉 Second Release of MCPHelper

A Sublime Text plugin that connects your editor to a local **Model Context Protocol (MCP) server**, letting you use OpenAI or Gemini-powered tools directly on selected code.

## ✨ Features

- **Generate code** from plain-text prompts
- **Review code** for bugs, security flaws, or improvements
- **Refactor code** to enhance readability, maintainability, and performance
- **Translate code** between languages like Python, JavaScript, Bash, etc.
- **Configurable settings** for MCP server URL, timeouts, and model parameters
- **Menu integration** for easy access to all commands
- **Robust error handling** with user-friendly error messages
- **Debug mode** for troubleshooting

## 🚀 Installation

### Quick Start

1. Download the `MCPHelper-v1.0.1.zip` file
2. Extract to your Sublime Text User packages folder:
   - **Windows**: `%APPDATA%\Sublime Text\Packages\User\`
   - **macOS**: `~/Library/Application Support/Sublime Text/Packages/User/`
   - **Linux**: `~/.config/sublime-text/Packages/User/`
3. Restart Sublime Text
4. Configure your MCP server (see documentation)

### Alternative: Direct GitHub Installation

1. Open Sublime Text
2. Press `Ctrl+Shift+P`
3. Type "Package Control: Add Repository"
4. Enter: `https://github.com/your-username/MCPHelperSublimePlugin`
5. Then install via "Package Control: Install Package"

## 📋 Requirements

- **Sublime Text 4** (Build 4000 or higher)
- **Python 3.6+** (usually included with Sublime Text)
- **A running MCP Server** with tools like `llm_generate_code_openai` configured

## 📖 Usage

1. Select code in any file
2. Press `Ctrl+Shift+P` and choose:

   - `MCP: Generate Code`
   - `MCP: Review Code`
   - `MCP: Refactor Code`
   - `MCP: Translate Code`

Or use the **MCP Helper** menu for easy access.

## ⚙️ Configuration

Open Sublime Text settings:

- Go to `Preferences > Package Settings > MCPHelper > Settings`
- Configure your MCP server URL and model parameters

## 🔧 Troubleshooting

- Ensure your MCP server is running at the configured URL
- Check the console for debug output
- Use the included `test_mcp_connection.py` script to verify connectivity

## 📄 Documentation

- [README.md](README.md) - Main documentation
- [INSTALLATION.md](INSTALLATION.md) - Detailed installation guide
- [PACKAGE_CONTROL.md](PACKAGE_CONTROL.md) - Distribution guide

## 🎯 What's New

- Enhanced error handling and user feedback
- Improved settings integration and menu system
- Better documentation and troubleshooting guides
- Fixed markdown linting issues across all files
- Updated version management and distribution tools

---

**Note**: This plugin requires a running [MCP Server](https://modelcontextprotocol.io) on your local machine. You must configure your own OpenAI or Gemini API keys in the MCP server.
