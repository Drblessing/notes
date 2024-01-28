"""
This module contains utility functions for creating and handling sliding windows
on sequences. These functions are useful for operations on sequences where
window-based processing is required.

Functions: 
    - sliding_window: Returns a generator that will iterate through the defined
        chunks of input sequence. Input sequence must be iterable.
"""

from collections.abc import Iterable, Generator, Sequence


def sliding_window[
    T
](seq: Sequence[T], window_size: int, step: int = 1) -> Generator[
    Sequence[T], None, None
]:
    """Returns a generator that will iterate through
    the defined chunks of input sequence. Input sequence
    must be iterable.
    """

    if not isinstance(seq, Iterable):
        raise TypeError("seq must be iterable.")
    if not isinstance(window_size, int):
        raise TypeError("window_size must be int.")
    if not isinstance(step, int):
        raise TypeError("step must be int.")

    # Handle edge cases
    # Empty sequence
    # Create a generator that returns nothing
    if len(seq) == 0:
        return

    if window_size > len(seq):
        raise ValueError("window_size must be smaller than seq length.")
    if step > window_size:
        raise ValueError("step must be smaller than or equal to window_size.")
    if step < 1:
        raise ValueError("step must be a positive integer.")
    for i in range(0, len(seq) - window_size + 1, step):
        yield seq[i : i + window_size]


# Testing and Examples
if __name__ == "__main__":
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
    try:
        list(sliding_window(seq, window_size, step))
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")

    # Test with an empty sequence
    seq = []
    window_size = 3
    step = 1
    result = list(sliding_window(seq, window_size, step))
    assert result == []
