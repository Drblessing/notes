# An ssh setup script for my home server.
# It copies my private key onto the server, adds my public key to the authorized_keys, and configures sshd.

# Set variables for file paths
KEY="${HOME}/.ssh/id_ed25519"
SSHD="${HOME}/github/notes/configs/.ssh/sshd_config"
PUBKEY=${HOME}/github/notes/configs/.ssh/id_ed25519.pub

# Set variable for ubuntu server
UBUNTU_SERVER="192.168.7.186"
UBUNTU_USER="drblessing"

# Copy ssh key
scp "$KEY" "$UBUNTU_USER@$UBUNTU_SERVER:~/.ssh/id_ed25519"
scp "$PUBKEY" "$UBUNTU_USER@$UBUNTU_SERVER:~/.ssh/id_ed25519.pub"