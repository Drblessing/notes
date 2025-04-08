# MacOS Configs

I like my MacOS to be cozy.

## Installation

**1. Install Homebrew.**

```zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**2. Install Xcode from Apple Store.**

Also install the iOS simulator. Do not install code completion model.

**3. Install 1Password.**

**4. Install the Notes Github repository.**

```zsh
mkdir ~/Github
cd ~/Github
git clone https://github.com/Drblessing/notes.git
```

**5. Install Homebrew packages**

Install formulae

```zsh
xargs brew install < ~/Github/notes/configs/homebrew/homebrew_formulae.txt
```

Install casks

```zsh
xargs brew install --cask < ~/Github/notes/configs/homebrew/homebrew_casks.txt
```

**6. Install dotfiles.**

```zsh
ln -s ~/Github/notes/configs/dotfiles/.zprofile ~/.zprofile
ln -s ~/Github/notes/configs/dotfiles/.zshrc ~/.zshrc
```

**7. Install VSCode Application.**

https://code.visualstudio.com/

Sync settings to Github.

Install "code" command in PATH.

**8. Install Google Chrome.**

https://www.google.com/chrome/

Login to your Google account, and sync settings.

**9. Install node.**

```zsh
nvm install --lts
```

**10. Install Python.**

```zsh
ln -s /opt/homebrew/bin/python3 /opt/homebrew/bin/python
ln -s /opt/homebrew/bin/pip3 /opt/homebrew/bin/pip
```

**11. Install Foundry.**

```zsh
curl -L https://foundry.paradigm.xyz | bash
```
