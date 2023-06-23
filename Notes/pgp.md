# Pretty Good Privacy (PGP)

Pretty Good Privacy (PGP) is a cryptography tool that allows you to encrypt and sign data.

**Encryption:** You can encrypt a file with the public key of the recipient. The recipient can then decrypt the file with their private key.

**Signing:** You can sign a file with your private key. The recipient can then verify the signature with your public key.

PGP keys are stored in pairs: a public key and a private key. Public keys are shared with others. Private keys are kept secret.

In PGP, a public keys is a cryptographic key that is used for encryption, verification of digital signature, and key exchange. It is part of an asymmetric key pair, which also includes a correspnoding private key. A public key is typically much longer than 256 bytes, and often represented in ASCII armor format, which includes the key material along with metadata. The size of the public key can vary depending on the specific encryption algorithm and key size used. For example, the RSA-based public keys used are typically represented by the modulus (N) and the public exponent (e). The size of the modulus determines the key size, and common key sizes range from 128 bytes to 512 bytes or even larger. The actual size of the public key in ASCII armor format would be larger than the raw key material due to additional metadata, such as headers and formatting. The size of the public key doesn't directly correlate with its security, the strength of the key depends on the specific encryption algorithm and key size. The ASCII armor format is a way of representing binary data, in plain text format. The binary data is encoded using ASCII characters.

PGP is closed source, whereas GNU Privacy Guard (GPG) is open source. GPG is a free implementation of PGP. GPG is the most widely used implementation of PGP.
