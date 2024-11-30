import pytest
from code.sliding_window import sliding_window


def test_sliding_window():
    # Test with a list of integers
    seq = [1, 2, 3, 4, 5, 6]
    window_size = 3
    step = 1
    result = list(sliding_window(seq, window_size, step))
    assert result == [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]

    # Test with a string
    seq = "abcdef"
    window_size = 3
    step = 1
    result = list(sliding_window(seq, window_size, step))
    assert result == ["abc", "bcd", "cde", "def"]

    # Test with a larger step
    seq = [1, 2, 3, 4, 5, 6]
    window_size = 3
    step = 2
    result = list(sliding_window(seq, window_size, step))
    assert result == [[1, 2, 3], [3, 4, 5]]

    # Test with a window size larger than the sequence
    seq = [1, 2, 3]
    window_size = 5
    step = 1
    with pytest.raises(ValueError):
        list(sliding_window(seq, window_size, step))

    # Test with an empty sequence
    seq = []
    window_size = 3
    step = 1
    result = list(sliding_window(seq, window_size, step))
    assert result == []
