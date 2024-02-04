"""
This module builds a hashmap from scratch using a list of lists,
and the built-in hash() function.
"""


class MyHashMap:
    def __init__(self):
        self.size = int(1e3)  # Initialize the size of the hashmap
        self.hashmap = [[] for _ in range(self.size)]  # Create a list of lists

    def _hash(self, key):
        """Return the hash of the key."""
        return hash(key) % self.size

    def put(self, key, value):
        """Insert a (key, value) pair into the hashmap."""
        hash_key = self._hash(key)  # Get the hash of the key
        # Check if the key already exists in the hashmap
        for i, (k, v) in enumerate(self.hashmap[hash_key]):
            if k == key:
                self.hashmap[hash_key][i] = (key, value)
                return
        # If the key does not exist, append the (key, value) pair to the hashmap
        self.hashmap[hash_key].append((key, value))

    def get(self, key):
        """Retrieve the value of a key from the hashmap."""
        hash_key = self._hash(key)
        # Check if the key exists in the hashmap
        for k, v in self.hashmap[hash_key]:
            if k == key:
                return v

        return None  # Return None if the key does not exist

    def remove(self, key):
        """Remove a (key, value) pair from the hashmap."""
        hash_key = self._hash(key)
        # Check if the key exists in the hashmap
        for i, (k, v) in enumerate(self.hashmap[hash_key]):
            if k == key:
                self.hashmap[hash_key].pop(i)
                return

    def __contains__(self, key):
        """Check if a key exists in the hashmap."""
        return self.get(key) != None

    def __getitem__(self, key):
        """Retrieve the value of a key using the [] operator."""
        return self.get(key)

    def __setitem__(self, key, value):
        """Insert a (key, value) pair using the [] operator."""
        self.put(key, value)

    def __delitem__(self, key):
        """Remove a (key, value) pair using the del operator."""
        self.remove(key)

    def __iter__(self):
        """Return an iterator that yields the keys in the hashmap."""
        for sublist in self.hashmap:
            for k, v in sublist:
                yield k

    def __len__(self):
        """Return the number of key-value pairs in the hashmap."""
        return sum(len(sublist) for sublist in self.hashmap)


if __name__ == "__main__":
    # Example usage
    hashmap = MyHashMap()
    hashmap.put("apple", 3)
    hashmap.put(3, "apple")

    print(hashmap.get("apple"))  # Output: 3
    print(hashmap.get(3))  # Output: 3

    hashmap.remove("apple")
    print(hashmap.get("apple"))  # Output: -1

    # Using operators and dunder methods
    hashmap["banana"] = 5
    print(f"Bannana in hashmap: {'banana' in hashmap}")  # Output: True
    print(f"Banana value: {hashmap['banana']}")  # Output: 5
    print("Deleting banana from hashmap")
    del hashmap["banana"]
    print(f"Bannana in hashmap: {'banana' in hashmap}")  # Output: False

    # Using len and iter
    hashmap["pear"] = 7
    hashmap["orange"] = 9
    print(f"Number of items in hashmap: {len(hashmap)}")  # Output: 2
    print("Items in hashmap:")
    for item in hashmap:
        print(item)
