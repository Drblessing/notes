# Tips-n-Tricks

## Table of Contents

1. [AI helper](#ai-helper)
2. [Free VPN](#free-vpn)
3. [Free Static Hosting](#free-static-hosting)
4. [Running applications, packages, or software on any OS](#running-applications-packages-or-software)
5. [DarkWeb](#darkweb)
6. [Security](#security)

## AI helper

LLMs, AI prompting, and AI chatbots are great helps while programming.

Ask chatGPT, google bard, and github codespaces for help.

## Free VPN

With OpenVPN, you can get free config files from [here](https://www.vpngate.net/en/), and [here](https://www.vpnbook.com/).
Be warned, though, that the free VPNs are usually slow, have limited bandwith, and may be stealing your data.

Cloudflare WARP is also a hidden gem that is a free VPN to your local Cloudflare data center.

## Free Static Hosting

You can host static assets a lot of places for free nowadays. Here's a list of some of them:

- [Github raw user content](https://github.com/)
  Soft 50mb limit.
- [Cloudflare Pages](https://pages.cloudflare.com/)
  You can host static assets up to 25mb.
- [Github Pages](https://pages.github.com/)
  You can host static assets up to 1gb.

These are for **hobby** projects. They are not to be used for commercial purposes.

## Running applications, packages, or software on any OS

First off, if you're using x86 Windows, you should switch to Linux or MacOS.

Here's my typical flow of trying to run packages, binaries, applications, software, etc.:

1. **Homebrew**: Check homebrew (or apt or pacman or whatever package manager you use) for the package. If it's there, install it and use it. This is the best option because it has pointers to the correct binary, and will auto-update it for you. Check the output messages for any post-installation instructions.

2. **Docker**: Check docker hub, ghcr, or the github repo for a docker image. If it's there, use it. This is the second best option because it's easy to use, and you can run it on any OS. Check the output messages for any post-installation instructions.

3. **Github**: Check the github repo for a binary. If it's there, download it and use it. This is the third best option because it's easy to use, and you can run it on any OS. Check the output messages for any post-installation instructions.

4. **Build from source**: Check the github repo for a build from source instructions. If it's there, build it and use it. This is the fourth best option because it's easy to use, and you can run it on any OS. Check the output messages for any post-installation instructions.

5. **App Store**: If you don't mind a GUI or App store, you can find it on the MacOS app store or FlatPak.

6. **Code from scratch**: If you can't find it anywhere, you can code it from scratch. This is the worst option because it's hard to do, and you can't run it on any OS.

## DarkWeb

The "darkweb" can be accessed through the official Tor Browser. Your jumping off point is dark.fail. Make sure to PGP verify .onion URLs when you can.

## Security

Well, gather 'round, folks, and let's talk 'bout the wild, unpredictable frontier of digital security. Like the lawless plains of the Wild West, this terrain can be fraught with danger, and a good sheriff knows how to protect his town.

### Passwords

First things first, you gotta have a strong lock on your door to keep the outlaws out. This starts with creating a robust password. Imagine concocting a potent brew that can't easily be replicated. That's where EFF Diceware comes in handy, generating strong, unique, and hard-to-crack passwords.

### Password Manager

Next, you'll be needing a safe to store all those passwords, something like a secure chest where you keep all your gold nuggets. That's what a password manager is - I myself use 1Password. The key to this chest? A solid passphrase brewed up with Diceware.

### 2FA

But having a good lock ain't enough, you need an extra layer of protection. Like having a trusted deputy guarding your door. That's your 2FA (Two-Factor Authentication) - use an authenticator app, not SMS. Now, remember, don't store these backups in your password manager, that's like putting all your eggs in one basket.

### Master Password

Next up, you need the key to the city. This is your master password, used to decrypt your 2FA backups. It should be a strong, unguessable passphrase, again brewed up with Diceware. Don't write this down anywhere, not in a journal or a hidden note, nowhere. This one, you gotta memorize. You could also use Shamir's Secret Sharing Scheme for an added layer of security - like having a map to your hidden gold, but the map is split into parts and shared with trusted friends.

### Encrypting and Decrypting

Lastly, all your precious digital cargo should be safely packed up. Like compressing gold dust into solid bars. That's where tar comes into play, bundling up your data. Then, it needs to be locked up tight in a secure vault - that's where GPG encryption comes into play. This way, even if bandits get to your data, all they'll have is a locked box they can't open.

So there ya have it, partner. With this guide, you're ready to face the wild frontier of the digital world, with your data secure as a fort in the Wild West. Now saddle up and ride forth!
