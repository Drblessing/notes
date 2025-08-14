#!/usr/bin/env bash
# forward_all_to_home.sh — forward ALL TCP/UDP ports from VPS -> HOME over Tailscale
# Usage: sudo bash forward_all_to_home.sh <HOME_TAILSCALE_IP>
set -euo pipefail

HOME_TS="${1:?Usage: sudo bash $0 <HOME_TAILSCALE_IP>}"
IFACE="$(ip route get 1.1.1.1 | awk '{print $5; exit}')"   # VPS public NIC (e.g., eth0)

echo "[*] Forwarding ALL ports from $IFACE -> $HOME_TS via tailscale0"

# 1) Enable IP forwarding (and persist)
echo 'net.ipv4.ip_forward=1' | sudo tee /etc/sysctl.d/99-ipforward.conf >/dev/null
sudo sysctl -p /etc/sysctl.d/99-ipforward.conf

# 2) NAT: ensure replies leave the VPS correctly (internet & Tailscale)
sudo iptables -t nat -C POSTROUTING -o "$IFACE" -j MASQUERADE 2>/dev/null || \
sudo iptables -t nat -A POSTROUTING -o "$IFACE" -j MASQUERADE
sudo iptables -t nat -C POSTROUTING -o tailscale0 -j MASQUERADE 2>/dev/null || \
sudo iptables -t nat -A POSTROUTING -o tailscale0 -j MASQUERADE

# 3) Create/refresh a dedicated DNAT chain and hook it into PREROUTING
sudo iptables -t nat -N TS_DNAT_ALL 2>/dev/null || true
sudo iptables -t nat -F TS_DNAT_ALL
sudo iptables -t nat -C PREROUTING -i "$IFACE" -j TS_DNAT_ALL 2>/dev/null || \
sudo iptables -t nat -A PREROUTING -i "$IFACE" -j TS_DNAT_ALL

# 4) DNAT *all* TCP+UDP ports to your home Tailscale IP
sudo iptables -t nat -A TS_DNAT_ALL -p tcp --dport 1:65535 -j DNAT --to-destination "$HOME_TS"
sudo iptables -t nat -A TS_DNAT_ALL -p udp --dport 1:65535 -j DNAT --to-destination "$HOME_TS"

# 5) Allow forwarding between IFACE <-> tailscale0
sudo iptables -C FORWARD -i "$IFACE" -o tailscale0 -j ACCEPT 2>/dev/null || \
sudo iptables -A FORWARD -i "$IFACE" -o tailscale0 -j ACCEPT
sudo iptables -C FORWARD -i tailscale0 -o "$IFACE" -m state --state ESTABLISHED,RELATED -j ACCEPT 2>/dev/null || \
sudo iptables -A FORWARD -i tailscale0 -o "$IFACE" -m state --state ESTABLISHED,RELATED -j ACCEPT

# 6) (Optional) make rules persistent across reboots
if ! command -v netfilter-persistent >/dev/null 2>&1; then
  sudo apt-get update -y && sudo apt-get install -y netfilter-persistent >/dev/null
fi
sudo netfilter-persistent save

echo "[✓] All ports are now forwarded to $HOME_TS"