class Solution(object):
    def maxCoins(self, nums):
        """
        DP: Top-Down
        Time Complexity:
        Space Complexity:
        Inspired by:
        https://leetcode.com/problems/burst-balloons/discuss/76245/Easiest-Java-Solution
        https://leetcode.com/problems/burst-balloons/discuss/76243/Python-DP-N3-Solutions
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        nums_len = len(nums)
        DP = [[0 for _ in range(nums_len)] for _ in range(nums_len)]

        def findMax(start, end):
            
