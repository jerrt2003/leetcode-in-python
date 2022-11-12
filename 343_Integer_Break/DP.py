# -*- coding: utf-8 -*-
class Solution(object):
    def integerBreak(self, n):
        """
        Solution: DP
        Time Complexity: nlog(n)
        Space Complexity: O(n)
        Perf: Runtime: 20 ms, faster than 89.16% / Memory Usage: 10.8 MB, less than 46.88%
        Inspired By: MySELF!!
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return 1
        DP = [-float('inf') for _ in range(n+1)]
        DP[0],DP[1]= 1,1
        for i in range(2, n+1):
            l, r = 1, i-1
            while l <= r:
                '''
                there are four possible out come for each combination:
                l*r
                DP[l]*r
                DP[r]*l
                DP[l]*DP[r]
                '''
                possible_outcome = [l*r, DP[l]*r, l*DP[r], DP[l]*DP[r]]
                DP[i] = max(max(*possible_outcome), DP[i])
                l += 1
                r -= 1
        return DP[-1]

print Solution().integerBreak(8)