class Solution(object):
    def search(self, nums, target):
        """
        Facebook
        T:O(nlog(n)) S:O(1)
        Runtime: 44 ms, faster than 63.37% of Python online submissions for Search in Rotated Sorted Array II.
        Memory Usage: 13.1 MB, less than 18.64% of Python online submissions for Search in Rotated Sorted Array II.
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l <= r:
            while l+1 < len(nums) and nums[l] == nums[l+1]:
                l += 1
            while r > 0 and nums[r] == nums[r-1]:
                r -= 1
            m = (l+r)/2
            if nums[m] == target:
                return True
            elif nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
            else:
                if nums[l] <= target < nums[m]:
                    r = m-1
                else:
                    l = m+1
        return False

