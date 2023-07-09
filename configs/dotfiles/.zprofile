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
# |              Pyenv Configuration          |
# |                                           |
# ---------------------------------------------
# if command -v pyenv 1>/dev/null 2>&1; then
#   eval "$(pyenv init -)"
# fi
