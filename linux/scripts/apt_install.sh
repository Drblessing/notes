#!/bin/bash
# APT packages installation script for Ubuntu servers
# This script installs essential packages for development and system administration

set -e  # Exit on any error

echo "Starting APT packages installation..."

# Update package lists
echo "Updating package lists..."
sudo apt update

# Make sure we have the notes repository path
if [ -z "$NOTES_REPO_PATH" ]; then
    NOTES_REPO_PATH=~/Github/notes
    echo "Using default notes repository path: $NOTES_REPO_PATH"
fi

# Install packages if the file exists
if [ -f "$NOTES_REPO_PATH/linux/packages/apt_packages.txt" ]; then
    echo "Installing APT packages..."
    
    # Read packages from file, skip comments and empty lines
    while IFS= read -r package || [ -n "$package" ]; do
        # Skip comments and empty lines
        if [[ "$package" =~ ^[[:space:]]*# ]] || [[ -z "${package// }" ]]; then
            continue
        fi
        
        # Trim whitespace
        package=$(echo "$package" | xargs)
        
        if [ -n "$package" ]; then
            echo "Installing: $package"
            sudo apt install -y "$package"
        fi
    done < "$NOTES_REPO_PATH/linux/packages/apt_packages.txt"
    
    echo "APT packages installation completed!"
else
    echo "Error: APT packages file not found at $NOTES_REPO_PATH/linux/packages/apt_packages.txt"
    exit 1
fi

# Clean up
echo "Cleaning up APT cache..."
sudo apt autoremove -y
sudo apt autoclean

echo "APT installation finished successfully!"
