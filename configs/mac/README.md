# MacOS Configs

I like my MacOS to be cozy.

## Installation

**1. Install MacOS**

Install MacOS, either from a newly purcahsed machine, or reinstalling on an existing machine.

Reinstalling MacOS: Settings > General > Transfer or Reset > Erase All Content and Settings.

**2. Install Apps from the App store.**

Since we will need these later, and they don't need any other configuration, we will install them now.

- Install Apple Pages.
- Install Apple Numbers.
- Install XCode.
  - Install iOS simulator.
  - Do not install code completion model.

**3. Install 1passowrd.**

Since we require 1pasword to login to Github, we will install it now.

- Install 1Password from Safari.
  - https://1password.com/downloads/mac
- Login to 1Password.

**4. Install Homebrew.**

Homebrew must be installed before Github respositories, because you need gh to login to Github through the terminal.

Install homebrew:

```zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install homebrew in .zshrc:

```zsh
if [[ "$(uname -m)" == "arm64" ]]; then
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
else
    echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zshrc
fi
export HOMEBREW_NO_ANALYTICS=1
```

**5. Install gh.**

```zsh
brew install gh
```

Login to your Github account:

```zsh
gh auth login
```

**6. Install the Notes Github repository.**

```zsh
mkdir ~/Github
cd ~/Github
git clone --recurse-submodules https://github.com/drblessing/notes.git
ln -s ~/Github/notes/configs/dotfiles/.zprofile ~/.zprofile
ln -s ~/Github/notes/configs/dotfiles/.zshrc ~/.zshrc
ln -s ~/Github/notes/configs/dotfiles/.gitconfig ~/.gitconfig
```

**7. Install Homebrew packages**

Install formulae:

```zsh
xargs brew install < ~/Github/notes/configs/homebrew/homebrew_formulae.txt
```

Install casks

```zsh
xargs brew install --cask < ~/Github/notes/configs/homebrew/homebrew_casks.txt
```

Loose threads:

```zsh
mkdir ~/.nvm
git lfs install
nvm install --lts
if [[ "$(uname -m)" == "arm64" ]]; then
    ln -s /opt/homebrew/bin/python3 /opt/homebrew/bin/python
    ln -s /opt/homebrew/bin/pip3 /opt/homebrew/bin/pip
else
    ln -s /usr/local/bin/python3 /usr/local/bin/python
    ln -s /usr/local/bin/pip3 /usr/local/bin/pip
fi
```

**8. Install VSCode Application.**

https://code.visualstudio.com/

- Sync settings to Github.
- Install "code" command in PATH.

**9. Install Google Chrome.**

https://www.google.com/chrome/

Login to your Google account, and sync settings.

**10. Install Foundry.**

```zsh
curl -L https://foundry.paradigm.xyz | bash
```

```zsh
foundryup
```

**11. Install Cloudflare WARP.**

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

In Screen Saver:

- Select Shuffle Landscape, every 12 hours.

In Spotlight:

- Turn off Siri Suggestions, Webiste, Tips, Presentations, Fonts, Movies, and Help Apple Improve Search in Search.

In Sound:

- Turn off "Play sound on startup".
- Turn off "Play user interface sound effects".

In Lock Screen:

- For Start Screen Save when inactive, select "For 5 minutes".
- For Turn display off on battery when inactive, select "For 10 minutes".
- For Turn display off on power adapter when inactive, select "For 30 minutes".
- For Require password, select "Immediately".
- Turn off "Show the Sleep, Restart, and Shut Down button.
- Turn off "Show user name and photo".
- Turn off "Show large clock".

In Internet Accounts:

- Sign into Google account, only sync Mail, not Calendar, Contacts, and Notes.

In Apple Pay:

- Add Debit Card.

In Widgets:

- Add Weather to menu bar.
- Add Clock to widgets.
- Add Weather to widgeets.
- Swipe left with two fingers from edge to see widgets.

```

```
