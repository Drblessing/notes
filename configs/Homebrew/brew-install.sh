#!/bin/bash

# Check if Homebrew is installed and install if we don't have it
if test ! $(which brew); then
  echo "Installing homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

brew update

echo "Installing packages..."
cat brew-list.txt | while read package || [[ -n "$package" ]]; do
  brew install $package
done

echo "Cleaning up..."
brew cleanup