"""
prefix_sum.py: A module for prefix sum operations and related utilities.

This module provides functions and classes for working with prefix sums,
including computation, range queries, and 2D prefix sums.

Author: Daniel Blessing
Date: 2024-06-22
"""


def compute_prefix_sum(arr: list[int]) -> list[int]:
    """
    Compute the prefix sum of a given array.

    Args:
        arr (list[int]): The input array.

    Returns:
        list[int]: The prefix sum array.
    """
    if not arr:  # Handle empty list
        return []

    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix


def range_sum(prefix: list[int], start: int, end: int) -> int:
    """
    Calculate the sum of elements in a range using a prefix sum array.

    Args:
        prefix (list[int]): The prefix sum array.
        start (int): The start index of the range (inclusive).
        end (int): The end index of the range (inclusive).

    Returns:
        int: The sum of elements in the specified range.
    """
    if start == 0:
        return prefix[end]
    return prefix[end] - prefix[start - 1]


class PrefixSumArray:
    """A class to represent a prefix sum array with utility methods."""

    def __init__(self, arr: list[int]):
        """
        Initialize the PrefixSumArray with a given array.

        Args:
            arr (list[int]): The input array.
        """
        self.original = arr
        self.prefix = compute_prefix_sum(arr)

    def get_range_sum(self, start: int, end: int) -> int:
        """
        Get the sum of elements in a range.

        Args:
            start (int): The start index of the range (inclusive).
            end (int): The end index of the range (inclusive).

        Returns:
            int: The sum of elements in the specified range.
        """
        return range_sum(self.prefix, start, end)

    def update(self, index: int, value: int) -> None:
        """
        Update an element in the original array and recompute the prefix sum.

        Args:
            index (int): The index to update.
            value (int): The new value.
        """
        diff = value - self.original[index]
        self.original[index] = value
        for i in range(index, len(self.prefix)):
            self.prefix[i] += diff


def compute_2d_prefix_sum(matrix: list[list[int]]) -> list[list[int]]:
    """
    Compute the 2D prefix sum of a given matrix.

    Args:
        matrix (list[list[int]]): The input matrix.

    Returns:
        list[list[int]]: The 2D prefix sum matrix.
    """

    if matrix == [] or matrix == [[]]:  # Handle empty matrix
        return [[0]]

    rows, cols = len(matrix), len(matrix[0])
    prefix_2d = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix_2d[i][j] = (
                prefix_2d[i - 1][j]
                + prefix_2d[i][j - 1]
                - prefix_2d[i - 1][j - 1]
                + matrix[i - 1][j - 1]
            )

    return prefix_2d


def range_sum_2d(
    prefix_2d: list[list[int]], row1: int, col1: int, row2: int, col2: int
) -> int:
    """
    Calculate the sum of elements in a 2D range using a 2D prefix sum matrix.

    Args:
        prefix_2d (list[list[int]]): The 2D prefix sum matrix.
        row1 (int): The start row of the range (inclusive).
        col1 (int): The start column of the range (inclusive).
        row2 (int): The end row of the range (inclusive).
        col2 (int): The end column of the range (inclusive).

    Returns:
        int: The sum of elements in the specified 2D range.
    """
    return (
        prefix_2d[row2 + 1][col2 + 1]
        - prefix_2d[row1][col2 + 1]
        - prefix_2d[row2 + 1][col1]
        + prefix_2d[row1][col1]
    )


if __name__ == "__main__":
    # Example usage
    arr = [1, 3, 4, 2, 5]
    psa = PrefixSumArray(arr)
    print(f"Original array: {arr}")
    print(f"Prefix sum array: {psa.prefix}")
    print(f"Sum of range [1, 3]: {psa.get_range_sum(1, 3)}")

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    prefix_2d = compute_2d_prefix_sum(matrix)
    print(
        f"2D Prefix sum of range (0,0) to (1,1): {range_sum_2d(prefix_2d, 0, 0, 1, 1)}"
    )
