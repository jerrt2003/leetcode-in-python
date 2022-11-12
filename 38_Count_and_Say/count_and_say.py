# -*- coding: utf-8 -*-
class Solution(object):
    def countAndSay(self, n):
        """
        Solution: Recursion
        Time Complexity:
        Space Complexity:
        Inspired By: MYSELF!!
        TP:
        - use recursion
        - remember to add the last count
        :type n: int
        :rtype: str
        """
        if n < 0: return 0
        i = 1
        res = "1"
        while i < n:
            res = self._find_res(res)
            i += 1
        return res


    def _find_res(self, nums):
        if len(nums) == 0: return 0
        if len(nums) == 1: return "1" + str(nums[0])
        res =""
        cont = 1
        i = 1
        while i < len(nums):
            if nums[i-1] == nums[i]:
                cont += 1
                i += 1
            else:
                res = res + str(cont) + str(nums[i-1])
                cont = 1
                i += 1
        return res + str(cont) + str(nums[i-1])


input = '111221'
sol = Solution()
print sol.countAndSay(3)