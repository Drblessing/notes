#!/bin/bash

# Complete Installation Script
# This script coordinates the installation of Homebrew, repositories, dotfiles, and other configurations

echo "Starting complete installation..."

# Create github directory if it doesn't exist
mkdir -p ~/github

# Run Homebrew installation script
echo "Running Homebrew installation..."
bash ~/github/notes/code/shell/homebrew_install.sh

# Run github login
echo "Running github login script..."
bash ~/github/notes/code/shell/gh_login.sh

# Run dotfiles installation script
echo "Running dotfiles installation script..."
bash ~/github/notes/code/shell/dotfiles_install.sh

# Run benv installation script
echo "Running benv installation script..."
bash ~/github/notes/code/shell/benv_install.sh

# Run newsboat installation script
echo "Running newsboat installation script..."
bash ~/github/notes/code/shell/newsboat_install.sh
