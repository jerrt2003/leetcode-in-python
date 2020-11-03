class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        Facebook
        T:O(2^n) S:O(2^n)
        Runtime: 516 ms, faster than 29.23% of Python online submissions for Target Sum.
        Memory Usage: 35.4 MB, less than 17.62% of Python online submissions for Target Sum.
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        DP = {}

        def dfs(total, idx):
            if total == S and idx == len(nums):
                return 1
            elif idx == len(nums):
                return 0
            cand = nums[idx]
            if (total, idx) in DP:
                return DP[(total, idx)]
            ret = 0
            for sign in [1, -1]:
                ret += dfs(total + cand * sign, idx + 1)
            DP[(total, idx)] = ret
            return DP[(total, idx)]

        return dfs(0, 0)



