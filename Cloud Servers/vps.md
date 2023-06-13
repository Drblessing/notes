# Setting up a cloud server

OS: Linux Ubuntu 22.04.2 LTS

### 1. Creating ssh key

ssh-keygen -t ed25519 -C "your_email@example.com"

### 2. Installing ssh key

ssh-copy-id -i ~/.ssh/id_ed25519.pub root@<ip-address>

### 3. Connet with ssh key

ssh -i ~/.ssh/id_ed25519 root@149.28.194.54

### 4. Security Hardening

1. Disable password authentication

You can do this by editing the SSH configuration file (/etc/ssh/sshd_config) on your server and setting PasswordAuthentication to no. Then restart the SSH service.

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
