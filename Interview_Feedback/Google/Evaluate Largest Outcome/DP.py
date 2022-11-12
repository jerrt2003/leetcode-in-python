# -*- coding: utf-8 -*-
class Solution(object):
    def evaluate(self, nums):
        N = len(nums)
        DP = [[0]*N for _ in range(N)]
        for x in range(N):
            DP[x][x] = nums[x]
        for size in range(2, N+1):
            for i in range(N-size+1):
                j = i+size-1
                for k in range(i, j):
                    DP[i][j] = max(DP[i][j], max(DP[i][k]*DP[k+1][j], DP[i][k]+DP[k+1][j]))
        return DP[0][N-1]

assert Solution().evaluate([1,2,1,2]) == 9
assert Solution().evaluate([0,0,0,2]) == 2
assert Solution().evaluate([0,3,0,2]) == 6