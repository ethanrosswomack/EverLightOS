# EverLight OS Cleanup Plan

## Issue
- Root repo: `EverLightOS/` (active)
- Nested folder: `EverLight_OS/` (mostly empty duplicates)

## Analysis Results
- `EverLight_OS/Core_Modules/` = EMPTY
- `EverLight_OS/MemoryVault/` = Contains valuable gists & web files
- Root `Core_Modules/` = ACTIVE (Council_Manifest.yml, etc.)
- Root `MemoryVault/` = Minimal (just Robin-Transcript-Keys.txt)

## Cleanup Actions

### 1. Merge MemoryVault Content
```bash
# Move valuable content from nested to root
mv EverLight_OS/MemoryVault/gists/ MemoryVault/
mv EverLight_OS/MemoryVault/*.html MemoryVault/
mv EverLight_OS/MemoryVault/*.json MemoryVault/
mv EverLight_OS/MemoryVault/*.md MemoryVault/
```

### 2. Remove Empty Duplicates
```bash
# Remove empty nested folders
rm -rf EverLight_OS/Core_Modules/
rm -rf EverLight_OS/DNA_Access_Codes/
rm -rf EverLight_OS/Protocols/
```

### 3. Keep Unique Content
- Keep: `EverLight_OS/MemoryVault/` (has gists)
- Keep: `EverLight_OS/EverLight_OS_Architecture_Sketch.md`
- Remove: Empty duplicate folders

## Final Structure
```
EverLightOS/
├── Core_Modules/           # ACTIVE (keep)
├── MemoryVault/           # MERGED (gists + web files)
├── Protocols/             # ACTIVE (keep)
├── Interfaces/            # ACTIVE (keep)
└── EverLight_OS/          # REMOVE after merge
```