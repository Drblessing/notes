services:
bitcoin:
image: dobtc/bitcoin
container_name: bitcoin
ports: - 8332:8332 - 8333:8333
volumes: - ./bitcoin:/home/bitcoin/.bitcoin
restart: always
stop_grace_period: 1m
