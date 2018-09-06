import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        dp = -sys.maxint-1
        result = -sys.maxint-1
        for num in nums:
            dp = max(num, num+dp)
            result = max(dp, result)
        return result

nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [-1,-2]
sol = Solution()
print sol.maxSubArray(nums)