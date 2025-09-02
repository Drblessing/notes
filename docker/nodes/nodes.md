# Nodes

My lightweight docker compose for running public goods infrastructure!

## Monero

### Storage

```bash
sudo mkdir -p /drive2/monero
sudo chown -R $USER:$USER /drive2/monero
sudo chmod -R 700 /drive2/monero
```

### Check Status

```bash
docker exec monero monerod status
```

### Check Logs

```bash
docker logs monero
```

## Bitcoin

### Storage

```bash
sudo mkdir -p /drive2/bitcoin
sudo chown -R $USER:$USER /drive2/bitcoin
sudo chmod -R 700 /drive2/bitcoin
```

### Environment Variables

```bash
export BITCOIN_RPC_USER=myuser
export BITCOIN_RPC_PASSWORD=mypass
```

### Status

```bash
docker compose ps
docker compose logs -f
docker logs bitcoin
docker exec bitcoin bitcoin-cli getblockchaininfo
docker exec bitcoin bitcoin-cli getblockcount
```

## Run

```bash
export BITCOIN_RPC_USER=myuser
export BITCOIN_RPC_PASSWORD=mypass
docker compose up -d
```
