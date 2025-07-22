# Install and fix docker for snap installation

# Install if not already installed
sudo snap install --ignore-running docker

# Fix permissions for docker group
sudo groupadd docker || true
sudo usermod -aG docker $USER || true

# Reload group memberships
newgrp docker || true

# Verify docker installation without sudo 
docker run hello-world