# -*- coding: utf-8 -*-
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        Solution: Hashmap + Stack (28 ms, beat 99.3%)
        Time Complexity: O(n)
        Space Complexity: O(m) <-- len of nums
        Inspired By: MySELF!!
        TP:
        - Using a dict to store the next greater number for each number in nums
        - Then we go through findNums to see if we can get a hit, if yes append the number to res, if not, append -1
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        res = []
        ref = {}
        i = 0
        while i+1 < len(nums):
            if nums[i] < nums[i+1]:
                ref[nums[i]] = nums[i+1]
                while stack and nums[stack[-1]] < nums[i+1]: # Once we decide we also need to "backtrack" previous undecide number to see if we can have a nextGreater number
                    ref[nums[stack.pop()]] = nums[i+1]
            else:
                stack.append(i) # if current if larger than next number, we store it into stack for later check
            i += 1
        for num in findNums:
            if num in ref:
                res.append(ref[num])
            else:
                res.append(-1)
        return res