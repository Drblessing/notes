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
# |          OpenJDK Configuration            |
# |                                           |
# ---------------------------------------------
export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"

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
# |             Poetry                        |
# |                                           |
# ---------------------------------------------
export PATH="/Users/dbless/.local/bin:$PATH"

# ---------------------------------------------
# |                                           |
# |             GCloud                        |
# |                                           |
# ---------------------------------------------
export PATH="$HOME/Github/notes/bin/google-cloud-sdk/bin:$PATH"

# ---------------------------------------------
# |                                           |
# |             Aliases                       |
# |                                           |
# ---------------------------------------------
alias lg="lazygit"
alias notes="code ~/Github/notes" 
alias bru="brew update && brew upgrade && brew cleanup"
alias c="clear"
alias ds="directory.sh"