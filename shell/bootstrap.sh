# Bootstrap Install ~/github/notes/shell/bootstrap.sh
# Install https://github.com/drblessing/notes into host machine ~/github/notes
# Usage: 
#   curl -fsSL https://raw.githubusercontent.com/drblessing/notes/master/shell/bootstrap.sh | bash

# Make a backup of existing notes directory if it exists
if [ -d "$HOME/github/notes" ]; then
    echo "Backing up existing notes directory to notes_backup"
    mv "$HOME/github/notes" "$HOME/github/notes_backup"
fi

# Create directory and clone 
mkdir -p "$HOME/github"
git clone https://github.com/drblessing/notes.git "$HOME/github/notes"
echo "Cloned notes repository to $HOME/github/notes"

echo "✓ Notes installed successfully!"
echo ""
echo "To install submodules, run:"
echo "cd $HOME/github/notes && git submodule update --init --recursive --depth 1"
echo ""
echo "To complete setup, run:"
echo "bash $HOME/github/notes/shell/main_install.sh"
