#!/usr/bin/env python3
"""
EverLight OS Cleanup Script
Safely merges nested EverLight_OS/ content into root structure
"""
import os
import shutil
from pathlib import Path

def safe_merge():
    root = Path(".")
    nested = root / "EverLight_OS"
    
    if not nested.exists():
        print("❌ EverLight_OS folder not found")
        return
    
    print("Analyzing structure...")
    
    # 1. Merge MemoryVault content
    nested_mv = nested / "MemoryVault"
    root_mv = root / "MemoryVault"
    
    if nested_mv.exists():
        print("Merging MemoryVault content...")
        
        # Create root MemoryVault if it doesn't exist
        root_mv.mkdir(exist_ok=True)
        
        # Move valuable content
        for item in nested_mv.iterdir():
            if item.name not in ["README.md"]:  # Skip duplicate README
                dest = root_mv / item.name
                if dest.exists():
                    print(f"Skipping {item.name} (already exists)")
                else:
                    shutil.move(str(item), str(dest))
                    print(f"Moved {item.name}")
    
    # 2. Move unique files
    arch_sketch = nested / "EverLight_OS_Architecture_Sketch.md"
    if arch_sketch.exists():
        shutil.move(str(arch_sketch), str(root / "EverLight_OS_Architecture_Sketch.md"))
        print("Moved Architecture Sketch to root")
    
    # 3. Remove empty/duplicate folders
    empty_folders = ["Core_Modules", "DNA_Access_Codes", "Protocols", "Races_&_Realms", "Sigils"]
    
    for folder in empty_folders:
        folder_path = nested / folder
        if folder_path.exists():
            if not any(folder_path.iterdir()):  # Only remove if empty
                shutil.rmtree(folder_path)
                print(f"Removed empty {folder}")
            else:
                print(f"Keeping non-empty {folder}")
    
    # 4. Final cleanup - remove nested folder if mostly empty
    remaining = list(nested.iterdir())
    if len(remaining) <= 1:  # Only Interfaces or similar left
        print("Removing mostly empty EverLight_OS folder...")
        shutil.rmtree(nested)
        print("Cleanup complete!")
    else:
        print(f"EverLight_OS still contains: {[f.name for f in remaining]}")

if __name__ == "__main__":
    print("EverLight OS Cleanup Script")
    print("=" * 40)
    safe_merge()