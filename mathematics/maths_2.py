# Primes explorer + prime counting + Riemann R(x)
# ------------------------------------------------
# pip install primesieve mpmath numpy

from primesieve import primes, count_primes
import numpy as np
import mpmath as mp
import sys
from math import log

# ---------- Config ----------
# Start safer; bump to 10**9 or 10**10 after testing
LIMIT = 10**8  # change to 10**10 at your own risk
MAKE_ARRAY = True  # set False to skip storing all primes

mp.mp.dps = 50  # high precision for li() and R(x)


# ---------- Helpers ----------
def mobius(n: int) -> int:
    """Möbius μ(n). Returns 0 if n has a squared prime factor; otherwise (-1)^k."""
    m = n
    primes_count = 0
    p = 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            primes_count += 1
            if m % p == 0:
                return 0
        p += 1 if p == 2 else 2  # 2,3,5,7,... (skip evens after 2)
    if m > 1:
        primes_count += 1
    return -1 if (primes_count % 2 == 1) else 1


def li(x):
    """Offset logarithmic integral li(x)."""
    if x <= 0:
        return mp.ninf
    if x == 1:
        return -mp.inf
    return mp.li(x)


def Riemann_R(x, max_terms=20):
    """
    Riemann prime counting function R(x) = sum_{n>=1} μ(n)/n * li(x^(1/n)).
    Truncate at max_terms; this converges fast for large x.
    """
    if x < 2:
        return mp.mpf(0)
    s = mp.mpf(0)
    for n in range(1, max_terms + 1):
        mu = mobius(n)
        if mu == 0:
            continue
        term = mu * li(x ** (mp.mpf(1) / n)) / n
        s += term
        # crude early stop if the tail is tiny
        if abs(term) < 1e-10 and n > 8:
            break
    return s


def pnt(x):
    """Prime Number Theorem main term x / log x."""
    return mp.mpf(x) / mp.log(x)


def fmt_int(x):  # pretty print integers with commas
    return f"{int(x):,}"


# ---------- Generate / Count ----------
arr = None
if MAKE_ARRAY:
    # NOTE: primes() requires an int, not a float
    print(f"Generating primes up to {fmt_int(LIMIT)} …")
    py_list = primes(int(LIMIT))  # Python list of ints
    # Convert *immediately* to compact uint64 to free Python-int overhead
    arr = np.asarray(py_list, dtype=np.uint64)
    del py_list

    print(f"{fmt_int(arr.size)} primes")
    print("First 10 primes:", arr[:10].tolist())
    print(f"Memory usage (GB): {arr.nbytes / 1e9:.3f}")
else:
    print("Skipping array creation; will use count_primes(x) for exact π(x).")


# ---------- Exact π(x) ----------
def pi_from_array(x, a: np.ndarray) -> int:
    """π(x) via binary search on the primes array."""
    # number of primes <= x
    return int(np.searchsorted(a, x, side="right"))


def pi_exact(x: int) -> int:
    """π(x) via primesieve's counter (no array needed)."""
    return int(count_primes(int(x)))


# ---------- Demo / Comparisons ----------
def compare_points(points, use_array=True, arr=None):
    """
    Print a small table comparing:
    π(x) (exact), R(x), li(x), x/log x, with absolute/relative errors.
    """
    header = (
        "x".ljust(14)
        + "pi(x)".rjust(14)
        + "R(x)".rjust(18)
        + "li(x)".rjust(18)
        + "x/log x".rjust(18)
        + "err R".rjust(12)
        + "err li".rjust(12)
        + "err x/log".rjust(12)
    )
    print("\n" + header)
    print("-" * len(header))
    for x in points:
        x_int = int(x)
        pi_x = (
            pi_from_array(x_int, arr)
            if (use_array and arr is not None)
            else pi_exact(x_int)
        )
        R_x = Riemann_R(x_int)
        li_x = li(x_int)
        pnt_x = pnt(x_int)

        # absolute errors vs exact π(x)
        eR = R_x - pi_x
        eL = li_x - pi_x
        eP = pnt_x - pi_x

        print(
            f"{fmt_int(x_int):<14}"
            f"{fmt_int(pi_x):>14}"
            f"{mp.nstr(R_x, 8):>18}"
            f"{mp.nstr(li_x, 8):>18}"
            f"{mp.nstr(pnt_x, 8):>18}"
            f"{mp.nstr(eR, 6):>12}"
            f"{mp.nstr(eL, 6):>12}"
            f"{mp.nstr(eP, 6):>12}"
        )


# Choose a few geometrically spaced checkpoints
def geom_points(lo, hi, k=10):
    lo = max(10, int(lo))
    xs = np.geomspace(lo, hi, num=k)
    return [int(round(v)) for v in xs]


# Run the comparison
if MAKE_ARRAY:
    pts = geom_points(10**3, min(LIMIT, 10**9), k=12)
    compare_points(pts, use_array=True, arr=arr)
else:
    # No array; you can go HUGE here without storing primes in RAM
    # (just be patient on very large x)
    pts = [10**k for k in range(4, 11)]  # 1e4,...,1e10
    compare_points(pts, use_array=False, arr=None)


# ---------- Extras you can toggle ----------
# 1) Estimate array RAM before generating (uses li(x) ~ π(x))
def estimate_array_gb(x):
    est_pi = li(x)  # a good approximation to π(x)
    bytes_needed = int(est_pi) * 8  # uint64
    return bytes_needed / 1e9


# print(f"Estimated GB for primes<=1e10: {estimate_array_gb(10**10):.2f}")
# print(f"Estimated GB for primes<=1e9 : {estimate_array_gb(10**9):.2f}")
