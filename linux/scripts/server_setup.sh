#!/bin/bash

# Remote Server Setup Script
# This script can be run on a fresh Ubuntu server to bootstrap the setup

set -e

echo "Ubuntu Server Bootstrap Setup"
echo "============================="
echo ""

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo "Error: Please run this script as a non-root user with sudo privileges"
    echo "This script will prompt for sudo password when needed"
    exit 1
fi

# Update system first
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install essential packages for bootstrapping
echo "Installing essential packages..."
sudo apt install -y curl wget git vim nano htop tree unzip build-essential

# Create Github directory
echo "Creating Github directory..."
mkdir -p ~/Github

# Clone the notes repository
echo "Cloning notes repository..."
if [ ! -d ~/Github/notes ]; then
    cd ~/Github
    git clone https://github.com/drblessing/notes.git
    echo "Notes repository cloned successfully"
else
    echo "Notes repository already exists, updating..."
    cd ~/Github/notes
    git pull origin main
fi

# Make scripts executable
echo "Making scripts executable..."
chmod +x ~/Github/notes/linux/scripts/*.sh

# Run the main installation script
echo "Running main installation script..."
bash ~/Github/notes/linux/scripts/main_install.sh

echo ""
echo "========================================="
echo "Bootstrap setup completed successfully!"
echo "========================================="
echo ""
echo "What was configured:"
echo "- System packages updated"
echo "- Essential and development tools installed"
echo "- Security packages and configurations"
echo "- UFW firewall enabled"
echo "- fail2ban configured"
echo "- SSH server hardened"
echo "- Dotfiles linked"
echo "- Monitoring tools setup"
echo ""
echo "Important security notes:"
echo "- SSH password authentication is now DISABLED"
echo "- Only SSH key authentication is allowed"
echo "- Make sure you have SSH keys configured before disconnecting!"
echo ""
echo "Next steps:"
echo "1. Copy your SSH public key to ~/.ssh/authorized_keys"
echo "2. Test SSH key authentication from another terminal"
echo "3. Reboot the server: sudo reboot"
echo "4. Verify all services are running after reboot"
echo ""
echo "Useful commands:"
echo "- sudo ufw status          : Check firewall status"
echo "- sudo fail2ban-client status : Check fail2ban status"
echo "- sysmon                   : System monitoring"
echo "- security-check           : Security status check"
