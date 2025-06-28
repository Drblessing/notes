# Bootstrap Install ~/github/notes/shell/bootstrap.sh
# Install https://github.com/drblessing/notes into host machine ~/github/notes
# Usage: 
#   curl -fsSL https://raw.githubusercontent.com/drblessing/notes/main/shell/bootstrap.sh | bash

# Make a backup of existing notes directory if it exists
if [ -d "$HOME/github/notes" ]; then
    echo "Backing up existing notes directory to notes_backup"
    mv "$HOME/github/notes" "$HOME/github/notes_backup"
fi

# Create directory and clone 
mkdir -p "$HOME/github"
git clone https://github.com/drblessing/notes.git "$HOME/github/notes"
echo "Cloned notes repository to $HOME/github/notes"
