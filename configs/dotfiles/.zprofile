# ---------------------------------------------
# |                                           |
# |              Homebrew Configuration       |
# |                                           |
# ---------------------------------------------
if [[ "$(uname -m)" == *"arm"* ]]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi
export HOMEBREW_NO_ANALYTICS=1
