#!/usr/bin/env python3
"""
Distribution script for MCPHelper Sublime Text plugin.
This script helps prepare the plugin for distribution.
"""

import os
import json
import subprocess
import sys
from pathlib import Path

def check_requirements():
    """Check if all required files exist."""
    required_files = [
        'MCPHelper.py',
        'MCPHelper.sublime-commands',
        'MCPHelper.sublime-settings',
        'Main.sublime-menu',
        'README.md',
        'INSTALLATION.md',
        'LICENSE',
        'package.json'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ All required files present")
    return True

def check_git_status():
    """Check git status and suggest actions."""
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True)
        if result.stdout.strip():
            print("⚠️  Uncommitted changes detected:")
            print(result.stdout)
            print("Consider committing changes before distribution.")
        else:
            print("✅ No uncommitted changes")
    except FileNotFoundError:
        print("⚠️  Git not found. Make sure you're in a git repository.")

def create_version_tag():
    """Create a version tag for distribution."""
    try:
        # Read current version from package.json
        with open('package.json', 'r') as f:
            package_data = json.load(f)
            version = package_data.get('version', '1.0.0')
        
        print(f"📦 Current version: {version}")
        
        # Check if tag already exists
        result = subprocess.run(['git', 'tag', '-l', f'v{version}'], 
                              capture_output=True, text=True)
        
        if result.stdout.strip():
            print(f"⚠️  Tag v{version} already exists")
            return False
        
        # Create tag
        tag_message = f"Release version {version}"
        subprocess.run(['git', 'tag', '-a', f'v{version}', '-m', tag_message])
        print(f"✅ Created tag v{version}")
        
        # Push tag
        subprocess.run(['git', 'push', 'origin', f'v{version}'])
        print(f"✅ Pushed tag v{version} to origin")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating tag: {e}")
        return False

def generate_zip():
    """Generate a distribution zip file."""
    import zipfile
    
    version = "1.0.0"
    try:
        with open('package.json', 'r') as f:
            package_data = json.load(f)
            version = package_data.get('version', '1.0.0')
    except:
        pass
    
    zip_name = f"MCPHelper-v{version}.zip"
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        files_to_include = [
            'MCPHelper.py',
            'MCPHelper.sublime-commands',
            'MCPHelper.sublime-settings',
            'Main.sublime-menu',
            'README.md',
            'INSTALLATION.md',
            'LICENSE',
            'package.json',
            'test_mcp_connection.py'
        ]
        
        for file in files_to_include:
            if os.path.exists(file):
                zipf.write(file)
                print(f"📁 Added {file} to zip")
    
    print(f"✅ Created distribution zip: {zip_name}")
    return zip_name

def main():
    """Main distribution script."""
    print("🚀 MCPHelper Distribution Script")
    print("=" * 40)
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Please fix missing files before distribution.")
        sys.exit(1)
    
    print("\n📋 Git Status:")
    check_git_status()
    
    print("\n🏷️  Version Management:")
    create_version_tag()
    
    print("\n📦 Creating Distribution Package:")
    zip_file = generate_zip()
    
    print("\n✅ Distribution preparation complete!")
    print(f"\n📁 Distribution files:")
    print(f"   - {zip_file}")
    print(f"   - GitHub repository")
    
    print("\n📖 Next steps:")
    print("   1. Upload to GitHub releases")
    print("   2. Submit to Package Control (see PACKAGE_CONTROL.md)")
    print("   3. Share the repository URL for direct installation")

if __name__ == "__main__":
    main() 