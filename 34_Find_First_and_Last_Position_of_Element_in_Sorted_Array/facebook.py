class Solution(object):
    def searchRange(self, nums, target):
        """
        Facebook
        BS
        T:O(logn) S:O(1)
        Runtime: 60 ms, faster than 99.45% of Python online submissions for Find First and Last Position of Element in Sorted Array.
        Memory Usage: 14 MB, less than 62.57% of Python online submissions for Find First and Last Position of Element in Sorted Array.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def findMin(x):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r - 1) / 2
                if nums[mid] >= x:
                    r = mid
                else:
                    l = mid + 1
            return l

        def findMax(x):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r - 1) / 2
                if nums[mid] > x:
                    r = mid
                else:
                    l = mid + 1
            return l

        start = findMin(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = findMax(target) - 1

        return [start, end]

