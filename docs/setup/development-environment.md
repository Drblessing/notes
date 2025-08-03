# Development Environment Setup

## Quick Start

After running the installation script, here's how to set up your development environment:

## 1. VSCode Configuration

Install essential extensions:

```bash
code --install-extension ms-python.python
code --install-extension GitHub.copilot
code --install-extension GitHub.copilot-chat
code --install-extension ms-vscode-remote.remote-ssh
```

## 2. Git Configuration

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global push.default current
```

## 3. Python Environment

```bash
# Install Python packages
pip install -r ~/github/notes/bin/requirements_tracked.txt

# Create virtual environment for projects
python -m venv ~/.venvs/default
source ~/.venvs/default/bin/activate
```

## 4. Node.js Setup

```bash
# Install global packages
npm install -g typescript prettier eslint

# Install common project packages
npm install $(cat ~/github/notes/configs/npm/packages.txt)
```

## 5. Security Setup

- Set up 1Password
- Configure 2FA for all accounts
- Generate SSH keys for GitHub:
  ```bash
  ssh-keygen -t ed25519 -C "your.email@example.com"
  ```

## 6. Verify Installation

```bash
# Check all tools are installed
which git node python code
echo $PATH | grep -q "$HOME/github/notes/bin" && echo "✓ Custom bin in PATH"
```
