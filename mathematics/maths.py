from primesieve import primes, count_primes
import numpy as np
import matplotlib

matplotlib.use("Agg")  # Use non-interactive backend
import matplotlib.pyplot as plt
from scipy.special import zeta

# ============= CONFIGURATION =============
MAX_VALUE = 1e10  # Change this to control how high we count primes
# Examples: 1e9 (1 billion), 1e10 (10 billion), 1e12 (1 trillion)
SAMPLE_LIMIT = 1e7  # Primes to load for gap analysis (keep reasonable for memory)
VIZ_MAX = 1e10  # Maximum value for visualization (lower = faster plots)
# =========================================


# Efficient prime counting function using primesieve
def pi(n):
    """Count the number of primes less than or equal to n using efficient C++ library"""
    return count_primes(0, int(n))


# For analysis, we only need a smaller sample of primes for gap analysis and Euler product
print("Generating sample of primes for analysis...")
x = np.array(primes(SAMPLE_LIMIT))
print(f"Loaded {len(x):,} primes up to {SAMPLE_LIMIT:.0e} for analysis")
print("First 10 primes:", x[:10])
print(f"Sample memory usage: {x.nbytes / 1e9:.3f} GB")


# Print prime counting function at various points (now can go VERY large!)
print("\n=== Prime Counting Function π(x) ===")
# Generate test values dynamically based on MAX_VALUE
test_values = [10**i for i in range(1, int(np.log10(MAX_VALUE)) + 1)]
print(f"Efficiently counting primes up to {MAX_VALUE:.0e}...")
for n in test_values:
    count = pi(n)
    # Compare with approximation x / ln(x)
    approx = n / np.log(n) if n > 1 else 0
    # Better approximation: Li(x) using the logarithmic integral
    li_approx = n / np.log(n) * (1 + 1 / np.log(n)) if n > 1 else 0
    error = abs(count - approx) / count * 100 if count > 0 else 0
    li_error = abs(count - li_approx) / count * 100 if count > 0 else 0
    print(f"π({n:.0e}) = {count:,}")
    print(f"  x/ln(x) = {approx:,.0f} (error: {error:.2f}%)")
    print(f"  Li(x) ≈ {li_approx:,.0f} (error: {li_error:.2f}%)")
    print()

# Analyze prime gaps (using our sample)
print("\n=== Prime Gaps Analysis ===")
print(f"(Analyzing gaps in first {len(x):,} primes)")
gaps = np.diff(x)
print(f"Mean gap: {np.mean(gaps):.2f}")
print(f"Max gap: {np.max(gaps)} (occurs after prime {x[np.argmax(gaps)]:,})")
print(f"Min gap: {np.min(gaps)}")
print(f"Twin primes (gap=2): {np.sum(gaps == 2):,}")

# Distribution of prime gaps
print("\n=== Most Common Prime Gaps ===")
unique_gaps, counts = np.unique(gaps, return_counts=True)
sorted_indices = np.argsort(counts)[::-1]
for i in range(min(10, len(unique_gaps))):
    idx = sorted_indices[i]
    print(f"Gap of {unique_gaps[idx]}: {counts[idx]:,} occurrences")

# Riemann Zeta Function exploration
print("\n=== Riemann Zeta Function ζ(s) ===")
print("The Riemann Hypothesis: All non-trivial zeros of ζ(s) have Re(s) = 1/2")
print("\nEuler Product Formula: ζ(s) = ∏(1 - p^(-s))^(-1) for Re(s) > 1")
print("This connects the zeta function to prime numbers!\n")

# Calculate zeta function at various points
s_values = [2, 3, 4, 5, 10, 20]
for s in s_values:
    zeta_val = zeta(s)
    # Approximate using Euler product with our primes
    euler_product = 1.0
    for p in x[:10000]:  # Use first 10000 primes
        # Convert to float to avoid overflow
        euler_product *= 1.0 / (1.0 - float(p) ** (-s))
    print(f"ζ({s}) = {zeta_val:.6f} | Euler product (10k primes): {euler_product:.6f}")

# Famous result: ζ(2) = π²/6
print(f"\nBasel Problem: ζ(2) = π²/6 = {np.pi**2 / 6:.6f}")
print(f"Actual ζ(2) = {zeta(2):.6f}")

# Create visualizations
print("\n=== Creating Visualizations ===")

fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Plot 1: Prime counting function - faster with fewer points and lower max
max_viz_power = int(np.log10(VIZ_MAX))
sample_points = np.logspace(1, max_viz_power, 30)  # Only 30 points for speed
print(f"Computing π(x) for visualization (up to 10^{max_viz_power})...")
pi_values = [pi(n) for n in sample_points]

axes[0, 0].loglog(sample_points, pi_values, "b-", label="π(x)", linewidth=2)
axes[0, 0].loglog(
    sample_points,
    sample_points / np.log(sample_points),
    "r--",
    label="x/ln(x)",
    linewidth=2,
)
axes[0, 0].set_xlabel("x", fontsize=12)
axes[0, 0].set_ylabel("Number of primes", fontsize=12)
axes[0, 0].set_title(
    f"Prime Counting Function π(x) [up to 10^{max_viz_power}]", fontsize=14
)
axes[0, 0].legend(fontsize=10)
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Prime distribution (first 10000 primes)
axes[0, 1].plot(range(10000), x[:10000], "b-", linewidth=1)
axes[0, 1].set_xlabel("Index", fontsize=12)
axes[0, 1].set_ylabel("Prime value", fontsize=12)
axes[0, 1].set_title("First 10,000 Primes", fontsize=14)
axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Prime gaps histogram
axes[1, 0].hist(gaps, bins=100, edgecolor="black", alpha=0.7)
axes[1, 0].set_xlabel("Gap size", fontsize=12)
axes[1, 0].set_ylabel("Frequency", fontsize=12)
axes[1, 0].set_title(
    f"Distribution of Prime Gaps (all {len(gaps):,} gaps)", fontsize=14
)
axes[1, 0].grid(True, alpha=0.3)

# Plot 4: Error in prime number theorem approximation
print("Computing errors for visualization...")
error_values = []
for n in sample_points[1:]:
    count = pi(n)
    approx = n / np.log(n)
    error_values.append((count - approx) / count * 100)

axes[1, 1].semilogx(sample_points[1:], error_values, "g-", linewidth=2)
axes[1, 1].set_xlabel("x", fontsize=12)
axes[1, 1].set_ylabel("Relative Error (%)", fontsize=12)
axes[1, 1].set_title("Error in Prime Number Theorem (π(x) vs x/ln(x))", fontsize=14)
axes[1, 1].grid(True, alpha=0.3)
axes[1, 1].axhline(y=0, color="r", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("prime_analysis.png", dpi=300, bbox_inches="tight")
print("Saved visualization to prime_analysis.png")
# plt.show()  # Commented out - file saved instead

print("\n=== Analysis Complete! ===")
print(f"Sample primes loaded: {len(x):,} (up to {SAMPLE_LIMIT:.0e})")
print(f"Largest prime in sample: {x[-1]:,}")
print(f"Memory used for sample: {x.nbytes / 1e9:.3f} GB")
print(f"\nLargest π(x) computed: π({MAX_VALUE:.0e}) = {pi(MAX_VALUE):,}")
print("\n💡 To compute larger values, change MAX_VALUE at the top of the file!")
print("   Using primesieve.count_primes() allows counting primes at")
print("   arbitrarily large values without storing them all in memory!")
