# -*- coding: utf-8 -*-
class Solution(object):
    def chocolate(self, chocolate, K):
        m = len(chocolate)
        DP = [[0 for _ in range(K+1)] for _ in range(m+1)]
        accumSum = [0]
        for num in chocolate:
            accumSum.append(num+accumSum[-1])
        DP[0][0] = float('inf')
        for i in range(1, m+1):
            for j in range(1, K+1):
                for pos in range(i):
                    DP[i][j] = max(DP[i][j], min(DP[pos][j-1], accumSum[i]-accumSum[pos]))
        return DP[-1][-1]

nums = [3, 4, 5, 5, 6]
k = 4
assert Solution().chocolate(nums, k) == 5
nums = [3, 4, 5, 5, 6]
k = 3
assert Solution().chocolate(nums, k) == 6
nums = [5, 5, 6, 7, 8, 9, 9, 5]
k = 8
assert Solution().chocolate(nums, k) == 5
nums = [5, 5, 6, 7, 8, 9, 9, 5]
k = 7
assert Solution().chocolate(nums, k) == 5
nums = [5, 5, 6, 7, 8, 9, 9, 5]
k = 1
assert Solution().chocolate(nums, k) == 54
nums = [5, 3, 4, 4]
k = 2
assert Solution().chocolate(nums, k) == 8
nums = [5, 3, 4, 4]
k = 3
assert Solution().chocolate(nums, k) == 4
nums = [4, 4, 4, 4]
k = 4
assert Solution().chocolate(nums, k) == 4