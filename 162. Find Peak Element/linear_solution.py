class Solution(object):
    def findPeakElement(self, nums):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 44 ms, faster than 28.32% of Python online submissions for Find Peak Element.
        Memory Usage: 13 MB, less than 8.26% of Python online submissions for Find Peak Element.
        :type nums: List[int]
        :rtype: int
        """
        nums = [-float('inf')] + nums + [-float('inf')]
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i - 1

