# ---------------------------------------------
# |                                           |
# |              Homebrew Configuration       |
# |                                           |
# ---------------------------------------------
eval "$(/opt/homebrew/bin/brew shellenv)"
export HOMEBREW_NO_ANALYTICS=1

# ---------------------------------------------
# |                                           |
# |              Foundry Configuration        |
# |                                           |
# ---------------------------------------------
export PATH="$PATH:/Users/dbless/.foundry/bin"

# ---------------------------------------------
# |                                           |
# |              NVM Configuration            |
# |                                           |
# ---------------------------------------------
export NVM_DIR="$HOME/.nvm"
[ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \. "/opt/homebrew/opt/nvm/nvm.sh"  # This loads nvm
[ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && \. "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"  # This loads nvm bash_completion

# ---------------------------------------------
# |                                           |
# |            / bin added to $PATH           |
# |                                           |
# ---------------------------------------------
export PATH="$HOME/Github/notes/bin:$PATH"

# ---------------------------------------------
# |                                           |
# |             Aliases                       |
# |                                           |
# ---------------------------------------------
alias notes="code ~/Github/notes" 
alias c="clear"
alias b="brew update && brew upgrade && brew cleanup"
alias d="directory.sh"
alias lg="lazygit.sh"
alias e="b && c && d"