# -*- coding: utf-8 -*-
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        Solution: Brutal Force (360 ms, beat 0.23%)
        Time Complexity: O(m*n)
        Space Complexity: O(m)
        Inspired By: MySELF
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res =[]
        for num in findNums:
            ref = nums[:]
            nextGreater = -1
            while ref:
                tmp = ref.pop()
                if tmp == num: break
                elif tmp > num:
                    nextGreater = tmp
            res.append(nextGreater)
        return res