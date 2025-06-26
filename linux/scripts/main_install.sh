#!/bin/bash
# Full Linux setup: APT packages, Snap packages, and dotfiles

set -e

echo "Starting full Linux server setup..."

# Define notes repo path
NOTES_REPO_PATH="${NOTES_REPO_PATH:-$HOME/github/notes}"
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
bash "$NOTES_REPO_PATH/linux/scripts/cloudflare_install.sh"
bash "$NOTES_REPO_PATH/linux/scripts/docker_install.sh"
bash "$NOTES_REPO_PATH/linux/scripts/dotfiles_install.sh"
bash "$NOTES_REPO_PATH/linux/scripts/fastfetch_install.sh"
bash "$NOTES_REPO_PATH/linux/scripts/plex_install.sh"
bash "$NOTES_REPO_PATH/linux/scripts/ufw_install.sh"


# Update 06/26/25: Disabling netdata until needed. UI is a mess.
# # Install netdata
# echo "Get netdata claim token from https://app.netdata.cloud/claim"
# # Input your claim token below
# read -p "Enter your Netdata claim token: " CLAIM_TOKEN
# if [ -z "$CLAIM_TOKEN" ]; then
#   echo "Error: Claim token cannot be empty."
#   exit 1
# fi

# echo "Installing Netdata..."
# curl https://get.netdata.cloud/kickstart.sh > /tmp/netdata-kickstart.sh && sh /tmp/netdata-kickstart.sh --stable-channel --disable-telemetry --claim-token "$CLAIM_TOKEN" --claim-url https://app.netdata.cloud --claim-rooms "default" --claim-description "Linux Server"

# Set server timezone to Detroit
echo "Setting server timezone to Detroit..."
sudo timedatectl set-timezone America/Detroit



echo "Full Linux setup complete ✅"
echo "You may want to restart your shell or run: source ~/.bashrc"