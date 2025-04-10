import hashlib


def get_hashing_algorithms():
    """Prints the available hashing algorithms."""
    print("Hashing algorithms guaranteed to be available on all python platforms:")
    print(sorted(hashlib.algorithms_guaranteed))

    print("\nHashing algorithms available on the current platform:")
    print(sorted(hashlib.algorithms_available))


def hash_message_sha3_256(message):
    """Hashes a message using SHA3-256 and prints the digest and other info."""
    hash_obj = hashlib.sha3_256()
    hash_obj.update(
        message.encode("utf-8")
    )  # Encode the message to bytes and update the hash object
    print("\nSHA3-256:")
    print("Digest (Hex):", hash_obj.hexdigest())  # Print the hexadecimal digest
    print("Digest size:", hash_obj.digest_size, "bytes")
    print("Block size:", hash_obj.block_size, "bytes")
    print("Hash name:", hash_obj.name)

    return hash_obj.hexdigest()


def hash_message_shake_256(message, output_size=100):
    """Hashes a message using SHAKE-256 with specified output size and prints the digest."""
    hash_obj = hashlib.shake_256()
    hash_obj.update(
        message.encode("utf-8")
    )  # Encode the message to bytes and update the hash object
    print("\nSHAKE-256 with output size of", output_size, "bytes:")
    print(
        "Digest (Hex):", hash_obj.hexdigest(output_size)
    )  # Specify output size for digest
    print("Hash name:", hash_obj.name)

    return hash_obj.hexdigest(output_size)


if __name__ == "__main__":
    get_hashing_algorithms()

    # Common used message
    message = "Hello, world!"
    hash_message_sha3_256(message)
    hash_message_shake_256(message)

    # Using the hex() method to convert bytes to hexadecimal
    print("Hello world in hex:", b"Hello, world!".hex())
    print("Testing utf-8 is equal to hex hashing...")
    # Hash hello world in hex
    hash_str = b"Hello, world!"
    hash_obj = hashlib.sha3_256()
    hash_obj.update(hash_str)
    hex_digest = hash_obj.hexdigest()
    print(hex_digest == hash_message_sha3_256(message))
    print(b"Hello World!" == "Hello World!".encode("utf-8"))
