#!/bin/bash

# This script configures Grafana by adding Prometheus as a data source
# and importing the Node Exporter dashboard (ID: 1860).
#
# Prerequisites: curl, jq
#
# Usage:
# 1. Make the script executable: chmod +x configure_grafana.sh
# 2. Run it: ./configure_grafana.sh

# --- Configuration ---
GRAFANA_URL="http://localhost:3000"
GRAFANA_USER="admin"
PROMETHEUS_URL="http://localhost:9090"
DASHBOARD_ID=1860
# --- End Configuration ---

# Prompt for Grafana admin password
read -sp "Enter Grafana admin password: " GRAFANA_PASS
echo

# --- Check Grafana Status ---
echo "Checking Grafana server status at $GRAFANA_URL..."
# Use curl to check if the Grafana login page is accessible.
if ! curl -s --head "$GRAFANA_URL/login" | head -n 1 | grep "200 OK" > /dev/null; then
    echo "Error: Could not connect to Grafana at $GRAFANA_URL."
    echo "Please ensure the Grafana service is running and accessible."
    echo "You can check its status with: sudo systemctl status grafana-server"
    exit 1
fi
echo "Grafana server is responding."

# --- Step 1: Add Prometheus Data Source ---
echo "Attempting to add Prometheus as a Grafana data source..."

DATASOURCE_PAYLOAD=$(cat <<EOF
{
  "name": "Prometheus",
  "type": "prometheus",
  "url": "$PROMETHEUS_URL",
  "access": "proxy",
  "isDefault": true
}
EOF
)

# Use curl to send the request to the Grafana API
HTTP_RESPONSE=$(curl -s -w "%{http_code}" -X POST \
  -H "Content-Type: application/json" \
  --user "$GRAFANA_USER:$GRAFANA_PASS" \
  --data "$DATASOURCE_PAYLOAD" \
  "$GRAFANA_URL/api/datasources")

HTTP_STATUS=$(echo "$HTTP_RESPONSE" | tail -n1)
HTTP_BODY=$(echo "$HTTP_RESPONSE" | sed '$d')

if [ "$HTTP_STATUS" -eq 200 ]; then
  echo "Prometheus data source created successfully."
elif [ "$HTTP_STATUS" -eq 409 ]; then
  echo "Prometheus data source already exists."
else
  echo "Error creating data source. Status: $HTTP_STATUS"
  echo "Response: $HTTP_BODY"
  exit 1
fi

# --- Step 2: Import Grafana Dashboard ---
echo "Attempting to import dashboard ID: $DASHBOARD_ID..."

# Get the dashboard JSON model from grafana.com
DASHBOARD_JSON=$(curl -s "https://grafana.com/api/dashboards/$DASHBOARD_ID/revisions/latest/download")

if [ -z "$DASHBOARD_JSON" ]; then
    echo "Failed to download dashboard JSON for ID $DASHBOARD_ID."
    exit 1
fi

# Create the payload for the import API
IMPORT_PAYLOAD=$(echo "$DASHBOARD_JSON" | jq \
  --arg ds_name "Prometheus" \
  '. | .overwrite = true | .inputs = [{"name": "DS_PROMETHEUS", "type": "datasource", "pluginId": "prometheus", "value": $ds_name}] | {dashboard: ., overwrite: .overwrite, inputs: .inputs}')

# Use curl to send the import request
HTTP_RESPONSE=$(curl -s -w "%{http_code}" -X POST \
  -H "Content-Type: application/json" \
  --user "$GRAFANA_USER:$GRAFANA_PASS" \
  --data "$IMPORT_PAYLOAD" \
  "$GRAFANA_URL/api/dashboards/import")

HTTP_STATUS=$(echo "$HTTP_RESPONSE" | tail -n1)
HTTP_BODY=$(echo "$HTTP_RESPONSE" | sed '$d')

if [ "$HTTP_STATUS" -eq 200 ]; then
  DASHBOARD_URL=$(echo "$HTTP_BODY" | jq -r '.importedUrl')
  echo "Dashboard imported successfully."
  echo "Access it here: $GRAFANA_URL$DASHBOARD_URL"
else
  echo "Error importing dashboard. Status: $HTTP_STATUS"
  echo "Response: $HTTP_BODY"
  exit 1
fi

echo "Grafana configuration complete."