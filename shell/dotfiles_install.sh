# Install dotfiles from the notes repository into the home directory.
# Supports both macOS and Linux.

# Determine the operating system.
OS="$(uname)"
if [[ "$OS" == "Darwin" ]]; then
    echo "Detected macOS"
    OS_TYPE="macOS"
elif [[ "$OS" == "Linux" ]]; then
    echo "Detected Linux"
    OS_TYPE="Linux"
else
    echo "Unsupported OS: $OS"
    exit 1
fi

# Linux specific setup
if [[ "$OS_TYPE" == "Linux" ]]; then
    echo "Performing Linux specific setup..."
    # Remove existing .bashrc 
    rm -rf ~/.bashrc
    # Link the Linux .bashrc from the notes repository to the home directory.
    ln -s ~/github/notes/configs/dotfiles/.bashrc ~/.bashrc
    # Source the new .bashrc
    source ~/.bashrc
    # Exit after Linux setup
    exit 0
fi

# First delete any existing dotfiles in the home directory.
rm -rf ~/.zshrc ~/.zprofile ~/.gitconfig

# Link the dotfiles from the notes repository to the home directory.
ln -s ~/github/notes/configs/dotfiles/.zprofile ~/.zprofile
ln -s ~/github/notes/configs/dotfiles/.zshrc ~/.zshrc
ln -s ~/github/notes/configs/dotfiles/.gitconfig ~/.gitconfig

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

