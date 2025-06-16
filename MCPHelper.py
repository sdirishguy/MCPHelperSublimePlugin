import sublime
import sublime_plugin
import threading
import json
import urllib.request
import urllib.error
import uuid

# MCP server endpoint for JSON-RPC communication
MCP_JSON_RPC_URL = "http://localhost:8000/mcp.json/"


# --- Core JSON-RPC Request Handler ---
def mcp_tool_call(tool, params):
    """
    Sends a JSON-RPC request to the local MCP server,
    invoking a registered tool with the given parameters.
    """
    # Construct the JSON-RPC payload
    payload = {
        "jsonrpc": "2.0",
        "id": str(uuid.uuid4()),  # Unique request ID
        "method": "tools/call",   # MCP standard method to invoke a tool
        "params": {
            "tool": tool,
            "arguments": {"params": params}
        }
    }
    data = json.dumps(payload).encode('utf-8')

    # Prepare the HTTP request
    req = urllib.request.Request(
        MCP_JSON_RPC_URL,
        data=data,
        headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    )

    # Debugging output (printed in Sublime's console)
    print("--- MCP Request ---")
    print("ENDPOINT:", MCP_JSON_RPC_URL)
    print("PAYLOAD:", json.dumps(payload, indent=2))

    try:
        # Make the HTTP request and read the response
        with urllib.request.urlopen(req, timeout=120) as resp:
            resp_data = resp.read().decode()
            print("--- MCP Raw Response ---")
            print(resp_data)
            result_json = json.loads(resp_data)

            # Handle error responses from the server
            if "error" in result_json and result_json["error"]:
                error_info = result_json["error"]
                return f"MCP Error: {error_info.get('message', 'Unknown error')} (Code: {error_info.get('code')})"

            # Handle successful responses
            if "result" in result_json:
                tool_call_result = result_json["result"]

                # If results are nested, try to extract the first item
                if "results" in tool_call_result and isinstance(tool_call_result["results"], list):
                    if tool_call_result["results"]:
                        first_content = tool_call_result["results"][0]
                        if isinstance(first_content, dict) and "data" in first_content:
                            return str(first_content["data"])
                    return json.dumps(tool_call_result["results"])  # If no 'data', dump the list

                return json.dumps(tool_call_result)  # Fallback for other result formats

            return "MCP call successful, but no 'result' field in response."

    except urllib.error.HTTPError as e:
        # Handle HTTP-specific errors
        error_content = e.read().decode() if e.fp else str(e)
        print(f"MCP CALL HTTP ERROR: {e.code} {e.reason}. Response: {error_content}")
        return f"MCP call failed: HTTP {e.code} {e.reason}"

    except Exception as e:
        # Catch-all for other exceptions (e.g. timeout, bad JSON)
        print(f"MCP CALL GENERAL ERROR: {e}")
        return f"MCP call failed: {e}"


# --- Threaded Helper to Keep UI Responsive ---
def run_tool_in_thread(tool, params, callback):
    """
    Runs the MCP call in a separate thread so the Sublime UI doesn't freeze.
    Once finished, calls the callback on the main thread.
    """
    def _worker():
        result = mcp_tool_call(tool, params)
        sublime.set_timeout(lambda: callback(result), 0)  # Back to main thread
    threading.Thread(target=_worker).start()


# --- Base Class for All MCP Sublime Commands ---
class McpBaseCommand(sublime_plugin.TextCommand):
    """
    Abstract base command class for invoking MCP tools.
    Subclasses must define TOOL_NAME and optionally override build_params().
    """

    TOOL_NAME = None  # Each subclass must set this

    def run(self, edit):
        sel = self.view.sel()[0]
        selected_text = self.view.substr(sel)

        if not selected_text:
            sublime.message_dialog("Select some code/text to use this MCP command.")
            return

        # If extra user input is needed (e.g., for translation), prompt the user
        if hasattr(self, "get_extra_input"):
            self.view.window().show_input_panel(
                self.extra_input_prompt, "", 
                lambda input_val: self.run_action(edit, selected_text, input_val), 
                None, None
            )
        else:
            self.run_action(edit, selected_text)

    def run_action(self, edit, selected_text, extra_input=None):
        """
        Trigger the tool call and update the status bar while it runs.
        """
        params = self.build_params(selected_text, extra_input)
        self.view.set_status("mcp_status", f"MCP: Calling {self.TOOL_NAME}...")

        def handle_response(result):
            self.view.erase_status("mcp_status")
            self.view.run_command("mcp_insert_result", {"result": result})

        run_tool_in_thread(self.TOOL_NAME, params, handle_response)

    def build_params(self, selected_text, extra_input=None):
        """
        Override this method to customize the payload sent to the tool.
        Default assumes a simple prompt.
        """
        return {"prompt": selected_text, "language": "python"}


# --- Helper Command to Insert LLM Output ---
class McpInsertResultCommand(sublime_plugin.TextCommand):
    """
    Inserts the result from an MCP tool back into the editor,
    replacing the originally selected text.
    """
    def run(self, edit, result):
        sel = self.view.sel()[0]
        self.view.replace(edit, sel, result)


# --- Concrete Tool Commands (using OpenAI LLM) ---

class McpGenerateCodeCommand(McpBaseCommand):
    """
    Generate code from a prompt using OpenAI's model.
    """
    TOOL_NAME = "llm_generate_code_openai"

    def build_params(self, selected_text, extra_input=None):
        return {
            "prompt": selected_text,
            "language": "python",
            "model": "gpt-4o",
            "temperature": 0.2,
            "max_tokens": 256
        }


class McpReviewCodeCommand(McpBaseCommand):
    """
    Review selected code for bugs, improvements, and security risks.
    """
    TOOL_NAME = "llm_generate_code_openai"

    def build_params(self, selected_text, extra_input=None):
        review_prompt = f"Review this code and suggest improvements, bugs, or security issues:\n{selected_text}"
        return {
            "prompt": review_prompt,
            "language": "python",
            "model": "gpt-4o",
            "temperature": 0.2,
            "max_tokens": 512
        }


class McpRefactorCodeCommand(McpBaseCommand):
    """
    Refactor selected code for better readability and maintainability.
    """
    TOOL_NAME = "llm_generate_code_openai"

    def build_params(self, selected_text, extra_input=None):
        refactor_prompt = f"Refactor this code to improve readability, maintainability, and performance:\n{selected_text}"
        return {
            "prompt": refactor_prompt,
            "language": "python",
            "model": "gpt-4o",
            "temperature": 0.2,
            "max_tokens": 512
        }


class McpTranslateCodeCommand(McpBaseCommand):
    """
    Translate code from one language to another (e.g., Python to JavaScript).
    """
    TOOL_NAME = "llm_generate_code_openai"
    extra_input_prompt = "Translate code to language (e.g., javascript, bash):"

    def get_extra_input(self):
        return True

    def build_params(self, selected_text, extra_input=None):
        language = extra_input or "javascript"
        translate_prompt = f"Translate this code to {language}:\n{selected_text}"
        return {
            "prompt": translate_prompt,
            "language": language,
            "model": "gpt-4o",
            "temperature": 0.2,
            "max_tokens": 512
        }


# --- Plugin Entry Hook ---
def plugin_loaded():
    """
    Called automatically by Sublime Text when the plugin is loaded.
    """
    print("MCP Helper for Sublime Text loaded!")
