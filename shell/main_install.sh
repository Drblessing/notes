# Complete Installation Script
# This script coordinates the installation of Homebrew, repositories, dotfiles, and other configurations

echo "Howdy, Partner! Starting the complete installation script..."

# Determine OS type
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

export OS_TYPE

# If/elif/else structure to handle OS-specific tasks
if [[ "$OS_TYPE" == "Linux" ]]; then
    echo "Linux specific installation steps will be handled in individual scripts."


elif [[ "$OS_TYPE" == "macOS" ]]; then
    # Install ssh keys for GitHub access
    

    # Create github directory if it doesn't exist
    mkdir -p ~/github

    # Run Homebrew installation script
    echo "Running Homebrew installation..."
    bash ~/github/notes/code/shell/homebrew_install.sh

    # Run github login
    echo "Running github login script..."
    bash ~/github/notes/code/shell/gh_login.sh

    # Run dotfiles installation script
    echo "Running dotfiles installation script..."
    bash ~/github/notes/code/shell/dotfiles_install.sh

    # Run benv installation script
    echo "Running benv installation script..."
    bash ~/github/notes/code/shell/benv_install.sh

    # Run newsboat installation script
    echo "Running newsboat installation script..."
    bash ~/github/notes/code/shell/newsboat_install.sh

else
    echo "Unsupported OS type: $OS_TYPE"
    exit 1
fi


