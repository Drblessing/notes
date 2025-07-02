# ufw_install.sh – opinionated UFW baseline + full Plex port set

# ── 1. Reset & sane defaults ────────────────────────────────────────────────────
sudo ufw --force reset
sudo ufw default deny incoming
sudo ufw default allow outgoing

# helper to keep the rule list readable
allow() { sudo ufw allow "$1" comment "$2" ; }

# ── 2. Core access ──────────────────────────────────────────────────────────────
allow ssh          "OpenSSH"
sudo ufw limit ssh                       # brute-force protection

allow http         "HTTP"
allow https        "HTTPS"

# ── 3. Generic service ports you mentioned ─────────────────────────────────────
for p in 8443 3000 5000 8000 9090; do
    allow "$p"     "Generic service $p"
done

# ── 4. Plex Media Server (complete set, incl. GDM & DLNA) ──────────────────────
allow 32400        "Plex Web"
allow 32469        "Plex DLNA"
allow 3005         "Plex Companion"
allow 8324         "Plex Companion (Roku)"
allow 1900         "DLNA discovery"
allow 5353         "mDNS / Bonjour"
allow 32410:32414  "Plex GDM discovery"

# ── 5. Bitcoin / IPFS / Monero / Ethereum / Arweave / Glances ──────────────────
allow 8333         "Bitcoin node"

allow 4001         "IPFS swarm"
# allow 5001         "IPFS API"
allow 8080         "IPFS gateway"
allow 5002         "IPFS WebUI"

allow 18080        "Monero node"
allow 18081        "Monero RPC"

allow 30303        "Ethereum node"
# allow 8545         "Ethereum RPC"

allow 1984         "Arweave node"

allow 61208        "Glances"

# ── 6. Enable & show status ─────────────────────────────────────────────────────
sudo ufw reload 
sudo ufw status verbose