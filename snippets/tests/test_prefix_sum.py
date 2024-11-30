import pytest
from code.prefix_sum import (
    compute_prefix_sum,
    range_sum,
    PrefixSumArray,
    compute_2d_prefix_sum,
    range_sum_2d,
)


def test_compute_prefix_sum():
    assert compute_prefix_sum([1, 2, 3, 4, 5]) == [1, 3, 6, 10, 15]
    assert compute_prefix_sum([-1, 0, 1]) == [-1, -1, 0]
    assert compute_prefix_sum([10]) == [10]


def test_range_sum():
    prefix = [1, 3, 6, 10, 15]
    assert range_sum(prefix, 1, 3) == 9
    assert range_sum(prefix, 0, 4) == 15
    assert range_sum(prefix, 2, 2) == 3


def test_prefix_sum_array():
    psa = PrefixSumArray([1, 2, 3, 4, 5])
    assert psa.prefix == [1, 3, 6, 10, 15]
    assert psa.get_range_sum(1, 3) == 9

    psa.update(2, 6)  # Change 3 to 6
    assert psa.original == [1, 2, 6, 4, 5]
    assert psa.prefix == [1, 3, 9, 13, 18]
    assert psa.get_range_sum(1, 3) == 12


def test_compute_2d_prefix_sum():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[0, 0, 0, 0], [0, 1, 3, 6], [0, 5, 12, 21], [0, 12, 27, 45]]
    assert compute_2d_prefix_sum(matrix) == expected


def test_range_sum_2d():
    prefix_2d = [[0, 0, 0, 0], [0, 1, 3, 6], [0, 5, 12, 21], [0, 12, 27, 45]]
    assert range_sum_2d(prefix_2d, 0, 0, 1, 1) == 12
    assert range_sum_2d(prefix_2d, 1, 1, 2, 2) == 28
    assert range_sum_2d(prefix_2d, 0, 0, 2, 2) == 45
    assert range_sum_2d(prefix_2d, 1, 1, 1, 2) == 11


def test_edge_cases():
    assert compute_prefix_sum([]) == []
    assert compute_2d_prefix_sum([[]]) == [[0]]

    with pytest.raises(IndexError):
        range_sum([], 0, 0)

    with pytest.raises(IndexError):
        range_sum_2d([[0]], 1, 1, 1, 1)


@pytest.mark.parametrize(
    "input_arr, expected",
    [
        ([1, 2, 3], [1, 3, 6]),
        ([-1, -2, -3], [-1, -3, -6]),
        ([0, 0, 0], [0, 0, 0]),
    ],
)
def test_compute_prefix_sum_parametrized(input_arr, expected):
    assert compute_prefix_sum(input_arr) == expected


@pytest.fixture
def sample_2d_matrix():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_2d_prefix_sum_with_fixture(sample_2d_matrix):
    result = compute_2d_prefix_sum(sample_2d_matrix)
    assert result[-1][-1] == 45  # Sum of all elements
    assert result[1][1] == 1  # Top-left element
    assert result[2][2] == 12  # 2x2 submatrix sum
