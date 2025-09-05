# Robot activated.
PS1=" \w 🎛️  "

# Aliases
alias up='sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y'
alias c="clear"
alias d="directory.sh"
alias lg="lazygit.sh"
alias myip="hostname -I | awk '{print \$1}'"

# Git
alias g="git fetch && git status"
alias gb="git branch -a"
alias gs="git stash list" # List all stashes
alias gsc="git stash clear" # Clear all stashes
alias gsp="git stash pop" # Restore most recent stash
alias gp="git pull" # Pull latest changes. Equivalent to git fetch && git merge
alias gsw="git switch" # Switch branches

# Path
export PATH="$HOME/github/notes/bin:$PATH"

# System settings
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export TZ=America/Detroit

# Python
alias s="source .venv/bin/activate" # Activate Python virtual environment

# nvm 
export NVM_DIR="$HOME/.nvm"
if [[ -n "$HOMEBREW_PREFIX" ]]; then
  [[ -s "$HOMEBREW_PREFIX/opt/nvm/nvm.sh" ]] && . "$HOMEBREW_PREFIX/opt/nvm/nvm.sh"
  [[ -s "$HOMEBREW_PREFIX/opt/nvm/etc/bash_completion.d/nvm" ]] && . "$HOMEBREW_PREFIX/opt/nvm/etc/bash_completion.d/nvm"
fi

# Disable telemetry
export HOMEBREW_NO_ANALYTICS=1
export NEXT_TELEMETRY_DISABLED=1

# nvm
alias nup="nvm install --lts && nvm alias default node && echo '✅ Node.js updated to latest LTS version!'"