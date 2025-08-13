# An ssh setup script for my home server.
# It copies my private key onto the server, adds my public key to the authorized_keys, and configures sshd.

# Set variables for file paths
KEY="${HOME}/.ssh/id_ed25519"
SSHD="${HOME}/github/notes/configs/.ssh/sshd_config"
PUBKEY=${HOME}/github/notes/configs/.ssh/id_ed25519.pub

# Set variable for ubuntu server
UBUNTU_SERVER="192.168.7.186"
UBUNTU_USER="drblessing"

# Make sure the .ssh directory exists
ssh "$UBUNTU_USER@$UBUNTU_SERVER" "mkdir -p ~/.ssh && chmod 700 ~/.ssh"

# Copy ssh key
scp "$KEY" "$UBUNTU_USER@$UBUNTU_SERVER:~/.ssh/id_ed25519"
scp "$PUBKEY" "$UBUNTU_USER@$UBUNTU_SERVER:~/.ssh/id_ed25519.pub"

# Chmod
ssh "$UBUNTU_USER@$UBUNTU_SERVER" "chmod 600 ~/.ssh/id_ed25519 && chmod 644 ~/.ssh/id_ed25519.pub"

# Move local authorized keys file to server
scp "$HOME/github/notes/configs/.ssh/authorized_keys" "$UBUNTU_USER@$UBUNTU_SERVER:~/.ssh/authorized_keys"

# Sudo copy sshd_config
scp "$SSHD" "$UBUNTU_USER@$UBUNTU_SERVER:/tmp/sshd_config"
ssh -t "$UBUNTU_USER@$UBUNTU_SERVER" 'sudo mv /tmp/sshd_config /etc/ssh/sshd_config && sudo systemctl restart ssh'