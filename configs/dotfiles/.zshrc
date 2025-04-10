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