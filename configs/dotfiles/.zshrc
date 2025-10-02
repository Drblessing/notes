# Giddy up, partner!
# PS1=" %1~ 🐴 " Disabled to debug vscode integrated terminal

# Homebrew
if [[ "$(uname -m)" == "arm64" ]]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
else
    eval "$(/usr/local/bin/brew shellenv)"
fi

# nvm 
export NVM_DIR="$HOME/.nvm"
if [[ -n "$HOMEBREW_PREFIX" ]]; then
  [[ -s "$HOMEBREW_PREFIX/opt/nvm/nvm.sh" ]] && . "$HOMEBREW_PREFIX/opt/nvm/nvm.sh"
  [[ -s "$HOMEBREW_PREFIX/opt/nvm/etc/bash_completion.d/nvm" ]] && . "$HOMEBREW_PREFIX/opt/nvm/etc/bash_completion.d/nvm"
fi

# LM Studio
export PATH="$PATH:$HOME/.lmstudio/bin"

# Disable telemetry
export HOMEBREW_NO_ANALYTICS=1
export NEXT_TELEMETRY_DISABLED=1

# Vscode "code" command
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"