# -*- coding: utf-8 -*-
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        Solution: Bottom-Up DP
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Perf: Runtime: 1756 ms, faster than 29.95% / Memory Usage: 26.3 MB, less than 47.37%
        Inspired By:
        - https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99101/Straight-forward-Java-DP-solution
        :type s: str
        :rtype: int
        """
        m = len(s)
        DP = [[0 for _ in range(m)] for _ in range(m)]
        for i in range(m-1, -1, -1): # need to build from last character since we will use DP[i][j] = DP[i+1][j-1] + 2
            DP[i][i] = 1
            for j in range(i+1, m):
                if s[i] == s[j]:
                    DP[i][j] = DP[i+1][j-1] + 2
                else:
                    DP[i][j] = max(DP[i+1][j], DP[i][j-1])
        return DP[0][m-1]