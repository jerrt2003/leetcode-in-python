from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        f = {}
        for word in words:
            res = 0
            for i in range(len(word)):
                res = max(res, f.get(word[:i] + word[i + 1 :], 0))
            f[word] = res + 1

        return max(f.values())
