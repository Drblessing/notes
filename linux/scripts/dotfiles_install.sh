#!/bin/bash

# Dotfiles Installation Script for Linux
# Links dotfiles from the notes repository to the home directory

set -e

echo "Installing Linux dotfiles..."

# Set the notes repository path
NOTES_REPO_PATH=~/Github/notes

# Check if notes repository exists
if [ ! -d "$NOTES_REPO_PATH" ]; then
    echo "Error: Notes repository not found at $NOTES_REPO_PATH"
    echo "Please clone the repository first:"
    echo "git clone https://github.com/drblessing/notes.git ~/Github/notes"
    exit 1
fi

# Backup existing dotfiles
echo "Backing up existing dotfiles..."
BACKUP_DIR=~/.dotfiles_backup_$(date +%Y%m%d_%H%M%S)
mkdir -p "$BACKUP_DIR"

# List of dotfiles to backup and link
DOTFILES=(".bashrc" ".bash_profile" ".gitconfig" ".zshrc")

for dotfile in "${DOTFILES[@]}"; do
    if [ -f ~/"$dotfile" ] && [ ! -L ~/"$dotfile" ]; then
        echo "Backing up existing $dotfile"
        mv ~/"$dotfile" "$BACKUP_DIR/"
    fi
done

# Create symbolic links to dotfiles from the repository
echo "Creating symbolic links to dotfiles..."

# Link bash configuration
if [ -f "$NOTES_REPO_PATH/linux/configs/dotfiles/.bashrc" ]; then
    ln -sf "$NOTES_REPO_PATH/linux/configs/dotfiles/.bashrc" ~/.bashrc
    echo "Linked .bashrc"
fi

if [ -f "$NOTES_REPO_PATH/linux/configs/dotfiles/.bash_profile" ]; then
    ln -sf "$NOTES_REPO_PATH/linux/configs/dotfiles/.bash_profile" ~/.bash_profile
    echo "Linked .bash_profile"
fi

# Link git configuration (reuse from main configs)
if [ -f "$NOTES_REPO_PATH/configs/dotfiles/.gitconfig" ]; then
    ln -sf "$NOTES_REPO_PATH/configs/dotfiles/.gitconfig" ~/.gitconfig
    echo "Linked .gitconfig"
fi

# Link zsh configuration for systems that have zsh
if command -v zsh &> /dev/null; then
    if [ -f "$NOTES_REPO_PATH/linux/configs/dotfiles/.zshrc" ]; then
        ln -sf "$NOTES_REPO_PATH/linux/configs/dotfiles/.zshrc" ~/.zshrc
        echo "Linked .zshrc"
    fi
fi

# Set up Python3 as default python if not already done
if command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "Setting up python3 as default python..."
    mkdir -p ~/.local/bin
    ln -sf "$(which python3)" ~/.local/bin/python
    ln -sf "$(which pip3)" ~/.local/bin/pip
fi

# Source the new configuration
echo "Sourcing new configuration..."
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi

# Create bin directory and add to PATH if it doesn't exist
if [ ! -d ~/Github/notes/bin ]; then
    echo "Warning: bin directory not found at ~/Github/notes/bin"
    echo "Some aliases may not work correctly"
fi

echo "Dotfiles installation completed successfully!"
echo ""
echo "Changes made:"
echo "- Linked dotfiles from repository"
echo "- Backed up original files to $BACKUP_DIR"
echo "- Configured PATH to include ~/Github/notes/bin"
echo "- Set up python3 as default python"
echo ""
echo "Note: You may need to log out and back in for all changes to take effect"
