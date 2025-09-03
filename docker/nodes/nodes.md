# Nodes

My lightweight docker compose for running public goods infrastructure!

## Ethereum

### Storage

```bash
sudo mkdir -p /drive1/ethereum
sudo mkdir -p /drive1/ethereum/reth /drive1/ethereum/lighthouse
sudo chown -R $USER:$USER /drive1/ethereum
sudo chmod -R 700 /drive1/ethereum
openssl rand -hex 32 | sudo tee /drive1/ethereum/jwt.hex >/dev/null
sudo chmod 600 /drive1/ethereum/jwt.hex
```

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

### Cookie Authentication

Bitcoin RPC uses cookie auth by default. The cookie is created at /drive2/bitcoin/.cookie (host) and /home/bitcoin/.bitcoin/.cookie (container).

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
docker compose up -d
```

#### TODO

- Add Monero Dashboard to this
