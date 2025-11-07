---
conversation_id: "684d11cb-cbe8-8011-8217-5ee4d6b3cecb"
title: "Third-party drivers decision"
accounts: ["Account2_exports"]
models: []
tags: []
message_count: 9
---
# Third-party drivers decision

##  — system


##  — user


## 2025-06-14T06:08:11.541980Z — user
{"content_type": "image_asset_pointer", "asset_pointer": "file-service://file-MLPcPcaq8hpEZ75cQvMsVz", "size_bytes": 1593672, "width": 1152, "height": 1536, "fovea": null, "metadata": {"dalle": null, "gizmo": null, "generation": null, "container_pixel_height": null, "container_pixel_width": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "asset_pointer_link": null, "watermarked_asset_pointer": null}}
3rd party drivers or no?

## 2025-06-14T06:08:13.322010Z — assistant
Whether or not to enable **“Search for third-party drivers”** depends on your use case:

---

### ✅ **Enable (Check it)** if:
- You're using **proprietary WiFi**, **GPU**, or **RAID/storage** drivers (e.g., NVIDIA, Broadcom, Intel RST).
- You want better **hardware compatibility** out-of-the-box, especially for newer machines or laptops.
- You're not concerned about fully open-source purity.

---

### ❌ **Skip (Leave unchecked)** if:
- You are running this on a **virtual machine**, headless server, or a system with **known working open-source drivers**.
- You’re trying to keep the system as **minimal** and clean as possible (e.g., for a lightweight server).
- You want to install only **audited, open-source components** for security or policy reasons.

---

If you're unsure or just want everything to work smoothly on first boot, it’s usually safe and helpful to **check it** — you can always remove any drivers later. Want me to help you identify if any of your current hardware *requires* proprietary drivers?

## 2025-06-14T06:08:23.230640Z — assistant


## 2025-06-14T06:09:10.990227Z — user
Anything I need to do on network config screen?

## 2025-06-14T06:09:11.379237Z — assistant
Yes — the **network configuration screen** is important and can affect whether your server is reachable, updated, or able to install packages during setup. Here's a quick breakdown depending on your goal:

---

## 🛠️ **On the Network Config Screen — What to Do**

### ✅ **If you want quick setup with DHCP (recommended default):**
- **Leave the settings as-is** if your interface shows a valid IP (like `192.168.x.x`, `10.x.x.x`, or `172.16.x.x`).
- This means DHCP from your router is working — Ubuntu will handle DNS, gateway, etc.

---

### 🔧 **If you're setting up a server with a static IP:**
Use a **static IP address** if:
- You’re deploying a web server, Nextcloud, or anything public-facing.
- You want consistent SSH access or port forwarding.

Here’s what to set manually:
- **IP address**: something like `192.168.1.50/24`
- **Gateway**: your router’s IP (e.g., `192.168.1.1`)
- **DNS**: `8.8.8.8`, `1.1.1.1`, or your router’s IP

> ⚠️ Be sure it doesn’t conflict with another device — assign one outside your router’s DHCP range if possible.

---

### 🌐 **Optional but smart:**
- If you see a checkbox to **configure a proxy**, skip it unless you're behind a corporate or secured network.
- If you're on **Wi-Fi**, it may prompt you to pick a network and enter a password — wired Ethernet is better for stability if available.

---

Would you like help crafting a good static config for your current setup? Just let me know your router’s IP and your preferred IP range.

## 2025-06-14T06:09:52.579607Z — user
Are you saying click create a bond?

## 2025-06-14T06:09:52.999884Z — assistant
Ah — **no**, you do **not** need to click **“Create a bond”** unless you know you're setting up **network interface bonding** (i.e. combining multiple network interfaces for redundancy or speed).

### 🔒 **TL;DR:**
**👉 Skip “Create a bond”** — that’s only for advanced setups.

---

## 🧠 What Each Option Means (So You’re Sure):
### ✅ **Use the default listed interface**
- Example: `ens33`, `eth0`, or `enpXsY`
- If it shows a valid IP address — you're good.
- DHCP is working → continue.

---

### ❌ **Don’t use:**
- **“Create a bond”** – combines interfaces (used in enterprise networking for link aggregation, high availability, etc.)
- **“Create a VLAN”** – used in segmented network environments (enterprise LANs)
- **“Create a bridge”** – used mostly for virtualization setups or Docker networking

---

### 👇 What You Should Do
1. **Pick the default interface** (usually selected by default).
2. If it shows `IP address: assigned via DHCP` — you’re done.
3. If you need a **static IP**, edit the settings instead of bonding.

Would you like a screenshot-style breakdown of the static IP config? Or want me to walk you through what you’re seeing right now?
