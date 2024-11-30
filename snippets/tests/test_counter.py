import pytest
from code.custom_counter import MyCounter


def test_counter():
    """Test MyCounter class."""
    counter = MyCounter("abracadabra")

    # Test __repr__
    assert repr(counter) == "MyCounter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})"

    # Test __getitem__
    assert counter["a"] == 5
    assert counter["b"] == 2
    assert counter["z"] == 0  # Not in counter

    # Test __setitem__
    counter["z"] = 1
    assert counter["z"] == 1

    # Test __delitem__
    del counter["z"]
    assert counter["z"] == 0

    # Test __iter__
    assert set(iter(counter)) == set("abrcd")

    # Test __len__
    assert len(counter) == 5

    # Test items, keys, values
    assert set(counter.items()) == set(
        [("a", 5), ("b", 2), ("r", 2), ("c", 1), ("d", 1)]
    )
    assert set(counter.keys()) == set("abrcd")
    assert set(counter.values()) == set([1, 2, 5])

    # Test get
    assert counter.get("a") == 5
    assert counter.get("z") == None
    assert counter.get("z", 0) == 0

    # Test most_common
    assert counter.most_common() == [("a", 5), ("b", 2), ("r", 2), ("c", 1), ("d", 1)]
    assert counter.most_common(2) == [("a", 5), ("b", 2)]

    # Test total
    assert counter.total() == 11
