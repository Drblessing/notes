# ---------------------------------------------
# |                                           |
# |            Prompt Configuration           |
# |                                           |
# ---------------------------------------------
PS1=" %1~ 😃 "

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
# |              NVM Configuration            |
# |                                           |
# ---------------------------------------------
# Check if the system is running on Apple Silicon and set the path accordingly.
if [[ "$(uname -m)" == "arm64" ]]; then
    export NVM_DIR="$HOME/.nvm"
    [ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \. "/opt/homebrew/opt/nvm/nvm.sh"  # This loads nvm
    [ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && \. "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"  
else
    export NVM_DIR="$HOME/.nvm"
    [ -s "/usr/local/opt/nvm/nvm.sh" ] && \. "/usr/local/opt/nvm/nvm.sh"  # This loads nvm
    [ -s "/usr/local/opt/nvm/etc/bash_completion.d/nvm" ] && \. "/usr/local/opt/nvm/etc/bash_completion.d/nvm"  
fi
# Added by LM Studio CLI (lms)
export PATH="$PATH:/Users/danielblessing/.lmstudio/bin"
# End of LM Studio CLI section

