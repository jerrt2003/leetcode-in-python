# -*- coding: utf-8 -*-
class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        Solution: DP (TLE)
        Time Complexity: O(n^2*m)
        Space Complexity: O(n*m)
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        m = len(weights)
        DP = [[float('inf') for _ in range(D+1)] for _ in range(m+1)]
        DP[0][0] = 0
        total_w = [0]
        for w in weights:
            total_w.append(total_w[-1]+w)
        for i in range(1, m+1):
            for j in range(1, D+1):
                for k in range(i):
                    DP[i][j] = min(DP[i][j], max(DP[k][j-1], total_w[i]-total_w[k]))
        return DP[-1][-1]

weights = [1,2,3,4,5,6,7,8,9,10]
D = 1


print Solution().shipWithinDays(weights, D)