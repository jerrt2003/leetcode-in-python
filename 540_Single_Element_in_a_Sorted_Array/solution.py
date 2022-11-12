class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        Facebook
        Binary Search
        T:O(logn) S:O(1)
        Runtime: 48 ms, faster than 98.31% of Python online submissions for Single Element in a Sorted Array.
        Memory Usage: 14.4 MB, less than 92.64% of Python online submissions for Single Element in a Sorted Array.
        https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/627921/Java-or-C%2B%2B-or-Python3-or-Easy-explanation-or-O(logn)-or-O(1)
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)

        def check(mid):
            if mid % 2 == 0:
                if nums[mid] == nums[mid-1]:
                    return True
                else:
                    return False
            else:
                if nums[mid] == nums[mid-1]:
                    return False
                else:
                    return True

        while l < r:
            mid = (l + r - 1) / 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return nums[-1] if l == len(nums) else nums[l-1]