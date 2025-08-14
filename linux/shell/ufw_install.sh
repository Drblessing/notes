set -euo pipefail

# Fresh start + IPv6 on
sudo ufw --force reset
sudo sed -i 's/^#\?IPV6=.*/IPV6=yes/' /etc/default/ufw

# Open-by-default posture
sudo ufw default allow incoming
sudo ufw default allow outgoing

# Core
sudo ufw allow 22/tcp   comment 'SSH'
sudo ufw limit 22/tcp   # brute-force protection
sudo ufw allow 80/tcp   comment 'HTTP'
sudo ufw allow 443/tcp  comment 'HTTPS'

# Helper
block() { sudo ufw deny "$1" comment "$2"; }

# 🔒 Block sensitive/admin/RPC surfaces from the internet
block 8545/tcp "ETH JSON-RPC (block public)"
block 8551/tcp "ETH Engine API (block public)"
block 5052/tcp "Beacon REST API (block public)"
block 2375/tcp "Docker API (block public)"
block 2376/tcp "Docker API TLS (block public)"
block 5001/tcp "IPFS API (block public)"    
block 8332/tcp "Bitcoin RPC (block public)"
block 18081/tcp "Monero RPC (block public)"
block 2345/tcp "Filecoin Lotus RPC (block public)"

# Go live
sudo ufw --force enable
sudo ufw status numbered
