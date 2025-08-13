Run this

```
#!/bin/bash
# port_forward.sh
# Forwards multiple public ports on VPS to your home server

# Home server's private (VPN/Tailscale) IP
TARGET_IP="100.107.253.41"

# Enable IP forwarding
sudo sysctl -w net.ipv4.ip_forward=1
sudo tee -a /etc/sysctl.conf <<< "net.ipv4.ip_forward=1"

# List of ports to forward (TCP and UDP where relevant)
PORTS=(
  8333     # Bitcoin node
  4001     # IPFS swarm
  8080     # IPFS gateway
  5002     # IPFS WebUI
  18080    # Monero node
  30303    # Ethereum node
  1984     # Arweave node
  9001     # Tor relay
  1347     # Filecoin
  2345     # Filecoin 2
  1234     # Filecoin 3
  9100     # Node Exporter
  9443     # Generic service 9443
  8443     # Generic service 8443
  3000     # Generic service 3000
  5000     # Generic service 5000
  8000     # Generic service 8000
  9090     # Generic service 9090
)

# Flush old rules
sudo iptables -t nat -F
sudo iptables -F

# Forward each port
for PORT in "${PORTS[@]}"; do
    # TCP forward
    sudo iptables -t nat -A PREROUTING -p tcp --dport $PORT -j DNAT --to-destination ${TARGET_IP}:$PORT
    sudo iptables -A FORWARD -p tcp -d ${TARGET_IP} --dport $PORT -j ACCEPT

    # UDP forward (optional — safe to include)
    sudo iptables -t nat -A PREROUTING -p udp --dport $PORT -j DNAT --to-destination ${TARGET_IP}:$PORT
    sudo iptables -A FORWARD -p udp -d ${TARGET_IP} --dport $PORT -j ACCEPT
done

# Save iptables rules (Debian/Ubuntu)
sudo apt install -y iptables-persistent
sudo netfilter-persistent save

echo "Port forwarding rules applied to forward ports to $TARGET_IP"
```
