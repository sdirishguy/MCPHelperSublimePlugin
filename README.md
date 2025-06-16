README.md

# MCPHelper – Sublime Text Plugin

This is a Sublime Text plugin that connects your editor to a local **Model Context Protocol (MCP) server**, letting you use OpenAI or Gemini-powered tools directly on selected code.

🔗 [Model Context Protocol Introduction](https://modelcontextprotocol.io/introduction)

---

## ✨ Features

- **Generate code** from plain-text prompts
- **Review code** for bugs, security flaws, or improvements
- **Refactor code** to enhance readability, maintainability, and performance
- **Translate code** between languages like Python, JavaScript, Bash, etc.

## 🖼️ Demo

Here's what the plugin looks like in Sublime Text:

![MCP Helper Sublime Demo](./screenshot.png)

---

## 🚀 Installation

1. Clone this repo or copy `MCPHelper.py` into your Sublime Text user packages folder:
   - Mac: `~/Library/Application Support/Sublime Text/Packages/User/`
   - Windows: `%APPDATA%\Sublime Text\Packages\User\`
   - Linux: `~/.config/sublime-text/Packages/User/`

2. (Optional but recommended) Copy `MCPHelper.sublime-commands` into the same folder for Command Palette access.

3. Make sure your local MCP server is running and accessible at:
http://localhost:8000/mcp.json/


4. Select some code in any file, press `Ctrl+Shift+P`, and run:

- `MCP: Generate Code`
- `MCP: Review Code`
- `MCP: Refactor Code`
- `MCP: Translate Code`

---

## ⚙️ Configuration

- All API logic is handled by your local MCP server.
- Tools like `llm_generate_code_openai` or `llm_generate_code_gemini` should be configured inside your MCP.
- Your OpenAI/Gemini API keys should **never** be stored in this plugin. They should live in the MCP server configuration only.

---

## 📂 Example MCP Tool Configuration

If you're running a local MCP server (see [`mcp_server_project`](https://github.com/your-repo)), make sure your `tools.py` has tools like:

```python
@mcp.tool(name="llm_generate_code_openai", description="LLM code gen with OpenAI.")
async def generate_code_openai(params: dict) -> dict:
 # Your OpenAI integration here
```

🧩 Extending
You can add new commands by subclassing McpBaseCommand and customizing build_params().



📄 License
This project is licensed under the MIT License. See LICENSE for details.



👤 Author
David Donohue
Built to streamline LLM-assisted development with a local-first mindset.
