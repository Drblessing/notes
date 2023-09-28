# Configs

## Overview

On new machines, I run [startup.sh](startup/startup.sh) to install all the programs I use. This is a WIP so it's not perfect yet.
This repo is always installed at ~/Github/notes, and I control all code, so I can be sure it's safe.

```bash
./startup.sh
```

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

## dotfiles

I have nothing too special in my .zshrc et al., just commands from software I have installed, adding the Github bin, and commenting/uncommenting pyenv when I need it.

## bin

Full of scripts I use. I symlink this to my $PATH so I can run them from anywhere.

Check them out [here](/bin/bin.md).

Most are python and bash scripts.
