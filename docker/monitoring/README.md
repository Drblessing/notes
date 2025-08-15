# Central Monitoring Stack 📊

One monitoring stack for ALL your services - Snowflake, Tor, IPFS, Bitcoin, Monero, and more!

## Setup

1. **Start the monitoring stack:**

```bash
cd monitoring
docker-compose up -d
```

2. **Access dashboards:**

- Grafana: http://localhost:3000 (admin/changeme)
- Prometheus: http://localhost:9090
- Node Exporter: http://localhost:9100/metrics

## Connecting Your Services

### For Services WITHOUT host networking

Add this to your service's docker-compose.yml:

```yaml
services:
  your-service:
    # ...your config...
    networks:
      - default
      - monitoring_network

networks:
  monitoring_network:
    external: true
```

### For Services WITH host networking (like Snowflake)

Services using `network_mode: host` can't join Docker networks, but Prometheus can still scrape them via `host.docker.internal` or `localhost`.

## Example Configurations

### Connecting IPFS

```yaml
# In your ipfs docker-compose.yml
services:
  ipfs:
    image: ipfs/go-ipfs:latest
    networks:
      - monitoring_network
    # ...rest of config...

networks:
  monitoring_network:
    external: true
```

Then uncomment the IPFS section in prometheus.yml and reload.

### Monitoring Snowflake

Since Snowflake doesn't expose metrics, monitor via logs:

```bash
# See connections helped
docker logs snowflake 2>&1 | grep -c "connected to relay"

# Watch live connections
docker logs -f snowflake 2>&1 | grep "Received"
```

## Adding Service Metrics to Prometheus

1. Edit `prometheus.yml`
2. Uncomment or add your service under `scrape_configs`
3. Reload Prometheus config without restart:

```bash
curl -X POST http://localhost:9090/-/reload
```

## Useful Grafana Dashboards

Import these dashboard IDs in Grafana (Dashboards → Import):

- **Node Exporter Full**: `1860` (System metrics)
- **Docker Containers**: `893`
- **Tor Relay**: `13179`
- **IPFS**: `10794`
- **Bitcoin Node**: `12840`

## Quick Commands

```bash
# Check what Prometheus is scraping
curl http://localhost:9090/api/v1/targets | jq

# Test if a service is reachable
docker exec prometheus wget -qO- http://node-exporter:9100/metrics | head

# Restart just monitoring stack
docker-compose restart

# Update monitoring images
docker-compose pull
docker-compose up -d
```

## Architecture Benefits

✅ **Independent**: Monitoring stays up during service updates  
✅ **Scalable**: Add unlimited services  
✅ **Flexible**: Each service manages its own lifecycle  
✅ **Persistent**: Metrics preserved across restarts

---

_One stack to monitor them all! 🔍_
