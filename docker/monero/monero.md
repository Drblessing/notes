# Monero

# Make the data dir

```bash
sudo mkdir -p /drive2/monero
sudo chown -R $USER:$USER /drive2/monero
sudo chmod -R 700 /drive2/monero
```

# Run the monero node

```bash
docker compose up -d
```

# Check logs

```bash
docker compose logs -f
```

# Check sync status

```bash
docker exec monero-node monero-blockchain-stats
```
