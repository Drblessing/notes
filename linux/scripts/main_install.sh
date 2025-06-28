#!/bin/bash
# Full Linux setup: APT packages, Snap packages, and dotfiles

# Set server timezone to Detroit
echo "Setting server timezone to Detroit..."
sudo timedatectl set-timezone America/Detroit



echo "Full Linux setup complete ✅"
echo "You may want to restart your shell or run: source ~/.bashrc"