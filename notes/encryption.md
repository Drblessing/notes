# Encryption

## Master Passphrase

Passphrases are a group of words that are better than passwords. I'll let XKCD explain:

![XKCD Password Strength](https://imgs.xkcd.com/comics/password_strength.png)

The best way to generate passphrases is to follow the EFF diceware guide: https://www.eff.org/dice

Six words should be enough for most people. If you're paranoid, go for eight.

## Encrypting Files

The GnuPG is the best way to encrypt files. It's a command line tool that can be used to encrypt and decrypt files. Use it with tar to first compress and then encrypt the files.

0. Prestart

[ ] Offline computer
[ ] Disabled Wifi and Bluetooth
[ ] Updated OS
[ ] Updated Virus Scanner
[ ] Update homebrew and packages
[ ] Virus scanned hard drive
[ ] Virus scanned USB drive
[ ] USB drive
[ ] GnuPG installed
[ ] Sha3sum installed
[ ] Secure physical location
[ ] File backups
[ ] Power cable plugged in
[ ] Storage space
[ ] Ample time
[ ] Relaxed state of mind

Install GnuPG

on MacOS:

```bash
brew install gnupg
```

On Linux:

```bash
sudo apt install gnupg
```

Verify the installation:

```bash
gpg --version
```

Install sha3sum:

On MacOS:

```bash
brew install sha3sum
```

On Linux:

```bash
sudo apt install sha3sum
```

Verify the installation:

```bash
sha3sum --version
```

1. Compress the files

```bash
tar -acvf secrets.tgz secrets
```

2. Take files keccak256 hash

```bash
keccak-256sum secrets.tgz > secrets.tgz.keccak256
```

3. Encrypt the files

With your diceware passphrase:

```bash
gpg --no-symkey-cache -c secrets.tgz
```

Note: If it tells you "Warning: You have entered an insecure passphrase.", then ignore it and click "<Take this oneanyway>". If you have followed the diceware guide, then your passprhase is secure. Refer back to the xkcd comic above.

4. Take encrypted files keccak256 hash

```bash
keccak-256sum secrets.tgz.gpg > secrets.tgz.gpg.keccak256
```

5. Test decryption

```bash
gpg --no-symkey-cache -d secrets.tgz.gpg > secrets.tgz
```

6. Verify hashes

```bash
keccak-256sum -c secrets.tgz.keccak256
```

Or you can do it manually.

7. Export

Save the following files to a USB drive:

- secrets.tgz.gpg
- secrets.tgz.gpg.keccak256
- secrets.tgz.keccak256

Delete the following files from your computer:

- secrets.tgz
- secrets/

There should be no trace of the files on your computer.

## Decrypting Files

0. Prestart

[ ] Offline computer
[ ] Disabled Wifi and Bluetooth
[ ] Updated OS
[ ] Updated Virus Scanner
[ ] Update homebrew and packages
[ ] Virus scanned hard drive
[ ] Virus scanned USB drive
[ ] USB drive
[ ] GnuPG installed
[ ] Sha3sum installed
[ ] Secure physical location
[ ] File backups
[ ] Power cable plugged in
[ ] Storage space
[ ] Ample time
[ ] Relaxed state of mind

1. Import files

Import the following files from the USB drive:

- secrets.tgz.gpg
- secrets.tgz.gpg.keccak256
- secrets.tgz.keccak256

2. Verify hashes

```bash
keccak-256sum -c secrets.tgz.gpg.keccak256
```

Or you can do it manually. Check the hash if you saved it elsewhare too.

3. Decrypt the files

```bash
gpg --no-symkey-cache -d secrets.tgz.gpg > secrets.tgz
```

4. Verify hashes

```bash
keccak-256sum -c secrets.tgz.keccak256
```

Or you can do it manually.

5. Extract the files

```bash
tar -xvf secrets.tgz
```

6. Delete the files

Delete the following files from your computer :

- secrets.tgz
- secrets.tgz.gpg
- secrets.tgz.gpg.keccak256
- secrets.tgz.keccak256
- secrets/

There should be no trace of the files on your computer.

## Summary

Congrats! You've just encrypted and decrypted files. You can now use this to encrypt your passwords, private keys, and other sensitive information.

A note on verifying hashes: it ensures the encrypted files have not been tampered with or been corrupted.

Also, if you want to fully delete the files, you can use a cli like `shred`. You can also never let the files touch your computer, and always keep them on a USB drive. This is the most secure way to do it.

If you're really paranoid, you can use a live boot environment like a USB drive with Tails OS. This is the most secure way to do it.
