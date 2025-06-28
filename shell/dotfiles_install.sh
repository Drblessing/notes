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
    # Make backup
    if [ -f ~/.bashrc ]; then
        cp ~/.bashrc ~/.bashrc.bak
        echo "Backup of existing .bashrc created at ~/.bashrc.bak"
    fi
    # Remove existing .bashrc 
    rm -f ~/.bashrc
    # Link the Linux .bashrc from the notes repository to the home directory.
    ln -s ~/github/notes/configs/dotfiles/.bashrc ~/.bashrc
    # Source the new .bashrc
    source ~/.bashrc

    # Install ~/.ssh files
    ln -s ~/github/notes/configs/ssh/config ~/.ssh/config
    ln -s ~/github/notes/configs/ssh/sshd_config ~/.ssh/sshd_config

    # Add to authorized_keys if not already present
    if [ -f ~/.ssh/id_ed25519.pub ]; then
        grep -q -f ~/.ssh/id_ed25519.pub ~/.ssh/authorized_keys
        if [ $? -ne 0 ]; then
            cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
            echo "Added public key to ~/.ssh/authorized_keys"
        else
            echo "Public key already present in ~/.ssh/authorized_keys"
        fi
    else
        echo "Warning: ~/.ssh/id_ed25519.pub not found. Please ensure your SSH keys are set up correctly."
    fi


    echo "Dotfiles installation complete. Please restart your terminal."

    # Exit after Linux setup
    exit 0
fi

# macOS specific setup
elif [[ "$OS_TYPE" == "macOS" ]]; then
    echo "Performing macOS specific setup..."
    # Make backups
    if [ -f ~/.zshrc ]; then
        cp ~/.zshrc ~/.zshrc.bak 
    fi
    if [ -f ~/.zprofile ]; then
        cp ~/.zprofile ~/.zprofile.bak 
    fi
    if [ -f ~/.gitconfig ]; then
        cp ~/.gitconfig ~/.gitconfig.bak
    fi

    # First delete any existing dotfiles in the home directory.
    rm -f ~/.zshrc ~/.zprofile ~/.gitconfig

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

    echo "Dotfiles installation complete. Please restart your terminal."
    exit 0
fi

