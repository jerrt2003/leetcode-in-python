# -*- coding: utf-8 -*-
class Solution:
    """
    Solution: Rotate all numbers at once
    Time Complexity: O(1)
    Space Complexity: O(n)
    TP:
    - 首先找出最後需要roate幾次
        - 因為K有可能會大於len(nums)所以k%n(餘數)即為最後需要roate的次數
    - 最後再利用list切割得到答案
    """
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        print nums

nums = [1,2,3,4,5,6,7]
k = 3
sol = Solution()
sol.rotate(nums, k)