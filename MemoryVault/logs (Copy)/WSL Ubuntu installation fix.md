---
conversation_id: "68ae40d5-de64-8328-a694-a442aa27fc5a"
title: "WSL Ubuntu installation fix"
accounts: ["Account1_exports"]
models: []
tags: []
message_count: 5
---
# WSL Ubuntu installation fix

##  — user


##  — system


## 2025-08-26T23:19:31.984951Z — user
{"content_type": "image_asset_pointer", "asset_pointer": "file-service://file-CkgYDHgVSCSg2yKSkdQ6uY", "size_bytes": 286678, "width": 2295, "height": 4080, "fovea": null, "metadata": {"dalle": null, "gizmo": null, "generation": null, "container_pixel_height": null, "container_pixel_width": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "asset_pointer_link": null, "watermarked_asset_pointer": null}}


## 2025-08-26T23:19:32.032057Z — assistant


## 2025-08-26T23:19:32.097871Z — assistant
Ah, I see what’s happening here. You’re trying to enable the Ubuntu subsystem under WSL (Windows Subsystem for Linux) on Windows, and it mostly worked, but the feature didn’t fully start. Let’s break down the output:  

1. **Installation succeeded:**  
```
The requested operation completed successfully. 
Downloading: Ubuntu
Installing: Ubuntu
The operation could not be started because a required feature is not installed.
```
The first part shows that the WSL feature itself was enabled successfully.  

2. **Error detail:**  
```
Error code: Wsl/InstallDistro/Service/RegisterDistro/CreateVm/HCS/HCS_E_SERVICE_NOT_AVAILABLE
```
This indicates that the actual Linux distro (Ubuntu) could not register with the Windows Host Compute Service. This usually happens if:  
- Hyper-V or the Virtual Machine Platform is **not enabled**, or  
- The system **needs a reboot** after enabling WSL, or  
- There’s a mismatch between WSL versions (WSL1 vs WSL2), or  
- Some services are not running correctly.

3. **Next steps to fix it:**  
- **Reboot** your PC. Many WSL changes only take effect after a restart.  
- Make sure the following Windows features are **enabled**:  
  - **Virtual Machine Platform**  
  - **Windows Hypervisor Platform** (sometimes required)  
  - **Windows Subsystem for Linux**  

You can enable them via PowerShell as administrator:  
```powershell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```
Then reboot.  

- After reboot, set WSL2 as default and install Ubuntu again:  
```powershell
wsl --set-default-version 2
wsl --install -d Ubuntu
```

That should register the distro correctly.  

If you want, I can give you a **step-by-step command sequence** that usually gets this working cleanly on a fresh Windows setup. Do you want me to do that?
