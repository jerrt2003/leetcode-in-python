# -*- coding: utf-8 -*-
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if nums is None or len(nums) == 0: return None
        self.res = 0
        self.target = S
        self.findCombo(nums, 0, 0)
        return self.res

    def findCombo(self, nums, curr_sum, curr_idx):
        if curr_idx == len(nums) and curr_sum == self.target:
            self.res += 1
            return
        elif curr_idx == len(nums):
            return
        next_nums = nums[:]
        self.findCombo(next_nums, curr_sum + next_nums[curr_idx], curr_idx+1)
        self.findCombo(next_nums, curr_sum - next_nums[curr_idx], curr_idx+1)


nums = [42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47]
S = 38

sol = Solution()
print sol.findTargetSumWays(nums, S)