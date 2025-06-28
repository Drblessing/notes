# Prompts user to cp the ssh private key for Github access
# from a client machine with the private key already set up. 

# Installation
echo "Please copy your ssh pub/priv key to this machine."
echo "For example, run:"
echo ""
echo "scp ~/.ssh/id_ed25519 user@server:~/.ssh/id_ed25519"
echo ""
echo "ssh-copy-id user@server"
echo ""
read -p "Press Enter once you have copied the key..."
echo ""

# Set correct permissions for the SSH key
mkdir -p ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
chmod 700 ~/.ssh

# Testing
echo "Testing SSH connection to GitHub..."
ssh -T git@github.com