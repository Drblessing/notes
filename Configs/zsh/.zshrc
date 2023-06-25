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
# |        Google Cloud SDK Configuration     |
# |                                           |
# ---------------------------------------------
if [ -f '/Users/dbless/google-cloud-sdk/path.zsh.inc' ]; then . '/Users/dbless/google-cloud-sdk/path.zsh.inc'; fi
if [ -f '/Users/dbless/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/dbless/google-cloud-sdk/completion.zsh.inc'; fi

# ---------------------------------------------
# |                                           |
# |          OpenJDK Configuration            |
# |                                           |
# ---------------------------------------------
export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"

# ---------------------------------------------
# |                                           |
# |         WakaTime Configuration            |
# |                                           |
# ---------------------------------------------
export WAKA="<API_KEY>"

# ---------------------------------------------
# |                                           |
# |            Prompt Configuration           |
# |                                           |
# ---------------------------------------------
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
# |        Google Cloud SDK Configuration     |
# |                                           |
# ---------------------------------------------
if [ -f '/Users/dbless/google-cloud-sdk/path.zsh.inc' ]; then . '/Users/dbless/google-cloud-sdk/path.zsh.inc'; fi
if [ -f '/Users/dbless/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/dbless/google-cloud-sdk/completion.zsh.inc'; fi

# ---------------------------------------------
# |                                           |
# |          OpenJDK Configuration            |
# |                                           |
# ---------------------------------------------
export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"

# ---------------------------------------------
# |                                           |
# |         WakaTime Configuration            |
# |                                           |
# ---------------------------------------------
export WAKA="<API_KEY>"

# ---------------------------------------------
# |                                           |
# |            Prompt Configuration           |
# |                                           |
# ---------------------------------------------
PS1="%1~ 🐴 "

# ---------------------------------------------
# |                                           |
# |            ~/bin added to $PATH           |
# |                                           |
# ---------------------------------------------
export PATH="$HOME/bin:$PATH"