#!/bin/bash
# Simple Snap package installer for Ubuntu servers

set -e

NOTES_REPO_PATH="${NOTES_REPO_PATH:-$HOME/github/notes}"
SNAP_LIST="$NOTES_REPO_PATH/linux/packages/snap_packages.txt"

echo "Starting Snap package installation..."

# Ensure snapd exists
if ! command -v snap &>/dev/null; then
  echo "Snapd not found. Installing..."
  sudo apt update
  sudo apt install -y snapd
  sudo systemctl enable --now snapd
fi

if [[ -f "$SNAP_LIST" ]]; then
  echo "Installing Snap packages from $SNAP_LIST..."
  grep -Ev '^\s*#|^\s*$' "$SNAP_LIST" | xargs -n1 sudo snap install
else
  echo "Error: Snap package list not found at $SNAP_LIST"
  exit 1
fi

echo "Snap package installation complete ✅"