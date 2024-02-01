"""
This module covers combinatoric iterators in itertools.

Itertools functions explored in this module:
- product(): Cartesian product of input iterables.
- permutations(): Permutations of input iterables.
- combinations(): Combinations of input iterables.
- combinations_with_replacement(): Combinations of input iterables with replacement.
"""

from itertools import product, permutations, combinations, combinations_with_replacement


def product_example():
    """
    Example of how to use product
    """
    print("Product 'ABCD' and 'xyz':")
    print(list(product("ABCD", "xyz")))
    print("Product range(2) and repeat=3:")
    print(list(product(range(2), repeat=3)))
    print("Product 'ABCD, repeat=2:'")
    print(list(product("ABCD", repeat=2)))
    print()


def permutations_example():
    """
    Example of how to use permutations
    """
    print("Permutations of 'ABCD' and 2:")
    print(list(permutations("ABCD", 2)))
    print("Permutations of 'ABCD' and 4:")
    print(list(permutations("ABCD", 4)))
    print()


def combinations_example():
    """
    Example of how to use combinations
    """
    print("Combinations of 'ABCD', 2:")
    print(list(combinations("ABCD", 2)))
    print("Combinations of 'ABCD', 3:")
    print(list(combinations("ABCD", 3)))
    print("Combinations of 'ABCD'")
    print(list(combinations("ABCD", 4)))
    print()


def combinations_with_replacement_example():
    """
    Example of how to use combinations_with_replacement
    """
    print("Combinations with replacement of 'ABCD', 2:")
    print(list(combinations_with_replacement("ABCD", 2)))
    print("Combinations with replacement of 'ABCD', 3:")
    print(list(combinations_with_replacement("ABCD", 3)))
    print()


if __name__ == "__main__":
    product_example()
    permutations_example()
    combinations_example()
    combinations_with_replacement_example()
