# ---------------------------------------------
# |                                           |
# |              Homebrew Configuration       |
# |                                           |
# ---------------------------------------------

# Homebrew has different installation paths for Intel and Apple Silicon Macs.
# Check if the system is running on Apple Silicon and set the path accordingly.
if [[ "$(uname -m)" == "arm64" ]]; then
    # On Apple Silicon, Homebrew is installed in /opt/homebrew
    # Command to initialize Homebrew on Apple Silicon Macs
    eval "$(/opt/homebrew/bin/brew shellenv)"
  
else
    # On Intel Macs, Homebrew is installed in /usr/local
    # Command to initialize Homebrew on Intel Macs
    eval "$(/usr/local/bin/brew shellenv)"
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