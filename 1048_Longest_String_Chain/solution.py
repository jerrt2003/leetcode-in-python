import collections
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        word_chain = [1 for _ in range(len(words))]

        for i, word in enumerate(words):
            if len(word) == 1 or i == 0:
                continue
            else:
                for j in range(i - 1, -1, -1):
                    if self.is_predecessor(words[j], word):
                        word_chain[i] = max(word_chain[i], word_chain[j] + 1)

        return max(word_chain)

    def is_predecessor(self, word1, word2):
        if len(word2) - len(word1) == 1:
            for i in range(len(word2)):
                if word2[:i] + word2[i + 1 :] == word1:
                    return True

        return False
