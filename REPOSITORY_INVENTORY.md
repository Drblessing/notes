# Repository Inventory: What's in Your Notes

A comprehensive catalog of your personal technology notes repository.

## Summary

Your notes repository is a well-organized personal knowledge base containing **143 files** across 11 main categories. It includes 39 Python utilities, 32 documentation files, 17 shell scripts, and references to 18 external repositories via git submodules. The repository serves as both a learning resource and a practical toolkit for development, infrastructure management, and system configuration.

## Overview

This repository contains your personal technology notes, scripts, configurations, and reference materials. It's organized as a comprehensive knowledge base covering development, infrastructure, security, and personal setup documentation.

## Directory Structure

### 📝 Documentation & Notes (`/docs`)

**Development Notes:**
- `git.md` - Git commands and workflows
- `processes.md` - Operating system processes
- `submodules.md` - Git submodule management
- `object oriented programming/` - OOP concepts and examples
- `tech interview/` - Technical interview preparation

**Infrastructure Notes:**
- `hardware/` - Hardware-related documentation
- `system/` - System administration notes

**Security Resources:**
- Cryptography research papers (RSA, Bitcoin whitepaper, Ethereum docs)
- PGP keys for notable figures (Satoshi Nakamoto, Vitalik Buterin, etc.)
- Security best practices and references

### 🤖 AI & Automation (`/ai`)

- `projects-guide.md` - ChatGPT Projects optimization guide
- AI project structuring best practices
- Examples for music projects and Ubuntu server dashboards

### ⚙️ Utility Scripts (`/bin`)

**Key Scripts:**
- `fortune.py` - Cowboy-themed fortune cookie generator
- `lazygit.py` / `lazygit.sh` - Git workflow automation
- `pomodoro/` - Pomodoro timer application
- `st.py` / `st.sh` - Custom utilities
- `compare-hashes.sh` - File integrity verification
- `directory.sh` - Directory management utilities

### 💻 Code Examples (`/code`)

**Python Library (`/code/python/src`):**
- `sorting.py` - Sorting algorithms
- `groupby.py` - Data grouping utilities
- `custom_counter.py` - Custom counter implementations
- `prime_factorization.py` - Mathematical computations
- `abc_examples.py` - Abstract base class examples
- `eth_library.py` - Ethereum blockchain utilities
- `logging_config.py` - Logging configurations
- `dunder_methods.py` - Python magic methods
- `custom_hashmap.py` - Data structure implementations
- `functools_examples.py` - Functional programming examples
- `call_stack.py` - Stack trace utilities
- `random_examples.py` - Random number generation

### 🔧 Configurations (`/configs`)

**System Configurations:**
- `.ssh/` - SSH keys and configurations
- `VSCode/` - Visual Studio Code settings
- `dotfiles/` - Shell and environment configurations
- `homebrew/` - Package manager configurations
- `mac/` - macOS-specific settings
- `newsboat/` - RSS feed reader configuration
- `npm/` - Node.js package manager settings
- `nvm/` - Node Version Manager configuration
- `python/` - Python environment and requirements

### 🐧 Linux Configuration (`/linux`)

- Package management scripts
- Shell configurations for Linux environments
- System administration utilities

### 🚀 Installation Scripts (`/shell`)

**Setup Automation:**
- `benv_install.sh` - Python environment setup
- `bootstrap.sh` - Initial system bootstrap
- `dotfiles_install.sh` - Dotfiles configuration
- `homebrew_install.sh` - Package manager installation
- `main_install.sh` - Master installation script
- `newsboat_install.sh` - RSS reader setup
- `nvm_initialize.sh` - Node.js environment setup
- `ssh_install.sh` - SSH configuration

### 📚 Reference Submodules (`/subrepos`)

**Web Development Frameworks:**
- `react.dev` - React documentation
- `next.js` - Next.js framework
- `expo` - React Native framework
- `three.js` - 3D graphics library
- `tailwindcss` - CSS framework
- `shadcn-ui` - UI component library
- `motion` - Animation library

**Blockchain & Cryptocurrency:**
- `foundry` - Ethereum development framework
- `wagmi` - React hooks for Ethereum
- `viem` - Ethereum library
- `rainbowkit` - Wallet connection library
- `openzeppelin` - Smart contract framework

**Cloud & Infrastructure:**
- `cloudflare-docs` - Cloudflare documentation
- `vercel` - Deployment platform
- `aws-doc-sdk-examples` - AWS SDK examples
- `aws-lambda-developer-guide` - Lambda documentation

**Development Tools:**
- `lodash` - JavaScript utility library
- `openai-cookbook` - OpenAI API examples

## Personal Technology Stack

### Primary Setup
- **Computer:** MacBook Pro (M1)
- **OS:** macOS with UTM Virtualization
- **IDE:** Visual Studio Code
- **Browser:** Chrome with uBlock Origin
- **Languages:** Python, JavaScript
- **Frameworks:** React, Next.js
- **Hosting:** Cloudflare
- **Package Manager:** Homebrew

### Infrastructure Services
- **IPFS Node** - Distributed file storage
- **Ethereum Node** - Smart contract platform
- **Bitcoin Node** - Cryptocurrency network
- **Monero Node** - Privacy-focused cryptocurrency
- **Tor Node** - Anonymous networking
- **Lightning Node** - Bitcoin payment layer
- **Public MCP Server** - AI chatbot service
- **Torrent Seeding** - 1TB open source software distribution

### Active Subscriptions
- Apple Music - Music streaming
- ChatGPT Plus - AI language model
- iCloud - Cloud storage
- Cloudflare - Hosting and DDoS protection
- Grok - AI language model
- GitHub Copilot - AI code assistant

## Reference Materials

### Cryptography & Security
- "A Method for Obtaining Digital Signatures..." (RSA paper)
- "New Directions in Cryptography" (Public-key cryptography)
- "How to Share a Secret" (Secret sharing algorithms)
- Bitcoin whitepaper by Satoshi Nakamoto
- Ethereum whitepaper by Vitalik Buterin
- Monero whitepaper (Privacy features)

### Technical Resources
- "Mastering Ethereum" by Andreas Antonopoulos
- "Flashboys 2.0" (HFT and crypto markets)
- EFF Large Wordlist (Secure passphrases)
- King James Bible

### PGP Key Collection
- Satoshi Nakamoto
- Vitalik Buterin (Ethereum founder)
- Charles Hoskinson (Cardano founder)
- Daniel Blessing (Repository owner)
- MoneroHashes (Release verification)
- Dark.fail (Darknet directory)
- binaryFate (Monero core team)

## Repository Statistics

### File Counts
- **Total Files:** 143 (excluding git and submodules)
- **Python Files:** 39 scripts and utilities
- **Markdown Documents:** 32 documentation files
- **Shell Scripts:** 17 installation and automation scripts
- **PDF References:** 9 technical papers and guides
- **Git Submodules:** 18 external repositories

### Organization
- **Main Directories:** 11 primary categories
- **Repository Size:** ~29MB (excluding submodules)
- **Configuration Categories:** 10+ tool configurations
- **Reference Collection:** Comprehensive cryptography and blockchain papers

## Quick Access Commands

```bash
# Install on new machine
bash -c "$(curl -fsSL https://raw.githubusercontent.com/danielblessing/notes/main/shell/github_notes_install.sh)"

# Update all submodules
git submodule update --remote --depth 1

# Run fortune script
./bin/fortune.py

# Access pomodoro timer
./bin/pomodoro/pomodoro.py
```

---

*This inventory was generated to provide a comprehensive overview of your personal notes repository structure and contents.*