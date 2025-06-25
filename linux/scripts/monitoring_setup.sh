#!/bin/bash

# Monitoring Setup Script
# Installs and configures system monitoring tools

set -e

echo "Setting up system monitoring..."

# Install monitoring packages if not already installed
echo "Installing monitoring packages..."
MONITORING_PACKAGES="htop neofetch fastfetch iotop nethogs"
for package in $MONITORING_PACKAGES; do
    if ! dpkg -l | grep -q "^ii  $package " 2>/dev/null; then
        echo "Installing $package..."
        sudo apt update
        sudo apt install -y $package 2>/dev/null || echo "Warning: Could not install $package"
    fi
done

# Create a system monitoring script
echo "Creating system monitoring script..."
sudo tee /usr/local/bin/sysmon > /dev/null <<'EOF'
#!/bin/bash
# System monitoring script

echo "=== System Monitor ==="
echo "Date: $(date)"
echo ""

echo "=== System Information ==="
if command -v neofetch &> /dev/null; then
    neofetch --disable theme icons
elif command -v fastfetch &> /dev/null; then
    fastfetch
else
    echo "Hostname: $(hostname)"
    echo "Uptime: $(uptime -p)"
    echo "Kernel: $(uname -r)"
fi
echo ""

echo "=== CPU Usage ==="
top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print "CPU Usage: " 100 - $1 "%"}'
echo ""

echo "=== Memory Usage ==="
free -h
echo ""

echo "=== Disk Usage ==="
df -h | grep -E '^/dev/'
echo ""

echo "=== Network Connections ==="
ss -tuln | head -10
echo ""

echo "=== Top Processes by CPU ==="
ps aux --sort=-%cpu | head -6
echo ""

echo "=== Top Processes by Memory ==="
ps aux --sort=-%mem | head -6
echo ""

echo "=== Recent Logins ==="
last -n 5
echo ""

echo "=== System Load ==="
uptime
echo ""
EOF

sudo chmod +x /usr/local/bin/sysmon

# Create a simple log monitoring script
echo "Creating log monitoring script..."
sudo tee /usr/local/bin/logmon > /dev/null <<'EOF'
#!/bin/bash
# Log monitoring script

echo "=== Log Monitor ==="
echo "Date: $(date)"
echo ""

echo "=== Recent System Errors ==="
sudo journalctl -p err --since "1 hour ago" --no-pager | tail -10
echo ""

echo "=== Recent SSH Attempts ==="
sudo grep "sshd" /var/log/auth.log | tail -10
echo ""

echo "=== Disk Space Warnings ==="
df -h | awk '$5 > 80 {print $0}' | head -5
echo ""

echo "=== Memory Warnings ==="
free | awk 'NR==2{printf "Memory Usage: %s/%s (%.2f%%)\n", $3,$2,$3*100/$2 }'
echo ""
EOF

sudo chmod +x /usr/local/bin/logmon

# Create a network monitoring script
echo "Creating network monitoring script..."
sudo tee /usr/local/bin/netmon > /dev/null <<'EOF'
#!/bin/bash
# Network monitoring script

echo "=== Network Monitor ==="
echo "Date: $(date)"
echo ""

echo "=== Network Interfaces ==="
ip addr show | grep -E "^[0-9]+:|inet "
echo ""

echo "=== Routing Table ==="
ip route
echo ""

echo "=== Active Connections ==="
ss -tuln
echo ""

echo "=== Firewall Status ==="
sudo ufw status verbose 2>/dev/null || echo "UFW not available"
echo ""

echo "=== Network Statistics ==="
cat /proc/net/dev | head -3
echo ""
EOF

sudo chmod +x /usr/local/bin/netmon

# Set up a simple monitoring cron job (optional)
echo "Setting up monitoring cron job..."
(crontab -l 2>/dev/null; echo "# System monitoring - runs every hour") | crontab -
(crontab -l 2>/dev/null; echo "0 * * * * /usr/local/bin/sysmon > /tmp/sysmon.log 2>&1") | crontab -

# Create monitoring aliases
echo "Adding monitoring aliases to bashrc..."
ALIAS_FILE=~/.bash_aliases
echo "# Monitoring aliases" >> "$ALIAS_FILE"
echo "alias sysmon='/usr/local/bin/sysmon'" >> "$ALIAS_FILE"
echo "alias logmon='/usr/local/bin/logmon'" >> "$ALIAS_FILE"
echo "alias netmon='/usr/local/bin/netmon'" >> "$ALIAS_FILE"
echo "alias ports='sudo ss -tuln'" >> "$ALIAS_FILE"
echo "alias procs='ps aux --sort=-%cpu'" >> "$ALIAS_FILE"

echo "Monitoring setup completed successfully!"
echo ""
echo "Available monitoring commands:"
echo "- sysmon    : System overview"
echo "- logmon    : Log monitoring"
echo "- netmon    : Network monitoring"
echo "- htop      : Interactive process viewer"
echo "- ports     : Show listening ports"
echo "- procs     : Show processes by CPU usage"
echo ""
echo "Monitoring runs automatically every hour and logs to /tmp/sysmon.log"
