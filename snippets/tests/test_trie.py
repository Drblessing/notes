import pytest
from src.trie import Trie


def test_insert_search():
    """Test insert and search methods."""
    trie = Trie()
    trie.insert("hello")
    assert trie.search("hello") == True
    assert trie.search("hell") == False
    assert trie.search("helloo") == False
    assert trie.search("world") == False


def test_delete():
    """Test delete method."""
    trie = Trie()
    trie.insert("hello")
    trie.delete("hello")
    assert trie.search("hello") == False


def test_starts_with():
    """Test starts_with method."""
    trie = Trie()
    trie.insert("hello")
    assert trie.starts_with("hell") == True
    assert trie.starts_with("hello") == True
    assert trie.starts_with("helloo") == False
    assert trie.starts_with("world") == False
