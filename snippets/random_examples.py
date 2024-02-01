"""
This module covers the random module, which is used to generate random numbers and make random choices.
"""

import random


def show_random_examples():
    """
    This function demonstrates various capabilities of the Python 'random' module.
    """

    # Random float: 0.0 <= number < 1.0
    print("Random Float:", random.random())

    # Choice from a list
    example_list = [1, 2, 3, 4, 5]
    print("Random Choice from a list from 1 to 5:", random.choice(example_list))

    # Shuffle a list
    random.shuffle(example_list)
    print("Shuffled List:", example_list)

    # Random integer chosen from range(5)
    print("Random Integer from range(5):", random.randrange(5))

    print("Random even integer from 10 to 20:", random.randrange(10, 21, 2))

    # Random element from a range
    print("Random Integer from range(10, 20):", random.randint(10, 20))

    # Select n different elements from a list
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(
        "Random Sample of 3 elements from a list 1 to 10:",
        random.sample(sample_list, 3),
    )

    # Sample 10 integers from 0 to 10e9
    print(
        "Random Sample of 10 integers from 0 to 1e12:",
        random.sample(range(int(1e12)), 10),
    )

    # random.choices() can be used to select elements with replacement
    print(
        "Random Sample of 5 elements from a list 1 to 3 with replacement:",
        random.choices(range(1, 4), k=5),
    )

    # Randomly choose True or False (like a coin flip)
    print("Random Boolean:", random.choice([True, False]))

    # Generate a random float within a specified range
    print("Random Float between 10.5 and 25.5:", random.uniform(10.5, 25.5))

    # Random binomial distribution
    print(
        "Random binomial distribution, like flipping a coin 10 times and counting heads:",
        random.binomialvariate(10, 0.5),
    )

    # Random number from a normal distribution
    print("Random number from a normal distribution:", random.normalvariate(0, 1))


def random_distributions():
    """Exploring more random distributions"""

    # Random number from a triangular distribution
    print("Random number from a triangular distribution:", random.triangular(0, 1, 0.5))

    # Random number from a log-normal distribution
    print("Random number from a log-normal distribution:", random.lognormvariate(0, 1))

    # Random number from a gamma distribution
    print("Random number from a gamma distribution:", random.gammavariate(1, 1))

    # Random number from a beta distribution
    print("Random number from a beta distribution:", random.betavariate(1, 1))

    # Random number from a Weibull distribution
    print("Random number from a Weibull distribution:", random.weibullvariate(1, 1))

    # Random number from a Pareto distribution
    print("Random number from a Pareto distribution:", random.paretovariate(1))

    # Random number from a von Mises distribution
    print("Random number from a von Mises distribution:", random.vonmisesvariate(0, 1))

    # 3 values from an exponential distribution
    print(
        "3 values from an exponential distribution:",
        random.expovariate(1),
        random.expovariate(1),
        random.expovariate(1),
    )


# Run the function to display the examples
if __name__ == "__main__":
    show_random_examples()
    # random_distributions()
