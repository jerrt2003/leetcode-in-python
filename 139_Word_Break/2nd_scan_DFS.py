# -*- coding: utf-8 -*-
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        Solution: DFS + memorization
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        Perf: Runtime: 28 ms, faster than 78.81% / Memory Usage: 7.2 MB, less than 15.57%
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        m = len(s)
        DP = [None for _ in range(m+1)]

        def helper(s, i, m, wordDict):
            if i == m:
                return True
            if DP[i] is not None:
                return DP[i]
            j = i + 1
            while j <= m:
                if s[i:j] in wordDict:
                    if helper(s, j, m, wordDict):
                        DP[j] = True
                        return True
                j += 1
            DP[i] = False
            return False

        return helper(s, 0, m, wordDict)

s = 'leetcode'
wordDict = ['leet','code']
print Solution().wordBreak(s, wordDict)