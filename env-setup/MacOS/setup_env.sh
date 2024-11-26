#!/bin/bash

# Don't forget to `chmod +x setup_env.sh` to make the script executable!

# Check if Homebrew is installed, install if not
if ! command -v brew >/dev/null 2>&1; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed."
fi

echo "Updating Homebrew..."
brew update

# Install Homebrew formulae
echo "Installing Homebrew formulae..."
while read line; do
    # Skip empty lines and lines starting with '#'
    [[ -z "$line" || "$line" == \#* ]] && continue
    brew install "$line"
done < "homebrew_formulae.txt"

# Install Homebrew casks
echo "Installing Homebrew casks..."
while read line; do
    # Skip empty lines and lines starting with '#'
    [[ -z "$line" || "$line" == \#* ]] && continue
    brew install --cask "$line"
done < "homebrew_casks.txt"


echo "Installation complete!"