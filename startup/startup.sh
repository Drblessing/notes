#!/bin/bash
# Plug and play startup script for macOS and Linux systems. Installs what I like.

# 1. Detect shell and operating system
# 2. Install git
# 3. Clone notes repo   
# 4. Install dotfiles


# 1. Detect shell and operating system
# Determine the shell
if [[ "$(basename $SHELL)" == "bash" ]]; then
    SHELL="bash"
    echo "bash detected."
elif [[ "$(basename $SHELL)" == "zsh" ]]; then
    SHELL="zsh"
    echo "zsh detected."
else
    echo "Unsupported shell: $(basename $SHELL)"
    exit 1
fi

# Determine the operating system
if [[ "$(uname)" == "Darwin" ]]; then
    OS="macOS"
    echo "macOS detected."
elif [[ "$(uname)" == "Linux" ]]; then
    OS="Linux"
    echo "Linux detected."
else
    echo "Unsupported operating system: $(uname)"
    exit 1
fi

# For macOS, check if Homebrew is installed. If not, install it.
if [[ "$OS" == "macOS" ]]; then
    if [[ ! -x "$(command -v brew)" ]]; then
        echo "Homebrew not found. Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        echo "Homebrew installed."
    # Else print homebrew version
    else
        echo "Homebrew found."
        brew --version | head -n 1
    fi
    # Update homebrew
    echo "Updating Homebrew..."
    brew update
fi

# 2. Install git
# Check if git is installed. If not, install it.
if [[ ! -x "$(command -v git)" ]]; then
    echo "Git not found. Installing git..."
    if [[ "$OS" == "macOS" ]]; then
        brew install git
    elif [[ "$OS" == "Linux" ]]; then
        sudo apt install git
    fi
    echo "Git installed."
# Else print git version
else
    echo "Git found."
    git --version
fi

# 3. Clone notes repo
# Check if notes repo is cloned. If not, clone it.
if [[ ! -d "$HOME/Github/notes" ]]; then
    echo "Notes repo not found. Cloning notes repo..."
    git clone https://github.com/Drblessing/notes.git "$HOME/Github/notes"
    echo "Notes repo cloned."
# Else pull latest notes repo
else
    echo "Notes repo found. Pulling latest notes repo..."
    cd "$HOME/Github/notes"
    git pull
    echo "Notes repo pulled."
fi

# 4. Install dotfiles

echo "Setup completed."


