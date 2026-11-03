#!/usr/bin/env bash
set -e

echo "[Kavita] =========================================="
echo "[Kavita] Starting Kavita Server for Home Assistant"
echo "[Kavita] =========================================="

# Apply timezone if configured in add-on options
if [ -f /data/options.json ]; then
    TZ_VAL=$(grep -o '"timezone"[^,}]*' /data/options.json | cut -d'"' -f4)
    if [ -n "$TZ_VAL" ]; then
        export TZ="$TZ_VAL"
        echo "[Kavita] Timezone set to: $TZ"
    fi
fi

# Ensure persistent storage directory in /data
mkdir -p /data/config
mkdir -p /data/cache

# If /kavita/config is a physical folder (not a symlink), migrate existing files
if [ -d /kavita/config ] && [ ! -L /kavita/config ]; then
    echo "[Kavita] Migrating initial files to /data/config..."
    cp -rn /kavita/config/* /data/config/ 2>/dev/null || true
    rm -rf /kavita/config
fi

# Enable iframe embedding for Home Assistant Ingress/Sidebar
export AllowIFraming="true"
export Kavita__AllowIFraming="true"

if [ -f /data/config/appsettings.json ]; then
    if ! grep -q '"AllowIFraming"' /data/config/appsettings.json; then
        sed -i 's/{/{\n  "AllowIFraming": true,/' /data/config/appsettings.json 2>/dev/null || true
    fi
fi

# Link /kavita/config to persistent storage
if [ ! -L /kavita/config ]; then
    ln -s /data/config /kavita/config
    echo "[Kavita] Persistent config linked -> /data/config"
fi

# Ensure default folders in /share/kavita
mkdir -p /share/kavita/manga 2>/dev/null || true
mkdir -p /share/kavita/comics 2>/dev/null || true
mkdir -p /share/kavita/books 2>/dev/null || true

# Symlink convenient root shortcuts
ln -sfn /share/kavita/manga /manga 2>/dev/null || true
ln -sfn /share/kavita/comics /comics 2>/dev/null || true
ln -sfn /share/kavita/books /books 2>/dev/null || true

echo "[Kavita] Library paths configured:"
echo "         - /share/kavita/books (or /books)"
echo "         - /share/kavita/manga (or /manga)"
echo "         - /share/kavita/comics (or /comics)"
echo "         - /media"
echo "[Kavita] Starting Kavita service on port 5000..."

cd /kavita
exec ./Kavita