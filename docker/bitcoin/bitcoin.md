# Bitcoin

# Make the data dir

```bash
sudo mkdir -p /drive2/bitcoin
sudo chown -R $USER:$USER /drive2/bitcoin
sudo chmod -R 700 /drive2/bitcoin
```

# Run the bitcoin node

```bash
docker-compose up -d
```
