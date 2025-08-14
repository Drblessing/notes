# Bitcoin

# Make the data dir

```bash
sudo mkdir -p /drive2/bitcoin
sudo chown -R $USER:$USER /drive2/bitcoin
sudo chmod -R 700 /drive2/bitcoin
```

# Run the bitcoin node

```bash
docker compose up -d
```

# Verify

```bash
docker compose ps
docker compose logs -f
docker exec bitcoin bitcoin-cli -datadir=/home/bitcoin/.bitcoin getblockchaininfo
docker exec bitcoin bitcoin-cli -datadir=/home/bitcoin/.bitcoin getblockcount
```
