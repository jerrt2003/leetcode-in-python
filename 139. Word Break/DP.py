# -*- coding: utf-8 -*-
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        Solution: DP
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/word-break/discuss/43995/A-Simple-Python-DP-solution
        Perf: Runtime: 36 ms, faster than 42.79% / Memory Usage: 7 MB, less than 90.99%
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        m = len(s)+1
        DP = [False for _ in range(m)]
        DP[0] = True
        for i in range(m):
            for j in range(i, m):
                if DP[i] and s[i:j+1] in wordDict:
                    DP[j+1] = True
        return DP[-1]