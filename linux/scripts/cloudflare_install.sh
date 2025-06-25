#!/bin/bash
# Install Cloudflare packages  for Ubuntu servers

set -e

echo "Installing Cloudflare packages..."

# Import Cloudflare GPG key
curl https://pkg.cloudflareclient.com/pubkey.gpg | sudo gpg --yes --dearmor --output /usr/share/keyrings/cloudflare-warp-archive-keyring.gpg

# Add Cloudflare Warp apt repository
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/cloudflare-warp-archive-keyring.gpg] https://pkg.cloudflareclient.com/ bookworm main" | sudo tee /etc/apt/sources.list.d/cloudflare-client.list

# Update and install
sudo apt update
sudo apt install -y cloudflare-warp

sudo mkdir -p --mode=0755 /usr/share/keyrings
curl -fsSL https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /usr/share/keyrings/cloudflare-main.gpg >/dev/null
echo 'deb [signed-by=/usr/share/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared noble main' | sudo tee /etc/apt/sources.list.d/cloudflared.list
sudo apt update
sudo apt install cloudflared

echo "✅ Cloudflare packages installation complete."