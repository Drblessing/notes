import pytest
from code.hashing import hash_message_shake_256, hash_message_sha3_256


def test_hash_message_shake_256():
    """Test hash_message_shake_256 function."""
    # Test with default output size
    result = hash_message_shake_256("hello")
    assert len(result) == 200  # 100 bytes = 200 hex characters
    assert isinstance(result, str)

    # Test with custom output size
    result = hash_message_shake_256("hello", output_size=50)
    assert len(result) == 100  # 50 bytes = 100 hex characters

    # Test with empty message
    result = hash_message_shake_256("")
    assert len(result) == 200

    # Test with non-ASCII characters
    result = hash_message_shake_256("héllo")
    assert len(result) == 200

    # Test with long message
    result = hash_message_shake_256("hello" * 1000)
    assert len(result) == 200


def test_hash_message_sha3_256():
    """Test hash_message_sha3_256 function."""
    # Test with empty message
    result = hash_message_sha3_256("")
    assert len(result) == 64  # 32 bytes = 64 hex characters
    assert isinstance(result, str)

    # Test with non-ASCII characters
    result = hash_message_sha3_256("héllo")
    assert len(result) == 64

    # Test with long message
    result = hash_message_sha3_256("hello" * 1000)
    assert len(result) == 64

    # Test hashing "hello world" and compare with the expected hash
    result = hash_message_sha3_256("hello world")
    assert result == "644bcc7e564373040999aac89e7622f3ca71fba1d972fd94a31c3bfbf24e3938"
