---
conversation_id: "683a744b-6e30-8011-b2f5-d3cd32929d89"
title: "Fixing Nextcloud 2FA"
accounts: ["Account2_exports"]
models: []
tags: []
message_count: 9
---
# Fixing Nextcloud 2FA

##  — system


##  — user


## 2025-05-31T03:15:23.200301Z — user
{"content_type": "image_asset_pointer", "asset_pointer": "file-service://file-L995kRNprR82Y9dbi39jrK", "size_bytes": 171515, "width": 708, "height": 1536, "fovea": null, "metadata": {"dalle": null, "gizmo": null, "generation": null, "container_pixel_height": null, "container_pixel_width": null, "emu_omit_glimpse_image": null, "emu_patches_override": null, "lpe_keep_patch_ijhw": null, "sanitized": true, "asset_pointer_link": null, "watermarked_asset_pointer": null}}
How do I use occ to fix this 

## 2025-05-31T03:15:24.604128Z — assistant
To resolve this **Nextcloud 2FA error** using the `occ` CLI tool, you’ll want to either:

1. **Disable 2FA enforcement for the user**, or  
2. **Configure a valid 2FA method** (like TOTP) via CLI so the user can log in.

---

## 🛠️ Option 1: Disable 2FA for the user

This is the quickest fix, especially if the 2FA method wasn’t initialized properly.

### Command:
```bash
sudo -u www-data php /path/to/nextcloud/occ twofactorauth:disable <username>
```

Replace `/path/to/nextcloud/` with the actual path (commonly `/var/www/nextcloud`)  
Replace `<username>` with the actual Nextcloud username.

---

## 🛠️ Option 2: Disable 2FA app entirely (if needed)
If multiple users are affected or the app is misbehaving:

```bash
sudo -u www-data php /path/to/nextcloud/occ app:disable twofactor_totp
```

---

## 🛡️ Optional: View 2FA status
See which users have 2FA enabled:

```bash
sudo -u www-data php /path/to/nextcloud/occ twofactorauth:state <username>
```

---

## ✅ After Fixing
Once logged in, go to **Settings → Security** and re-enable a working 2FA method like TOTP (e.g., Google Authenticator) if needed.

---

Would you like me to generate a one-liner for your exact server path and username? If so, let me know the values.

## 2025-05-31T03:15:31.478422Z — assistant


## 2025-05-31T09:59:26.149998Z — user
How do I make a secondary ad,in account from Terminal

## 2025-05-31T09:59:27.140655Z — assistant
To create a **secondary admin account** in **Nextcloud** using the `occ` command via terminal, follow these steps:

---

## 🛠️ Create a New Admin User from Terminal

### 🔹 Step 1: Create the user
```bash
sudo -u www-data php /path/to/nextcloud/occ user:add <new_username>
```

You’ll be prompted to enter a password and optional email.

> Example:
```bash
sudo -u www-data php /var/www/nextcloud/occ user:add admin2
```

---

### 🔹 Step 2: Add the user to the admin group
```bash
sudo -u www-data php /path/to/nextcloud/occ group:adduser admin <new_username>
```

> Example:
```bash
sudo -u www-data php /var/www/nextcloud/occ group:adduser admin admin2
```

---

### ✅ Done!
This `admin2` user now has full admin rights and can log in normally.

---

## 🧠 Optional Tips

- If you’re not using `www-data` (e.g. on some systems it's `apache` or `nginx`), adjust the `sudo -u` user accordingly.
- You can check existing groups with:
  ```bash
  sudo -u www-data php /path/to/nextcloud/occ group:list
  ```

---

Would you like me to generate the exact commands for your setup if you tell me the path to your Nextcloud and the username you'd like to assign?

## 2025-05-31T10:00:53.496692Z — user
sudo -u www-data php /mnt/data/nextcloud/nextcloud/occ group:adduser admin devs

## 2025-05-31T10:00:54.242927Z — assistant
That command is **almost correct**, assuming:

- The Nextcloud installation is located at `/mnt/data/nextcloud/nextcloud`
- The username you're adding (`devs`) already exists

---

## ✅ Here’s the correct command:
```bash
sudo -u www-data php /mnt/data/nextcloud/nextcloud/occ group:adduser admin devs
```

If the user `devs` does **not** already exist, you must create them first:

---

### 🧱 Step-by-step (to create and promote `devs` as admin):

```bash
# Step 1: Create the user (if not already created)
sudo -u www-data php /mnt/data/nextcloud/nextcloud/occ user:add devs

# Step 2: Add the user to the admin group
sudo -u www-data php /mnt/data/nextcloud/nextcloud/occ group:adduser admin devs
```

You’ll be prompted to enter a password for the user when using `user:add`.

---

Let me know if you want the user to be auto-created with a password and email **non-interactively**, and I’ll format that version too.
