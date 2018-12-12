# -*- coding: utf-8 -*-
class Solution(object):
    def search(self, nums, target):
        """
        Solution: DP
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        Inspired By: MySELF!!
        TP:
        - 從 Q.33 + Q.154 得出來的解法
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right -= 1
        return False

nums = [2,5,6,0,0,1,2]
#nums = [4,5,6,7,0,1,2]
target = 7
print Solution().search(nums, target)