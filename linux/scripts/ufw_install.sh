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
sudo ufw allow 32400/tcp comment "Allow Plex Media Server"
sudo ufw allow 32400/udp comment "Allow Plex Media Server"
sudo ufw allow 1900/udp comment "Allow Plex discovery"
sudo ufw allow 5353/udp comment "Allow mDNS for Plex"
sudo ufw limit ssh
sudo ufw disable
sudo ufw enable
sudo ufw status verbose