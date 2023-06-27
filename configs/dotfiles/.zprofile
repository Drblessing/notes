# ---------------------------------------------
# |                                           |
# |              Homebrew Configuration       |
# |                                           |
# ---------------------------------------------
eval "$(/opt/homebrew/bin/brew shellenv)"

# ---------------------------------------------
# |                                           |
# |              Poetry Configuration         |
# |                                           |
# ---------------------------------------------
export PATH="/Users/dbless/.local/bin:$PATH"

# ---------------------------------------------
# |                                           |
# |              Pyenv Configuration          |
# |                                           |
# ---------------------------------------------
# if command -v pyenv 1>/dev/null 2>&1; then
#   eval "$(pyenv init -)"
# fi