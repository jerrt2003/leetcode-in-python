# -*- coding: utf-8 -*-
class Solution(object):
    def search(self, nums, target):
        """
        Solution: DP
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        """
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right-1) / 2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[right-1]:
                if nums[mid] < target <= nums[right-1]:
                    left = mid + 1
                else:
                    right = mid
            elif nums[mid] > nums[right-1]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                right -= 1
        return False
