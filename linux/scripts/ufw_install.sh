# ufw setup script

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
sudo ufw allow 9090
sudo ufw allow 32400/tcp comment "Allow Plex Media Server"
sudo ufw allow 32400/udp comment "Allow Plex Media Server"
sudo ufw allow 1900/udp comment "Allow Plex discovery"
sudo ufw allow 5353/udp comment "Allow mDNS for Plex"
# Bitcoin node ports
sudo ufw allow 8333 comment "Allow Bitcoin node"
# IPFS ports
sudo ufw allow 4001 comment "Allow IPFS swarm port"
sudo ufw allow 5001 comment "Allow IPFS API port"
sudo ufw allow 8080 comment "Allow IPFS gateway port"
# IPFS WebUI port
sudo ufw allow 5002 comment "Allow IPFS WebUI port"
# Monero node ports
sudo ufw allow 18080 comment "Allow Monero node"
sudo ufw allow 18081 comment "Allow Monero RPC port"
# Ethereum node ports
sudo ufw allow 30303 comment "Allow Ethereum node"
sudo ufw allow 8545 comment "Allow Ethereum RPC port"
# Arweave node ports
sudo ufw allow 1984 comment "Allow Arweave node"
# Glances
sudo ufw allow 61208 comment "Allow Glances"

sudo ufw limit ssh
sudo ufw disable
sudo ufw enable
sudo ufw status verbose