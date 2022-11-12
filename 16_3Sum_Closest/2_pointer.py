# -*- coding: utf-8 -*-
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        Solution: Use 2-pointer, O(n^2) solution
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        Inspired By: MySELF!! (216ms, beat 17.40%)
        TP:
        - idea is same as Q.15
            - Using a while loop to go through the list to locate first number
            - Once the 1st number is located, determine the sub-array and apply 2 pointer algorithm
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return 0
        nums.sort()
        self.target = target
        self.diff = self.res = float('inf')
        for i in range(len(nums)):
            sub_nums = nums[:i] + nums[i+1:]
            if self.findMinDiff(sub_nums, nums[i]):
                return target
        return self.res

    def findMinDiff(self, sub_nums, base_num):
        l = 0
        r = len(sub_nums)-1
        while l < r:
            tmp_sum = base_num + sub_nums[l] + sub_nums[r]
            if tmp_sum == self.target:
                return True
            diff = abs(self.target - tmp_sum)
            if diff < self.diff:
                self.diff = diff
                self.res = tmp_sum
            if tmp_sum > self.target:
                r -= 1
            elif tmp_sum < self.target:
                l += 1
        return False

nums = [-1, 2, 1, -4]
target = 1

print Solution().threeSumClosest(nums, target)