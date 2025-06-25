# ---------------------------------------------
# |                                           |
# |            Bash Profile Configuration     |
# |                                           |
# ---------------------------------------------

# Source .bashrc if it exists
if [ -f ~/.bashrc ]; then
    . ~/.bashrc
fi

# ---------------------------------------------
# |                                           |
# |            Environment Variables          |
# |                                           |
# ---------------------------------------------
export PATH="$HOME/Github/notes/bin:$PATH"
export PATH="$HOME/.local/bin:$PATH"

# ---------------------------------------------
# |                                           |
# |            System Settings                |
# |                                           |
# ---------------------------------------------
# Set default editor
export EDITOR=vim
export VISUAL=vim

# Set locale
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

# ---------------------------------------------
# |                                           |
# |            Welcome Message                |
# |                                           |
# ---------------------------------------------
echo "Welcome to $(hostname)! 😃"
echo "Today is $(date)"
echo ""

# Show system info on login (only for interactive shells)
if [[ $- == *i* ]] && command -v neofetch &> /dev/null; then
    neofetch
fi
