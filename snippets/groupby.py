"""
A module exploring the groupby function in itertools.

The groupby function is used to group items together based on a key. The data must be sorted by the key for groupby to work correctly. This is because groupby only groups items together if they are adjacent to each other in the data.
This is helpful if you want to group items together based on key and position in the data.
However, again, if you want to group all items together based on a key, such as age, 
you must sort the data by age first.

Group by also maintains the order of the data, so if the data is sorted by the key,
the groups will be in the same order as the data.

This is a bit of a weird design choice, but it is what it is.
"""

from itertools import groupby


def groupby_example():
    """
    Example of how to use groupby
    """
    data = [
        {"name": "Edward", "age": 24},
        {"name": "Alan", "age": 23},
        {"name": "Bob", "age": 23},
        {"name": "Charlie", "age": 23},
        {"name": "David", "age": 24},
        {"name": "Frank", "age": 25},
    ]
    # To group all items with the same key together, the data must be sorted by the key
    data.sort(key=lambda x: x["age"])
    print("Group by age")
    print(list(groupby(data, key=lambda x: x["age"])))
    for age, items in groupby(data, key=lambda x: x["age"]):
        print(f"Age: {age}")
        for item in items:
            print(f'  {item["name"]}')


def groupby_list_of_tuples():
    """
    Example of how to use groupby with a list of tuples
    """
    data = [
        ("Alan", 23),
        ("Bob", 23),
        ("Charlie", 23),
        ("David", 24),
        ("Edward", 24),
        ("Frank", 25),
    ]
    data.sort(key=lambda x: x[1])
    for age, items in groupby(data, key=lambda x: x[1]):
        print(f"Age: {age}")
        for item in items:
            print(f"  {item[0]}")


if __name__ == "__main__":
    groupby_example()
    print()
    groupby_list_of_tuples()
