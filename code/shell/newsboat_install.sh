#!/bin/bash
# Install newsboat configuration
# Run from any directory

echo "Setting up newsboat configuration..."

# Create newsboat config directory if it doesn't exist
mkdir -p ~/.newsboat

# Remove existing config files if they exist
if [ -f ~/.newsboat/config ]; then
    echo "Removing existing newsboat config..."
    rm ~/.newsboat/config
fi

if [ -f ~/.newsboat/urls ]; then
    echo "Removing existing newsboat urls..."
    rm ~/.newsboat/urls
fi

# Link the config files from the notes repository
ln -s ~/Github/notes/configs/newsboat/config ~/.newsboat/config
ln -s ~/Github/notes/configs/newsboat/urls ~/.newsboat/urls

echo "Newsboat configuration installed successfully!"
echo "Run 'newsboat' to start reading feeds"