#!/bin/bash

# Complete Installation Script
# This script coordinates the installation of Homebrew, repositories, dotfiles, and other configurations

echo "Starting complete installation..."

# Create Github directory if it doesn't exist
mkdir -p ~/Github

# Run Homebrew installation script
echo "Running Homebrew installation..."
bash ~/Github/notes/configs/shell/homebrew_install.sh