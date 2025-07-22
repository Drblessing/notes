# Install and fix docker for snap installation
# Install if not already installed
sudo snap install --ignore-running docker

# Fix permissions for docker group
sudo snap connect docker:home

# Verify docker installation
docker run hello-world