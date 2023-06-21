# System Commands

## Hardware

### Ram

1. Get total ram

```bash
free -h
```

On a mac:

```
top -l 1 | grep PhysMem
```

Available Memory = Physical Memory - Memory Used

2. Get ram speed

```bash
sudo apt-get install dmidecode
sudo dmidecode -t memory
```

## Networking

1. Get local IP address

```bash
curl ifconfig.me
```

2. Current logged in user

```bash
whoami
```

3. Ping a server

```base
ping 1.1.1.1
```

4. Send DNS query

```bash
nslookup cloudfare.com
```
