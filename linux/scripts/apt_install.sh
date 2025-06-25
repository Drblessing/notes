#!/bin/bash
# Simple APT package installer for Ubuntu servers

# Init
set -e
NOTES_REPO_PATH="${NOTES_REPO_PATH:-$HOME/github/notes}"
APT_LIST="$NOTES_REPO_PATH/linux/packages/apt_packages.txt"
echo "Starting APT package installation..."

# Installation
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

# Install snap packages
SNAP_LIST="$NOTES_REPO_PATH/linux/packages/snap_packages.txt"
if [[ -f "$SNAP_LIST" ]]; then
  echo "Installing snap packages from $SNAP_LIST..."
  grep -Ev '^\s*#|^\s*$' "$SNAP_LIST" | xargs sudo snap install
else
  echo "Error: Snap package list not found at $SNAP_LIST"
  exit 1
fi

echo "APT installation complete ✅"