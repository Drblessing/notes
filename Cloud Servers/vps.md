# Setting up a cloud server

OS: Linux Ubuntu 22.04.2 LTS

### 1. Creating ssh key

```
ssh-keygen -t ed25519 -C "your_email@example.com"
```

### 2. Installing ssh key

```
ssh-copy-id -i ~/.ssh/id_ed25519.pub root@<ip-address>
```

### 3. Connet with ssh key

```
ssh -i ~/.ssh/id_ed25519 root@149.28.194.54
```

### 4. Security Hardening

1. Disable password authentication

You can do this by editing the SSH configuration file:

`/etc/ssh/sshd_config`

on your server and setting PasswordAuthentication to no. Then restart the SSH service.

```
sudo systemctl restart ssh
```

2. Uncomplicated Firewall (UFW)

Install:

```
sudo apt-get install ufw
```

Open SSH:

```
sudo ufw allow 22/tcp comment 'Allow SSH port'
```

Deny all incoming and outgoing connections:

```
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

Allow ETH execution client ports:

```
sudo ufw allow 30303 comment 'Allow execution client port'
```

Allow conensus client ports:

```
# Lighthouse, Lodestar, Nimbus, Teku
sudo ufw allow 9000 comment 'Allow l consensus client port'

# Prysm
sudo ufw allow 13000/tcp comment 'Allow p consensus client port'
sudo ufw allow 12000/udp comment 'Allow p1 consensus client port'
```

Finally, enable and view the status of the firewall:

```
sudo ufw enable
sudo ufw status numbered
```

3. Fail2ban

Install:

```
sudo apt-get install fail2ban -y
```

Add configuration:

```
sudo nano /etc/fail2ban/jail.local
```

Add this to bottom:

```
[sshd]
enabled = true
port = 22
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
```

Enable:

```
sudo systemctl restart fail2ban
```

### 5. Convenience

1. Add server to .ssh/config

```

Host myserver
User root
HostName <ip-address>
Port 22
IdentityFile ~/.ssh/id_ed25519

```

2. Add alias to .bashrc

```

alias myserver='ssh myserver'

```

Reload bash

3. Add ssh key to ssh-agent

```

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

```

4. Sync local time with chrony

```

sudo apt-get install chrony -y

```

Check status:

```

chronyc tracking

```

```

chronyc sources

```

Set local time:

```

sudo dpkg-reconfigure tzdata

```

Check time:

```

date

```

```

```
