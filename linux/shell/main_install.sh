# Full Linux setup: APT packages, Snap packages, and dotfiles
echo "Starting full Linux setup..."
# Run APT package installer
echo "Running APT package installer..."
bash ~/github/notes/linux/shell/apt_install.sh
# Install Docker
echo "Installing Docker..."
bash ~/github/notes/linux/shell/docker_install.sh
# Install Cloudflare Warp and Cloudflared
echo "Installing Cloudflare Warp and Cloudflared..."
bash ~/github/notes/linux/shell/cloudflare_install.sh
# Install Fastfetch
echo "Installing Fastfetch..."
bash ~/github/notes/linux/shell/fastfetch_install.sh
# Install dotfiles
echo "Installing dotfiles..."
bash ~/github/notes/shell/dotfiles_install.sh
# Set server timezone to Detroit
echo "Setting server timezone to Detroit..."
sudo timedatectl set-timezone America/Detroit
echo "Full Linux setup complete ✅"
echo "You may want to restart your shell or run: source ~/.bashrc"