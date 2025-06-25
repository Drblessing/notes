#!/bin/bash

# Security Setup Script
# Configures various security measures for Ubuntu server

set -e

echo "Setting up security measures..."

# Install security packages if not already installed
echo "Ensuring security packages are installed..."
SECURITY_PACKAGES="fail2ban unattended-upgrades rkhunter chkrootkit lynis"
for package in $SECURITY_PACKAGES; do
    if ! dpkg -l | grep -q "^ii  $package "; then
        echo "Installing $package..."
        sudo apt update
        sudo apt install -y $package
    fi
done

# Configure fail2ban
echo "Configuring fail2ban..."
if [ -f ~/Github/notes/linux/configs/fail2ban/jail.local ]; then
    sudo cp ~/Github/notes/linux/configs/fail2ban/jail.local /etc/fail2ban/jail.local
    sudo systemctl enable fail2ban
    sudo systemctl restart fail2ban
    echo "fail2ban configured and started"
else
    echo "Warning: fail2ban config not found, using defaults"
    sudo systemctl enable fail2ban
    sudo systemctl start fail2ban
fi

# Configure automatic security updates
echo "Configuring automatic security updates..."
sudo dpkg-reconfigure -plow unattended-upgrades

# Create unattended-upgrades configuration
sudo tee /etc/apt/apt.conf.d/20auto-upgrades > /dev/null <<EOF
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
APT::Periodic::Download-Upgradeable-Packages "1";
APT::Periodic::AutocleanInterval "7";
EOF

# Configure unattended-upgrades for security updates only
sudo tee /etc/apt/apt.conf.d/50unattended-upgrades > /dev/null <<'EOF'
Unattended-Upgrade::Allowed-Origins {
    "${distro_id}:${distro_codename}";
    "${distro_id}:${distro_codename}-security";
    "${distro_id}ESMApps:${distro_codename}-apps-security";
    "${distro_id}ESM:${distro_codename}-infra-security";
};

Unattended-Upgrade::Package-Blacklist {
    // Add packages you don't want to auto-update here
};

Unattended-Upgrade::DevRelease "false";
Unattended-Upgrade::Remove-Unused-Dependencies "true";
Unattended-Upgrade::Automatic-Reboot "false";
Unattended-Upgrade::Automatic-Reboot-Time "02:00";
EOF

# Set up log rotation
echo "Configuring log rotation..."
sudo systemctl enable logrotate

# Create a security monitoring script
echo "Creating security monitoring script..."
sudo tee /usr/local/bin/security-check > /dev/null <<'EOF'
#!/bin/bash
# Simple security check script

echo "=== Security Status Check ==="
echo "Date: $(date)"
echo ""

echo "=== Firewall Status ==="
sudo ufw status
echo ""

echo "=== Fail2ban Status ==="
sudo fail2ban-client status
echo ""

echo "=== Recent Auth Failures ==="
sudo grep "authentication failure" /var/log/auth.log | tail -5
echo ""

echo "=== System Updates Available ==="
apt list --upgradable 2>/dev/null | grep -c upgradable || echo "No updates available"
echo ""

echo "=== Disk Usage ==="
df -h / | tail -1
echo ""

echo "=== Memory Usage ==="
free -h | grep Mem
echo ""
EOF

sudo chmod +x /usr/local/bin/security-check

# Set secure permissions on important files
echo "Setting secure file permissions..."
sudo chmod 600 /etc/ssh/sshd_config
sudo chmod 644 /etc/passwd
sudo chmod 600 /etc/shadow
sudo chmod 644 /etc/group

# Disable root login if not already disabled
echo "Ensuring root login is disabled..."
sudo passwd -l root

echo "Security setup completed successfully!"
echo ""
echo "Security features enabled:"
echo "- fail2ban for intrusion prevention"
echo "- Automatic security updates"
echo "- Log rotation"
echo "- Secure file permissions"
echo "- Root login disabled"
echo ""
echo "Run 'sudo security-check' to view security status"
