# ---------------------------------------------
# |                                           |
# |              Homebrew Configuration       |
# |                                           |
# ---------------------------------------------
eval "$(/opt/homebrew/bin/brew shellenv)"

# ---------------------------------------------
# |                                           |
# |              Pyenv Configuration          |
# |                                           |
# ---------------------------------------------
# if command -v pyenv 1>/dev/null 2>&1; then
#   eval "$(pyenv init -)"
# fi

# ---------------------------------------------
# |                                           |
# |              Rust Configuration           |
# |                                           |
# ---------------------------------------------
. "$HOME/.cargo/env"

# ---------------------------------------------
# |                                           |
# |              Foundry Configuration        |
# |                                           |
# ---------------------------------------------
export PATH="$PATH:/Users/dbless/.foundry/bin"
