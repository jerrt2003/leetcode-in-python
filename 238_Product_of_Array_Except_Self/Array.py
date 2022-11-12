# -*- coding: utf-8 -*-
class Solution(object):
    def productExceptSelf(self, nums):
        """
        Facebook
        Solution: Array
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/product-of-array-except-self/discuss/65632/My-solution-beats-100-java-solutions
        TP:
        - Product of array except current number = (prodcut of array before current number) * (product of array after current number)
        - So what we can do is:
            - Scan the array twice
            - First scan we retrieve product before num
            - Second scan we retrieve product after num
            - Then we can multiply the product to get answer
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        prodcut_before_num = 1
        for i in range(len(nums)):
            res.append(prodcut_before_num)
            prodcut_before_num = prodcut_before_num * nums[i]
        prodcut_after_num = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * prodcut_after_num # result is prodcut_before_num * prodcut_after_num
            prodcut_after_num = prodcut_after_num * nums[i] # get prodcut_after_num
        return res

a = [1,2,3,4]
sol = Solution()
print sol.productExceptSelf(a)

