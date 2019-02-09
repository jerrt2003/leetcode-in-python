# -*- coding: utf-8 -*-
class Solution(object):
    def minDistance(self, word1, word2):
        """
        Solution: DP / Levenshtein distance
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        Inspired By: https://www.youtube.com/watch?v=We3YDTzNXEk
        Perf: Runtime: 148 ms, faster than 46.59% / Memory Usage: 10.5 MB, less than 34.26%
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)+1
        n = len(word2)+1
        DP = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            DP[i][0] = i
        for j in range(1, n):
            DP[0][j] = j
        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = min(min(DP[i-1][j], DP[i][j-1]), DP[i-1][j-1]) + 1
        return DP[-1][-1]