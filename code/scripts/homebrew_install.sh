# Install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Activate homebrew
if [[ "$(uname -m)" == "arm64" ]]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
else
    echo eval "$(/usr/local/bin/brew shellenv)"
fi
export HOMEBREW_NO_ANALYTICS=1

# Install formulae
xargs brew install < ~/Github/notes/configs/homebrew/homebrew_formulae.txt

# Install casks
xargs brew install --cask < ~/Github/notes/configs/homebrew/homebrew_casks.txt

# Install nvm
mkdir -p ~/.nvm
nvm install --lts

# Install git lfs
git lfs install

# Cleanup 
brew cleanup
brew doctor

