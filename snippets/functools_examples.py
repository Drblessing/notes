"""
This module covers the functools module: higher-order functions and operations on callable objects.
A higher-order function is a function that takes a function as an argument, or returns a function.

Functions:
- reduce
- cache
- lru_cache
- cached_property
"""

from functools import reduce, cache, lru_cache, cached_property


# Cache: Simple lightweight unbounded function cache.
# Called "memoize" or "memoization" in other languages.
# Returns the same as lru_cache(maxsize=None), creating
# a thin wrapper around a dictionary lookup for the function arguments.
# The cache is unbounded, so it will grow indefinitely.
# Smaller and faster than lru_cache with a size limit,
# Because it does not need to manage the cache size, or evict old values.
# Trheadsafe and can be used in a multithreaded environment.
@cache
def factorial(n):
    "A simple recursive factorial function"
    return n * factorial(n - 1) if n else 1


def test_cache():
    "View the cache in the factorial function"

    factorial(10)  # No previously cached result, made 11 recursive calls
    print(factorial.cache_info())
    factorial(5)  # 5! is already cached, so no recursive calls are made
    # It just looks up cached value result.
    factorial(12)  # Make two new recrusive calls, the rest are cached
    print(factorial.cache_info())

    # Can add a breakpoint on line 36 to inspect the cache


# @Cached_property can be used to cache a property of a class, useful
# if its immutable and expensive to calculate.

# @lru_cache(maxsize=128, typed=False)
# This creates a least-recently-used cache for the decorated function.
# It has a size limit, and will evict the least recently used items.
# Similar to @cache, but with a size limit.


def reduce_examples():
    "Examples of using reduce"
    # Reduce is a higher-order function that applies a function of two arguments
    # cumulatively to the items of an iterable, from left to right, so as to
    # reduce the iterable to a single value.
    print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))  # 15
    print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))  # 120


if __name__ == "__main__":
    test_cache()
    reduce_examples()
