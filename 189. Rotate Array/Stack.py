# -*- coding: utf-8 -*-
class Solution(object):
    def rotate(self, nums, k):
        """
        Solutio: Using Stack
        Time Complexity: O(n)
        Space Complexity: O(1)
        TP:
        - Using tack to pop
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())
        print nums

nums = [1,2,3,4,5,6,7]
k = 3
sol = Solution()
sol.rotate(nums, k)