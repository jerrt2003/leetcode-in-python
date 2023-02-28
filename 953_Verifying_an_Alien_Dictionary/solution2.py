import collections

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_2_idx = collections.defaultdict(int)
        for i, v in enumerate(order):
            char_2_idx[v] = i
        for i in range(len(words)-1):
            word_1 = words[i]
            word_2 = words[i+1]
            is_ordered = False
            for j in range(min(len(word_1), len(word_2))):
                if char_2_idx[word_1[j]] < char_2_idx[word_2[j]]:
                    is_ordered = True
                    break
                elif char_2_idx[word_1[j]] > char_2_idx[word_2[j]]:
                    return False
            if is_ordered:
                continue
            if len(word_1) > len(word_2):
                return False
        return True