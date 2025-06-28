#!/bin/bash
# Install Fastfetch from PPA (for Ubuntu 22.04+)


echo "Installing Fastfetch..."

sudo add-apt-repository -y ppa:zhangsongcui3371/fastfetch
sudo apt update
sudo apt install -y fastfetch

echo "✅ Fastfetch installation complete."