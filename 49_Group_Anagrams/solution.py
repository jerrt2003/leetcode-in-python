import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 利用array做成一個tuple當作key
        ans_map = collections.defaultdict(list)
        for word in strs:
            key = [0 for _ in range(26)]
            for w in word:
                key[ord(w)-ord('a')] += 1
            ans_map[tuple(key)].append(word)
        return [v for v in ans_map.values()]