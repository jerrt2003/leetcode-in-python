# -*- coding: utf-8 -*-
class Solution(object):
    def missingNumber(self, nums):
        """
        Solution: 用減法
        Time Complexity:
        Space Complexity:
        Inspired by: https://leetcode.com/problems/missing-number/discuss/69795/Java-solution-O(1)-space-and-O(n)-in-time
        TP:
        - we have only one missing number
        - We calculate what's the total sum should be (T_SUM)
        - then we find what's the current sum is (C_SUM)
        - missing number is: T_SUM - C_SUM
        Note:
        - 另外一種解法則是用hashset, 稍慢
        Time Complexity: O(n)
        Space Complexity: O(1)
        :type nums: List[int]
        :rtype: int
        """
        T_SUM = int((1+len(nums))/2.0*len(nums))
        C_SUM = 0
        for num in nums:
            C_SUM += num
        return T_SUM - C_SUM


nums = [3,0,1,4]
sol = Solution()
print sol.missingNumber(nums)


