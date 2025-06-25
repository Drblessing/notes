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

## Directory Structure

```
linux/
├── README.md                 # This file
├── SETUP_GUIDE.md           # Detailed setup guide
├── configs/                 # Configuration files
│   ├── sshd_config         # SSH server config
│   ├── limits.conf         # System limits
│   ├── sysctl.conf         # Kernel parameters
│   ├── dotfiles/           # Shell configuration
│   ├── ufw/                # Firewall rules
│   └── fail2ban/           # Intrusion prevention
├── packages/               # Package lists
│   ├── essential.txt       # Core system packages
│   ├── development.txt     # Development tools
│   └── security.txt        # Security packages
└── scripts/               # Installation scripts
    ├── main_install.sh     # Main installation script
    ├── server_setup.sh     # Remote bootstrap script
    ├── firewall_setup.sh   # UFW configuration
    ├── security_setup.sh   # Security hardening
    ├── dotfiles_install.sh # Shell configuration
    ├── monitoring_setup.sh # System monitoring
    └── maintenance.sh      # Regular maintenance
```

## Post-Installation

### SSH Key Setup

1. Copy your SSH public key to the server:

   ```bash
   ssh-copy-id user@server-ip
   ```

2. Or manually add it:

   ```bash
   mkdir -p ~/.ssh
   echo "your-public-key-here" >> ~/.ssh/authorized_keys
   chmod 600 ~/.ssh/authorized_keys
   ```

3. Test SSH key authentication before disconnecting!

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

## Contributing

To add new features or configurations:

1. Add packages to appropriate `.txt` files
2. Update configuration files in `configs/`
3. Modify installation scripts in `scripts/`
4. Test on a fresh Ubuntu installation
5. Update this documentation

## Security Notes

⚠️ **Important Security Reminders:**

- SSH password authentication is disabled
- Only SSH key authentication works
- Make sure you have SSH keys configured before disconnecting
- The server is configured to be very restrictive by default
- Always test changes in a safe environment first

This setup prioritizes security and minimalism while providing a productive development environment. All configurations can be customized based on your specific needs.
