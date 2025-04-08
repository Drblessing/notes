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

**12. Install Cloudflare WARP.**

https://one.one.one.one/

**12. Install MacOS settings.**

In iCloud settings:

- Turn on Photos iCloud sync.
- Turn on Drive iCloud sync.
- Turn on Passwords iCloud sync.
- Turn on Notes iCloud sync.
- Turn on Messages iCloud sync.
- Turn off Mail iCloud sync.

In Network settings:

- Turn on Firewall.

In Battery settings:

- Turn on Low Power Mode Never.

In General > Software Update settings:

- Turn on all Automatic Updates.

In Accessibility > Zoom:

- Turn on "Use scroll gesture with modifier keys to zoom".

In Appearance settings:

- Turn on "Auto" Appearance.
- Select Green Accent color.

In Apple Intelligence & Siri:

- Turn off "Aplpe Intelligence".

In Control Center:

- For Wi-Fi, select "Don't Show in Menu Bar".
- For battery, select "Don't Show in Menu Bar", "Show in Control Center", and "Show Percentage".

In Control Center > Menu Bar Only:

- For Clock Options, for Style, select "Analog".
- For Spotlight, select "Don't Show in Menu Bar".
- For Automatically hide and shoe the menu bar, select "Always".

In Desktop & Dock:

- Select Size Medium.
- Select Magnification Small.
- Select "Automatically hide and show the Dock".
- For Default web browser, select "Google Chrome".
- Unselect "Tiled windows have margins."
- Unselect "Displays have separate Space."
