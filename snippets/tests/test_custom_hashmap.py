import pytest
from snippets.custom_hashmap import MyHashMap


def test_put_get():
    """Test put and get methods."""
    hashmap = MyHashMap()
    hashmap.put("key1", "value1")
    assert hashmap.get("key1") == "value1"


def test_remove():
    """Test remove method."""
    hashmap = MyHashMap()
    hashmap.put("key1", "value1")
    hashmap.remove("key1")
    assert hashmap.get("key1") is None


def test_contains():
    """Test __contains__ method."""
    hashmap = MyHashMap()
    hashmap.put("key1", "value1")
    assert ("key1" in hashmap) == True


def test_getitem_setitem():
    """Test __getitem__ and __setitem__ methods."""
    hashmap = MyHashMap()
    hashmap["key1"] = "value1"
    assert hashmap["key1"] == "value1"


def test_delitem():
    """Test __delitem__ method."""
    hashmap = MyHashMap()
    hashmap["key1"] = "value1"
    del hashmap["key1"]
    assert ("key1" in hashmap) == False


def test_iter():
    """Test __iter__ method."""
    hashmap = MyHashMap()
    hashmap["key1"] = "value1"
    hashmap["key2"] = "value2"
    keys = [key for key in hashmap]
    assert set(keys) == set(["key1", "key2"])


def test_len():
    """Test __len__ method."""
    hashmap = MyHashMap()
    hashmap["key1"] = "value1"
    hashmap["key2"] = "value2"
    assert len(hashmap) == 2
