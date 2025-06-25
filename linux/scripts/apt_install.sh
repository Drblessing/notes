#!/bin/bash
# Simple APT package installer for Ubuntu servers

set -e

NOTES_REPO_PATH="${NOTES_REPO_PATH:-$HOME/github/notes}"
APT_LIST="$NOTES_REPO_PATH/linux/packages/apt_packages.txt"

echo "Starting APT package installation..."

sudo apt update

if [[ -f "$APT_LIST" ]]; then
  echo "Installing packages from $APT_LIST..."
  grep -Ev '^\s*#|^\s*$' "$APT_LIST" | xargs sudo apt install -y
else
  echo "Error: Package list not found at $APT_LIST"
  exit 1
fi

echo "Running APT cleanup..."
sudo apt autoremove -y
sudo apt autoclean

echo "APT installation complete ✅"