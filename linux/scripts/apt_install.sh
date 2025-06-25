#!/bin/bash
# Simple APT package installer for Ubuntu servers

set -e

NOTES_REPO_PATH="${NOTES_REPO_PATH:-$HOME/github/notes}"
APT_LIST="$NOTES_REPO_PATH/linux/packages/apt_packages.txt"

echo "Starting APT package installation..."

# Add fastfetch PPA
sudo add-apt-repository -y ppa:zhangsongcui3371/fastfetch
# Update package lists
sudo apt update





if [[ -f "$APT_LIST" ]]; then
  echo "Installing packages from $APT_LIST..."
  grep -Ev '^\s*#|^\s*$' "$APT_LIST" | xargs sudo apt install -y
else
  echo "Error: Package list not found at $APT_LIST"
  exit 1
fi

# Docker installation
echo "Installing Docker..."

# Uninstall any docker junk
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo groupadd docker
sudo usermod -aG docker $USER

# Cloudflare Warp installation
echo "Installing Cloudflare Warp..."

curl https://pkg.cloudflareclient.com/pubkey.gpg | sudo gpg --yes --dearmor --output /usr/share/keyrings/cloudflare-warp-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/cloudflare-warp-archive-keyring.gpg] https://pkg.cloudflareclient.com/ bookworm main" | sudo tee /etc/apt/sources.list.d/cloudflare-client.list
sudo apt-get update && sudo apt-get install cloudflare-warp


echo "Running APT cleanup..."
sudo apt autoremove -y
sudo apt autoclean

echo "APT installation complete ✅"