#!/bin/bash
# Snap packages installation script for Ubuntu servers
# This script installs snap packages

set -e  # Exit on any error

echo "Starting Snap packages installation..."

# Check if snapd is installed
if ! command -v snap &> /dev/null; then
    echo "Snapd is not installed. Installing snapd..."
    sudo apt update
    sudo apt install -y snapd
    
    # Enable snapd service
    sudo systemctl enable snapd
    sudo systemctl start snapd
    
    echo "Snapd installed successfully!"
else
    echo "Snapd is already installed."
fi

# Make sure we have the notes repository path
if [ -z "$NOTES_REPO_PATH" ]; then
    NOTES_REPO_PATH=~/Github/notes
    echo "Using default notes repository path: $NOTES_REPO_PATH"
fi

# Install snap packages if the file exists
if [ -f "$NOTES_REPO_PATH/linux/packages/snap_packages.txt" ]; then
    echo "Installing Snap packages..."
    
    # Read packages from file, skip comments and empty lines
    while IFS= read -r package || [ -n "$package" ]; do
        # Skip comments and empty lines
        if [[ "$package" =~ ^[[:space:]]*# ]] || [[ -z "${package// }" ]]; then
            continue
        fi
        
        # Trim whitespace
        package=$(echo "$package" | xargs)
        
        if [ -n "$package" ]; then
            echo "Installing snap: $package"
            sudo snap install "$package"
        fi
    done < "$NOTES_REPO_PATH/linux/packages/snap_packages.txt"
    
    echo "Snap packages installation completed!"
else
    echo "Error: Snap packages file not found at $NOTES_REPO_PATH/linux/packages/snap_packages.txt"
    exit 1
fi

echo "Snap installation finished successfully!"
