# PGP

## Introduction

Welcome to my tutorial on using the GPG Command Line Interface (CLI) to manage my PGP keys and encrypt your communication. In this tutorial, we will walk you through everything you need to know to get started, from installing GPG to encrypting and signing messages. By the end of this tutorial, you'll be able to generate your own PGP keys, share them on a keyserver, and encrypt and sign your messages.

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

To list keyids, you can use the `--list-keys` command.
Keyids are the last 8 characters of the fingerprint.

```bash
gpg --list-keys --keyid short
```

To get the key fingerprint, you can ues the `--fingerprint` command:

While both Key IDs and fingerprints can be used to identify GPG keys, fingerprints are generally considered more reliable for verification purposes. When sharing your public key with others, it is recommended to provide the fingerprint to ensure that the correct key is being used.

When using GPG commands or interacting with keys, both Key IDs and fingerprints can be used interchangeably, depending on the context and requirements of the specific operation.

```bash
gpg --fingerprint <your email address>
```

## Exporting Your Public Key

Once you have generated your key pair, you will need to export your public key so that you can share it with others. You can do this with the following command:

```bash
gpg --armor --export <your email address, or keyid> > public_key.asc
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

You can also clear-sign, which will sign the message and output plaintext:

```bash
gpg --clear-sign message.txt
```

You can also create a detached signature, which will output the signature to a separate file:

```bash
gpg --detach-sign message.txt
```

Note that while the output may still have the .gpg extension, it is not an encrypted file, but rather a signature file, and anyone can read it and verify the signature.

## Verifying a Signed Message

You can verify a signed message using the `--verify` command:

```bash
gpg --verify message.txt.gpg
```

## Encrypting and Signing a Message

You can encrypt and sign a message using the `--encrypt` and `--sign` commands together:

```bash
gpg --encrypt --sign --recipient <recipient email> message.txt
```

Note that only the recipient will be able to decrypt the message and verify the signature.

## Notes

There's a lot going on here, let's recap. We'll break it down by file extensions.

**.sig:** This is a detached signature. It is not encrypted, and anyone can read it. It can be used to verify the authenticity of a signed message, that is not included in the file.

**.asc:** This is an ASCII-armored public key. It is not encrypted, and anyone can read it. It can be used to encrypt messages to the key owner. It can also be the output of a clear signature, which includes the message and the signature verifying it. This is also always unencrypted.

**.gpg:** Either encrypted or unencrypted. One possibility is that this is an encrypted message to a recipient of a public key. The encrypted message is either signed or unsigned. Only the recipient can verify the signature, because it has to be decrypted first. It can also be an uncrypted but signed message from a sender. Anyone can read the message, and verify the signature, if they have the public key of the sender.

## Conclusion and Further Resources

Congratulations, you now know the basics of using GnuPG on the command line! With these skills, you can generate your own PGP keys, encrypt and sign your messages, and verify the authenticity of received messages. As with any security tool, remember to keep your private key secure and regularly update your keyring with the latest public keys from your contacts.

For further learning, we recommend checking out the GnuPG manual and the following online resources:

- [GnuPG Manual](https://www.gnupg.org/documentation/manuals/gnupg/)
- [MIT PGP Public Key Server](https://pgp.mit.edu/)
- [Email Self-Defense](https://emailselfdefense.fsf.org/en/)

Remember, security is an ongoing process, not a one-time setup. Stay safe and secure out there!

Happy encrypting!
