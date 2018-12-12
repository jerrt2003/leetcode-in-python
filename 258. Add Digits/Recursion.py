# -*- coding: utf-8 -*-
class Solution(object):
    def addDigits(self, num):
        """
        Solution: Recursion
        Time Complexity:
        Space Complexity:
        Inspired By: MySelf!!
        :type num: int
        :rtype: int
        """
        res = num/10 + num%10
        while res > 9:
            res = res/10 + res%10
        return res

num = 19
print Solution().addDigits(num)