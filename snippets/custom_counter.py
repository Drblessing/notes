"""
This module contains a custom conter class, to show 
how the counter in the collections module works.
"""

from collections import Counter  # To test at the end
from random import randint


class MyCounter:
    """A custom implementation of the Counter class."""

    def __init__(self, iterable=None):
        self._data = {}
        if iterable is not None:
            for item in iterable:
                if item in self._data:
                    self._data[item] += 1
                else:
                    self._data[item] = 1

    def __repr__(self):
        return f"MyCounter({self._data})"

    def __getitem__(self, item):
        """Returns the count of the item, 0 if not found."""
        return self._data.get(item, 0)

    def __setitem__(self, item, count):
        """Sets the count of the item."""
        self._data[item] = count

    def __delitem__(self, item):
        """Deletes the item from the counter."""
        if item in self._data:
            del self._data[item]

    def __iter__(self):
        """Allows iteration over the counter's elements (keys)."""
        return iter(self._data)

    def __len__(self):
        """Returns the number of unique elements."""
        return len(self._data)

    def items(self):
        """Returns a set-like object providing a view on the counter's items."""
        return self._data.items()

    def keys(self):
        """Returns an object providing a view on the counter's keys."""
        return self._data.keys()

    def values(self):
        """Returns an object providing a view on the counter's values."""
        return self._data.values()

    def get(self, item, default=None):
        """Returns the count of the item, or default if not found."""
        return self._data.get(item, default)

    def most_common(self, n=None):
        """Returns a list of the n most common elements and their counts.
        If n is None, returns all elements in descending order of count."""
        return sorted(self._data.items(), key=lambda item: item[1], reverse=True)[:n]

    def total(self):
        """Returns the total count of all items in the counter."""
        return sum(self._data.values())

    # Additional methods can be implemented to mimic Counter's functionality further.


if __name__ == "__main__":
    nums = [randint(1, 10) for _ in range(100)]
    cc = MyCounter(nums)
    print(cc)
    counter = Counter(nums)
    print(counter)
