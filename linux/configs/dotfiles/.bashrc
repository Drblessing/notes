# Interactive shell check
case $- in
    *i*) ;;
      *) return;;
esac

# Prompt
PS1=" \w 🐴 "

# Package management shortcuts
alias up='sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y'
alias myip='curl -s ifconfig.me'

# Path
export PATH="$HOME/github/notes/bin:$HOME/.local/bin:$PATH"

# Disable telemetry
export NEXT_TELEMETRY_DISABLED=1
export GATSBY_TELEMETRY_DISABLED=1

# System Settings
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export TZ=America/Detroit

# History settings
HISTCONTROL=ignoreboth
shopt -s histappend
HISTSIZE=1000
HISTFILESIZE=2000
shopt -s checkwinsize

# Color support for ls, grep, etc.
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# Handy ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Bash completion
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# Welcome message
echo "Welcome to $(hostname)! 😃"
echo "Today is $(date)"
echo ""