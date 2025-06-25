#!/bin/bash

# System Maintenance Script
# Regular maintenance tasks for Ubuntu server

set -e

echo "Running system maintenance..."
echo "Date: $(date)"
echo "=============================="

# Update package lists
echo "Updating package lists..."
sudo apt update

# Show available upgrades
echo ""
echo "Available package upgrades:"
apt list --upgradable 2>/dev/null | grep -c upgradable || echo "No upgrades available"

# Clean package cache
echo ""
echo "Cleaning package cache..."
sudo apt autoremove -y
sudo apt autoclean

# Update locate database
echo ""
echo "Updating locate database..."
sudo updatedb 2>/dev/null || echo "locate not installed"

# Check disk usage
echo ""
echo "Disk usage check:"
df -h | grep -E '^/dev/' | awk '{print $5 " " $6}' | while read line; do
    usage=$(echo $line | awk '{print $1}' | sed 's/%//')
    partition=$(echo $line | awk '{print $2}')
    if [ $usage -gt 80 ]; then
        echo "Warning: $partition is $usage% full"
    else
        echo "OK: $partition is $usage% full"
    fi
done

# Check memory usage
echo ""
echo "Memory usage:"
free -h | grep Mem | awk '{printf "Memory: %s/%s (%.1f%%)\n", $3, $2, ($3/$2)*100}'

# Check system load
echo ""
echo "System load:"
uptime

# Check failed login attempts
echo ""
echo "Recent failed login attempts:"
sudo grep "authentication failure" /var/log/auth.log 2>/dev/null | tail -5 || echo "No recent failures found"

# Check service status
echo ""
echo "Critical service status:"
services=("ssh" "ufw" "fail2ban")
for service in "${services[@]}"; do
    if systemctl is-active --quiet $service; then
        echo "✓ $service is running"
    else
        echo "✗ $service is not running"
    fi
done

# Log rotation check
echo ""
echo "Log sizes:"
du -sh /var/log/* 2>/dev/null | sort -h | tail -5

echo ""
echo "Maintenance completed at $(date)"
