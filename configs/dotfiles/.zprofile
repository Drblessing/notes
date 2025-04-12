# ---------------------------------------------
# |                                           |
# |              Foundry Configuration        |
# |                                           |
# ---------------------------------------------
export PATH="$PATH:~/.foundry/bin"

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