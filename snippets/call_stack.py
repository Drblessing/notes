def print_message(message):
    print(message)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def calculate_factorial(number):
    print_message(f"Calculating the factorial of {number}")
    result = factorial(number)
    print_message(f"The factorial of {number} is {result}")
    return result


def main():
    number = 5
    calculate_factorial(number)


if __name__ == "__main__":
    main()
