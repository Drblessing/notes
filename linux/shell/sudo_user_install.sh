# Install current user as sudo.
# I use this for convenience,
# since I only allow ssh connections into this machine,
# and have strict firewall and ssh settings.

# Add user to the sudo group
sudo usermod -aG sudo $USER

# Allow passwordless sudo
echo "$USER ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/010-$USER-nopasswd >/dev/null
sudo chmod 0440 /etc/sudoers.d/010-$USER-nopasswd

# Verify
sudo -k   # invalidate any cached auth
sudo true # should NOT prompt for a password now