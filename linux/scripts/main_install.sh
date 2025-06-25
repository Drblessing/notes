#!/bin/bash
# Full Linux setup: APT packages, Snap packages, and dotfiles

set -e

echo "Starting full Linux server setup..."

# Define notes repo path
NOTES_REPO_PATH="${NOTES_REPO_PATH:-$HOME/Github/notes}"
export NOTES_REPO_PATH

# Verify notes repo exists
if [ ! -d "$NOTES_REPO_PATH" ]; then
  echo "Error: Notes repo not found at $NOTES_REPO_PATH"
  echo "Please clone it first:"
  echo "git clone <your-repo-url> $NOTES_REPO_PATH"
  exit 1
fi

# Run install scripts
bash "$NOTES_REPO_PATH/linux/scripts/apt_install.sh"
bash "$NOTES_REPO_PATH/linux/scripts/snap_install.sh"
bash "$NOTES_REPO_PATH/linux/scripts/dotfiles_install.sh"

echo "Full Linux setup complete ✅"
echo "You may want to restart your shell or run: source ~/.bashrc"