<p align="center">
  <img src="kavita/logo.png" alt="Kavita Logo" width="120" />
</p>

# 📖 Kavita — Home Assistant Add-on Repository

<p align="center">
  <strong><a href="README.md">English</a></strong> | <strong><a href="README_UK.md">Українська</a></strong>
</p>

<p align="center">
  <a href="https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FS88EM%2Fkavita-homeassistant">
    <img src="https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg" alt="Open your Home Assistant and show the add-on store" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/arch-aarch64%20%7C%20amd64%20%7C%20armv7-blue" alt="Supported Architectures" />
  <img src="https://img.shields.io/badge/version-0.9.1.4-blue" alt="Add-on Version" />
  <img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License" />
</p>

This repository provides **[Kavita](https://www.kavitareader.com)** as a native **Home Assistant Add-on** for **Home Assistant OS / Supervised** (Raspberry Pi 4/5, x86/ARM mini PCs, and Virtual Machines).

**Kavita** is a fast, beautiful, self-hosted digital library designed from the ground up for manga, webtoons, comics, and ebooks.

---

## ✨ Features

* 🔒 **Data Persistence Guaranteed:** Your SQLite database (`app.db`), bookmarks, reading progress, and cover cache are safely stored in Home Assistant's persistent `/data/config` directory, surviving container restarts and add-on updates.
* 📂 **Instant Samba Access:** Pre-configured paths mapped directly to your Home Assistant Samba share (`\\homeassistant.local\share\kavita\`).
* 📱 **Built-in OPDS Server:** Seamless integration with third-party mobile readers for Android and iOS (Mihon / Tachiyomi, Panels, Chunky, Moon+ Reader, Paperback, etc.).
* ⚡ **Multi-Architecture Support:** Built for `aarch64` (64-bit ARM, e.g. Raspberry Pi 4/5), `amd64` (Intel/AMD), and `armv7`.
* 🌐 **Reverse Proxy & SSL Ready:** Works out-of-the-box in local networks or behind HTTPS reverse proxies (KeenDNS, Cloudflare Tunnel, NGINX Proxy Manager, etc.).

---

## 🚀 Installation

### Option 1: 1-Click Install via My Home Assistant
Click the badge below to open your Home Assistant instance and automatically add this repository:

[![Open your Home Assistant and show the add-on store](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FS88EM%2Fkavita-homeassistant)

### Option 2: Manual Installation
1. In Home Assistant, navigate to: **Settings** → **Add-ons** → **Add-on Store**.
2. Click the **three dots menu** (top right) → **Repositories**.
3. Add the following repository URL:
   ```text
   https://github.com/S88EM/kavita-homeassistant
   ```
4. Click **Add**, close the dialog, and refresh the store.
5. Find **Kavita** in the list, click **Install**, and once finished, click **Start**.

---

## 📚 Adding Books & Manga

You can drop your `.cbz`, `.cbr`, `.epub`, and `.pdf` files directly onto your Home Assistant server using Windows File Explorer or macOS Finder via **Samba Share**:

| Content Type | Samba Network Share | Path Inside Kavita |
| :--- | :--- | :--- |
| **Books (EPUB, PDF)** | `\\homeassistant.local\share\kavita\books` | `/books` |
| **Manga (CBZ, CBR, ZIP)** | `\\homeassistant.local\share\kavita\manga` | `/manga` |
| **Comics (CBZ, CBR, PDF)** | `\\homeassistant.local\share\kavita\comics` | `/comics` |
| **Other Media** | `\\homeassistant.local\media` | `/media` |

### Setting Up Libraries in Kavita:
1. Open the Kavita Web UI on port `5000` (or click **Open Web UI** on the add-on page in Home Assistant).
2. Complete the initial admin registration.
3. Go to **Server Settings** → **Libraries** → **Add Library**.
4. Choose the library type and set the folder path to: `/books`, `/manga`, or `/comics`.
5. Click **Save** to start scanning!

---

## 📱 Mobile Readers (OPDS)

Kavita includes a full OPDS server to browse and download your collection directly to mobile reading apps:

* **Android:** [Mihon](https://mihon.app/) (via the Kavita extension), Moon+ Reader, Kuro Reader, CDisplayEx.
* **iOS:** Panels, Chunky Comic Reader, Paperback.

To obtain your personal OPDS URL and API key, open Kavita and navigate to:  
**User Settings** → **3rd Party Clients** / **Auth Keys**.

---

## ⚙️ Configuration

The add-on options can be adjusted in the **Configuration** tab in Home Assistant:

```yaml
timezone: "UTC" # Change to your local timezone (e.g. Europe/Kyiv, America/New_York)
```

---

## 📁 Repository Structure

```text
├── kavita/             # Home Assistant Add-on directory
│   ├── config.yaml     # Add-on manifest and schema
│   ├── build.yaml      # Architecture mapping (jvmilazz0/kavita)
│   ├── Dockerfile      # Container configuration
│   ├── run.sh          # Entrypoint with persistent storage migration
│   ├── DOCS.md         # Add-on documentation tab in HA
│   ├── CHANGELOG.md    # Release history
│   ├── icon.png        # Add-on icon
│   └── logo.png        # Add-on logo
├── repository.yaml     # Supervisor repository manifest
├── LICENSE             # MIT License
├── README.md           # English documentation
└── README_UK.md        # Ukrainian documentation
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
Kavita is developed by [Kareadita](https://github.com/Kareadita/Kavita) and is licensed under the GPL-3.0 License.
