#!/bin/bash

# This script configures Prometheus to scrape metrics from node_exporter.
# It appends a new scrape configuration to the prometheus.yml file.

# Define the node_exporter scrape configuration
CONFIG_BLOCK="
  - job_name: 'node_exporter'
    static_configs:
      - targets: ['localhost:9100']
"

# Append the configuration to prometheus.yml
echo "$CONFIG_BLOCK" | sudo tee -a /etc/prometheus/prometheus.yml > /dev/null

# Restart Prometheus to apply the new configuration
echo "Restarting Prometheus..."
sudo systemctl restart prometheus

# Check the status of the Prometheus service
echo "Checking Prometheus status..."
sudo systemctl status prometheus --no-pager