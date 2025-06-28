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

    ln -sfn ~/github/notes/configs/dotfiles/.bashrc ~/.bashrc
    source ~/.bashrc

    echo "Dotfiles installation complete. Please restart your terminal."
    exit 0
fi

# macOS specific setup
elif [[ "$OS_TYPE" == "macOS" ]]; then
    echo "Performing macOS specific setup..."

    # Link the dotfiles from the notes repository to the home directory.
    ln -sfn ~/github/notes/configs/dotfiles/.zprofile ~/.zprofile
    ln -sfn ~/github/notes/configs/dotfiles/.zshrc ~/.zshrc
    ln -sfn ~/github/notes/configs/dotfiles/.gitconfig ~/.gitconfig

    # Link python to python3 from homebrew.
    if [[ "$(uname -m)" == "arm64" ]]; then
        ln -sfn /opt/homebrew/bin/python3 /opt/homebrew/bin/python
        ln -sfn /opt/homebrew/bin/pip3 /opt/homebrew/bin/pip
    else
        rm -sfn /usr/local/bin/python /usr/local/bin/pip
        ln -sfn /usr/local/bin/python3 /usr/local/bin/python
        ln -sfn /usr/local/bin/pip3 /usr/local/bin/pip
    fi

    # Source the new files
    source ~/.zprofile
    source ~/.zshrc

    echo "Dotfiles installation complete. Please restart your terminal."
    exit 0
fi

