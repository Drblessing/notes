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
    # if len(seq) == 0:
    #     return

    if window_size > len(seq):
        raise ValueError("window_size must be smaller than seq length.")
    if step > window_size:
        raise ValueError("step must be smaller than or equal to window_size.")
    if step < 1:
        raise ValueError("step must be a positive integer.")
    for i in range(0, len(seq) - window_size + 1, step):
        yield seq[i : i + window_size]
