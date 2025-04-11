#!/bin/bash

# Complete Installation Script
# This script coordinates the installation of Homebrew, repositories, dotfiles, and other configurations

echo "Starting complete installation..."

# Create Github directory if it doesn't exist
mkdir -p ~/Github

# Run Homebrew installation script
echo "Running Homebrew installation..."
bash ~/Github/notes/code/shell/homebrew_install.sh

# Run Github login
echo "Running GitHub login script..."
bash ~/Github/notes/code/shell/gh_login.sh

# Run dotfiles installation script
echo "Running dotfiles installation script..."
bash ~/Github/notes/code/shell/dotfiles_install.sh

# Run repository installation script
echo "Running repository installation script..."
bash ~/Github/notes/code/shell/repos_install.sh

# Run benv installation script
echo "Running benv installation script..."
bash ~/Github/notes/code/shell/benv_install.sh

