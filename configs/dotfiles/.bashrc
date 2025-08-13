# Set the command prompt
PS1=" \w 🎛️  "

# Aliases
alias up='sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y'
alias c="clear"
alias d="directory.sh"
alias lg="lazygit.sh"
alias n="newsboat"
alias localip="hostname -I | awk '{print \$1}'"

# Git
alias g="git fetch && git status"
alias gb="git branch -a"
alias gs="git stash list" # List all stashes
alias gsc="git stash clear" # Clear all stashes
alias gsp="git stash pop" # Restore most recent stash
alias gp="git pull" # Pull latest changes. Equivalent to git fetch && git merge
alias gsw="git switch" # Switch branches

# Deno
alias dr="deno run --allow-all"

# Path
export PATH="$HOME/github/notes/bin:$PATH"

# Disable telemetry
export HOMEBREW_NO_ANALYTICS=1
export NEXT_TELEMETRY_DISABLED=1
export GATSBY_TELEMETRY_DISABLED=1

# System settings
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export TZ=America/Detroit

. "/home/drblessing/.deno/env"
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
