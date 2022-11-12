# -*- coding: utf-8 -*-
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        DP = [0 for _ in range(n+1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if j == 1:
                    DP[j] = 1
                    prev = DP[j]
                else:
                    DP[j] = DP[j] + prev
                    prev = DP[j]
        return DP[-1][-1]

assert Solution().uniquePaths(3,2)