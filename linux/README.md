# Linux Server Setup

Configuration files and scripts for setting up new Ubuntu servers with my preferred configurations, including security hardening, SSH key management, and essential packages.

## Quick Setup

For a complete server setup, run:

```bash
curl -fsSL https://raw.githubusercontent.com/drblessing/notes/main/linux/scripts/server_setup.sh | bash
```

`ssh -i /Users/danielblessing/.ssh/id_ed25519 'drblessing@192.168.7.57'`

Or for manual installation:

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

## File Structure

```
linux/
├── README.md                      # This file
├── scripts/                       # Installation and setup scripts
│   ├── main_install.sh           # Main orchestration script
│   ├── server_setup.sh           # Remote installation script
│   ├── package_install.sh        # Package installation
│   ├── dotfiles_install.sh       # Dotfiles setup
│   ├── ssh_setup.sh              # SSH configuration
│   ├── security_hardening.sh     # Security configurations
│   └── firewall_setup.sh         # UFW firewall setup
├── configs/                       # Configuration files
│   ├── dotfiles/                  # Shell configuration files
│   │   ├── .bashrc               # Bash configuration
│   │   ├── .bash_profile         # Bash login profile
│   │   ├── .zshrc                # Zsh configuration (if installed)
│   │   └── .gitconfig            # Git configuration
│   ├── ssh/                       # SSH configuration
│   │   ├── config                # SSH client config
│   │   ├── sshd_config           # SSH daemon config
│   │   └── authorized_keys       # Public keys (template)
│   └── security/                  # Security configurations
│       ├── ufw_rules.conf        # UFW firewall rules
│       ├── fail2ban.conf         # Fail2ban configuration
│       └── sysctl.conf           # Kernel parameters
└── packages/                      # Package lists
    ├── apt_packages.txt          # APT packages to install
    ├── snap_packages.txt         # Snap packages to install
    └── python_packages.txt       # Python packages to install
```

## Security Features

- **SSH Hardening**: Disable password auth, configure key-only access
- **UFW Firewall**: Enable with secure defaults (SSH, HTTP, HTTPS)
- **Fail2ban**: Protect against brute force attacks
- **Automatic Updates**: Configure unattended security updates
- **User Permissions**: Proper sudo configuration

## Compatibility

Tested on:

- Ubuntu 20.04 LTS
- Ubuntu 22.04 LTS
- Ubuntu 24.04 LTS
- Debian 11/12 (should work with minor modifications)

## Customization

Edit the following files to customize for your environment:

- `packages/apt_packages.txt` - Add/remove packages
- `configs/security/ufw_rules.conf` - Modify firewall rules
- `configs/dotfiles/.bashrc` - Customize shell environment
- `configs/ssh/config` - Add your server configurations
