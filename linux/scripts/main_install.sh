#!/bin/bash
# Main Installation Script for Ubuntu Server Setup
# This script coordinates the complete server setup process

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${GREEN}[$(date +'%Y-%m-%d %H:%M:%S')] $1${NC}"
}

warn() {
    echo -e "${YELLOW}[$(date +'%Y-%m-%d %H:%M:%S')] WARNING: $1${NC}"
}

error() {
    echo -e "${RED}[$(date +'%Y-%m-%d %H:%M:%S')] ERROR: $1${NC}"
}

# Check if running as root
if [[ $EUID -eq 0 ]]; then
    error "This script should not be run as root. Please run as a regular user with sudo privileges."
    exit 1
fi

# Check if sudo is available
if ! command -v sudo &> /dev/null; then
    error "sudo is required but not installed. Please install sudo first."
    exit 1
fi

log "Starting Ubuntu Server Setup..."
log "This script will:"
log "  1. Update system packages"
log "  2. Install essential packages"
log "  3. Setup SSH configuration"
log "  4. Configure firewall (UFW)"
log "  5. Apply security hardening"
log "  6. Install dotfiles"
log "  7. Setup development environment"

# Confirm before proceeding
read -p "Do you want to continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    log "Installation cancelled."
    exit 0
fi

# Set up directory structure
NOTES_REPO_PATH="$HOME/Github/notes"
LINUX_CONFIG_PATH="$NOTES_REPO_PATH/linux"

# Check if notes repository exists
if [ ! -d "$NOTES_REPO_PATH" ]; then
    log "Cloning notes repository..."
    mkdir -p "$HOME/Github"
    cd "$HOME/Github"
    git clone https://github.com/drblessing/notes.git
    cd "$NOTES_REPO_PATH"
else
    log "Notes repository already exists, updating..."
    cd "$NOTES_REPO_PATH"
    git pull origin main
fi

# Make scripts executable
chmod +x "$LINUX_CONFIG_PATH/scripts"/*.sh

# Run installation steps
log "Step 1: Installing packages..."
bash "$LINUX_CONFIG_PATH/scripts/package_install.sh"

log "Step 2: Setting up SSH configuration..."
bash "$LINUX_CONFIG_PATH/scripts/ssh_setup.sh"

log "Step 3: Configuring firewall..."
bash "$LINUX_CONFIG_PATH/scripts/firewall_setup.sh"

log "Step 4: Applying security hardening..."
bash "$LINUX_CONFIG_PATH/scripts/security_hardening.sh"

log "Step 5: Installing dotfiles..."
bash "$LINUX_CONFIG_PATH/scripts/dotfiles_install.sh"

log "Setup completed successfully! 🎉"
log ""
log "Next steps:"
log "  1. Copy your SSH private key to ~/.ssh/id_ed25519"
log "  2. Set proper permissions: chmod 600 ~/.ssh/id_ed25519"
log "  3. Test SSH key authentication before disabling passwords"
log "  4. Reboot the system to ensure all changes take effect"
log "  5. Review firewall rules: sudo ufw status"
log ""
log "Important security notes:"
log "  - SSH password authentication is now DISABLED"
log "  - Only SSH key authentication is allowed"
log "  - UFW firewall is enabled with default deny incoming"
log "  - Fail2ban is configured to protect against brute force attacks"
log ""
warn "Please test SSH access with keys before closing this session!"

# Show system status
log "Current system status:"
echo "UFW Status:"
sudo ufw status
echo ""
echo "Fail2ban Status:"
sudo systemctl status fail2ban --no-pager -l || echo "Fail2ban not running"
echo ""
echo "SSH Service Status:"
sudo systemctl status ssh --no-pager -l
