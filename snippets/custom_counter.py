"""
This module contains a custom conter class, to show 
how the counter in the collections module works.
"""

from collections import Counter  # To test at the end
from random import randint


class MyCounter:
    """A custom implementation of the Counter class."""

    def __init__(self, iterable):
        self._data = {}
        for item in iterable:
            if item in self._data:
                self._data[item] += 1
            else:
                self._data[item] = 1


if __name__ == "__main__":
    nums = [randint(1, 10) for _ in range(100)]
    cc = MyCounter(nums)
    print(cc)
    counter = Counter(nums)
    print(counter)
