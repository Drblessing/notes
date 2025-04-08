# Configs

## Overview

I like MacOS configurd to be cozy and easy.

## Installation

I keep my configuration in this Githup repository for easy access and syncing across machines.

On new machines, I first install homebrew, then git, then clone this repository.

Then, I symlink my ~/.zshrc to [dotfiles/zshrc](dotfiles/.zshrc) as well as my .zshenv, and .zprofile.

```
cp ~/.zshrc ~/.zshrc.bak
cp ~/.zshenv ~/.zshenv.bak
cp ~/.zprofile ~/.zprofile.bak
rm ~/.zshrc
rm ~/.zshenv
rm ~/.zprofile
ln -s ~/Github/configs/dotfiles/.zshrc ~/.zshrc
ln -s ~/Github/configs/dotfiles/.zshenv ~/.zshenv
ln -s ~/Github/configs/dotfiles/.zprofile ~/.zprofile
```

Then, I add my ~/Github/notes/configs/bin to my $PATH in my .zshrc.

```
echo "PATH=$PATH:~/Github/configs/bin" > ~/.zshrc
```

Now, I can edit my configs and scripts and push them to Github, and they'll be installed on all my machines.

## Python Installation

I use homebrew to manage my python installations and easily update them. In scenarios where this is inconvenient, I'll install the specific version using the python installer from pyhton.org, or build from source.

I always use virtual environments for my python projects.

## Node Installation

I use nvm installed via homebrew to manage my node and npm.

## dotfiles

Smiles!

## bin

Full of scripts I use. I symlink this to my $PATH so I can run them from anywhere.

Check them out [here](/bin/bin.md).

Most are python and bash scripts.

```

```
