"""
A trie implementation in Python.
It takes an interable of elements and creates a trie data structure.
Time Complexities: 
Insertion: O(m) where m is the length of the word.
Search: O(m) where m is the length of the word.
Delete: O(m) where m is the length of the word.

The trie structures gets expensive in terms of space complexity.
Space complexity is O(n * m) where n is the number of words and m is the length of the word.

In practical terms, though, tries are incredibly space-efficient for datasets with a lot of shared prefixes, 
like dictionaries, because they allow for the sharing of common prefixes. It's like carpooling to work; 
everyone going in the same direction piles into one car, saving on gas and reducing traffic.

Trie nodes are indeed a classic example of the time-space tradeoff in computer science. 
This concept essentially means that in many algorithms and data structures, including tries, 
you can often achieve faster execution times (time efficiency) at the expense of using more memory (space efficiency), or vice versa.

In the case of tries: 

Time Efficiency: Tries provide very efficient search, insert, and delete operations, all typically running in O(m) time, 
where m is the length of the key being processed. 
This efficiency is fantastic for operations involving large sets of strings, 
such as autocomplete features, spell checkers, or prefix matching, making tries a go-to choice when performance is critical. 
It's like having a fast-pass in an amusement park; you get to enjoy the rides (operations) quickly!

Space Cost: The tradeoff comes in the form of space complexity. 
A trie can consume more memory than other data structures like hash tables or binary search trees when storing the same set of keys, e
specially if the set of characters (alphabet) is large and the keys are short. 
This is because each node in a trie may need to hold a large number of pointers (to its child nodes), 
even if many of those pointers are null (especially in sparse tries). 
It's akin to renting a huge warehouse to store your vast collection of hats,
because you want the luxury of picking any hat at a moment's notice, even if it means a lot of unused space.
"""

from typing import Iterable, Hashable


class TrieNode:
    """A node in the trie structure."""

    def __init__(self):
        self.children: dict[Hashable, "TrieNode"] = {}
        self.is_end_of_iterable: bool = False


class Trie:
    """A trie data structure. Normally used
    for words, but can be used for anything.
    The only requirement is that the elements
    are hashable."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, iterable: Iterable[Hashable]):
        """Inserts an interable into the trie."""
        node = self.root
        for element in iterable:
            if element not in node.children:
                node.children[element] = TrieNode()
            node = node.children[element]
        node.is_end_of_iterable = True

    def search(self, iterable: Iterable[Hashable]) -> bool:
        """Searches for an iterable in the trie."""
        node = self.root
        for element in iterable:
            if element not in node.children:
                return False
            node = node.children[element]
        return node.is_end_of_iterable

    def delete(self, iterable: Iterable[Hashable]):
        """Deletes an iterable from the trie."""
        node = self.root
        for char in iterable:
            if char in node.children:
                node = node.children[char]
            else:
                return  # The iterable is not in the trie, so we can't delete it
        node.is_end_of_iterable = False

    def starts_with(self, prefix: Iterable[Hashable]) -> bool:
        """Returns if there is any iterable in the trie that starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True
