"""
A module to calculate the prime factorization of a number.
"""


def prime_factors(n):
    factors = []

    # Get the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # Check for odd numbers
    # We gaurantee that i is a prime number,
    # because if it is not, it would have been divided by a smaller prime number
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)

    return factors
