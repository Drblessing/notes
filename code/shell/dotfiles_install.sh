# Install dotfiles from the notes repository into the home directory.

# First delete any existing dotfiles in the home directory.
rm -rf ~/.zshrc ~/.zprofile ~/.zshrc ~/.gitconfig

# Link the dotfiles from the notes repository to the home directory.
ln -s ~/Github/notes/configs/dotfiles/.zprofile ~/.zprofile
ln -s ~/Github/notes/configs/dotfiles/.zshrc ~/.zshrc
ln -s ~/Github/notes/configs/dotfiles/.gitconfig ~/.gitconfig

# Link python to python3 from homebrew.
if [[ "$(uname -m)" == "arm64" ]]; then
    rm -rf /opt/homebrew/bin/python /opt/homebrew/bin/pip
    ln -s /opt/homebrew/bin/python3 /opt/homebrew/bin/python
    ln -s /opt/homebrew/bin/pip3 /opt/homebrew/bin/pip
else
    rm -rf /usr/local/bin/python /usr/local/bin/pip
    ln -s /usr/local/bin/python3 /usr/local/bin/python
    ln -s /usr/local/bin/pip3 /usr/local/bin/pip
fi

# Source the new files
source ~/.zprofile
source ~/.zshrc


# Install Node.js LTS version
echo "Installing Node.js LTS version..."
nvm install --lts