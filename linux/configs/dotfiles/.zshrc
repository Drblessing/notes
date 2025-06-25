# ---------------------------------------------
# |                                           |
# |            ZSH Configuration              |
# |                                           |
# ---------------------------------------------

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# ---------------------------------------------
# |                                           |
# |            Prompt Configuration           |
# |                                           |
# ---------------------------------------------
PS1=" %1~ 😃 "

# ---------------------------------------------
# |                                           |
# |              History Configuration        |
# |                                           |
# ---------------------------------------------
HISTSIZE=1000
SAVEHIST=1000
HISTFILE=~/.zsh_history
setopt SHARE_HISTORY
setopt HIST_IGNORE_DUPS
setopt HIST_IGNORE_ALL_DUPS
setopt HIST_IGNORE_SPACE

# ---------------------------------------------
# |                                           |
# |              ZSH Options                  |
# |                                           |
# ---------------------------------------------
setopt AUTO_CD
setopt CORRECT
setopt GLOB_DOTS
setopt NO_CASE_GLOB

# ---------------------------------------------
# |                                           |
# |              Aliases                      |
# |                                           |
# ---------------------------------------------
alias notes="cd ~/Github/notes"
alias c="clear"
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'

# Package management shortcuts
alias apt-update='sudo apt update && sudo apt upgrade'
alias apt-search='apt search'
alias apt-install='sudo apt install'

# System shortcuts
alias ports='sudo netstat -tuln'
alias myip='curl ifconfig.me'
alias weather='curl wttr.in'

# Git shortcuts
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline'

# ---------------------------------------------
# |                                           |
# |              Path Configuration           |
# |                                           |
# ---------------------------------------------
export PATH="$HOME/Github/notes/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"

# ---------------------------------------------
# |                                           |
# |              Node.js Configuration        |
# |                                           |
# ---------------------------------------------
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

# ---------------------------------------------
# |                                           |
# |              Python Configuration         |
# |                                           |
# ---------------------------------------------
alias ve='python3 -m venv'
alias va='source venv/bin/activate'

# ---------------------------------------------
# |                                           |
# |              Environment Variables        |
# |                                           |
# ---------------------------------------------
export EDITOR=vim
export VISUAL=vim
export BROWSER=lynx
export PAGER=less

# Disable telemetry
export HOMEBREW_NO_ANALYTICS=1
export NEXT_TELEMETRY_DISABLED=1
export GATSBY_TELEMETRY_DISABLED=1

# ---------------------------------------------
# |                                           |
# |              Custom Functions             |
# |                                           |
# ---------------------------------------------
mkcd() {
    mkdir -p "$1" && cd "$1"
}

extract() {
    if [ -f $1 ] ; then
        case $1 in
            *.tar.bz2)   tar xjf $1     ;;
            *.tar.gz)    tar xzf $1     ;;
            *.bz2)       bunzip2 $1     ;;
            *.rar)       unrar e $1     ;;
            *.gz)        gunzip $1      ;;
            *.tar)       tar xf $1      ;;
            *.tbz2)      tar xjf $1     ;;
            *.tgz)       tar xzf $1     ;;
            *.zip)       unzip $1       ;;
            *.Z)         uncompress $1  ;;
            *.7z)        7z x $1        ;;
            *)     echo "'$1' cannot be extracted via extract()" ;;
        esac
    else
        echo "'$1' is not a valid file"
    fi
}

psg() {
    ps aux | grep -v grep | grep "$1" -i --color=auto
}

serverstatus() {
    echo "=== System Information ==="
    uname -a
    echo ""
    echo "=== Uptime ==="
    uptime
    echo ""
    echo "=== Disk Usage ==="
    df -h
    echo ""
    echo "=== Memory Usage ==="
    free -h
    echo ""
    echo "=== Network Connections ==="
    sudo netstat -tuln | grep LISTEN
}
