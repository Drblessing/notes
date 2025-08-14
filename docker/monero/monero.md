# Monero

# Make the data dir

```bash
sudo mkdir -p /drive2/monero
sudo chown -R $USER:$USER /drive2/monero
sudo chmod -R 700 /drive2/monero
```

# Download the ban list

```bash
wget -O /drive2/monero/ban_list.txt https://raw.githubusercontent.com/Boog900/monero-ban-list/refs/heads/main/ban_list.txt
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
docker exec monerod monerod status
```
