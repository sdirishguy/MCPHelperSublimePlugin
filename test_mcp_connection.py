#!/usr/bin/env python3
"""
Simple test script to verify MCP server connection.
Run this to check if your MCP server is accessible.
"""

import urllib.request
import json
import sys

def test_mcp_connection(url="http://localhost:8000/mcp.json/"):
    """Test connection to MCP server."""
    print(f"Testing connection to MCP server at: {url}")
    
    try:
        # Simple GET request to check if server is accessible
        req = urllib.request.Request(url, headers={'Accept': 'application/json'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            print(f"✅ Connection successful! Status: {resp.getcode()}")
            return True
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

def test_mcp_tool_call(url="http://localhost:8000/mcp.json/"):
    """Test a simple MCP tool call."""
    print(f"\nTesting MCP tool call to: {url}")
    
    # Simple test payload
    payload = {
        "jsonrpc": "2.0",
        "id": "test-123",
        "method": "tools/call",
        "params": {
            "tool": "llm_generate_code_openai",
            "arguments": {
                "params": {
                    "prompt": "print hello world",
                    "language": "python"
                }
            }
        }
    }
    
    try:
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(
            url,
            data=data,
            headers={
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        )
        
        with urllib.request.urlopen(req, timeout=10) as resp:
            resp_data = resp.read().decode()
            result = json.loads(resp_data)
            
            if "error" in result:
                print(f"❌ Tool call failed: {result['error']}")
                return False
            else:
                print("✅ Tool call successful!")
                return True
                
    except Exception as e:
        print(f"❌ Tool call failed: {e}")
        return False

if __name__ == "__main__":
    print("MCP Server Connection Test")
    print("=" * 40)
    
    # Test basic connection
    if test_mcp_connection():
        # Test tool call
        test_mcp_tool_call()
    else:
        print("\n💡 Troubleshooting tips:")
        print("1. Make sure your MCP server is running")
        print("2. Check if the server URL is correct")
        print("3. Verify the server is accessible from this machine")
        print("4. Check server logs for any errors")
        sys.exit(1)
    
    print("\n🎉 All tests completed!") 