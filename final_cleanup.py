#!/usr/bin/env python3
"""
Final EverLight OS Cleanup - Handle remaining content
"""
import os
import shutil
from pathlib import Path

def final_cleanup():
    root = Path(".")
    nested = root / "EverLight_OS"
    
    # Move Genesis_Wheel to root Interfaces
    genesis_src = nested / "Interfaces" / "Genesis_Wheel"
    genesis_dest = root / "Interfaces" / "Genesis_Wheel"
    
    if genesis_src.exists():
        if genesis_dest.exists():
            print("Genesis_Wheel already exists in root, skipping")
        else:
            shutil.move(str(genesis_src), str(genesis_dest))
            print("Moved Genesis_Wheel to root/Interfaces/")
    
    # Move Manifesto if different from root
    manifesto_src = nested / "Manifesto"
    manifesto_dest = root / "Manifesto"
    
    if manifesto_src.exists():
        if manifesto_dest.exists():
            print("Manifesto already exists in root, removing duplicate")
            shutil.rmtree(manifesto_src)
        else:
            shutil.move(str(manifesto_src), str(manifesto_dest))
            print("Moved Manifesto to root")
    
    # Remove remaining empty structure
    if nested.exists():
        remaining = list(nested.iterdir())
        if not remaining or (len(remaining) == 1 and remaining[0].name == "MemoryVault"):
            shutil.rmtree(nested)
            print("Removed empty EverLight_OS folder")
        else:
            print(f"EverLight_OS still contains: {[f.name for f in remaining]}")

if __name__ == "__main__":
    print("Final EverLight OS Cleanup")
    print("=" * 30)
    final_cleanup()
    print("Cleanup complete!")