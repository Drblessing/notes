# Main comprehensive installation script for home server.

# Passwordless sudo user installation script
/bin/bash ~/github/notes/linux/shell/sudo_user_install.sh

# Run apt installation script
/bin/bash ~/github/notes/linux/shell/apt_install.sh

# Run app installation script
/bin/bash ~/github/notes/linux/shell/app_install.sh

# Run docker installation script
/bin/bash ~/github/notes/linux/shell/docker_install.sh

# Miscellaneous tasks

# Cockpit
sudo systemctl enable --now cockpit.socket

# Docker 
sudo groupadd docker
sudo usermod -aG docker $USER

# Portainer
sudo docker volume create portainer_data
sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:lts

# Mounted drive at /drive2 ownership
sudo chown -R $USER:$USER /drive2
sudo chmod -R 755 /drive2

# Dotfiles installation
/bin/bash ~/github/notes/shell/dotfiles_install.sh

# Benv installation
/bin/bash ~/github/notes/shell/benv_install.sh

echo "Installation complete!" 
echo "Now run ssh_setup.sh on your personal computer."