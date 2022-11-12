# -*- coding: utf-8 -*-
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        Solution: DFS
        Time Complexity:
        Space Complexity:
        Perf: TLE
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.res = []

        def dfs(s, wordDict, current):
            if len(s) == 0:
                self.res.append(current.strip())
                return
            for word in wordDict:
                m = len(word)
                if s[:m] == word:
                    dfs(s[m:], wordDict, current + " " + word)
            return

        dfs(s, wordDict, "")
        return self.res

s = "aaaaaaa"
wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa"]

print Solution().wordBreak(s, wordDict)