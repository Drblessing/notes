# ufw_install.sh  
# An opinionated UFW baseline

# Reset
sudo ufw --force reset

# Defaults
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Helper to keep the rule list readable
allow() { sudo ufw allow "$1" comment "$2" ; }

# Core access
allow ssh          "OpenSSH"
sudo ufw limit ssh                       # brute-force protection

allow http         "HTTP"
allow https        "HTTPS"

# Generic services
for p in 8443 3000 5000 8000 9090; do
    allow "$p"     "Generic service $p"
done

# Public goods
allow 8333         "Bitcoin node"
allow 4001         "IPFS swarm"
allow 8080         "IPFS gateway"
allow 5002         "IPFS WebUI"
allow 18080        "Monero node"
allow 30303        "Ethereum node"
allow 1984         "Arweave node"
allow 9001         "Tor relay"
allow 1347         "Filecoin"
allow 2345         "Filecoin 2"
allow 1234         "Filecoin 3"
allow 9100         "Node Exporter"
allow 9443         "Generic service 9443"


# ── 6. Enable & show status ─────────────────────────────────────────────────────
sudo ufw --force enable
sudo ufw status verbose