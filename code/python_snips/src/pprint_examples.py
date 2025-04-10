"""
The pprint module, useful for printing json and other data structures.
"""

import pprint

# Example 1
data = {"name": "John", "age": 30, "city": "New York"}

print(data)
pprint.pprint(data)
print()


# Example 2: Pretty-printing a list of dictionaries
data_list = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 28, "city": "Chicago"},
    {"name": "Doe", "age": 32, "city": "San Francisco"},
]

print(data_list)
pprint.pprint(data_list)
# Example 3: Controlling the width of the output
pprint.pprint(data_list, width=30)
print()

# Example 4: Specifying the depth of nested structures to print
deep_data = {"a": {"b": {"c": {"d": "e"}}}}
pprint.pprint(deep_data, depth=2)


# Example 5: A large json object
import json
import requests
from urllib.request import urlopen

with urlopen("https://pypi.org/pypi/sampleproject/json") as resp:
    data = json.load(resp)["info"]
    print(data)
    pprint.pprint(data)
