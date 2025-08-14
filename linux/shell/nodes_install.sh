# Install public goods infrastructure.

# Ethereum node
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/coincashew/EthPillar/main/install.sh)"
# ethpillar

# Monero Node.
# Stop any existing nodes. 
docker stop monerod 2>/dev/null && docker rm monerod 2>/dev/null
# Create the data directory.
sudo mkdir -p /drive2/monero
# Own the data directory.
sudo chown -R 1000:1000 /drive2/monero
# Start the node.
docker run -d --name monerod --restart unless-stopped -p 18080:18080 -p 127.0.0.1:18081:18081 -v /drive2/monero:/home/monero/.bitmonero sethsimmons/simple-monerod:latest --p2p-bind-ip=0.0.0.0 --p2p-bind-port=18080 --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18081 --confirm-external-bind --no-igd 

# Bitcoin Node. 
# Stop any existing nodes.
docker stop bitcoind 2>/dev/null && docker rm bitcoind 2>/dev/null
# Create the data directory.
sudo mkdir -p /drive2/bitcoin
# Own the data directory.
sudo chown -R 1000:1000 /drive2/bitcoin
# Start the node.
docker run -d --name bitcoind --restart unless-stopped -p 8333:8333 -p 127.0.0.1:8332:8332 -v /drive2/bitcoin:/home/bitcoin/.bitcoin ruimarinho/bitcoin-core:latest -printtoconsole -rpcallowip=127.0.0.1/32 -rpcbind=0.0.0.0 -rpcport=8332