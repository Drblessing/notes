from typing import Iterable, Hashable, List


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

    def find_shortest_root(self, iterable: Iterable[Hashable]) -> Hashable:
        """Returns the shortest root of the iterable in the trie.
        If the iterable is not in the trie, returns the original iterable."""

        node = self.root
        shortest_root = iterable

        # Iterate through the iterable, checking for is_end_of_iterable
        for i, char in enumerate(iterable):
            if char in node.children:
                node = node.children[char]
                if node.is_end_of_iterable:
                    shortest_root = iterable[: i + 1]
                    return shortest_root
            else:
                return shortest_root

        return shortest_root


def substring_iterator(word):
    return (word[:i] for i in range(1, len(word)))


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        sentence_words = sentence.split(" ")

        new_sentence = []
        for word in sentence_words:
            new_sentence.append(trie.find_shortest_root(word))

        return " ".join(new_sentence)


def test_replaceWords():
    dictionary = ["a", "aa", "aaa", "aaaa"]
    sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"

    solution = Solution()

    assert solution.replaceWords(dictionary, sentence) == "a a a a a a a a bbb baba a"


test_replaceWords()
