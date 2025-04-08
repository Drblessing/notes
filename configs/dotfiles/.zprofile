# ---------------------------------------------
# |                                           |
# |              Homebrew Configuration       |
# |                                           |
# ---------------------------------------------
if [[ "$(uname -m)" == *"arm"* ]]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi
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
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" 
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# ---------------------------------------------
# |                                           |
# |            Prompt Configuration           |
# |                                           |
# ---------------------------------------------
PS1=" %1~ 😃 "

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
alias lg="lazygit"
alias e="b && c && d"