class Solution(object):
    def findMin(self, nums):
        """
        Facebook
        T:O(logn) S:O(1)
        Runtime: 40 ms, faster than 76.79% of Python online submissions for Find Minimum in Rotated Sorted Array II.
        Memory Usage: 13.2 MB, less than 8.43% of Python online submissions for Find Minimum in Rotated Sorted Array II.
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r)/2
            if nums[m] > nums[r]:
                l = m+1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1
        return nums[l]