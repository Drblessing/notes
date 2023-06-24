# PGP

## Table of Contents

Introduction
<br>Installing GPG
<br>Creating a New Key Pair
<br>Exporting Your Public Key
<br>Sharing Your Public Key to a Keyserver
<br>Importing Someone Else's Public Key
<br>Encrypting a Message
<br>Decrypting a Message
<br>Signing a Message
<br>Verifying a Signed Message
<br>Conclusion and Further Resources

## Introduction

Welcome to our tutorial on using the GPG Command Line Interface (CLI) to manage your PGP keys and encrypt your communication. In this tutorial, we will walk you through everything you need to know to get started, from installing GPG to encrypting and signing messages. By the end of this tutorial, you'll be able to generate your own PGP keys, share them on a keyserver, and encrypt and sign your messages.

## Installing GPG

Before we start working with PGP keys and messages, we first need to install GnuPG (GPG), the open-source implementation of PGP. You can download it from the official website: https://gnupg.org/

For users on a Unix-like operating system such as Linux or macOS, GnuPG can typically be installed through the terminal using package managers like `apt` or `brew`. For example, on a Debian-based Linux system, you would use the following command:

```bash
sudo apt-get install gnupg
```

On macOS, you can install GnuPG using Homebrew:

```bash
brew install gnupg
```

Windows users can download here: https://gpg4win.org/

## Creating a New Key Pair

Once you have GnuPG installed, the first thing you will need to do is to create your key pair. This includes both your public key, which others will use to encrypt messages to you, and your private key, which you will use to decrypt those messages.

You can generate a new key pair with the following command:

```bash
gpg --full-generate-key
```

To get the key fingerprint, you can ues the `--fingerprint` command:

```bash
gpg --fingerprint <your email address>
```

## Exporting Your Public Key

Once you have generated your key pair, you will need to export your public key so that you can share it with others. You can do this with the following command:

```bash
gpg --armor --export <your email address> > public_key.asc
```

## Sharing Your Public Key to a Keyserver

Keyservers are online databases where you can upload your public key to make it easily accessible to others. To share your public key to a keyserver, you can use the `--send-keys` command, with the key id or the email address:

```bash
gpg --send-keys <your-email>
```

or:

```bash
gpg --send-keys <key-fingerprint>
```

To set your keyserver on your pgp config file, you can use the following command:

```bash
gpg --keyserver <keyserver url> --send-keys <key fingerprint>
```

## Importing Someone Else's Public Key

To import someone else's public key, you can use the `--import` command:

```bash
gpg --import <public_key.asc>
```

Alternatively, you can import a public key from a keyserver using the `--recv-keys` command:

```bash
gpg --keyserver <keyserver url> --recv-keys <key fingerprint>
```

## Encrypting a Message

Once you have imported someone else's public key, you can use it to encrypt a message to them.

First, suppose you have a text file named `message.txt` that you want to encrypt.

You can do this with the `--encrypt` command:

```bash
gpg --encrypt --recipient <recipient email> message.txt
```

You can list the keys in your keyring with the `--list-keys` command:

```bash
gpg --list-keys
```

To import a public key from a keyserver using the `--recv-keys` command:

```bash
gpg --keyserver <keyserver url> --recv-keys <key fingerprint>
```

## Decrypting a Message

Once you have received an encrypted message, you can decrypt it using the `--decrypt` command:

```bash
gpg --decrypt message.txt.gpg > message.txt
```

## Signing a Message

You can sign a message using the `--sign` command:

```bash
gpg --sign message.txt
```

## Verifying a Signed Message

You can verify a signed message using the `--verify` command:

```bash
gpg --verify message.txt.gpg
```

## Conclusion and Further Resources

Congratulations, you now know the basics of using GnuPG on the command line! With these skills, you can generate your own PGP keys, encrypt and sign your messages, and verify the authenticity of received messages. As with any security tool, remember to keep your private key secure and regularly update your keyring with the latest public keys from your contacts.

For further learning, we recommend checking out the GnuPG manual and the following online resources:

- [GnuPG Manual](https://www.gnupg.org/documentation/manuals/gnupg/)
- [MIT PGP Public Key Server](https://pgp.mit.edu/)
- [Email Self-Defense](https://emailselfdefense.fsf.org/en/)

Remember, security is an ongoing process, not a one-time setup. Stay safe and secure out there!

Happy encrypting!
