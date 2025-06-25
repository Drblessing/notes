#!/bin/bash
# Complete Linux Installation Script
# This script coordinates the installation of packages, dotfiles, and other configurations for Ubuntu servers

set -e  # Exit on any error

echo "Starting complete Linux installation..."

# Create Github directory if it doesn't exist
mkdir -p ~/Github

# Set the notes repository path
export NOTES_REPO_PATH=~/Github/notes

# Check if we're in the notes repository
if [ ! -d "$NOTES_REPO_PATH" ]; then
    echo "Error: Notes repository not found at $NOTES_REPO_PATH"
    echo "Please clone the notes repository first:"
    echo "git clone <your-notes-repo-url> ~/Github/notes"
    exit 1
fi

# Run APT packages installation
echo "Running APT packages installation..."
bash "$NOTES_REPO_PATH/linux/scripts/apt_install.sh"

# Run Snap packages installation
echo "Running Snap packages installation..."
bash "$NOTES_REPO_PATH/linux/scripts/snap_install.sh"

# Run dotfiles installation
echo "Running Linux dotfiles installation..."
bash "$NOTES_REPO_PATH/linux/scripts/dotfiles_install.sh"

# Set up basic security (UFW firewall)
echo "Setting up basic UFW firewall..."
sudo ufw --force reset
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw --force enable

# Enable and start fail2ban if it was installed
if command -v fail2ban-server &> /dev/null; then
    echo "Enabling fail2ban..."
    sudo systemctl enable fail2ban
    sudo systemctl start fail2ban
fi

echo "Linux installation completed successfully!"
echo ""
echo "Next steps:"
echo "1. Restart your shell or run 'source ~/.bashrc'"
echo "2. Configure SSH keys if needed"
echo "3. Set up any additional services"
echo "4. Review UFW firewall rules: sudo ufw status"
