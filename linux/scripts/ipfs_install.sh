wget https://dist.ipfs.tech/kubo/v0.35.0/kubo_v0.35.0_linux-amd64.tar.gz
tar -xvzf kubo_v0.35.0_linux-amd64.tar.gz
cd kubo
sudo bash install.sh
sudo systemctl enable ipfs
sudo systemctl start ipfs
rm -rf kubo kubo_v0.35.0_linux-amd64.tar.gz
echo "IPFS installation completed successfully."