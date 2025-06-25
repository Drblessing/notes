#!/bin/bash
# Install Linux dotfiles from the notes repository into the home directory
# This script creates symlinks to dotfiles for Linux environments

set -e  # Exit on any error

echo "Starting Linux dotfiles installation..."

# Make sure we have the notes repository path
if [ -z "$NOTES_REPO_PATH" ]; then
    NOTES_REPO_PATH=~/Github/notes
    echo "Using default notes repository path: $NOTES_REPO_PATH"
fi

# Check if Linux dotfiles directory exists
if [ ! -d "$NOTES_REPO_PATH/linux/configs/dotfiles" ]; then
    echo "Error: Linux dotfiles directory not found at $NOTES_REPO_PATH/linux/configs/dotfiles"
    exit 1
fi

echo "Removing existing dotfiles in home directory..."
# Remove existing dotfiles (if they exist)
rm -f ~/.bashrc ~/.bash_profile ~/.gitconfig

echo "Creating symlinks to Linux dotfiles..."

# Link the Linux-specific dotfiles
if [ -f "$NOTES_REPO_PATH/linux/configs/dotfiles/.bashrc" ]; then
    ln -s "$NOTES_REPO_PATH/linux/configs/dotfiles/.bashrc" ~/.bashrc
    echo "Linked .bashrc"
else
    echo "Warning: .bashrc not found in Linux dotfiles"
fi

if [ -f "$NOTES_REPO_PATH/linux/configs/dotfiles/.bash_profile" ]; then
    ln -s "$NOTES_REPO_PATH/linux/configs/dotfiles/.bash_profile" ~/.bash_profile
    echo "Linked .bash_profile"
else
    echo "Warning: .bash_profile not found in Linux dotfiles"
fi

if [ -f "$NOTES_REPO_PATH/linux/configs/dotfiles/.gitconfig" ]; then
    ln -s "$NOTES_REPO_PATH/linux/configs/dotfiles/.gitconfig" ~/.gitconfig
    echo "Linked .gitconfig"
else
    echo "Warning: .gitconfig not found in Linux dotfiles"
fi

# Check if zsh is installed and link zsh dotfiles if available
if command -v zsh &> /dev/null; then
    echo "Zsh detected, linking zsh dotfiles..."
    
    # Remove existing zsh dotfiles
    rm -f ~/.zshrc ~/.zprofile
    
    # Link macOS zsh files if zsh is available (they should work on Linux too)
    if [ -f "$NOTES_REPO_PATH/configs/dotfiles/.zshrc" ]; then
        ln -s "$NOTES_REPO_PATH/configs/dotfiles/.zshrc" ~/.zshrc
        echo "Linked .zshrc"
    fi
    
    if [ -f "$NOTES_REPO_PATH/configs/dotfiles/.zprofile" ]; then
        ln -s "$NOTES_REPO_PATH/configs/dotfiles/.zprofile" ~/.zprofile
        echo "Linked .zprofile"
    fi
else
    echo "Zsh not installed, skipping zsh dotfiles"
fi

# Make sure python3 is available as python (if not already linked)
if command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "Creating python -> python3 symlink in ~/.local/bin"
    mkdir -p ~/.local/bin
    ln -sf "$(which python3)" ~/.local/bin/python
    
    if command -v pip3 &> /dev/null; then
        ln -sf "$(which pip3)" ~/.local/bin/pip
    fi
fi

# Source the new bashrc if we're in a bash shell
if [ -n "$BASH_VERSION" ] && [ -f ~/.bashrc ]; then
    echo "Sourcing new .bashrc..."
    source ~/.bashrc
fi

echo "Linux dotfiles installation completed successfully!"
echo "You may need to restart your shell or run 'source ~/.bashrc' to apply changes."
