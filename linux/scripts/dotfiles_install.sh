#!/bin/bash
# Symlink Linux dotfiles from the notes repo into the home directory

set -e

# Define repo path
NOTES_REPO_PATH="${NOTES_REPO_PATH:-$HOME/github/notes}"
LINUX_DOTFILES="$NOTES_REPO_PATH/linux/configs/dotfiles"

echo "Using notes repo: $NOTES_REPO_PATH"

# Remove existing dotfiles
echo "Removing existing dotfiles..."
rm -f ~/.bashrc ~/.gitconfig 

# Symlink bash-related dotfiles
echo "Linking bash dotfiles..."
ln -s "$LINUX_DOTFILES/.bashrc" ~/.bashrc
ln -s "$NOTES_REPO_PATH/configs/dotfiles/.gitconfig" ~/.gitconfig

echo "Dotfiles linked ✅"