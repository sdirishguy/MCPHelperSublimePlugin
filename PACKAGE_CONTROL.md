# Package Control Distribution Guide

## Prerequisites

1. **GitHub Repository**: Your plugin must be in a public GitHub repository
2. **Proper Structure**: Ensure your plugin follows Package Control conventions
3. **Version Tagging**: Use semantic versioning for releases

## Steps to Submit to Package Control

### 1. Prepare Your Repository

Ensure your repository has:
- `README.md` with clear installation and usage instructions
- `LICENSE` file
- Proper file structure
- Semantic version tags

### 2. Create a Release

```bash
# Tag your current version
git tag -a v1.0.0 -m "Initial release"
git push origin v1.0.0
```

### 3. Submit to Package Control

1. Fork the [Package Control Channel](https://github.com/wbond/package_control_channel)
2. Add your plugin to `repository/repositories.json`:

```json
{
    "name": "MCPHelper",
    "description": "Sublime Text plugin for Model Context Protocol (MCP) integration",
    "author": "David Donohue",
    "homepage": "https://github.com/your-username/MCPHelperSublimePlugin",
    "repository": {
        "type": "git",
        "url": "https://github.com/your-username/MCPHelperSublimePlugin.git"
    },
    "labels": ["mcp", "ai", "code-generation"],
    "releases": [
        {
            "version": "1.0.0",
            "url": "https://github.com/your-username/MCPHelperSublimePlugin/archive/v1.0.0.zip",
            "sublime_text": ">=4000",
            "platforms": ["*"]
        }
    ]
}
```

3. Submit a pull request to the Package Control Channel

### 4. Alternative: Direct GitHub Installation

Users can install directly from GitHub:

1. Open Sublime Text
2. Press `Ctrl+Shift+P`
3. Type "Package Control: Add Repository"
4. Enter: `https://github.com/your-username/MCPHelperSublimePlugin`
5. Then install via "Package Control: Install Package"

## Repository Requirements

### File Structure
```
MCPHelperSublimePlugin/
├── MCPHelper.py
├── MCPHelper.sublime-commands
├── MCPHelper.sublime-settings
├── Main.sublime-menu
├── package.json
├── README.md
├── INSTALLATION.md
├── LICENSE
└── test_mcp_connection.py
```

### Required Files
- **MCPHelper.py**: Main plugin file
- **README.md**: Documentation and usage instructions
- **LICENSE**: License information
- **package.json**: Plugin metadata (optional but recommended)

## Version Management

Use semantic versioning:
- **MAJOR.MINOR.PATCH** (e.g., 1.0.0)
- Create tags for each release
- Update version in package.json and plugin files

## Testing Before Distribution

1. **Test Installation**: Install from your repository
2. **Test Functionality**: Ensure all commands work
3. **Test Documentation**: Verify installation instructions
4. **Test Dependencies**: Ensure MCP server requirements are clear

## Distribution Checklist

- [ ] Repository is public on GitHub
- [ ] All files are properly structured
- [ ] README.md is comprehensive
- [ ] LICENSE file is included
- [ ] Version is tagged and released
- [ ] Installation instructions are clear
- [ ] Dependencies are documented
- [ ] Plugin has been tested thoroughly 