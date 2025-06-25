#!/bin/bash
# Install Docker CE from the official Docker apt repository on Ubuntu

set -e

echo "Starting Docker installation..."

# Remove any old Docker-related packages
echo "Removing old Docker packages (if any)..."
sudo apt remove -y docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc || true

# Install prerequisites
echo "Installing prerequisites..."
sudo apt update
sudo apt install -y ca-certificates curl gnupg

# Add Docker’s official GPG key
echo "Adding Docker GPG key..."
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo tee /etc/apt/keyrings/docker.asc > /dev/null
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Set up the Docker apt repository
echo "Adding Docker apt repository..."
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package index and install Docker Engine
echo "Installing Docker Engine and tools..."
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Ensure docker group exists and add current user
echo "Adding user '$USER' to docker group..."
sudo groupadd -f docker
sudo usermod -aG docker "$USER"

echo "✅ Docker installation complete. You may need to log out and back in (or run 'newgrp docker')."