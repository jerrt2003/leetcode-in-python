# -*- coding: utf-8 -*-
class NumArray(object):

    def __init__(self, nums):
        """
        Solution: DP
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        Perf: Runtime: 40 ms, faster than 86.61% / Memory Usage: 14.6 MB, less than 0.74%
        :type nums: List[int]
        """
        self.nums = nums
        if not nums: return None
        self.DP = list()
        self.DP.append(nums[0])
        for i in range(1, len(nums)):
            self.DP.append(nums[i] + self.DP[i - 1])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums: return None
        return self.DP[j] - self.DP[i] + self.nums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)