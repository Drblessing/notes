Generating PGP and SSH keys securely is important to protect your encrypted data and SSH sessions. You need to use the GPG (GNU Privacy Guard) for generating PGP keys and ssh-keygen for SSH keys.

Please follow these steps:

PGP Key Generation:

Open Terminal and ensure GPG is installed by typing gpg --version. If it's not installed, you can install it using brew install gpg.

Generate a new key pair: gpg --full-generate-key

You will be asked to choose the type of key you want. Choose "RSA and RSA" which works for both signatures and encryption.

Set the key size. To future-proof your key, you may want to use 4096 bits.

Set the expiration date for your key. Given your requirements, you might want to set it to "never".

Verify the details and confirm.

You will then be prompted for user information: name, email, and optionally a comment.

You'll also be prompted to enter a passphrase. Choose a strong passphrase and keep it safe.

The key generation will begin. This process can take some time depending on the key size and the performance of your computer.

SSH Key Generation:

In the Terminal, type: ssh-keygen -t rsa -b 4096. This generates a 4096-bit RSA key pair.

When prompted to "Enter file in which to save the key," press Enter to accept the default file location.

At the prompt, type a secure passphrase. It is advised to use a passphrase for your SSH key, but you can also create a key without a passphrase.

That's it. You've created your SSH key.

After generation, you may want to export your keys to a safe place:

For PGP: gpg --output ~/Desktop/mykey.sec --armor --export-secret-keys YOURKEYIDHERE

For SSH: Just copy id_rsa and id_rsa.pub files usually found in the ~/.ssh/ directory.

To encrypt these keys with GPG, you can use the following commands:

For PGP: gpg -c ~/Desktop/mykey.sec
For SSH: gpg -c ~/.ssh/id_rsa
This will create a file with .gpg extension which is the encrypted version of your file. You will be asked to set a passphrase which will be used to decrypt the file later.

You can decrypt the files with the command gpg -d filename.gpg > filename.

Remember to keep your keys and passphrases in a secure place. If you lose them, you won't be able to decrypt your data.

Also, it is good to remember to rotate your keys regularly. Even if you set your keys to never expire, it is still a good security practice to rotate keys at regular intervals.

It's worth noting that while 4096-bit RSA keys are currently very secure, no encryption is future-proof. Advances in technology, including the development of quantum computers, could eventually make it possible to break these keys.
