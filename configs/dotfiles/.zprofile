# Github bin Path
export PATH="$HOME/github/notes/bin:$PATH"

# Foundry
export PATH="$PATH:~/.foundry/bin"

# Aliases
alias notes="code ~/github/notes" 
alias c="clear"
alias d="directory.sh"
alias lg="lazygit.sh"
alias h="ssh home-server"

# Homebrew
alias b="brew update && brew upgrade && brew cleanup && echo '✅ Homebrew packages updated!'"

# Git
alias g="git fetch && git status"
alias gb="git branch -a"
alias gst="git stash list" # List all stashes
alias gsc="git stash clear" # Clear all stashes
alias gsp="git stash pop" # Restore most recent stash
alias gp="git pull" # git fetch && git merge
alias gs="git switch" # Switch branches

# Python
alias s="source .venv/bin/activate" # Activate Python virtual environment

# nvm
alias nup="nvm install --lts && nvm alias default node && echo '✅ Node.js updated to latest LTS version!'"
