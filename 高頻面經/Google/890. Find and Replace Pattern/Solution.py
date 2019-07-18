# -*- coding: utf-8 -*-
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        Time: O(n**2)
        Space: O(2n) -> O(n)
        Perf: Runtime: 20 ms, faster than 82.48% / Memory Usage: 11.7 MB, less than 82.00%
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for word in words:
            if len(word) != len(pattern):
                continue
            maps = dict()
            mapsReverse = dict()
            isMatch = True
            for w1, w2 in zip(pattern, word):
                if w1 not in maps and w2 not in mapsReverse:
                    maps[w1] = w2
                    mapsReverse[w2] = w1
                elif w1 in maps and maps[w1] != w2:
                    isMatch = False
                    break
                elif w2 in mapsReverse and mapsReverse[w2] != w1:
                    isMatch = False
                    break
            if isMatch:
                res.append(word)
        return res


#words = ["abc","deq","mee","aqq","dkd","ccc"]
words = ['ccc']
pattern = "abb"
assert Solution().findAndReplacePattern(words, pattern) == ["mee","aqq"]