# Simple APT package installer for Ubuntu servers
echo "Starting APT package installation..."
sudo apt update
xargs -r sudo apt install -y < <(grep -hvE '^\s*($|#)' ~/github/notes/linux/packages/apt_packages.txt)
sudo apt autoremove -y
sudo apt autoclean -y
echo "APT installation complete ✅"