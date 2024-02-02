"""
This module contains a custom conter class, to show 
how the counter in the collections module works.
"""

from collections import Counter
from random import randint


class CustomCounter:
    def __init__(self, data):
        self.data = data
        self.counter = Counter(data)

    def __repr__(self):
        return f"CustomCounter({self.data})"

    def __str__(self):
        return f"CustomCounter({self.data})"

    def most_common(self, n=5):
        return self.counter.most_common(n)

    def subtract(self, data):
        self.counter.subtract(data)

    def update(self, data):
        self.counter.update(data)

    def elements(self):
        return self.counter.elements()

    def values(self):
        return self.counter.values()

    def keys(self):
        return self.counter.keys()

    def items(self):
        return self.counter.items()

    def clear(self):
        self.counter.clear()

    def copy(self):
        return self.counter.copy()

    def get(self, key):
        return self.counter.get(key)

    def __add__(self, other):
        return self.counter + other

    def __sub__(self, other):
        return self.counter - other

    def __or__(self, other):
        return self.counter | other

    def __and__(self, other):
        return self.counter & other

    def __xor__(self, other):
        return self.counter ^ other

    def __eq__(self, other):
        return self.counter == other

    def __ne__(self, other):
        return self.counter != other

    def __le__(self, other):
        return self.counter <= other

    def __lt__(self, other):
        return self.counter < other

    def __ge__(self, other):
        return self.counter >= other

    def __gt__(self, other):
        return self.counter > other

    def __len__(self):
        return len(self.counter)

    def __iter__(self):
        return iter(self.counter)

    def __contains__(self, item):
        return item in self.counter

    def __getitem__(self, key):
        return self.counter[key]

    def __setitem__(self, key, value):
        self.counter[key] = value

    def __delitem__(self, key):
        del self.counter[key]

    def __missing__(self, key):
        return self.counter.__missing__(key)

    def __hash__(self):
        return hash(self.counter)

    def __sizeof__(self):
        return self.counter.__sizeof__()

    def __reversed__(self):
        return reversed(self.counter)

    def __call__(self):
        return self.counter


if __name__ == "__main__":
    nums = [randint(1, 10) for _ in range(100)]
    cc = CustomCounter(nums)
    print(cc)
    counter = Counter(nums)
    print(counter)
