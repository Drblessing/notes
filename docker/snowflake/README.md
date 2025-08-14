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
