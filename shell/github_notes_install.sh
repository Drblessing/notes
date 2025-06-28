# Prompts user to cp the ssh private key for Github access
# from a client machine with the private key already set up. 

# Prompt user to cp the ssh private key 
echo "To enable GitHub access, please copy your SSH private key to this machine."
echo "For example, from your client machine, run:"
echo "scp ~/.ssh/id_ed25519 user@server:~/.ssh/id_ed25519"
echo "If you don't have access to the server yet, use ssh-copy-id."
echo "ssh-copy-id user@server"
echo "This should prompt you for your password, and then you can modify the sshd_config file"
echo "to force key-based authentication."
echo "If this is a personal device, like a new macbook, you have to manually copy they key."
read -p "Press Enter once you have copied the key..."
echo ""
echo "Testing SSH connection to GitHub..."
ssh -T git@github.com