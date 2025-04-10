#!/bin/bash
# Homebrew installation script
# This script installs and configures Homebrew and related packages

# Check if Homebrew is already installed
if command -v brew &> /dev/null; then
    echo "Homebrew is already installed. Updating..."
    brew update
    brew upgrade
    brew cleanup
    # Exit if Homebrew is already installed
    exit 0
else
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi


# Activate homebrew in the current shell
echo "Activating Homebrew..."
if [[ "$(uname -m)" == "arm64" ]]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
else
    eval "$(/usr/local/bin/brew shellenv)"
fi

# Disable Homebrew analytics
export HOMEBREW_NO_ANALYTICS=1

# Make sure we have the notes repository path
if [ -z "$NOTES_REPO_PATH" ]; then
    NOTES_REPO_PATH=~/Github/notes
    echo "Using default notes repository path: $NOTES_REPO_PATH"
fi


# Install formulae if the file exists
if [ -f "$NOTES_REPO_PATH/configs/homebrew/homebrew_formulae.txt" ]; then
    echo "Installing Homebrew formulae..."
    xargs brew install < "$NOTES_REPO_PATH/configs/homebrew/homebrew_formulae.txt"
else
    echo "Warning: Homebrew formulae file not found at $NOTES_REPO_PATH/configs/homebrew/homebrew_formulae.txt"
fi

# Install casks if the file exists
if [ -f "$NOTES_REPO_PATH/configs/homebrew/homebrew_casks.txt" ]; then
    echo "Installing Homebrew casks..."
    xargs brew install --cask < "$NOTES_REPO_PATH/configs/homebrew/homebrew_casks.txt"
else
    echo "Warning: Homebrew casks file not found at $NOTES_REPO_PATH/configs/homebrew/homebrew_casks.txt"
fi

# Install git lfs
echo "Setting up Git LFS..."
git lfs install

# Create ~/.nvm directory if it doesn't exist
mkdir -p ~/.nvm

# Cleanup 
echo "Performing Homebrew cleanup..."
brew cleanup
brew doctor
