class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        Facebook
        Sliding Window
        T:O(n) S:O(1)
        Runtime: 72 ms, faster than 30.14% of Python online submissions for Longest Continuous Increasing Subsequence.
        Memory Usage: 13.8 MB, less than 29.01% of Python online submissions for Longest Continuous Increasing Subsequence.
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        ans = -float('inf')
        count = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
        ans = max(ans, count)
        return ans