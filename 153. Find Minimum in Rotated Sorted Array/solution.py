class Solution(object):
    def findMin(self, nums):
        """
        Facebook
        T:O(logn) S:O(1)
        Runtime: 28 ms, faster than 78.83% of Python online submissions for Find Minimum in Rotated Sorted Array.
        Memory Usage: 13.1 MB, less than 32.55% of Python online submissions for Find Minimum in Rotated Sorted Array.
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r)/2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        return nums[l]

print Solution().findMin([3,4,5,1,2])