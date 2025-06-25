# Linux Server Setup Guide

This guide provides a complete setup for new Ubuntu servers with security hardening, essential tools, and my preferred configurations.

## Quick Start

### Option 1: Remote Bootstrap (Recommended)

Run this single command on a fresh Ubuntu server:

```bash
curl -fsSL https://raw.githubusercontent.com/drblessing/notes/main/linux/scripts/server_setup.sh | bash
```

### Option 2: Manual Setup

If you prefer to review everything first:

```bash
# 1. Clone the repository
git clone https://github.com/drblessing/notes.git ~/Github/notes

# 2. Make scripts executable
chmod +x ~/Github/notes/linux/scripts/*.sh

# 3. Run the main installation
bash ~/Github/notes/linux/scripts/main_install.sh
```

## What Gets Installed & Configured

### Essential Packages

- System utilities: curl, wget, git, vim, nano, htop, tree, unzip
- Build tools: build-essential, software-properties-common
- Security tools: ufw, fail2ban, unattended-upgrades
- Monitoring: neofetch, fastfetch

### Development Tools

- Python 3 with pip and venv
- Node.js with npm
- Go programming language
- Docker and docker-compose
- Git LFS
- jq (JSON processor)
- tmux and screen

### Security Configuration

- **SSH Hardening**:
  - Password authentication disabled
  - Key-only authentication
  - Rate limiting enabled
  - Root login disabled
- **Firewall**: UFW configured with restrictive rules
- **Intrusion Prevention**: fail2ban monitoring SSH
- **Automatic Updates**: Security patches auto-installed
- **File Permissions**: Secure defaults applied

### Shell Environment

- Custom bash configuration with useful aliases
- PATH configured to include ~/Github/notes/bin
- Python3 set as default python
- Git configuration linked from main configs
- Custom prompt with emoji 😃

## Post-Installation

### VSCode Setup

From your local machine, connect to the server using VSCode with the Remote - SSH extension:

- Open the command palette and select "Remote-SSH: Connect to Host...".
- Enter your server's SSH connection string: `user@server-ip`.
- Once connected, you can open the terminal and start using the server directly from VS.Code.

### SSH Key Setup

Copy your SSH public key to the server:

```bash
ssh-copy-id user@server-ip
```

### Verification Commands

```bash
# Check firewall status
sudo ufw status verbose

# Check fail2ban status
sudo fail2ban-client status

# Run system monitor
sysmon

# Run security check
sudo security-check

# Check service status
systemctl status ssh ufw fail2ban
```

### Useful Aliases

The setup includes these helpful aliases:

- `u` - Update and upgrade packages
- `c` - Clear terminal
- `ll` - Detailed file listing
- `sysmon` - System monitoring overview
- `logmon` - Log monitoring
- `netmon` - Network monitoring
- `ports` - Show listening ports

## Security Features

### Firewall (UFW)

- Default deny incoming
- SSH allowed with rate limiting
- Minimal attack surface

### Intrusion Prevention (fail2ban)

- SSH brute force protection
- Automatic IP banning
- Email notifications (configurable)

### Automatic Updates

- Security patches installed automatically
- System reboot handling
- Package blacklist support

### System Hardening

- Secure SSH configuration
- Kernel security parameters
- File system protections
- Process limits configured

## Maintenance

### Regular Tasks

```bash
# Run maintenance script
bash ~/Github/notes/linux/scripts/maintenance.sh

# Update system
sudo apt update && sudo apt upgrade

# Check security status
sudo security-check

# Monitor system resources
sysmon
```

### Log Monitoring

Important logs to monitor:

- `/var/log/auth.log` - Authentication attempts
- `/var/log/syslog` - System messages
- `/var/log/fail2ban.log` - Intrusion attempts
- `journalctl -f` - Real-time system logs

## Customization

### Adding Packages

Edit the package files in `packages/` and re-run:

```bash
sudo xargs apt install -y < ~/Github/notes/linux/packages/your-packages.txt
```

### Firewall Rules

Add custom rules in `configs/ufw/rules.conf` or manually:

```bash
sudo ufw allow 8080/tcp  # Example: allow port 8080
```

### Environment Variables

Add to `configs/dotfiles/.bashrc` or create `~/.bash_local`:

```bash
export MY_CUSTOM_VAR="value"
```

## Troubleshooting

### SSH Access Issues

If you lose SSH access:

1. Use console/VNC access if available
2. Check UFW rules: `sudo ufw status`
3. Temporarily allow password auth if needed
4. Check SSH service: `sudo systemctl status ssh`

### Service Issues

```bash
# Check service status
sudo systemctl status servicename

# View service logs
sudo journalctl -u servicename -f

# Restart service
sudo systemctl restart servicename
```

### Firewall Issues

```bash
# Disable UFW temporarily
sudo ufw disable

# Reset UFW rules
sudo ufw --force reset

# Re-run firewall setup
bash ~/Github/notes/linux/scripts/firewall_setup.sh
```
