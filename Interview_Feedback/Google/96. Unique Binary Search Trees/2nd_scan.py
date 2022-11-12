# -*- coding: utf-8 -*-
class Solution(object):
    def numTrees(self, n):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: previous scan solution (鎖鏈)
        Perf: Runtime: 20 ms, faster than 91.76%  / Memory Usage: 6.9 MB, less than 68.06%
        :type n: int
        :rtype: int
        """
        DP = [1,1]
        for i in range(2, n+1):
            tmp = 0
            for root in range(1, i+1):
                tmp += DP[root-1]*DP[i-root]
            DP.append(tmp)
        return DP[-1]

print Solution().numTrees(5)