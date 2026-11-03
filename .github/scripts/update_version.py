#!/usr/bin/env python3
import json
import os
import re
import sys
import urllib.request
from datetime import datetime

GITHUB_API_URL = "https://api.github.com/repos/Kareadita/Kavita/releases/latest"

def main():
    print(f"Checking latest release from {GITHUB_API_URL}...")
    req = urllib.request.Request(
        GITHUB_API_URL,
        headers={"User-Agent": "HomeAssistant-Addon-Updater"}
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"Error fetching latest release: {e}", file=sys.stderr)
        sys.exit(1)

    latest_tag = data.get("tag_name", "").strip()
    latest_version = latest_tag.lstrip("v")
    if not latest_version:
        print("Failed to find valid tag_name in response", file=sys.stderr)
        sys.exit(1)

    print(f"Latest Kavita release: {latest_tag} -> version: {latest_version}")

    config_path = os.path.join("kavita", "config.yaml")
    with open(config_path, "r", encoding="utf-8", newline="") as f:
        config_content = f.read()

    match = re.search(r'version:\s*"([^"]+)"', config_content)
    if not match:
        print(f"Could not find version field in {config_path}", file=sys.stderr)
        sys.exit(1)

    current_version = match.group(1).strip()
    print(f"Current add-on version: {current_version}")

    if current_version == latest_version:
        print("Add-on is already up to date with the latest Kavita release.")
        if "GITHUB_OUTPUT" in os.environ:
            with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8", newline="\n") as f:
                f.write("updated=false\n")
        return

    print(f"Updating add-on version from {current_version} to {latest_version}...")

    # 1. Update kavita/config.yaml
    new_config = re.sub(
        r'version:\s*"[^"]+"',
        f'version: "{latest_version}"',
        config_content,
        count=1
    )
    with open(config_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_config)
    print(f"Updated {config_path}")

    # 2. Update README.md and README_UK.md badges
    for readme_name in ["README.md", "README_UK.md"]:
        if os.path.exists(readme_name):
            with open(readme_name, "r", encoding="utf-8", newline="") as f:
                content = f.read()
            # Replace badge: version-<old>-<color> -> version-<new>-blue
            updated = re.sub(
                r'badge/version-[0-9a-zA-Z\.]+(?:-[a-zA-Z]+)?',
                f'badge/version-{latest_version}-blue',
                content
            )
            with open(readme_name, "w", encoding="utf-8", newline="\n") as f:
                f.write(updated)
            print(f"Updated {readme_name}")

    # 3. Update kavita/CHANGELOG.md
    changelog_path = os.path.join("kavita", "CHANGELOG.md")
    today_str = datetime.now().strftime("%Y-%m-%d")
    new_entry = f"## {latest_version} ({today_str})\n- Оновлено Kavita до офіційного релізу v{latest_version}\n\n"

    if os.path.exists(changelog_path):
        with open(changelog_path, "r", encoding="utf-8", newline="") as f:
            cl_content = f.read()
        if cl_content.startswith("# Changelog\n\n"):
            updated_cl = "# Changelog\n\n" + new_entry + cl_content[len("# Changelog\n\n"):]
        else:
            updated_cl = "# Changelog\n\n" + new_entry + cl_content
    else:
        updated_cl = f"# Changelog\n\n{new_entry}"

    with open(changelog_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(updated_cl)
    print(f"Updated {changelog_path}")

    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8", newline="\n") as f:
            f.write("updated=true\n")
            f.write(f"version={latest_version}\n")
            f.write(f"old_version={current_version}\n")

    print(f"Successfully bumped version to {latest_version}!")

if __name__ == "__main__":
    main()
