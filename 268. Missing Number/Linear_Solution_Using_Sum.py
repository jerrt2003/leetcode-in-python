# -*- coding: utf-8 -*-
class Solution(object):
    def missingNumber(self, nums):
        """
        Solution: O(n)
        Time Complexity: O(n)
        Space Complexity: O(1)
        TP:
        - [0,1,2,4]
        - w/o missing number the array should look like [0,1,2,3,4]
        - so we first calculate the SUM of original array which will be (nums[0] + nums[-1])*(len(nums))/2 --> (0+4)*(5/2) --> n * (n+1) /2
        - then we subtract to current array sum to get missing number
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = n * (n+1)/2
        return total_sum - sum(nums)