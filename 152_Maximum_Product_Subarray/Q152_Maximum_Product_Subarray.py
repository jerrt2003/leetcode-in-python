class Solution(object):
    def maxProduct(self, nums):
        """
        From: https://leetcode.com/problems/maximum-product-subarray/discuss/48330/Simple-Java-code
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        rmax = nums[0]
        rmin = nums[0]
        for i in range(1, len(nums)):
            tmp = rmax # because rmax might be changed during line 12 when line 13 try to access
            rmax = max(max(rmax*nums[i], rmin*nums[i]), nums[i])
            rmin = min(min(tmp*nums[i], rmin*nums[i]), nums[i])
            result = max(result, rmax)
        return result

#a = [2,3,-2,4]
a = [-4,-3,-2]
sol = Solution()
print sol.maxProduct(a)