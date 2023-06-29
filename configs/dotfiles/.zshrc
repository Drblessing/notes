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
PS1="%1~ 🐴 "

# ---------------------------------------------
# |                                           |
# |            ~/bin added to $PATH           |
# |                                           |
# ---------------------------------------------
export PATH="$HOME/bin:$PATH"
export PATH="$HOME/Github/notes/configs/bin:$PATH"