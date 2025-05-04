from trie import Trie


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise ValueError("Input must be a list of strings")

        if not strings:
            return ""

        for string in strings:
            self.put(string)

        current = self.root
        longest_common_prefix = []

        while current and len(current.children) == 1 and current.value is None:
            char = next(iter(current.children))
            longest_common_prefix.append(char)
            current = current.children[char]

        return "".join(longest_common_prefix)


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""

    print("All tests passed.")
