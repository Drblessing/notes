from primesieve import primes, count_primes, nth_prime
import numpy as np
import time

# Count all of the primes up to a large number, haha
start = time.time()
LARGE_NUMBER = 1e8
print("PRIME COUNTING PROGRAM")
print("-" * 30)
print(f"Counting primes up to {LARGE_NUMBER:,}")
print(f"Number of primes: {count_primes(LARGE_NUMBER):,}")
print(f"The one millionth prime is {nth_prime(1_000_000):,}")
print(f"The one billionth prime is {nth_prime(1_000_000_000):,}")
print(f"The one trillionth prime is {nth_prime(1_000_000_000_000):,}")
end = time.time()
print(f"Execution time: {end - start:.2f} seconds")
