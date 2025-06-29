# Foundry
export PATH="$PATH:~/.foundry/bin"

# Path
export PATH="$HOME/github/notes/bin:$PATH"

# Aliases
alias notes="code ~/github/notes" 
alias c="clear"
alias d="directory.sh"
alias lg="lazygit.sh"
alias n="newsboat"
alias p="ssh personal-server"

# Homebrew
alias b="brew update && brew upgrade && brew cleanup"

# Git
alias g="git fetch && git status"
alias gb="git branch -a"
alias gs="git stash list" # List all stashes
alias gsc="git stash clear" # Clear all stashes
alias gsp="git stash pop" # Restore most recent stash
alias gp="git pull" # Pull latest changes. Equivalent to git fetch && git merge
alias gsw="git switch" # Switch branches