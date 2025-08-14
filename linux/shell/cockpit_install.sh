sudo apt update
sudo apt install -y cockpit cockpit-pcp
sudo systemctl enable --now cockpit.socket
sudo ufw allow 9090/tcp