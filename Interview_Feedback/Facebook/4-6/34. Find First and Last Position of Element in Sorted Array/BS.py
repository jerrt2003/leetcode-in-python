# -*- coding: utf-8 -*-
class Solution(object):
    def searchRange(self, nums, target):
        """
        Solution: BS
        Time Complexity: O(log(n))
        Space Complexity: O(log(n))
        Inspired By: MySELF!!
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0: return [-1, -1]
        self.right_most = -float('inf')
        self.left_most = float('inf')
        self.search(0, len(nums)-1, nums, target)
        if self.left_most == float('inf') and self.right_most == -float('inf'):
            return [-1, -1]
        return [self.left_most, self.right_most]

    def search(self, l, r, nums, target):
        if l == r and nums[l] == target:
            self.left_most = min(self.left_most, l)
            self.right_most = max(self.right_most, l)
            return
        elif l == r:
            return
        mid = (l+r)/2
        self.search(l, mid, nums, target)
        self.search(mid+1, r, nums, target)

nums = [10,7,7,9,8,8,8,10]
target = 9

print Solution().searchRange(nums, target)