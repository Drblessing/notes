set -e

sudo ufw reset
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw allow 8080
sudo ufw allow 8443
sudo ufw allow 3000
sudo ufw allow 5000
sudo ufw allow 8000
sudo ufw disable
sudo ufw enable
sudo ufw status verbose