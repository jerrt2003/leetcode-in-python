class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        N = len(nums)
        DP = [[float('inf')] * (m+1) for _ in range(N+1)]
        DP[0][0] = 0
        sum_array = [0]
        for i in range(len(nums)):
            sum_array.append(nums[i]+sum_array[-1])
        for i in range(1, N+1):
            for j in range(1, m+1):
                for k in range(i):
                    DP[i][j] = min(DP[i][j], max(DP[k][j-1], sum_array[i]-sum_array[k]))
        return DP[-1][-1]

nums = [7,2,5,10,8]
m = 2

assert Solution().splitArray(nums, m) == 18