# nvm_initialize
# Assume nvm is already installed
# either via homebrew or apt

mkdir -p ~/.nvm
nvm install --lts

# Install global packages from ~/github/notes/configs/npm/npm-global.txt
echo "Installing global npm packages..."
xargs npm install -g < ~/github/notes/configs/npm/npm-global.txt