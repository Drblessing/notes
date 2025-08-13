# U="${SUDO_USER:-$USER}"
# H="$(getent passwd "$U" | cut -d: -f6 || echo "/home/$U")"
# KEY="${1:-./id_ed25519}"
# SSHD="${2:-$HOME/github/notes/configs/ssh/sshd_config}"
# # Copy SSH key
# sudo mkdir -p "$H/.ssh"
# sudo cp "$KEY" "$H/.ssh/id_ed25519"
# [[ -f "$KEY.pub" ]] && sudo cp "$KEY.pub" "$H/.ssh/id_ed25519.pub"
# sudo chown -R "$U:$U" "$H/.ssh"
# sudo chmod 700 "$H/.ssh"
# sudo chmod 600 "$H/.ssh/id_ed25519"
# # Copy sshd_config and restart
# sudo cp "$SSHD" /etc/ssh/sshd_config
# sudo systemctl restart ssh || sudo service ssh restart
# echo "Done. SSH key installed and service restarted."

# ssh setup for my home server


# Set variables for SSH key paths
KEY="${HOME}/.ssh/id_ed25519"
SSHD="${HOME}/github/notes/configs/.ssh/sshd_config"
PUBKEY=${HOME}/github/notes/configs/.ssh/id_ed25519.pub