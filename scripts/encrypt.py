from base64 import urlsafe_b64encode
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet


def derive_simple_key(password: str) -> bytes:
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password.encode())
    # Use urlsafe_b64encode to ensure the hash can be used as a Fernet key
    return urlsafe_b64encode(digest.finalize())


def encrypt_seed(seed_phrase: str, password: str) -> bytes:
    key = derive_simple_key(password)
    f = Fernet(key)
    return f.encrypt(seed_phrase.encode())


def decrypt_seed(encrypted_seed: bytes, password: str) -> str:
    key = derive_simple_key(password)
    f = Fernet(key)
    return f.decrypt(encrypted_seed).decode()