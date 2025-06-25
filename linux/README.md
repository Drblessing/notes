# Linux Server Setup

Configuration files and scripts for setting up new Ubuntu servers with my preferred configurations, including security hardening, SSH key management, and essential packages.

## Quick Setup

For a complete server setup, run:

```bash
curl -fsSL https://raw.githubusercontent.com/drblessing/notes/main/linux/scripts/server_setup.sh | bash
```

## Or for manual installation:

```bash
# 1. Clone the notes repository
git clone https://github.com/drblessing/notes.git ~/Github/notes

# 2. Run the main installation script
bash ~/Github/notes/linux/scripts/main_install.sh
```

## Installation Steps

The setup process includes:

1. **System Updates** - Update package manager and install security updates
2. **Essential Packages** - Install core development and security tools
3. **SSH Configuration** - Setup SSH keys and harden SSH daemon
4. **Firewall Setup** - Configure UFW with secure defaults
5. **Dotfiles** - Install bash/zsh configuration files
6. **Security Hardening** - Apply basic security configurations
7. **Development Environment** - Setup Python, Node.js, and Git

## Manual Steps

Some steps require manual intervention:

- **SSH Keys**: Copy your private key to `~/.ssh/id_ed25519` (not included in repo for security)
- **UFW Rules**: Review and customize firewall rules for your specific needs
- **User Permissions**: Add user to appropriate groups (sudo, docker, etc.)

## Security Features

- **SSH Hardening**: Disable password auth, configure key-only access
- **UFW Firewall**: Enable with secure defaults (SSH, HTTP, HTTPS)
- **Fail2ban**: Protect against brute force attacks
- **Automatic Updates**: Configure unattended security updates
- **User Permissions**: Proper sudo configuration

## Customization

Edit the following files to customize for your environment:

- `packages/apt_packages.txt` - Add/remove packages
- `configs/security/ufw_rules.conf` - Modify firewall rules
- `configs/dotfiles/.bashrc` - Customize shell environment
- `configs/ssh/config` - Add your server configurations
