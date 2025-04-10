# Install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Activate homebrew
if [[ "$(uname -m)" == "arm64" ]]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
else
    echo eval "$(/usr/local/bin/brew shellenv)"
fi
export HOMEBREW_NO_ANALYTICS=1

# Rip the dotfiles installation
bash ~/Github/notes/configs/dotfiles/dotfiles_install.sh

# Source the new dotfiles
source ~/.zprofile
source ~/.zshrc

# Install formulae
xargs brew install < ~/Github/notes/configs/homebrew/homebrew_formulae.txt

# Install casks
xargs brew install --cask < ~/Github/notes/configs/homebrew/homebrew_casks.txt

# Make .nvm directory
mkdir -p ~/.nvm

# Source the new dotfiles again
source ~/.zprofile
source ~/.zshrc

nvm install --lts

# Install git lfs
git lfs install

# gh auth online
gh auth login
gh auth refresh -h github.com -s repo,read:org


# Cleanup 
brew cleanup
brew doctor

