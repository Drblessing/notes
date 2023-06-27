# Tips-n-Tricks

## Table of Contents

1. [Free VPN](#free-vpn)
2. [Running applications, packages, or software on any OS](#running-applications-packages-or-software)

## Free VPN

With OpenVPN, you can get free config files from [here](https://www.vpngate.net/en/), and [here](https://www.vpnbook.com/).
Be warned, though, that the free VPNs are usually slow, have limited bandwith, and may be stealing your data.

## Running applications, packages, or software on any OS

First off, if you're using x86 Windows, you should switch to Linux or MacOS.

Here's my typical flow of trying to run packages, binaries, applications, software, etc.:

1. **Homebrew**: Check homebrew (or apt or pacman or whatever package manager you use) for the package. If it's there, install it and use it. This is the best option because it has pointers to the correct binary, and will auto-update it for you. Check the output messages for any post-installation instructions.

2. **Docker**: Check docker hub, ghcr, or the github repo for a docker image. If it's there, use it. This is the second best option because it's easy to use, and you can run it on any OS. Check the output messages for any post-installation instructions.

3. **Github**: Check the github repo for a binary. If it's there, download it and use it. This is the third best option because it's easy to use, and you can run it on any OS. Check the output messages for any post-installation instructions.

4. **Build from source**: Check the github repo for a build from source instructions. If it's there, build it and use it. This is the fourth best option because it's easy to use, and you can run it on any OS. Check the output messages for any post-installation instructions.

5. **App Store**: If you don't mind a GUI or App store, you can find it on the MacOS app store or FlatPak.

6. **Code from scratch**: If you can't find it anywhere, you can code it from scratch. This is the worst option because it's hard to do, and you can't run it on any OS.
