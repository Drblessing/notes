#!/bin/bash

# UFW Firewall Setup Script
# Configures Ubuntu UFW firewall with secure defaults

set -e

echo "Setting up UFW firewall..."

# Install UFW if not already installed
if ! command -v ufw &> /dev/null; then
    echo "Installing UFW..."
    sudo apt update
    sudo apt install -y ufw
fi

# Reset UFW to defaults
echo "Resetting UFW to defaults..."
sudo ufw --force reset

# Set default policies
echo "Setting default policies..."
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow SSH (essential for remote access)
echo "Allowing SSH access..."
sudo ufw allow ssh

# Enable SSH rate limiting to prevent brute force attacks
echo "Enabling SSH rate limiting..."
sudo ufw limit ssh

# Allow HTTP and HTTPS (uncomment if running web services)
# echo "Allowing HTTP/HTTPS..."
# sudo ufw allow 80/tcp
# sudo ufw allow 443/tcp

# Allow custom ports (add as needed for your applications)
# Examples:
# sudo ufw allow 3000/tcp  # Node.js development server
# sudo ufw allow 8080/tcp  # Alternative HTTP port
# sudo ufw allow 5432/tcp  # PostgreSQL
# sudo ufw allow 3306/tcp  # MySQL

# Enable UFW
echo "Enabling UFW..."
sudo ufw --force enable

# Show status
echo "UFW Firewall Status:"
sudo ufw status verbose

echo "UFW firewall setup completed successfully!"
echo ""
echo "Note: Make sure you can still SSH to this server before disconnecting!"
echo "If you lose SSH access, you may need console access to fix the firewall rules."
