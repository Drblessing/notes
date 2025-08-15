# Snowflake Proxy Docker Setup

## Overview

This Docker Compose setup runs a Snowflake proxy to help users in censored regions access the Tor network.

## Quick Start

1. Start the proxy:

```bash
docker compose up -d
```

2. Check logs:

```bash
docker compose logs -f snowflake-proxy
```

3. Stop the proxy:

```bash
docker compose down
```

## Configuration

The proxy runs with the following default settings:

- Relay: wss://snowflake.bamsoftware.com/
- STUN server: stun.l.google.com:19302
- Network mode: host (required for NAT traversal)

## Notes

- The proxy uses host networking to properly handle NAT traversal
- Logs are limited to 10MB with 3 file rotations
- The container will automatically restart unless explicitly stopped

# Snowflake Proxy - Help Fight Censorship! 🌐

## Quick Start

```bash
docker-compose up -d
```

## Monitoring Your Impact

The Snowflake proxy doesn't expose Prometheus metrics, but you can track your contribution via logs:

```bash
# Total connections helped today
docker logs snowflake 2>&1 | grep "$(date +%b\ %d)" | grep -c "connected to relay"

# Live connection watching
docker logs -f snowflake

# See traffic summaries (if using -summary-interval flag)
docker logs snowflake | grep "In the last"
```

## Integration with Central Monitoring

Since Snowflake uses `network_mode: host`, it can't join the monitoring network directly. However, you can:

1. Monitor the host itself via Node Exporter (already in monitoring stack)
2. Create a custom exporter that parses Snowflake logs
3. Use Grafana's Loki for log aggregation (future enhancement)

## Understanding the Logs

- `connected to relay` - You're helping someone!
- `Received` - Active data transfer
- `NAT type: unrestricted` - Your NAT is properly configured
- `traffic throughput` - Bandwidth you're providing

## Tips

- Keep it running 24/7 for maximum impact
- Check logs periodically to see your contribution
- No additional configuration needed - it just works!

---

_Every proxy helps someone access free information!_
